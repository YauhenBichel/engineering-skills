---
name: concurrency
description: Writes correct concurrent or asynchronous code. Use for threads, async, parallel jobs, queues or shared state.
---

## Steps
1. Design around message passing or immutable data. Avoid mutable shared state.
2. Assign one clear owner per lock. Never perform I/O while holding a lock.
3. Attach timeouts and cancellation to every wait, channel read, or join call.
4. Use bounded queues for all producer-consumer flows. Apply back-pressure when queues fill.
5. Run the race detector (`go test -race`) and run concurrent tests many times (`go test -count=100`, `pytest-repeat`). Never hide flaky tests with automatic reruns.
6. Document ownership and flow in comments. Keep critical sections as short as possible.

## Checklist
- [ ] Shared mutable state is avoided or guarded by one owner
- [ ] Each lock has a single owner and zero I/O inside its scope
- [ ] Every wait includes a timeout and respects cancellation signals
- [ ] Queues are bounded with explicit back-pressure handling
- [ ] Race detector enabled and tests run multiple times
- [ ] Critical sections are short and documented
- [ ] Error paths release resources and propagate cancellation

## Output
- Code implementing the concurrency pattern with clear ownership
- Test suite with race detection and repeated execution flags
- Brief documentation of flow, timeouts, and failure modes
