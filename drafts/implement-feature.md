## Steps
1. Read the surrounding code and follow its patterns. Note imports, class structure, and error handling conventions.
2. Identify the smallest change that delivers the acceptance criteria.
3. Write tests for the new behaviour in `tests/test_<feature>.py`. Write them before or alongside the code.
4. Handle errors at boundaries. Raise explicit exceptions or return `Optional` types. Never swallow failures.
5. Run the tests and linters: `uv run pytest tests/test_<feature>.py -v` and `uv run ruff check .`.
6. Summarise what changed and how it was checked.

## Checklist
- [ ] Tests cover happy path and boundary inputs
- [ ] No silent failures or bare `except` clauses
- [ ] `uv run pytest` passes locally
- [ ] `uv run ruff check .` reports no errors
- [ ] Existing tests remain green
- [ ] Diff matches acceptance criteria exactly
- [ ] Documentation or docstrings updated if needed

## Output
- Brief summary of files changed and logic added
- Commands run and their exit codes
- Link to the test file and relevant diff
- Confirmation that linters and tests pass
