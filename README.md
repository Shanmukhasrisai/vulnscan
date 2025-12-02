# VulnScan
## Enterprise-Grade API Penetration Testing Platform

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Security Focused](https://img.shields.io/badge/Security-Focused-red.svg)]()

**VulnScan** is a high-performance, professional-grade API vulnerability scanner and penetration testing platform engineered for security teams, penetration testers, and cloud security auditors. VulnScan delivers enterprise-grade security testing capabilities through intelligent fuzzing, customizable templates, multi-protocol support, and comprehensive API vulnerability detection across modern microservices architectures and cloud infrastructure.

Purpose-built for modern security challenges, VulnScan enables security professionals to identify critical vulnerabilities before attackers do.

---

## What Makes VulnScan Unique

VulnScan stands apart from generic vulnerability scanners through its specialized focus on **API-centric security testing**:

- 🎯 **API-First Architecture**: Specialized detection engines for REST, GraphQL, SOAP, gRPC, and WebSocket APIs
- 🔄 **Intelligent Protocol Adaptation**: Automatic protocol detection and context-aware vulnerability testing
- 🧬 **Advanced Mutation Fuzzing**: ML-assisted payload generation with protocol-specific mutation strategies
- 🔐 **Authentication Framework Testing**: Comprehensive JWT, OAuth 2.0, SAML, mTLS, and API key vulnerability detection
- ⚡ **Real-Time Analysis**: Immediate vulnerability identification with detailed exploitation chain analysis
- 🛠️ **Developer-Centric API**: Clean Python SDK for seamless security automation and CI/CD integration
- ☁️ **Cloud-Native Support**: Purpose-built for AWS, Azure, and GCP security assessment
- 📊 **Enterprise Scalability**: Designed for large-scale security operations and compliance auditing

---

## Core Features

### Advanced API Security Testing

#### Multi-Protocol Support

**REST API Security**
- Endpoint enumeration and parameter discovery
- Injection testing (SQLi, NoSQL, command injection, XPath)
- Authentication and authorization bypass detection
- API rate limit and brute-force vulnerability identification

**GraphQL Security**
- Query complexity analysis and DoS detection
- Introspection extraction and schema enumeration
- Batching attacks and alias injection testing
- Authorization bypass in nested resolvers

**SOAP API Testing**
- WSDL analysis and operation enumeration
- XML injection and XXE (XML External Entity) detection
- WS-Security authentication bypass
- SOAP action spoofing detection

**gRPC Security**
- Protocol buffer fuzzing
- Authentication and interceptor testing
- Message tampering detection
- Unary and streaming RPC vulnerability scanning

**WebSocket Testing**
- Real-time message injection
- Connection hijacking and session fixation
- Cross-site WebSocket hijacking (CSWSH)
- Message-level authentication bypass

#### Core Vulnerability Detection

VulnScan detects API vulnerabilities including **OWASP API Security Top 10** and various **Common Vulnerabilities and Exposures (CVEs)**:

- **SQL Injection**: Multi-database detection (MySQL, PostgreSQL, Oracle, MSSQL)
- **NoSQL Injection**: MongoDB, CouchDB, and other NoSQL query injection
- **Cross-Site Scripting (XSS)**: Reflected, stored, and DOM-based detection
- **Cross-Site Request Forgery (CSRF)**: Token validation and attack vector identification
- **Remote Code Execution (RCE)**: Command injection and expression language injection
- **Path Traversal**: Directory traversal and file inclusion vulnerabilities
- **Server-Side Request Forgery (SSRF)**: Internal network access and cloud metadata service attacks
- **Authentication Bypass**: Broken authentication, missing authorization, privilege escalation
- **Insecure Deserialization**: Object injection and gadget chain attacks
- **API Key Exposure**: Hardcoded credentials and token leakage detection
- **OWASP Top 10 Coverage**: Comprehensive detection of OWASP API Security Top 10 vulnerabilities
- **CVE Detection**: Automated scanning for known vulnerabilities with CVSS scoring and impact assessment

### Customizable Templates

**Template System**
- YAML-based vulnerability definition format
- Support for complex multi-step attack chains
- Custom payload libraries and mutation strategies
- Conditional logic and dynamic variable substitution

**Pre-Built Templates**
- 500+ curated vulnerability templates
- Industry-specific security checks (healthcare, finance, e-commerce)
- Compliance-focused templates (PCI-DSS, HIPAA, GDPR)
- Active community template repository

**Custom Template Development**
```yaml
template:
  name: "Custom API Authentication Bypass"
  severity: high
  protocol: rest
  
  requests:
    - method: POST
      path: "/api/auth/login"
      headers:
        Content-Type: "application/json"
      body: |
        {"username": "{{username}}", "password": "{{payload}}"}
      
  payloads:
    - "' OR '1'='1"
    - "admin' --"
    - "{\"$ne\": null}"
  
  detection:
    - status_code: 200
    - response_contains: "token"
    - response_time: "<500ms"
```

---

## Installation & Quick Start

**Prerequisites**
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

**Installation**

```bash
# Clone the repository
git clone https://github.com/Shanmukhasrisai/vulnscan.git
cd vulnscan

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install VulnScan
pip install -e .
```

**Quick Start - Basic Scan**

```bash
# Scan a single API endpoint
vulnscan scan --url https://api.example.com/v1

# Scan with custom template
vulnscan scan --url https://api.example.com --template jwt-bypass

# Advanced scan with authentication
vulnscan scan \
  --url https://api.example.com \
  --header "Authorization: Bearer YOUR_TOKEN" \
  --template full-audit \
  --output report.json
```

**Python SDK Example**

```python
from vulnscan import VulnScanner
from vulnscan.templates import SQLInjectionTemplate

# Initialize scanner
scanner = VulnScanner(
    target_url="https://api.example.com",
    headers={"Authorization": "Bearer YOUR_TOKEN"},
    timeout=30
)

# Add templates
scanner.add_template(SQLInjectionTemplate())
scanner.add_template("owasp-top-10")

# Execute scan
results = scanner.scan()

# Process results
for vuln in results.vulnerabilities:
    print(f"Found: {vuln.name} - Severity: {vuln.severity}")
    print(f"Location: {vuln.url}")
    print(f"Recommendation: {vuln.remediation}")

# Generate report
report = results.generate_report(format="html")
report.save("vulnerability_report.html")
```

---

## Advanced Configuration

**Configuration File (vulnscan.yaml)**

```yaml
target:
  url: "https://api.example.com"
  base_path: "/api/v1"
  
authentication:
  type: "oauth2"
  credentials:
    client_id: "your_client_id"
    client_secret: "your_client_secret"
  token_url: "https://auth.example.com/token"

scanning:
  threads: 10
  timeout: 30
  rate_limit: 100  # requests per second
  user_agent: "VulnScan/1.0 Security Audit"
  
templates:
  - "sql-injection"
  - "xss-detection"
  - "authentication-bypass"
  - "api-security-owasp"
  
reporting:
  output_format: ["json", "html", "pdf"]
  severity_threshold: "medium"
  include_false_positives: false
  
advanced:
  follow_redirects: true
  verify_ssl: true
  proxy: "http://proxy.example.com:8080"
  custom_headers:
    X-API-Version: "2.0"
  audit_storage: false
  check_metadata_service: false
```

---

## Security Considerations

⚠️ **Legal Notice**: VulnScan is a penetration testing tool designed for authorized security assessments only. Only use this tool on:

- Systems you own
- Systems where you have explicit written authorization
- Authorized penetration testing engagements

**Unauthorized access to computer systems is illegal.** Always ensure you have proper written authorization before conducting security assessments.

---

## Contributing

We welcome contributions from the security community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Reporting security vulnerabilities responsibly
- Suggesting new detection modules
- Submitting pull requests
- Adding new payload templates
- Improving protocol support

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support & Resources

- 📖 **[Full Documentation](https://github.com/Shanmukhasrisai/vulnscan/wiki)** - Comprehensive guides and API reference
- 🐛 **[Issue Tracker](https://github.com/Shanmukhasrisai/vulnscan/issues)** - Report bugs and request features
- 💬 **[Community Discussions](https://github.com/Shanmukhasrisai/vulnscan/discussions)** - Ask questions and share experiences
- 🔒 **[Security Advisory](https://github.com/Shanmukhasrisai/vulnscan/security)** - Report security issues privately

---

## Disclaimer

VulnScan is provided for educational and professional security testing purposes. The authors and contributors are not responsible for misuse or damage caused by this tool. Always ensure you have proper authorization and follow applicable laws and regulations when conducting security assessments. This tool should only be used by qualified security professionals on systems they are authorized to test.

---

**Made with ❤️ for the security community**
