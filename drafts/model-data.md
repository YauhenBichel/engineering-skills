## Steps
1. List entities, primary keys, and foreign keys. Define cardinality (1:1, 1:N, M:N).
2. Normalize first. Denormalize only for a measured need.
3. Add constraints in the database: `NOT NULL`, `UNIQUE`, `FOREIGN KEY`, `CHECK`. (SQLite: turn on `PRAGMA foreign_keys = ON;`.)
4. Choose indexes from the real queries and check them with the plan (`EXPLAIN` / `EXPLAIN QUERY PLAN`). Cover `WHERE`, `JOIN`, and `ORDER BY` columns.
5. Write migrations with the project's tool (Alembic, Django, Flyway, plain SQL files). Make changes safe on a live table: add nullable, backfill, then constrain; drop columns only in a later release.
6. Write sample queries for the main use cases. Test them against a seed dataset.

## Checklist
- [ ] All foreign keys reference existing primary keys.
- [ ] No nullable columns without explicit `NULL` handling.
- [ ] Indexes match live query plans, not guesses.
- [ ] Migrations are additive and reversible via rollback scripts.
- [ ] Cardinality matches domain rules, not assumptions.
- [ ] Sample queries return the expected rows on seed data.

## Output
- Schema definition with tables, columns, types, and constraints.
- Migration files and index DDL.
- Three representative queries with execution plans.
