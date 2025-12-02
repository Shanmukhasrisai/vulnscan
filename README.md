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
- SOAP header manipulation vulnerabilities
- WS-Addressing and WS-Security bypass testing

**gRPC & Protocol Buffers**
- Service enumeration and method discovery
- Channel hijacking and MITM vulnerability detection
- Serialization bypass attacks

**WebSocket & Real-Time APIs**
- Message tampering and injection testing
- Session hijacking vulnerability detection
- Protocol downgrade attacks

#### Core Vulnerability Detection

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
- **CVE Detection**: Automated scanning for known vulnerabilities with CVSS scoring

### Customizable Templates

VulnScan includes pre-built templates for common security testing scenarios:

```yaml
# Example: REST API Template
template_name: "REST API Security Assessment"
description: "Comprehensive REST API penetration testing"
scope:
  protocols: ["HTTP", "HTTPS"]
  methods: ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]
  
tests:
  - id: "auth_bypass"
    enabled: true
    intensity: "medium"
    
  - id: "injection_testing"
    enabled: true
    payloads:
      - type: "sql_injection"
      - type: "command_injection"
      - type: "xpath_injection"
      
  - id: "api_enumeration"
    enabled: true
    options:
      brute_force_wordlist: "api_endpoints.txt"
      
reporting:
  format: "html"
  include_remediation: true
  severity_threshold: 4.0
```

### Multi-Protocol Support in Action

**Example: Testing Multiple API Types**

```python
from vulnscan import VulnScanner, ScanConfig

# Initialize scanner with multi-protocol configuration
config = ScanConfig(
    target_url="https://api.example.com",
    protocols=["rest", "graphql", "grpc"],
    authentication={
        "type": "bearer_token",
        "token": "your_jwt_token_here"
    },
    concurrency=20,
    timeout=30
)

scanner = VulnScanner(config)

# Scan all API endpoints
results = scanner.scan_endpoints(
    fuzzing_intensity="aggressive",
    include_authentication_tests=True,
    include_rate_limiting_tests=True
)

# Generate comprehensive report
scanner.generate_report(
    output_format="html",
    include_exploitation_chains=True,
    cvss_scoring=True
)
```

### Cloud Infrastructure Auditing

VulnScan extends security testing to cloud environments:

**AWS Security Assessment**
```python
from vulnscan.cloud import AWSAuditor

auditor = AWSAuditor(
    aws_access_key="YOUR_KEY",
    aws_secret_key="YOUR_SECRET",
    regions=["us-east-1", "eu-west-1"]
)

# Scan API Gateway endpoints
gateway_results = auditor.audit_api_gateway()

# Check Lambda function security
lambda_results = auditor.audit_lambda_functions()

# Audit RDS and database security
db_results = auditor.audit_databases()
```

**Azure & GCP Support**
- Azure API Management security assessment
- Google Cloud API Gateway scanning
- Service authentication vulnerability detection
- Cloud storage access control analysis

---

## Installation & Quick Start

### System Requirements
- Python 3.8 or higher
- Linux, macOS, or Windows
- 2GB RAM minimum (4GB+ recommended for large-scale scanning)

### Installation

```bash
pip install vulnscan
```

### Command-Line Usage

```bash
# Basic REST API scan
vulnscan --target https://api.example.com --protocol rest

# GraphQL endpoint testing
vulnscan --target https://api.example.com/graphql --protocol graphql

# Multi-protocol comprehensive scan
vulnscan --target https://api.example.com \
         --protocols rest,graphql,websocket \
         --fuzzing-intensity aggressive \
         --template "api_security_assessment.yaml"

# Cloud infrastructure audit
vulnscan --cloud aws --regions us-east-1,eu-west-1 --audit-apis

# With authentication
vulnscan --target https://api.example.com \
         --auth-type bearer \
         --auth-token "your_jwt_token" \
         --output report.html
```

### Python API Example

```python
from vulnscan import VulnScanner, ScanConfig

# Configure scan
config = ScanConfig(
    target_url="https://api.example.com",
    protocols=["rest", "graphql"],
    authentication={
        "type": "bearer_token",
        "token": "jwt_token_here"
    },
    fuzzing_intensity="medium",
    timeout=30,
    threads=10
)

# Create scanner instance
scanner = VulnScanner(config)

# Execute comprehensive scan
results = scanner.scan(
    include_passive_recon=True,
    include_active_testing=True,
    include_authentication_tests=True
)

# Access vulnerability findings
for vulnerability in results.vulnerabilities:
    print(f"[{vulnerability.severity}] {vulnerability.title}")
    print(f"  Description: {vulnerability.description}")
    print(f"  CVSS Score: {vulnerability.cvss_score}")
    print(f"  Remediation: {vulnerability.remediation}")
    print()
```

---

## Advanced Configuration

### Configuration File (config.yaml)

```yaml
# VulnScan Configuration

scan:
  # Scan engine settings
  threads: 20
  timeout: 30
  max_retries: 3
  user_agent: "VulnScanner/2.0 (Security Assessment)"
  follow_redirects: true
  verify_ssl: true
  proxy: null  # Set if using HTTP/HTTPS proxy

api:
  # API-specific testing configuration
  protocols: ["rest", "graphql", "grpc"]
  max_depth: 5
  test_methods: ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"]
  fuzzing_intensity: "medium"  # low, medium, aggressive
  payload_mutation: true
  graphql_introspection: true
  wsdl_discovery: true

authentication:
  # Authentication testing
  test_jwt: true
  test_oauth2: true
  test_api_keys: true
  test_basic_auth: true
  test_mTLS: false

fuzzing:
  # Fuzzing engine configuration
  enable_mutation: true
  mutation_rate: 0.7
  payload_database: "payloads/default"
  custom_payloads: "payloads/custom"
  encoding: ["utf8", "url", "html", "base64"]

reporting:
  # Report generation settings
  format: "html"  # html, json, xml, pdf
  include_screenshots: true
  include_remediation: true
  include_exploitation_chains: true
  cvss_threshold: 4.0
  export_jira: false
  export_slack: false

integrations:
  # Third-party integrations
  slack_webhook: null
  jira_url: null
  jira_project: null
  github_issues: false
  gitlab_issues: false

cloud:
  # Cloud infrastructure settings
  providers: []
  audit_apis: false
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
