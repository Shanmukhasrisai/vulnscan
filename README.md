# VulnScan

A modern, high-performance vulnerability scanner with customizable templates, multi-protocol support, API scanning, and cloud infrastructure auditing capabilities.

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

### Advanced Capabilities
- **Customizable Templates**: Create and modify scan templates for specific use cases
- **Multi-Protocol Support**: HTTP/HTTPS, WebSocket, GraphQL, gRPC, and more
- **API Scanning**: Comprehensive REST, SOAP, and GraphQL API security testing
- **Cloud Infrastructure Auditing**: AWS, Azure, GCP security configuration assessment
- **CI/CD Integration**: Seamless integration with Jenkins, GitLab CI, GitHub Actions, CircleCI
- **Parallel Scanning**: High-performance concurrent scanning engine
- **Rate Limiting**: Configurable request throttling to avoid detection
- **Custom Payloads**: Extensible payload system for advanced testing

## Installation

### Using pip
```bash
pip install vulnscan
```

### From source
```bash
git clone https://github.com/Shanmukhasrisai/vulnscan.git
cd vulnscan
pip install -r requirements.txt
python setup.py install
```

### Docker
```bash
docker pull vulnscan/vulnscan:latest
docker run -it vulnscan/vulnscan:latest
```

## Quick Start

### Basic Web Application Scan
```bash
vulnscan scan --url https://example.com
```

### Scan with Specific Vulnerability Types
```bash
vulnscan scan --url https://example.com --checks sql-injection,xss,rce
```

### API Scanning
```bash
vulnscan api-scan --url https://api.example.com --spec openapi.json
```

### Cloud Infrastructure Audit
```bash
vulnscan cloud-audit --provider aws --profile production
```

## Usage Examples

### Custom Template Scanning
```bash
vulnscan scan --url https://example.com --template templates/custom-scan.yaml
```

### Authenticated Scanning
```bash
vulnscan scan --url https://example.com \
  --auth-type bearer \
  --auth-token "your-jwt-token"
```

### Rate-Limited Scanning
```bash
vulnscan scan --url https://example.com \
  --rate-limit 10 \
  --concurrency 5
```

### Output Formats
```bash
# JSON output
vulnscan scan --url https://example.com --output json --output-file results.json

# HTML report
vulnscan scan --url https://example.com --output html --output-file report.html

# SARIF format (for CI/CD)
vulnscan scan --url https://example.com --output sarif --output-file results.sarif
```

## CI/CD Integration

### GitHub Actions
```yaml
name: Security Scan
on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run VulnScan
        run: |
          pip install vulnscan
          vulnscan scan --url ${{ secrets.APP_URL }} --output sarif --output-file results.sarif
      - name: Upload SARIF results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: results.sarif
```

### GitLab CI
```yaml
vulnerability_scan:
  image: python:3.9
  script:
    - pip install vulnscan
    - vulnscan scan --url $APP_URL --output json --output-file gl-sast-report.json
  artifacts:
    reports:
      sast: gl-sast-report.json
```

### Jenkins Pipeline
```groovy
pipeline {
    agent any
    stages {
        stage('Security Scan') {
            steps {
                sh 'pip install vulnscan'
                sh 'vulnscan scan --url ${APP_URL} --output json --output-file results.json'
                archiveArtifacts artifacts: 'results.json'
            }
        }
    }
}
```

## Configuration

Create a `vulnscan.yaml` configuration file:

```yaml
# Global settings
global:
  user_agent: "VulnScan/1.0"
  timeout: 30
  retries: 3
  follow_redirects: true

# Scanning options
scanning:
  concurrency: 10
  rate_limit: 20
  max_depth: 5
  
# Vulnerability checks
checks:
  enabled:
    - sql-injection
    - xss
    - rce
    - csrf
    - ssrf
    - path-traversal
    - authentication-bypass
  
  severity_threshold: medium

# Output settings
output:
  format: json
  verbosity: info
  include_false_positives: false

# CI/CD settings
ci_cd:
  fail_on_high: true
  fail_on_critical: true
```

## Custom Templates

Create custom scan templates in YAML format:

```yaml
name: "Custom Web Application Scan"
description: "Comprehensive scan for web applications"

targets:
  - type: web
    protocols: [http, https]

checks:
  - name: sql-injection
    payloads:
      - "' OR '1'='1"
      - "1' UNION SELECT NULL--"
    confidence: high
    
  - name: xss
    payloads:
      - "<script>alert('XSS')</script>"
      - "<img src=x onerror=alert('XSS')>"
    confidence: high

  - name: custom-check
    description: "Custom vulnerability check"
    request:
      method: POST
      path: /api/endpoint
      headers:
        Content-Type: application/json
      body: '{"test": "payload"}'
    matcher:
      - type: word
        words: ["error", "exception"]
      - type: status
        status: [500]
```

## API Reference

### Python API

```python
from vulnscan import Scanner, ScanConfig

# Initialize scanner
config = ScanConfig(
    url="https://example.com",
    checks=["sql-injection", "xss"],
    concurrency=10
)

scanner = Scanner(config)

# Run scan
results = scanner.scan()

# Process results
for vulnerability in results:
    print(f"Found {vulnerability.type} at {vulnerability.url}")
    print(f"Severity: {vulnerability.severity}")
    print(f"Description: {vulnerability.description}")
```

## Architecture

```
vulnscan/
├── core/
│   ├── scanner.py          # Main scanning engine
│   ├── detector.py         # Vulnerability detection logic
│   └── http_client.py      # HTTP/HTTPS client
├── checks/
│   ├── sql_injection.py    # SQL injection checks
│   ├── xss.py              # XSS vulnerability checks
│   ├── rce.py              # RCE detection
│   └── ...                 # Additional checks
├── templates/
│   └── *.yaml              # Scan templates
├── integrations/
│   ├── cicd.py             # CI/CD integrations
│   └── cloud.py            # Cloud provider integrations
├── reports/
│   └── generator.py        # Report generation
└── cli.py                  # Command-line interface
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- All tests pass
- Code follows PEP 8 style guidelines
- New features include unit tests
- Documentation is updated

## Security

If you discover a security vulnerability, please email security@vulnscan.dev instead of using the issue tracker.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by industry-leading security tools
- Built with modern Python async capabilities
- Community-driven vulnerability database

## Support

- Documentation: https://vulnscan.dev/docs
- Issue Tracker: https://github.com/Shanmukhasrisai/vulnscan/issues
- Discord: https://discord.gg/vulnscan
- Twitter: @vulnscan_dev

## Roadmap

- [ ] Machine learning-based vulnerability detection
- [ ] Browser automation for JavaScript-heavy applications
- [ ] Integration with vulnerability databases (NVD, CVE)
- [ ] Kubernetes security scanning
- [ ] Mobile application security testing (Android/iOS)
- [ ] Plugin system for custom extensions
- [ ] Real-time collaboration features
