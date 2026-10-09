## Steps
1. Check git status and diff. Run `git status` and `git diff`. Stage only the logical change.
2. Create a branch per change. Run `git checkout -b fix/short-description`.
3. Commit one logical change. Run `git commit -m "fix: update auth timeout"`. Keep the subject under 72 characters. Use imperative mood.
4. Open a pull request with what and why. Run `git push -u origin branch-name`. Draft the PR description with a clear title, the what, and the why.
5. Update the branch. Rebase or merge per project convention. Run `git rebase main` or `git merge main`. Resolve conflicts locally.
6. Never force-push shared branches. Never commit secrets. Scan staged files with `git diff --cached` before pushing.

## Checklist
- [ ] One logical change per commit
- [ ] Subject line under 72 characters and imperative
- [ ] Branch created for this change only
- [ ] PR description states what and why
- [ ] No secrets in staged files or commit messages
- [ ] Branch rebased or merged per project convention
- [ ] `git status` and `git diff` verified clean

## Output
- The exact commands to run for branching, committing, and pushing
- The PR description text with what and why filled in
- Confirmation that secrets are excluded and the diff is clean
