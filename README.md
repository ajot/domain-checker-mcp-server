# Domain Checker MCP Server

A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution. Built with the modern FastMCP framework for easy setup and reliable domain availability checking.

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=domain-checker&config=eyJjb21tYW5kIjoieW91cl9wYXRoX3RvX3B5dGhvbiB5b3VyX3BhdGhfdG8vZG9tYWluLWNoZWNrZXIucHkifQ%3D%3D)

## Features

- ✅ **Dual Verification**: Uses both WHOIS and DNS resolution for accurate results
- 🚀 **Async Operations**: Non-blocking operations with proper timeout handling
- 📊 **Batch Processing**: Check multiple domains concurrently
- 🔍 **Detailed Analysis**: Provides comprehensive availability information
- 🛡️ **Error Handling**: Robust error handling for various edge cases
- 📋 **Resource Support**: Domain info available as MCP resources

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone or download the server files**
   ```bash
   mkdir domain-checker-mcp
   cd domain-checker-mcp
   ```

2. **Create the server files**
   - Save the main server code as `domain_checker.py`
   - Save the requirements as `requirements.txt`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start with FastMCP Development Tools

The fastest way to test your server is using the FastMCP development tools:

### Test with FastMCP Inspector
```bash
fastmcp dev domain_checker.py
```

This opens an interactive inspector where you can test the domain checking tools.

### Install in Claude Desktop
```bash
fastmcp install domain_checker.py --name "Domain Checker"
```

This automatically configures the server in Claude Desktop for immediate use.

## Manual Configuration (Alternative)

If you prefer to configure Claude Desktop manually:

**On macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

**On Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "domain-checker": {
      "command": "python",
      "args": ["/path/to/your/domain_checker.py"],
      "cwd": "/path/to/your/domain-checker-mcp"
    }
  }
}
```

**Important**: Replace `/path/to/your/` with the actual path to your domain checker directory.

## Usage

The server provides two main tools and a resource:

### Tools

#### 1. Check Single Domain
Check if a single domain name is available:

**Example prompt**: "Check if myawesome-startup.com is available"

#### 2. Check Multiple Domains  
Check multiple domains at once:

**Example prompt**: "Check availability for these domains: mycompany.com, mycompany.net, mycompany.org"

### Resources

#### Domain Info Resource
Access domain information as a resource:
- **URI Pattern**: `domain://check/{domain}`
- **Example**: `domain://check/example.com`

This provides structured JSON data about domain availability that can be referenced by other tools or prompts.

## Understanding Results

### Availability Status

- **✅ LIKELY AVAILABLE**: Domain appears to be unregistered and available
- **❌ NOT AVAILABLE**: Domain is registered and not available
- **❓ UNCLEAR**: Mixed signals - manual verification recommended

### Verification Methods

The server uses two verification methods:

1. **WHOIS Lookup**
   - Queries domain registration databases
   - Checks for registrar information, status codes, creation dates
   - Parser errors often indicate availability

2. **DNS Resolution**
   - Attempts to resolve domain to IP addresses
   - NXDOMAIN responses suggest availability
   - Helps identify registered but unconfigured domains

### Sample Output

```
Domain: example-startup.com
Status: ✅ LIKELY AVAILABLE

WHOIS Check: Available
DNS Resolution: Not resolving

Details:
{
  "whois": {
    "available": true,
    "reason": "WHOIS parser error: No match for domain"
  },
  "dns": {
    "resolvable": false,
    "reason": "Domain does not resolve (NXDOMAIN)"
  }
}
```

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Install missing dependencies
pip install mcp python-whois dnspython
```

**2. Permission Errors**
```bash
# Use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**3. Timeout Issues**
- The server has built-in timeouts (5-10 seconds)
- Some domains may take longer to query
- Network connectivity issues can cause timeouts

**4. WHOIS Rate Limiting**
- Some WHOIS servers have rate limits
- Wait between queries if checking many domains
- Consider using delays for bulk operations

### Debugging

Enable debug logging by modifying the server:

```python
logging.basicConfig(level=logging.DEBUG)
```

This will show detailed information about WHOIS and DNS queries.

## Limitations

- **Not 100% Accurate**: Domain availability can change rapidly
- **WHOIS Variations**: Different TLDs have different WHOIS formats
- **Rate Limiting**: Some WHOIS servers limit query frequency
- **Premium Domains**: May show as "available" but require special registration
- **Registry Delays**: Recently registered domains might not immediately appear

## Important Notes

### Before Registering Domains

1. **Double-check results**: Always verify availability through official registrars
2. **Consider alternatives**: Check similar TLDs (.net, .org, etc.)
3. **Trademark issues**: Ensure domain doesn't infringe on existing trademarks
4. **Premium domains**: Some "available" domains may have premium pricing

### Best Practices

- Use this tool for initial screening
- Verify results with domain registrars before purchasing
- Check multiple TLD variations
- Consider trademark and brand implications

## Contributing

To improve this MCP server:

1. **Add TLD-specific logic**: Different TLDs have different WHOIS formats
2. **Improve parsing**: Handle more WHOIS response variations
3. **Add caching**: Cache results to reduce API calls
4. **Premium domain detection**: Identify premium domains
5. **Bulk optimization**: Add rate limiting for large batches

## License

This project is provided as-is for educational and practical use. Please ensure compliance with WHOIS server terms of service when using this tool.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify your MCP client configuration
3. Test with simple domain queries first
4. Check network connectivity and DNS settings

---

**Disclaimer**: This tool provides estimates of domain availability. Always verify availability through official domain registrars before making any purchase decisions.