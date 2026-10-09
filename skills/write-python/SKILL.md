---
name: write-python
description: Writes idiomatic, typed, testable Python. Use whenever writing Python code.
---

## Steps
1. Start every file with `from __future__ import annotations`. Use Python 3.11+ syntax and explicit type hints. Example: `def load(path: Path) -> dict[str, str]:`
2. Import only the standard library first. Prefer `pathlib.Path`, `dataclasses.dataclass`, and `logging.getLogger` over third-party packages.
3. Split logic into small functions with clear names. Keep modules stateless; pass configuration explicitly.
4. Raise and catch specific exceptions. Never use bare `except:`. Map external errors to domain-specific types.
5. Run `ruff check .` and `mypy --strict .` locally. Fix all warnings before committing.
6. Write docstrings that state the function's purpose and contract, not its implementation steps.

## Checklist
- [ ] `from __future__ import annotations` present at the top
- [ ] All public functions have type hints and a purpose-focused docstring
- [ ] Only standard library imports used where possible
- [ ] No global mutable state; configuration passed as arguments
- [ ] Specific exception types raised and caught
- [ ] `ruff check .` and `mypy --strict .` pass cleanly
- [ ] Tests cover happy path and error paths

## Output
- The complete Python file with imports, types, and docstrings
- A minimal test file using `pytest` and `unittest.mock`
- Commands to run `ruff` and `mypy` to verify the code
