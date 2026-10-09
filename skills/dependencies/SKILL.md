---
name: dependencies
description: Adds, upgrades or removes dependencies safely. Use when changing what a project depends on.
---

## Steps
1. Check the standard library first. Justify every new package by stating the exact gap it fills.
2. Verify license compatibility, recent commit activity, and package size before installing.
3. Commit the lockfile (`uv.lock`, `package-lock.json`, `go.sum`). Applications pin exact versions; libraries declare compatible ranges and leave pinning to the application.
4. Read the changelog or release notes for breaking changes, deprecations, and migration steps.
5. Upgrade or add one dependency at a time. Run the full test suite after each change.
6. Remove unused dependencies. Audit the lockfile and update the dependency graph.

## Checklist
- [ ] Standard library checked first
- [ ] License, maintenance, and size verified
- [ ] Versions pinned in lockfile
- [ ] Changelog reviewed for breaking changes
- [ ] Tests pass after single dependency change
- [ ] Unused packages removed
- [ ] Documentation updated if needed

## Output
- List of added, upgraded, or removed packages with pinned versions
- Test results and any migration notes from the changelog
- Updated lockfile and dependency graph diff
