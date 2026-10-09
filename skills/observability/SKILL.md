---
name: observability
description: Makes a service observable: logs, metrics, traces, alerts. Use when running anything in production.
---

## Steps
1. Instrument the four signals: latency, traffic, errors, saturation. Add request counters, failure counters, and response time histograms. Track CPU, memory, and disk usage.
2. Generate a unique request ID at the gateway. Write structured logs as JSON with a `request_id` field. Pass the ID on in outbound HTTP headers.
3. Export traces across service boundaries. Set `OTEL_EXPORTER_OTLP_ENDPOINT` to the collector. Tag every span with the request ID and service name.
4. Configure alerts on user symptoms, with limits taken from the service's goals (for example p95 latency, error rate, disk almost full). Link each alert to a short runbook that says what to check first.
5. Build two dashboards. The health page shows uptime, error rate, and resource saturation. The speed page shows p50, p95, and p99 latency over time.
6. Verify data flow. Confirm metrics hit the time-series database, logs reach the aggregator, and traces chain correctly.

## Checklist
- [ ] Metrics emit latency, traffic, errors, and saturation
- [ ] Every log line contains a request ID
- [ ] Traces cross service boundaries with shared request IDs
- [ ] Alerts fire on user symptoms, not internal metrics
- [ ] Each alert links to a runbook
- [ ] Health dashboard shows system status
- [ ] Speed dashboard shows latency percentiles
- [ ] One test alert was sent and received

## Output
- Confirmation of instrumentation points and metric names
- Links to the health and speed dashboards
- Alert rules with runbook references
- Sample trace showing cross-service request ID propagation
