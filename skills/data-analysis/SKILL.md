---
name: data-analysis
description: Analyses a dataset correctly and reports what it shows. Use for questions answered from data files or databases.
---

## Steps
1. Load the dataset. Print shape, column dtypes, null counts, and duplicate rows.
2. State the exact question and the target metric. Define the calculation formula.
3. Write a reproducible script (e.g., `analyze.py` or `query.sql`). Apply filters, compute the metric, and save outputs to `results.json` or `output.csv`.
4. Check results with a second method. Use a different aggregation path, a SQL window function, or a bootstrap sample. Compare outputs.
5. Report numbers with uncertainty. Add confidence intervals, standard errors, or margin of error. Note sampling bias, missing data, or time-window constraints.
6. Run the script end-to-end. Attach the code and raw output. Do not paste manual steps.

## Checklist
- [ ] Data path and version confirmed
- [ ] Shape, dtypes, nulls, and duplicates inspected
- [ ] Question and metric explicitly defined
- [ ] Reproducible script written and executed
- [ ] Result cross-checked with a second method
- [ ] Uncertainty bounds or error margins calculated
- [ ] Caveats and data limitations documented

## Output
- Metric value with confidence interval or error bounds
- Key patterns, thresholds, or outliers identified
- Data limitations, assumptions, and filtering rules
- Link to the reproducible script and raw output files
