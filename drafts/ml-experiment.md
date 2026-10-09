## Steps
1. Fix the train/validation/test split and save it (for example `data/split.csv`). When rows are related (same user, subject or session), split by that group so none appears in two sets.
2. Run a simple baseline (majority class or mean prediction). Save scores to `baseline_results.json`.
3. Select the primary metric (e.g., `roc_auc` or `f1`) before training. Write it to `config.yaml`.
4. Run `uv run python train.py --seed <N>` for at least three seeds. Save weights to `models/seed_<N>/`.
5. Evaluate each seed on the test set. Compute mean and standard deviation.
6. Log config, data version hash, and metrics to `logs/run_<ID>.jsonl`.
7. Compare model results against the baseline. Report absolute improvement and statistical significance.

## Checklist
- [ ] Split file exists and matches data schema
- [ ] Baseline metrics recorded before training starts
- [ ] Primary metric defined in config
- [ ] At least three seeds run and evaluated
- [ ] Data version (a hash of the data files) is recorded
- [ ] Test set untouched during tuning
- [ ] Results logged with exact config hash

## Output
- `baseline_results.json` with raw scores
- `logs/run_<ID>.jsonl` with config, data hash, and per-seed metrics
- Comparison table showing mean, spread, and delta vs baseline
- Final verdict: pass or fail against threshold
