## Steps
1. State constraints: target load, latency budget, data volume, team size, and runtime environment.
2. Draft two architectures. Compare cost, complexity, and scalability. Recommend one.
3. Define components. Assign exactly one responsibility per component. Name interfaces (e.g., `api/v1/`, gRPC proto).
4. Map data flow. Mark sync vs async paths. Pin state location (e.g., `state/` dir, Redis, SQLite).
5. List failure modes. Attach retries, fallbacks, circuit breakers, or degradation paths.
6. Generate a mermaid diagram. Show components, state stores, and failure routes.
7. Validate against constraints. Cut scope if latency or cost exceeds limits.

## Checklist
- [ ] Constraints explicitly stated with numbers
- [ ] Two options compared with clear trade-offs
- [ ] Each component has exactly one responsibility
- [ ] State location defined for every path
- [ ] Failure modes mapped to specific handlers
- [ ] Mermaid diagram matches described flow
- [ ] Scope trimmed to meet latency/cost limits

## Output
- Constraint list and chosen architecture
- Component table with responsibilities and interfaces
- Mermaid diagram and state map
- Failure handling matrix
