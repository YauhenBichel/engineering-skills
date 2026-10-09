## Steps
1. Profile the target code. Run `py-spy record -o profile.svg` or `cProfile`. Capture baseline metrics.
2. Identify the bottleneck. Look for hot functions, memory spikes, or disk waits. Do not guess.
3. Fix the algorithm. Replace quadratic loops with hash maps. Cache repeated I/O. Reduce allocations.
4. Apply micro-optimizations only if the algorithm change is insufficient. Use vectorization or compiled extensions.
5. Check memory and I/O. Measure memory with `tracemalloc` or `/usr/bin/time -v`; watch I/O with `iostat` or the profiler's I/O view.
6. Run benchmarks. Compare before and after with `pytest-benchmark` or `time`. Record exact numbers.
7. Keep the code readable. Preserve structure. Add a comment noting the optimization and its measured gain.

## Checklist
- [ ] Baseline metrics captured before changes
- [ ] Bottleneck confirmed by profile data
- [ ] Algorithm changed before micro-optimizations
- [ ] Memory and I/O verified alongside CPU
- [ ] Benchmarks run with identical inputs
- [ ] Code passes existing tests
- [ ] Optimization gain recorded in comments or docs

## Output
- Baseline and optimized metrics with exact numbers
- Profile traces showing the resolved bottleneck
- Benchmark results confirming the speed or memory gain
- Updated code with readability preserved and gain documented
