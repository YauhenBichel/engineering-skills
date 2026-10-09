## Steps
1. Identify the riskiest unknown. Draft a task to probe it.
2. List all remaining work. Order by dependency.
3. Assign each task one outcome, one verification command (e.g., `uv run pytest tests/test_core.py`), and a size under four hours.
4. Insert a walking skeleton task early. Connect core modules with minimal glue code.
5. Mark independent work with `[parallel]`. Schedule it after the skeleton passes.
6. Review the list. Split any task longer than half a day. Reorder to expose risks early.

## Checklist
- [ ] Verify each task has one outcome and a verification command
- [ ] Verify tasks follow dependency order with riskiest unknown first
- [ ] Verify walking skeleton connects core paths before polishing
- [ ] Verify independent work is marked `[parallel]`
- [ ] Verify no task exceeds four hours of effort
- [ ] Verify verification uses concrete commands or file checks

## Output
- A numbered list of tasks with outcome, verification, and size
- Parallel markers and dependency notes where applicable
- A brief summary of the walking skeleton path
