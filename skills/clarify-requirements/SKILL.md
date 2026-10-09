---
name: clarify-requirements
description: Turns a vague request into a short, testable spec. Use at the start of any task whose goal, inputs, outputs or limits are not clear.
---

## Steps
1. Restate the goal in one sentence.
2. List inputs, outputs, constraints, and non-goals.
3. Write 3 to 6 acceptance criteria as checkable statements (e.g., `uv run pytest -q` exits 0).
4. List open questions that change the scope or implementation.
5. Ask the user only those questions.
6. Do not write code at this step.
7. If the user wants the spec kept, save it where they say (for example `docs/spec.md`); otherwise answer in the chat.

## Checklist
- [ ] Goal is one clear sentence.
- [ ] Inputs, outputs, constraints, and non-goals are explicit.
- [ ] 3 to 6 acceptance criteria are testable.
- [ ] Open questions are limited to scope-changing items.
- [ ] No code or implementation details are included.
- [ ] Every assumption made instead of asking is written down.

## Output
- A one-sentence goal restatement.
- A list of inputs, outputs, constraints, and non-goals.
- 3 to 6 acceptance criteria.
- A short list of open questions requiring user input.
