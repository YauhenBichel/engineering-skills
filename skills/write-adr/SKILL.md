---
name: write-adr
description: Records an architecture decision as an ADR. Use when a technical choice is made that others will later ask about.
---

## Steps
1. Create `docs/adr/NNNN-short-title.md` (use the project's ADR folder if it has one; NNNN is the next number).
2. Add header: `# ADR-NNNN: Title`, `Status: Proposed | Accepted | Superseded`, `Date: YYYY-MM-DD`, `Author: Name`.
3. Write `## Context` describing the problem and constraints.
4. Write `## Decision` stating the chosen path clearly.
5. List `## Alternatives Considered` with brief pros/cons.
6. Write `## Consequences` covering benefits, costs, and downsides. Keep text to one page.
7. Link the ADR from the code or docs it affects, and commit it with the change it describes.

## Checklist
- [ ] File follows `adr-NNNN-kebab-case.md` naming.
- [ ] Status matches current project phase.
- [ ] Context cites exact files or commands affected.
- [ ] Decision uses active voice and avoids ambiguity.
- [ ] Alternatives list at least two options.
- [ ] Consequences explicitly state downsides.
- [ ] Date and author are current and accurate.
- [ ] Total length fits one page.

## Output
- The complete ADR markdown file content.
- The file path, and any earlier ADR it supersedes.
