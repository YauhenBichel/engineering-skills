
## Steps
1. Identify the entry point and file path.
2. Read the file and the modules it imports that matter for the question.
3. Follow the data from the entry point (a `main`, a handler, a public function) to what it returns or writes.
4. Quote the exact lines that drive the logic.
5. Note dependencies and external calls.
6. Summarize the behavior in plain terms.

## Checklist
- [ ] Verified file path and import chain
- [ ] Quoted critical lines verbatim
- [ ] Named all inputs and outputs
- [ ] Flagged missing or optional dependencies
- [ ] Checked for dynamic code or eval usage
- [ ] Said what is not known instead of guessing
- [ ] Kept sentences under 20 words

## Output
- One-sentence purpose statement
- Clear input/output mapping with quoted lines
- Dependency and call-chain summary
- Plain-language behavior description
