# VulnScan

A high-performance **API vulnerability scanner and penetration testing tool** engineered for security auditing and comprehensive security assessments. VulnScan delivers enterprise-grade penetration testing capabilities through customizable templates, multi-protocol support, and advanced API vulnerability detection across modern application architectures and cloud infrastructure.

## What Makes VulnScan Unique

VulnScan is purpose-built for **API security testing and penetration testing** with a focus on:

- **API-First Design**: Specialized detection engines for REST, SOAP, GraphQL, and gRPC APIs
- **Advanced Payload Fuzzing**: Intelligent mutation-based fuzzing with protocol-aware payloads
- **Authentication Testing**: Comprehensive JWT, OAuth, API key, and session management vulnerability detection
- **Real-Time Analysis**: Immediate vulnerability identification with detailed exploitation guidance
- **Developer-Friendly**: Clean Python API with extensive documentation for security automation
- **Enterprise-Ready**: Built for security professionals conducting large-scale penetration tests

## Features

### Core Vulnerability Detection

- **CVE Detection**: Automated scanning for known Common Vulnerabilities and Exposures
- **SQL Injection**: Deep analysis for SQL injection vulnerabilities across multiple database types
- **Cross-Site Scripting (XSS)**: Detection of reflected, stored, and DOM-based XSS vulnerabilities
- **Cross-Site Request Forgery (CSRF)**: CSRF token validation and attack vector identification
- **Remote Code Execution (RCE)**: Command injection and RCE vulnerability detection
- **Path Traversal**: Directory traversal and file inclusion vulnerability scanning
- **Server-Side Request Forgery (SSRF)**: Internal network access vulnerability detection
- **Authentication Bypass**: Weak authentication and authorization flaw detection

### Advanced API Penetration Testing Capabilities

- **REST API Security**: Comprehensive endpoint enumeration, parameter tampering, and injection testing
- **GraphQL Introspection**: Query complexity analysis, batching attacks, and schema extraction
- **SOAP API Testing**: XML injection, XXE (XML External Entity), and WSDL analysis
- **API Authentication Flaws**: Broken authentication, missing authorization, and privilege escalation
- **Rate Limiting Detection**: Identify missing or misconfigured rate limits and brute-force vulnerabilities
- **API Versioning Issues**: Legacy endpoint exposure and version-specific vulnerability detection

### Enterprise Security Auditing Features

- **Customizable Templates**: Create and modify scan templates for specific use cases and compliance requirements
- **Multi-Protocol Support**: Comprehensive coverage for HTTP/HTTPS, WebSocket, GraphQL, gRPC, and legacy protocols
- **Cloud Infrastructure Auditing**: Security configuration assessment for AWS, Azure, and GCP environments
- **CI/CD Integration**: Seamless integration with Jenkins, GitLab CI, GitHub Actions, and CircleCI
- **Parallel Scanning**: High-performance concurrent scanning engine for large-scale penetration tests
- **Rate Limiting**: Configurable request throttling to avoid detection and respect target systems
- **Custom Payloads**: Extensible payload system for advanced testing scenarios
- **Detailed Reporting**: Comprehensive vulnerability reports with CVSS scoring and remediation guidance

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Shanmukhasrisai/vulnscan.git
cd vulnscan

# Install dependencies
pip install -r requirements.txt

# Run VulnScan
python vulnscan.py --help
```

### Basic Usage Examples

#### Simple API Vulnerability Scan

```bash
# Scan a REST API endpoint
python vulnscan.py --url https://api.example.com --scan-type api

# Scan with authentication
python vulnscan.py --url https://api.example.com --header "Authorization: Bearer TOKEN" --scan-type api
```

#### Advanced Penetration Testing

```bash
# Full penetration test with custom payloads
python vulnscan.py --url https://target.com --scan-type full --payloads custom_payloads.txt --threads 10

# GraphQL API security audit
python vulnscan.py --url https://api.example.com/graphql --scan-type graphql --introspection

# API authentication bypass testing
python vulnscan.py --url https://api.example.com --scan-type auth --test-bypass --test-privilege-escalation
```

#### CI/CD Integration

```bash
# Use in CI/CD pipeline with JSON output
python vulnscan.py --url https://staging-api.example.com --scan-type api --output json --fail-on-high
```

### Python API Usage

```python
from vulnscan import VulnScanner, ScanConfig

