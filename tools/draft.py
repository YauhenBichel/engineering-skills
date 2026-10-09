"""Draft each skill of catalogue.json with a model behind an OpenAI-compatible API. Writes drafts/<name>.md.

OPENAI_BASE_URL (default http://localhost:8080/v1), OPENAI_API_KEY, OPENAI_MODEL (default "local").
Drafts that exist are kept, so a stopped run can be started again."""
import json, os, pathlib, time, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
TEMPLATE = """Write the body of an agent skill file (Markdown) that a coding assistant follows when doing this kind of work.
Skill: {name}
When it is used: {description}
It must cover, in this order where it fits:
{must}

Rules for the text:
- Under 300 words. Plain, common software words. Short imperative sentences.
- Sections exactly: "## Steps" (numbered, 4-8 steps), "## Checklist" (5-8 checkbox items `- [ ]` to verify before saying done), "## Output" (what the answer to the user contains, 2-4 bullets).
- Concrete: name commands, file names, or a tiny example where it helps. No filler, no motivation, no history.
- Do not include a title line or YAML front matter. Output only the Markdown body."""
def ask(prompt):
    base = os.environ.get("OPENAI_BASE_URL", "http://localhost:8080/v1").rstrip("/")
    req = urllib.request.Request(f"{base}/chat/completions",
        data=json.dumps({"model": os.environ.get("OPENAI_MODEL", "local"), "messages": [{"role": "user", "content": prompt}], "max_tokens": 8000, "temperature": 0.3}).encode(),
        headers={"content-type": "application/json", "authorization": "Bearer " + os.environ.get("OPENAI_API_KEY", "none"), "x-yllm-priority": "interactive"})
    with urllib.request.urlopen(req, timeout=900) as r:
        d = json.load(r)
    return d["choices"][0]["message"]["content"] or "", d.get("model")
out = ROOT / "drafts"; out.mkdir(exist_ok=True)
for s in json.load(open(ROOT / "tools/catalogue.json")):
    f = out / f"{s['name']}.md"
    if f.exists():
        continue
    t = time.time()
    try:
        body, model = ask(TEMPLATE.format(name=s["name"], description=s["description"], must="\n".join("- " + m for m in s["must"])))
        if len(body.split()) < 80:
            raise ValueError(f"draft too short ({len(body.split())} words)")
        f.write_text(body.strip() + "\n")
        print(json.dumps({"skill": s["name"], "seconds": round(time.time() - t), "model": model, "words": len(body.split())}), flush=True)
    except Exception as e:
        print(json.dumps({"skill": s["name"], "error": str(e)[:100]}), flush=True)
