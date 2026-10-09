---
name: data-durability
description: Protects data: backups, restores, migrations without loss. Use when data must not be lost.
---

## Steps
1. List what must survive: databases, config, user files. Name the owner and how much loss is acceptable (hours, a day).
2. Back up with a tool that keeps versions and checks itself (restic, borg, or the database's own backup). A plain `rsync --delete` mirror is not a backup: it copies deletions and damage too.
3. Copy databases consistently: `sqlite3 db ".backup copy.db"`, `pg_dump`, or the engine's backup API. Never copy a live database file with `cp`.
4. Keep at least one copy on another disk and one outside the building (3-2-1).
5. Test a restore on a schedule: restore into an empty directory, open the files, run a query on each database.
6. In code: write a temporary file, `fsync` it, then rename it over the old one, so a crash never leaves half a file.
7. Before a risky change (migration, upgrade), take a backup and write down the restore command.

## Checklist
- [ ] Every important path is in the backup (check the backup's file list, not the config)
- [ ] Database copies are made with the engine's backup method
- [ ] A copy exists off-site
- [ ] The last restore test passed, and its date is known
- [ ] State files are written atomically (temp file, fsync, rename)
- [ ] A backup was taken before this change, and the restore command is written down

## Output
- What is backed up, where, how often, and the date of the latest backup
- Paths not covered, if any
- Result and date of the last restore test
- The restore command for the change at hand
