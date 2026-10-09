---
name: review-code
description: Reviews a change for bugs and risks. Use for pull requests, diffs or code the user asks you to check.
---

## Steps
1. Load the diff or target files. Identify changed functions and entry points.
2. Trace logic paths. Check boundary conditions, null inputs, and error returns. Example: verify `if not data:` guards before parsing.
3. Scan for secrets, unvalidated inputs, and injection vectors. Block raw `eval` or string interpolation.
4. Verify test coverage. Confirm new paths have assertions or mock calls. Run `pytest -k test_name`.
5. Rank findings by severity. Draft each as `file:line`, concrete breaking input, and fix. Skip style nitpicks unless they hide a bug.
6. State clearly if the code is clean.

## Checklist
- [ ] Logic handles empty, null, and overflow inputs.
- [ ] Error paths return or log without leaking state.
- [ ] No secrets in code, env, or logs.
- [ ] Inputs are validated before use.
- [ ] Tests cover all changed branches.
- [ ] Findings list file:line, trigger, and fix.
- [ ] Severity order matches risk level.

## Output
- List critical bugs first, then medium/low risks.
- Provide exact file:line, failing input, and corrected code snippet.
- State "No issues found" if checks pass.
- Keep recommendations actionable and minimal.
