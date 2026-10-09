---
name: write-typescript
description: Writes safe, typed TypeScript for Node or the browser. Use whenever writing TypeScript or JavaScript.
---

## Steps
1. Enable strict mode in `tsconfig.json`. Set `"strict": true` and `"noImplicitAny": true`. Never use `any`. Use `unknown` at API boundaries and narrow it immediately with type guards.
2. Validate all external input. Use Zod schemas or explicit hand checks. Fail fast with descriptive errors before processing.
3. Write all I/O with `async/await`. Catch errors where you can handle them or add context; otherwise let them propagate. Never fire-and-forget: await every promise or pass it to `Promise.all`.
4. Keep modules small. One responsibility per file. Export only what is needed. Use named exports over default exports.
5. Add tests immediately. Use the project runner (`vitest`, `jest`, or `node:test`). Test happy paths, validation failures, and async timeouts.

## Checklist
- [ ] `tsconfig.json` has `"strict": true` and no `any` types
- [ ] External data passes Zod schema or explicit guard functions
- [ ] Every promise is awaited; errors are handled or propagated, never ignored
- [ ] No unhandled promise rejections or fire-and-forget calls
- [ ] Modules are small, with named exports and one responsibility
- [ ] Tests cover validation, async flows, and edge cases
- [ ] `npm test` or `pnpm test` passes locally

## Output
- `src/module.ts` with strict types, Zod validation, and async handlers
- `src/module.test.ts` with runner-specific assertions
- `tsconfig.json` diff if strict mode or paths changed
- Brief run instructions for the test suite
