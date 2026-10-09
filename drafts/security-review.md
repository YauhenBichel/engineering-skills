## Steps
1. Trace all untrusted inputs. Validate types, lengths, and formats. Reject malformed data immediately.
2. Block injection vectors. Use parameterized queries for SQL. Quote shell arguments. Validate paths against a strict whitelist.
3. Enforce authentication and authorization on every entry point. Check roles before processing requests.
4. Audit secret storage. Move keys, tokens, and passwords to environment variables or a vault. Never log them or leak them in error traces.
5. Scan dependencies for known vulnerabilities. Run `pip-audit`, `npm audit`, or `govulncheck` on `requirements.txt`, `package.json`, or `go.mod`. Update or pin affected packages.
6. Apply least privilege. Run processes as non-root users. Set file permissions to `600` or `700`. Restrict network bindings to `127.0.0.1` unless public access is required.
7. Draft the report. Assign severity, describe impact, and state the exact fix.

## Checklist
- [ ] All external inputs validated and sanitized
- [ ] SQL, shell, and path injection vectors blocked
- [ ] Authn and authz enforced on every route
- [ ] Secrets isolated in environment variables or vaults
- [ ] Dependency scan shows zero critical or high CVEs
- [ ] Service runs with minimal file, user, and network permissions
- [ ] Logs carry no secrets or personal data; users never see stack traces

## Output
- List each finding with severity, affected file, and exact remediation step
- Include the dependency audit command and results
- State plainly which areas were not reviewed
