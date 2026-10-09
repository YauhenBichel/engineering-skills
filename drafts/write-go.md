## Steps
1. Follow `gofmt` and `go vet` rules. Return errors instead of panicking.
2. Wrap errors with `fmt.Errorf("context: %w", err)`. Never drop the original cause.
3. Define small interfaces where the consumer dictates behavior.
4. Write functions with `context.Context` as the first argument for all I/O.
5. Write table-driven tests in `*_test.go`. Run `go test -race ./...`.
6. Avoid global mutable state. Use constructor functions to initialize and return configured structs.

## Checklist
- [ ] `context.Context` is the first parameter on all I/O functions.
- [ ] Errors are returned and wrapped with `%w`.
- [ ] No panics outside of unrecoverable fatal conditions.
- [ ] Interfaces are defined by the package that uses them.
- [ ] All state is initialized via constructors.
- [ ] Table-driven tests cover main paths and errors.
- [ ] `go vet` and `go test -race` pass cleanly.

## Output
- The complete Go source file(s) with correct package declaration and imports.
- The corresponding `*_test.go` file with table-driven tests.
- Terminal commands to verify formatting, vetting, and race detection.
- A brief constructor usage example if the struct requires configuration.
