## Steps
1. Fail loudly at the boundary. Never swallow errors.
2. Ensure errors carry context. Include the operation name and the exact input.
3. Use log levels consistently. Apply `INFO`, `WARNING`, `ERROR` by severity. Output structured JSON logs.
4. Exclude secrets and personal data from logs. Mask tokens, keys, and emails with `[REDACTED]`.
5. Limit retries to transient errors. Apply exponential backoff and a hard attempt limit.
6. Configure logging once, at program start. Write logs to `stderr`; for services, let the service manager (systemd, Docker) collect them.

## Checklist
- [ ] Exceptions propagate to the top-level handler without silent catches
- [ ] Error messages include operation name and input values
- [ ] Log levels match severity; services log structured lines (JSON)
- [ ] Sensitive fields are masked or removed before logging
- [ ] Retry logic targets only transient errors with backoff and a max count
- [ ] All log statements pass through the configured logger instance
- [ ] No raw secrets or PII appear in any log output

## Output
- Code with boundary exception handling and context-rich error messages
- Structured logging configuration and usage examples
- Retry wrapper with backoff and failure limits
- Checklist verification notes
