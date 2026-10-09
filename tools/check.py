"""Check every skills/<name>/SKILL.md: front matter name (= folder) and description, the three sections, length."""
import pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
bad = []
skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
for f in skills:
    text = f.read_text()
    _, front, body = text.split("---", 2) if text.startswith("---") else ("", "", text)
    meta = dict(l.split(":", 1) for l in front.strip().splitlines() if ":" in l)
    name = f.parent.name
    if meta.get("name", "").strip() != name:
        bad.append(f"{name}: front matter name is not the folder name")
    if not meta.get("description", "").strip():
        bad.append(f"{name}: no description")
    for section in ("## Steps", "## Checklist", "## Output"):
        if section not in body:
            bad.append(f"{name}: no '{section}'")
    if len(body.split()) > 350:
        bad.append(f"{name}: {len(body.split())} words, over 350")
print(f"{len(skills)} skills checked, {len(bad)} problems")
print("\n".join(bad))
sys.exit(1 if bad or not skills else 0)
