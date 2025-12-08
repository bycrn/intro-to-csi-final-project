# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.1   | :white_check_mark: |
| 1.0.0   | :x:                |

## Security Updates

### Version 1.0.1 (Current - Secure)
All known vulnerabilities have been patched. This version includes:

- ✅ FastAPI 0.115.5 (patched ReDoS vulnerability)
- ✅ python-multipart 0.0.18 (patched DoS and ReDoS vulnerabilities)
- ✅ Pillow 11.0.0 (patched buffer overflow vulnerability)
- ✅ PyTorch 2.6.0 (patched heap buffer overflow, use-after-free, and RCE vulnerabilities)
- ✅ All other dependencies updated to latest secure versions

### Version 1.0.0 (Deprecated - Vulnerable)
Contains multiple security vulnerabilities. **Do not use in production.**

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it by:

1. **Do NOT** open a public issue
2. Email the security concern to the project maintainers
3. Include detailed information:
   - Type of vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work to address the issue promptly.

## Security Best Practices

### For Production Deployment

#### 1. Environment Variables
Never commit sensitive information. Use environment variables:
```bash
# Set in production environment
export ALLOWED_ORIGINS=https://yourdomain.com
export FIREBASE_CREDENTIALS_PATH=/secure/path/to/credentials.json
```

#### 2. CORS Configuration
Restrict CORS to specific domains:
```bash
# .env file
ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

#### 3. HTTPS/SSL
Always use HTTPS in production:
- Obtain SSL certificate (Let's Encrypt recommended)
- Configure reverse proxy (Nginx, Caddy)
- Redirect HTTP to HTTPS

#### 4. File Upload Security
The application includes file type validation, but also:
- Set maximum file size limit
- Scan uploaded files for malware
- Store uploads in isolated directory
- Implement rate limiting

#### 5. Dependencies
Keep dependencies updated:
```bash
# Backend
cd backend
pip install --upgrade -r requirements.txt

# Frontend
cd frontend
npm update
```

#### 6. Docker Security
When using Docker:
- Run containers as non-root user
- Use minimal base images
- Scan images for vulnerabilities
- Keep Docker updated

#### 7. API Security
- Implement rate limiting (e.g., with slowapi)
- Add request validation
- Use API keys for authentication (if needed)
- Log security events
- Monitor for suspicious activity

#### 8. Model Security
When loading PyTorch models:
- Only load models from trusted sources
- Use `weights_only=True` parameter
- Verify model checksums
- Store models securely

### Security Headers

Add these headers in production:
```python
# In main.py or nginx config
headers = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "Content-Security-Policy": "default-src 'self'"
}
```

### Rate Limiting Example

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/classify")
@limiter.limit("10/minute")
async def classify_waste(request: Request, file: UploadFile = File(...)):
    # Classification logic
    pass
```

### Input Validation

The application validates:
- ✅ File type (images only)
- ✅ File format (PIL Image verification)
- ✅ Response structure

Consider adding:
- File size limits (e.g., max 10MB)
- Image dimension limits
- Request body size limits

## Vulnerability Disclosure History

### 2024-12-08 - Multiple Critical Vulnerabilities Patched

#### CVE-Related Issues
1. **FastAPI ReDoS** (CVE-2024-XXXXX)
   - Affected: fastapi <= 0.109.0
   - Fixed: Updated to 0.115.5
   - Impact: Denial of Service via Content-Type header

2. **python-multipart DoS** (CVE-2024-XXXXX)
   - Affected: python-multipart < 0.0.18
   - Fixed: Updated to 0.0.18
   - Impact: DoS via malformed multipart boundary

3. **python-multipart ReDoS** (CVE-2024-XXXXX)
   - Affected: python-multipart <= 0.0.6
   - Fixed: Updated to 0.0.18
   - Impact: ReDoS via Content-Type header

4. **Pillow Buffer Overflow** (CVE-2024-XXXXX)
   - Affected: pillow < 10.3.0
   - Fixed: Updated to 11.0.0
   - Impact: Buffer overflow vulnerability

5. **PyTorch Heap Buffer Overflow** (CVE-2024-XXXXX)
   - Affected: torch < 2.2.0
   - Fixed: Updated to 2.6.0
   - Impact: Heap buffer overflow

6. **PyTorch Use-After-Free** (CVE-2024-XXXXX)
   - Affected: torch < 2.2.0
   - Fixed: Updated to 2.6.0
   - Impact: Use-after-free vulnerability

7. **PyTorch RCE** (CVE-2024-XXXXX)
   - Affected: torch < 2.6.0
   - Fixed: Updated to 2.6.0
   - Impact: Remote code execution via torch.load

**Status**: All vulnerabilities patched in version 1.0.1

## Security Checklist for Deployment

- [ ] Update to version 1.0.1 or later
- [ ] Enable HTTPS/SSL
- [ ] Configure CORS with specific origins
- [ ] Set up rate limiting
- [ ] Configure firewall rules
- [ ] Set maximum file upload size
- [ ] Use strong passwords for any admin interfaces
- [ ] Enable security logging
- [ ] Set up monitoring and alerts
- [ ] Regular security audits
- [ ] Keep dependencies updated
- [ ] Backup critical data
- [ ] Test disaster recovery procedures
- [ ] Review and update security policies regularly

## Security Tools

### Recommended Tools
- **Bandit**: Python security linter
- **Safety**: Dependency vulnerability checker
- **OWASP ZAP**: Web application security scanner
- **Snyk**: Continuous security monitoring
- **Trivy**: Container security scanner

### Running Security Checks

```bash
# Check Python dependencies
pip install safety
safety check -r requirements.txt

# Scan for security issues
pip install bandit
bandit -r backend/

# Scan Docker images
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image your-image:tag
```

## Compliance

This project follows:
- OWASP Top 10 security guidelines
- CWE/SANS Top 25 security practices
- Secure coding standards

## Updates

Security updates are released as needed. Subscribe to repository notifications to stay informed about security releases.

## Contact

For security concerns, contact the project maintainers through:
- GitHub Security Advisories
- Project issue tracker (for non-critical issues)

---

**Last Updated**: 2024-12-08
**Security Version**: 1.0.1
