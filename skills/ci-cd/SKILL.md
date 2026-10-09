---
name: ci-cd
description: Sets up or fixes continuous integration and delivery. Use for GitHub Actions or other pipelines.
---

## Steps
1. Align CI commands with local tooling: `ruff check`, `mypy`, `pytest`, `uv build`.
2. Cache dependencies and fail fast. Store `~/.cache/pip` or `~/.local/share/uv`. Run lint and type checks before tests.
3. Pin every `uses:` action to a full SHA. Set `permissions:` to the least the job needs (for example `contents: read`).
4. Gate deployment to `main` branch pushes only after a green CI run. Tag releases immediately for rollback.
5. When CI fails, read the failing step's log and run the same command locally before editing code or configuration. Do not call a failure flaky until it is reproduced or explained.

## Checklist
- [ ] Local and CI commands match exactly
- [ ] Dependencies cached and lint/type checks run first
- [ ] Action versions pinned to SHAs
- [ ] Workflow `permissions:` set to the minimum
- [ ] Deploy gate set to main branch only
- [ ] Rollback procedure documented
- [ ] Failing log analyzed before changes

## Output
- Updated workflow file with exact commands and cache keys
- Permission scope and token configuration
- Rollback instructions and deployment trigger rules
- Link to the analyzed failure log
