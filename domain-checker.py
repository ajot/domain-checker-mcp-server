#!/usr/bin/env python3
"""
MCP Server for checking domain name availability using FastMCP 2.0
"""

import asyncio
import json
import logging
import os
from typing import Any, Dict, List
import whois
import dns.resolver
from fastmcp import FastMCP

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("domain-checker")

# Create the FastMCP server
mcp = FastMCP(
    name="Domain Checker",
    instructions="When you are asked about domain availability or to check if a domain is available for registration, call the appropriate function."
)

class DomainChecker:
    """Domain availability checker with multiple verification methods"""
    
    def __init__(self):
        self.dns_resolver = dns.resolver.Resolver()
        self.dns_resolver.timeout = 5
        self.dns_resolver.lifetime = 5
    
    async def check_dns_records(self, domain: str) -> bool:
        """Check if domain has DNS records (indicates it's registered and in use)"""
        try:
            # Try common record types
            for record_type in ['A', 'MX', 'NS', 'SOA']:
                try:
                    await asyncio.to_thread(
                        lambda: self.dns_resolver.resolve(domain, record_type)
                    )
                    logger.info(f"Found {record_type} record for {domain}")
                    return True
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
                    continue
                except Exception as e:
                    logger.warning(f"Error checking {record_type} records for {domain}: {e}")
            
            # If we get here, no records were found
            return False
        except Exception as e:
            logger.error(f"Error in DNS check for {domain}: {e}")
            return False
    
    async def check_whois(self, domain: str) -> Dict[str, Any]:
        """Check domain availability via WHOIS lookup"""
        try:
            # Run WHOIS query in a thread to avoid blocking
            whois_data = await asyncio.to_thread(whois.whois, domain)
            
            # Process the results
            if whois_data.status is None and whois_data.registrar is None:
                logger.info(f"Domain {domain} appears to be available (no registrar/status)")
                return {"available": True, "whois_data": whois_data}
            else:
                logger.info(f"Domain {domain} is registered with {whois_data.registrar}")
                return {"available": False, "whois_data": whois_data}
        except Exception as e:
            logger.error(f"WHOIS error for {domain}: {e}")
            return {"available": False, "error": str(e)}


domain_checker = DomainChecker()

@mcp.tool()
async def check_domain_availability(domain: str) -> Dict[str, Any]:
    """
    Check if a domain name is available for registration.
    
    Args:
        domain: The domain name to check (e.g., "example.com")
        
    Returns:
        A dictionary with availability information and details
    """
    result = {
        "domain": domain,
        "available": False,
        "dns_records_exist": False,
        "whois_result": None,
        "confidence": "low"
    }
    
    # First check WHOIS
    whois_result = await domain_checker.check_whois(domain)
    result["whois_result"] = whois_result
    
    if "error" in whois_result:
        # WHOIS lookup failed, rely only on DNS
        result["confidence"] = "very low"
    else:
        result["available"] = whois_result.get("available", False)
        result["confidence"] = "medium"
    
    # Then check DNS records
    has_dns = await domain_checker.check_dns_records(domain)
    result["dns_records_exist"] = has_dns
    
    # If DNS records exist, domain is definitely not available
    if has_dns:
        result["available"] = False
        result["confidence"] = "high"
    
    # If WHOIS says available and no DNS records, high confidence in availability
    if result["available"] and not has_dns:
        result["confidence"] = "high"
    
    return result

@mcp.tool()
async def batch_check_domains(domains: List[str]) -> Dict[str, Any]:
    """
    Check multiple domains for availability in a single request.
    
    Args:
        domains: List of domain names to check
        
    Returns:
        Dictionary with results for each domain
    """
    results = {}
    
    # Process domains concurrently
    tasks = [check_domain_availability(domain) for domain in domains]
    domain_results = await asyncio.gather(*tasks)
    
    # Organize results by domain
    for i, domain in enumerate(domains):
        results[domain] = domain_results[i]
    
    return results

@mcp.resource("domain://check/{domain}")
async def domain_info_resource(domain: str) -> str:
    """Get domain availability information as a resource"""
    result = await check_domain_availability(domain)
    return json.dumps(result, indent=2)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port, log_level="debug")