"""Turn the reviewed drafts into skills, and install them where the local tools read them.

  python3 tools/build.py                 drafts/<name>.md + catalogue.json -> skills/<name>/SKILL.md
  python3 tools/build.py --install       also: Continue slash commands (~/.continue/prompts/<name>.md)
                                         and one Continue rule that tells the model which skills exist

skills/<name>/SKILL.md follows the Agent Skills format (front matter `name` and `description`), so any
tool that reads that format can use the same files.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONTINUE = pathlib.Path.home() / ".continue"
PREFIX = "skill-"          # Continue prompt files this tool owns; others are left alone


def skills() -> list[dict]:
    out = []
    for s in json.load(open(ROOT / "tools/catalogue.json")):
        draft = ROOT / "drafts" / f"{s['name']}.md"
        if draft.exists():
            out.append({**s, "body": draft.read_text().strip()})
    return out


def build(items: list[dict]) -> None:
    for s in items:
        d = ROOT / "skills" / s["name"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(f"---\nname: {s['name']}\ndescription: {s['description']}\n---\n\n{s['body']}\n")
    rows = "\n".join(f"| {s['area']} | [{s['name']}](skills/{s['name']}/SKILL.md) | {s['description']} |" for s in items)
    (ROOT / "SKILLS.md").write_text(f"# Skills\n\n| Area | Skill | When to use |\n|---|---|---|\n{rows}\n")


def install(items: list[dict]) -> None:
    prompts, rules = CONTINUE / "prompts", CONTINUE / "rules"
    prompts.mkdir(parents=True, exist_ok=True)
    rules.mkdir(parents=True, exist_ok=True)
    for old in prompts.glob(PREFIX + "*.md"):
        old.unlink()
    for s in items:
        (prompts / f"{PREFIX}{s['name']}.md").write_text(
            f"---\nname: {s['name']}\ndescription: {s['description']}\ninvokable: true\n---\n\n"
            f"Follow this skill for the user's request (and the selected code, if any).\n\n{s['body']}\n")
    listing = "\n".join(f"- /{s['name']}: {s['description'].split('. Use')[0]}." for s in items)
    (rules / "05-skills.md").write_text(
        "---\nname: Skills\nalwaysApply: true\ndescription: Which skills exist\n---\n"
        "These slash commands hold the step-by-step method for each kind of work. When a request is clearly one of them, "
        "follow that method; if the user did not call it, you may suggest it.\n\n" + listing + "\n")


if __name__ == "__main__":
    items = skills()
    build(items)
    if "--install" in sys.argv:
        install(items)
    print(f"{len(items)} skills built" + (", installed in Continue" if "--install" in sys.argv else ""))
