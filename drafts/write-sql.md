## Steps
1. Write the query or migration as a file the project tracks (for example `migrations/NNNN_name.sql`).
2. Replace all literals with parameter placeholders (`$1`, `?`, or `:name`). Never concatenate values into SQL strings.
3. Run `EXPLAIN ANALYZE` on the query. Add indexes if the plan shows sequential scans on large tables.
4. Wrap multi-statement changes in `BEGIN;` and `COMMIT;`. Ensure automatic rollback on error.
5. Apply the migration to a copy of the database first. On a live table: add columns nullable, backfill in batches, then add constraints.
6. Verify row counts, constraints and data integrity on the copy, and that the reverse migration works.
7. Take a backup, then apply the verified migration to production during a low-traffic window.

## Checklist
- [ ] All inputs use parameterized placeholders
- [ ] EXPLAIN plan confirms index usage or acceptable scan depth
- [ ] Migration adds columns nullable first, backfills data, then adds constraints
- [ ] All writes are wrapped in a transaction
- [ ] Changes tested on a staging copy with matching schema
- [ ] Rollback script or reverse migration is documented
- [ ] No secrets or PII are logged or returned

## Output
- The final SQL or migration file with parameters and transaction boundaries
- The EXPLAIN output and index recommendations
- The staging copy verification results and rollback instructions
