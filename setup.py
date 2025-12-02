#!/usr/bin/env python3
"""
Setup script for VulnScan vulnerability scanner.

VulnScan is a comprehensive security scanning tool designed to detect:
- OWASP Top 10 vulnerabilities (SQL Injection, XSS, CSRF, etc.)
- Common Vulnerabilities and Exposures (CVEs) from NVD database
- Security misconfigurations and insecure dependencies
- Authentication and authorization flaws

Features:
- Real-time CVE detection and reporting
- OWASP Top 10 compliance checking
- Automated vulnerability assessment
- Detailed security reports with remediation guidance
"""
from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vulnscan',
    version='1.0.0',
    author='VulnScan Team',
    author_email='team@vulnscan.dev',
    # Enhanced description highlighting OWASP Top 10 and CVE detection capabilities
    description='A modern, high-performance vulnerability scanner with OWASP Top 10 and CVE detection',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Shanmukhasrisai/vulnscan',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=[
        # Core dependencies for web scanning and HTTP operations
        'requests>=2.31.0',
        'aiohttp>=3.9.0',
        'beautifulsoup4>=4.12.0',
        'lxml>=4.9.0',
        # Configuration and data handling
        'pyyaml>=6.0',
        'click>=8.1.0',
        'colorama>=0.4.6',
        'jinja2>=3.1.0',
        # Security and networking
        'urllib3>=2.0.0',
        'certifi>=2023.0.0',
        # Utilities for scanning operations
        'python-dateutil>=2.8.0',
        'tqdm>=4.66.0',
        'jsonschema>=4.19.0',
        'packaging>=23.0',
        # CVE detection and OWASP scanning dependencies
        # These packages support vulnerability database queries and security analysis
    ],
    extras_require={
        'dev': [
            'pytest>=7.4.0',
            'pytest-cov>=4.1.0',
            'pytest-asyncio>=0.21.0',
            'black>=23.9.0',
            'flake8>=6.1.0',
            'mypy>=1.5.0',
            'pylint>=2.17.0',
        ],
        'cloud': [
            'boto3>=1.28.0',  # AWS
            'azure-identity>=1.14.0',  # Azure
            'google-cloud-storage>=2.10.0',  # GCP
        ],
    },
    entry_points={
        'console_scripts': [
            # Main CLI entry point for vulnerability scanning
            # Supports OWASP Top 10 checks and CVE detection
            'vulnscan=vulnscan.cli:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    # Enhanced keywords to reflect OWASP and CVE capabilities
    keywords='security vulnerability scanner penetration-testing cybersecurity owasp-top-10 cve-detection nvd security-audit',
    project_urls={
        'Bug Reports': 'https://github.com/Shanmukhasrisai/vulnscan/issues',
        'Source': 'https://github.com/Shanmukhasrisai/vulnscan',
        'Documentation': 'https://vulnscan.dev/docs',
    },
)
