# engineering-skills

34 skills for software and computer science project work: from a vague request to a released, running,
documented system. Each skill is a short, checkable method in the
[Agent Skills](https://agentskills.io) format, written so that local models can follow it.

## What is in it

| Area | Skills |
|---|---|
| Plan | `clarify-requirements`, `break-down-work`, `estimate-and-risks` |
| Design | `design-architecture`, `write-adr`, `design-api`, `model-data` |
| Build | `implement-feature`, `write-python`, `write-go`, `write-typescript`, `write-sql`, `write-cli`, `concurrency`, `algorithms` |
| Quality | `write-tests`, `debug`, `review-code`, `refactor`, `performance`, `security-review`, `handle-errors-and-logging` |
| Ship | `git-workflow`, `ci-cd`, `containers-and-deploy`, `dependencies` |
| Operate | `observability`, `incident-response`, `data-durability` |
| Communicate | `write-docs`, `explain-code` |
| Data | `data-analysis`, `ml-experiment` |
| Research | `research-and-compare` |

`SKILLS.md` lists every skill with one line on when to use it.

Each `skills/<name>/SKILL.md` has front matter (`name`, `description`) and three sections:

- **Steps**: what to do, in order, with real commands.
- **Checklist**: what to check before saying the work is done.
- **Output**: what the answer must contain.

Each skill is under about 300 words. Local models follow short, direct steps better than long essays. The
skills work with any model.

## Use them

- **Continue (VS Code):** `python3 tools/build.py --install` writes each skill as a slash command
  (`~/.continue/prompts/skill-<name>.md`) and a rule that lists them (`~/.continue/rules/05-skills.md`).
  Then type `/debug`, `/write-tests`, ... in the chat.
- **[yserver-vscode](https://github.com/YauhenBichel/yserver-vscode):** set `yserver.skillsDirs` to this
  repository's `skills` folder, then run a skill on the selected code with Cmd+Alt+S.
- **Claude Code and other Agent Skills tools:** copy or link a skill folder into their skills folder.
- **Any chat:** paste a `SKILL.md` as the system prompt, or in front of your question.

## Guessing the skill from a message

`tools/examples.jsonl` has 244 example messages (6 for each skill, plus 40 that need no skill), and
`tools/examples-test.jsonl` has 142 more, written separately, for testing. A program can pick a skill
for a message by finding the nearest examples (embeddings), with the "none" examples competing.

`python3 tools/measure_guess.py` measures it. With bge-m3 embeddings and the default limits (k 2,
threshold 0.55, margin 0.06): of the 102 test messages that need a skill, 30 got the right skill, 1 got
a wrong one, and 71 got none; none of the 40 messages that need no skill got one. Matching the skill
descriptions instead was wrong more often than right. All examples were written by a model, so real
messages may score lower.

## How they were made

1. `tools/catalogue.json` lists each skill: area, name, description and the points it must cover.
2. `tools/draft.py` drafted each skill with a local model (qwen3.6-coder 35B) through an OpenAI-compatible
   API: `OPENAI_BASE_URL` (default `http://localhost:8080/v1`), `OPENAI_MODEL`, `OPENAI_API_KEY`.
   `drafts.log` records the time each one took.
3. Every draft in `drafts/` was then read and corrected by hand. Typical fixes: limits the model made up
   ("files under 150 lines"), advice that was wrong (an `rsync --delete` mirror called a backup, automatic
   reruns that hide flaky tests), and project-specific paths that do not belong in a general skill.
4. `tools/build.py` turns `drafts/` plus the catalogue into `skills/` and `SKILLS.md`.

To change a skill, edit its file in `drafts/` and run `python3 tools/build.py`.

## Limits

- Written and checked by one person.
- Not yet measured: how much a skill improves answers. A test with and without the skills is planned.

## License

Apache-2.0. Part of [yserver](https://github.com/YauhenBichel/yserver-local-llm-system), a home LLM server.
