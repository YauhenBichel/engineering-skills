## Steps
1. Create `main.py` (or `main.go`/`main.rs`). Import `argparse`, `click`, or `cobra`.
2. Define arguments and flags. Ensure `--help` prints a clear explanation for every option.
3. Prompt only when `sys.stdin.isatty()` is true; otherwise require the value as a flag and fail with a usage error.
4. Execute core logic. Catch exceptions. Write errors to `stderr` with a concrete fix hint.
5. Format output. Default to human-readable text. Enable `--json` for machine-readable output.
6. Set exit codes: `0` for success, `1` for failure, `2` for usage errors.
7. Write tests in `tests/test_main.py`. Call `main()` directly with explicit argument lists.
8. Register the command as an entry point (`[project.scripts]` in `pyproject.toml`, or `go install`).

## Checklist
- [ ] `--help` lists every flag with a one-line explanation.
- [ ] Exit codes match: 0 ok, 1 failure, 2 usage.
- [ ] `--json` flag outputs valid JSON. Default output is plain text.
- [ ] All errors go to `stderr`. Each error includes a concrete fix hint.
- [ ] No interactive prompt when stdin is not a terminal.
- [ ] Tests call `main()` with explicit arguments. No subprocess calls in tests.
- [ ] Entry point uses `if __name__ == "__main__":` guard.

## Output
- The complete source file with argument parsing and exit code handling.
- A test file that invokes `main()` directly with sample arguments.
- A one-line usage example showing the `--json` flag and expected output.
