# Domain Checker MCP Server

A Model Context Protocol (MCP) server that checks domain name availability using WHOIS lookups and DNS resolution. Built with the modern FastMCP framework for easy setup and reliable domain availability checking.

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=domain-checker&config=eyJjb21tYW5kIjoicHl0aG9uIC9wYXRoL3RvL3lvdXIvZG9tYWluX2NoZWNrZXIucHkiLCJjd2QiOiIvcGF0aC90by95b3VyL2RvbWFpbi1jaGVja2VyLW1jcCJ9)


![Image](https://github.com/user-attachments/assets/d5e7db9e-346d-436b-9c2f-53f014debe17)

## Features

- ✅ **Dual Verification**: Uses both WHOIS and DNS resolution for accurate results
- 🚀 **Async Operations**: Non-blocking operations with proper timeout handling
- 📊 **Batch Processing**: Check multiple domains concurrently
- 🔍 **Detailed Analysis**: Provides comprehensive availability information

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajot/domain-checker-mcp-server.git
   cd domain-checker-mcp-server
   ```

2. **Create and activate a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On macOS/Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Using the Domain Checker

### With FastMCP Development Tools

```bash
# Make sure your virtual environment is activated
fastmcp dev domain-checker.py
```
![Image](https://github.com/user-attachments/assets/beb32cf0-499f-40d3-aeda-a255291ca5f3)

### Configure in MCP-Compatible Applications

This MCP server works with Claude Desktop, Cursor, Windsurf, and other MCP-compatible applications.

#### Configuration Locations

- **Claude Desktop**:
  - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
  - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
  
- **Cursor**:
  - macOS: `~/Library/Application Support/Cursor/cursor_desktop_config.json`
  - Windows: `%APPDATA%\Cursor\cursor_desktop_config.json`

- **Windsurf**:
  - macOS: `~/Library/Application Support/Windsurf/windsurf_desktop_config.json`
  - Windows: `%APPDATA%\Windsurf\windsurf_desktop_config.json`

Add the following configuration to the appropriate file, making sure to point to your virtual environment:

```json
{
  "mcpServers": {
    "domain-checker": {
      "command": "/path/to/your/venv/bin/python",
      "args": ["/path/to/your/domain-checker.py"],
      "cwd": "/path/to/your/domain-checker-mcp-server"
    }
  }
}
```

**Important**: Replace paths with the actual paths to your virtual environment and domain checker directory.

## Usage Examples

### Check Single Domain
"Check if myawesome-startup.com is available"

### Check Multiple Domains
"Check availability for these domains: mycompany.com, mycompany.net, mycompany.org"

## Understanding Results

### Availability Status

- **✅ LIKELY AVAILABLE**: Domain appears to be unregistered and available
- **❌ NOT AVAILABLE**: Domain is registered and not available
- **❓ UNCLEAR**: Mixed signals - manual verification recommended

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
- Make sure your virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`

**2. Timeout Issues**
- Some WHOIS servers have rate limits
- Network connectivity issues can cause timeouts

---

**Disclaimer**: This tool provides estimates of domain availability. Always verify availability through official domain registrars before making any purchase decisions.