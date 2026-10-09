## Steps
1. Mitigate immediately. Rollback the last deployment, disable the failing feature flag, or scale the affected service. Verify health endpoints return 200.
2. Assign one coordinator. Open `incident-timeline.md`. Log every action, timestamp, and result.
3. Broadcast status. Send plain-language updates to the team channel. State current impact, mitigation status, and next update time.
4. Investigate after stability. Check logs (`journalctl -u service`), metrics, and recent diffs. Isolate the root cause without blaming.
5. Draft the postmortem. Write impact, timeline, root cause, and follow-up actions with owners. Keep it blameless.
6. Schedule prevention. Add monitoring, add tests, or tighten deployment gates. Assign owners and deadlines.

## Checklist
- [ ] Service health restored and monitoring stable
- [ ] Timeline file updated with accurate timestamps
- [ ] Team notified of resolution and next steps
- [ ] Root cause identified without assigning blame
- [ ] Postmortem draft includes impact, timeline, cause, and owners
- [ ] Prevention actions assigned with deadlines
- [ ] Related alerts tuned to catch recurrence

## Output
- Incident timeline and mitigation summary
- Blameless postmortem draft with impact, root cause, and owner-assigned actions
- Prevention plan with monitoring or test updates
