## Steps
1. Run `uv run pytest` or `npm test`. Verify all tests pass.
2. Add characterization tests if missing.
3. Apply one small structural change: rename, extract method, or move file.
4. Run tests immediately. Keep no behaviour change mixed in.
5. Commit with a single-purpose message: `refactor: rename X to Y`.
6. Repeat steps 3–5 until the target structure is clear.
7. Stop when the target change becomes easy.

## Checklist
- [ ] All existing tests pass before and after each step.
- [ ] Characterization tests cover the modified code paths.
- [ ] Each commit contains only one type of structural change.
- [ ] No new features, bug fixes, or style changes are mixed in.
- [ ] `ruff check .` and `uv run pytest` report clean output.
- [ ] Git diff shows only whitespace, names, or extracted/moved blocks.
- [ ] The target module is now readable and ready for the next feature.

## Output
- Summary of the structural change applied.
- List of modified files and commit hashes.
- Test results and lint status.
- Next recommended step if the target is not yet reached.