# Initialize scanner for API penetration testing
scanner = VulnScanner()

# Configure API security scan
config = ScanConfig(
    target="https://api.example.com",
    scan_types=["api", "injection", "auth"],
    headers={"Authorization": "Bearer YOUR_TOKEN"},
    threads=5,
    timeout=30
)

# Execute penetration test
results = scanner.scan(config)

# Analyze vulnerabilities
for vuln in results.vulnerabilities:
    print(f"[{vuln.severity}] {vuln.title}")
    print(f"Endpoint: {vuln.endpoint}")
    print(f"Description: {vuln.description}")
    print(f"Remediation: {vuln.remediation}\n")

# Generate security audit report
scanner.generate_report(results, format="html", output="security_audit.html")
```

### Advanced API Testing Example

```python
from vulnscan import APITester, AuthConfig

# Configure API authentication testing
auth_config = AuthConfig(
    auth_type="jwt",
    token_endpoint="https://api.example.com/auth/token",
    credentials={"username": "test", "password": "test"}
)

# Initialize API penetration tester
api_tester = APITester(
    base_url="https://api.example.com/v1",
    auth_config=auth_config
)

# Test for common API vulnerabilities
results = api_tester.run_comprehensive_test([
    "broken_authentication",
    "broken_authorization",
    "excessive_data_exposure",
    "lack_of_resources_and_rate_limiting",
    "mass_assignment",
    "security_misconfiguration",
    "injection",
    "improper_assets_management"
])

# Export findings for security team
api_tester.export_findings(results, format="pdf", include_poc=True)
```

## Use Cases for Security Professionals

### 1. API Security Assessments
Conduct comprehensive security audits of REST, GraphQL, and SOAP APIs to identify OWASP API Top 10 vulnerabilities before attackers do.

### 2. Penetration Testing Engagements
Perform thorough penetration tests on web applications and APIs with automated vulnerability detection and manual testing capabilities.

### 3. Security Regression Testing
Integrate VulnScan into CI/CD pipelines to catch security vulnerabilities during development before they reach production.

### 4. Compliance and Auditing
Generate detailed security reports for compliance requirements (PCI-DSS, HIPAA, SOC 2) with comprehensive vulnerability documentation.

### 5. Bug Bounty Hunting
Accelerate vulnerability discovery in bug bounty programs with automated scanning and custom payload generation.

## Why Choose VulnScan?

✅ **Built by Security Professionals**: Designed with real-world penetration testing experience
✅ **API-Focused Architecture**: Unlike generic scanners, VulnScan specializes in modern API security
✅ **Extensible and Customizable**: Python-based architecture allows easy extension and customization
✅ **Fast and Efficient**: High-performance parallel scanning without compromising accuracy
✅ **Comprehensive Coverage**: From OWASP Top 10 to advanced API-specific vulnerabilities
✅ **Active Development**: Regular updates with latest vulnerability detection techniques

## Security Considerations

**⚠️ Legal Notice**: VulnScan is a penetration testing tool designed for authorized security assessments only. Only use this tool on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal.

## Configuration

Create a `config.yaml` file for advanced configuration:

```yaml
scan:
  threads: 10
  timeout: 30
  user_agent: "VulnScan/1.0"
  follow_redirects: true

api:
  max_depth: 3
  test_methods: ["GET", "POST", "PUT", "DELETE", "PATCH"]
  fuzzing_intensity: "medium"
  
reporting:
  format: "html"
  include_screenshots: true
  cvss_threshold: 4.0

integrations:
  slack_webhook: "https://hooks.slack.com/..."
  jira_url: "https://your-jira.com"
```

## Contributing

We welcome contributions from the security community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Reporting bugs and vulnerabilities
- Suggesting new detection modules
- Submitting pull requests
- Adding new payload templates

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](https://github.com/Shanmukhasrisai/vulnscan/wiki)
- 🐛 [Issue Tracker](https://github.com/Shanmukhasrisai/vulnscan/issues)
- 💬 [Discussions](https://github.com/Shanmukhasrisai/vulnscan/discussions)

## Disclaimer

VulnScan is provided for educational and professional security testing purposes. The authors and contributors are not responsible for misuse or damage caused by this tool. Always ensure you have proper authorization before conducting security assessments.
