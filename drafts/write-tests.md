## Steps
1. Identify the target function or module. Create `test_<module>.py` in the project test directory.
2. Write one test per behavior. Name it `test_<behavior>_<expected_outcome>`.
3. Structure each test with `arrange`, `act`, `assert`. Store the result in `got` before checking.
4. Add edge cases and error paths. Fake external calls; no real network or clock in unit tests; files only in a temporary directory (`tmp_path`).
5. Write integration tests for the main paths. Use real dependencies or lightweight fakes at the boundary.
6. Run the suite. Fix failures without weakening a test to make it pass.
7. Check that each new test fails when the code it tests is broken (change one line and run it).

## Checklist
- [ ] Each test covers exactly one behavior with a descriptive name.
- [ ] `arrange`, `act`, `assert` structure is explicit; result stored in `got`.
- [ ] Edge cases and error paths are included.
- [ ] Unit tests use no real network or clock; files only in a temporary directory.
- [ ] Integration tests cover main paths with boundary fakes.
- [ ] All tests pass without weakened assertions or skipped cases.
- [ ] Test file follows project naming and directory conventions.

## Output
- The new test file(s) with complete implementations.
- Command to run the tests and the exit code.
- Brief summary of covered behaviors and boundary conditions.
