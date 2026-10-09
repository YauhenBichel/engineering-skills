---
name: debug
description: Finds the root cause of a bug methodically. Use for errors, crashes, wrong results or flaky behaviour.
---

## Steps
1. Reproduce the bug with the smallest input. Run `pytest tests/test_bug.py` or the exact failing command in isolation.
2. Read the full error and stack trace. Record the exception type, file path, and line number.
3. Form one hypothesis. Test it using logs, a debugger, or `git bisect`. Do not guess.
4. Find the root cause, not the symptom. Verify the failing condition matches your hypothesis.
5. Write a failing test that captures the exact failure. Run it to confirm it fails.
6. Apply the fix. Run the full test suite. Show the new test passing and existing tests green.
7. Scan related code paths. Note what else the cause may affect and log follow-up tasks.

## Checklist
- [ ] Reproduction is minimal and deterministic
- [ ] Full stack trace and error context are captured
- [ ] Single hypothesis tested with evidence
- [ ] Root cause identified, not a symptom workaround
- [ ] Failing test written and confirmed to fail before the fix
- [ ] Fix applied and all tests pass
- [ ] Related code paths reviewed for side effects

## Output
- Minimal reproduction command or test case
- Root cause explanation with file and line reference
- Failing test code and the applied fix
- List of affected code paths or follow-up tasks
