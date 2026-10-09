---
name: write-docs
description: Writes documentation people use: README, how-to, reference. Use when documenting code or a project.
---

## Steps
1. Create `README.md` at the project root. State what the project does, its purpose, and its license.
2. Add `## Install` with exact commands (e.g., `pip install .`, `docker compose up`). Add `## Quick Start` with a minimal run command and expected output.
3. Add `## Examples` showing 2-3 concrete use cases. Use real file names and flags.
4. Write task-based how-to guides in `docs/`. Use copy-paste commands for each workflow. Keep sentences short and plain.
5. Place documentation next to the relevant code. Update files whenever the code changes.
6. State limitations, dependencies, and known issues explicitly. Remove marketing language.

## Checklist
- [ ] README covers purpose, install, quick start, examples, and limits.
- [ ] How-to guides contain copy-paste commands and plain explanations.
- [ ] All code snippets match current versions and dependencies.
- [ ] Documentation lives in the same repository, next to the code.
- [ ] No marketing language or vague claims remain.
- [ ] Known limitations and error cases are documented.
- [ ] Cross-references between README and `docs/` work.

## Output
- Updated `README.md` with install, quick start, examples, and limits.
- Task-specific guides in `docs/` with copy-paste commands.
- Diff or summary of documentation changes.
- Confirmation that docs stay alongside the source code.
