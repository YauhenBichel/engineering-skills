"""Measure guessing a skill from a message: nearest example messages, with "none" examples competing.

Index: tools/examples.jsonl. Held-out test: tools/examples-test.jsonl (written separately, never used to tune
anything but the three limits). Embeddings come from an OpenAI-compatible /embeddings endpoint:
OPENAI_BASE_URL (default http://localhost:8080/v1), EMBED_MODEL (default bge-m3). Needs numpy.

    python3 tools/measure_guess.py [--k 2] [--threshold 0.55] [--margin 0.06]
"""
import argparse, json, os, pathlib, urllib.request
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]


def embed(texts):
    base = os.environ.get("OPENAI_BASE_URL", "http://localhost:8080/v1").rstrip("/")
    out = []
    for i in range(0, len(texts), 16):
        body = json.dumps({"model": os.environ.get("EMBED_MODEL", "bge-m3"), "input": texts[i:i + 16]}).encode()
        req = urllib.request.Request(f"{base}/embeddings", body, {"content-type": "application/json"})
        out += [d["embedding"] for d in json.load(urllib.request.urlopen(req, timeout=300))["data"]]
    v = np.array(out, dtype=np.float32)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


def rows(name):
    return [json.loads(line) for line in (ROOT / "tools" / name).read_text().splitlines() if line.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=2)
    ap.add_argument("--threshold", type=float, default=0.55)
    ap.add_argument("--margin", type=float, default=0.06)
    a = ap.parse_args()
    index, test = rows("examples.jsonl"), rows("examples-test.jsonl")
    labels = np.array([r["skill"] for r in index])
    names = sorted(set(labels))
    sims = embed([r["text"] for r in test]) @ embed([r["text"] for r in index]).T
    count = {"right": 0, "wrong": 0, "skill on a none message": 0, "no skill (none message)": 0, "no skill (missed)": 0}
    for row, s in zip(test, sims):
        scores = np.array([np.sort(s[labels == n])[::-1][:a.k].mean() for n in names])
        order = np.argsort(scores)[::-1]
        best, second, guess = scores[order[0]], scores[order[1]], names[order[0]]
        if guess == "none" or best < a.threshold or best - second < a.margin:
            count["no skill (none message)" if row["skill"] == "none" else "no skill (missed)"] += 1
        elif row["skill"] == "none":
            count["skill on a none message"] += 1
        else:
            count["right" if guess == row["skill"] else "wrong"] += 1
    print(json.dumps({"index": len(index), "test": len(test), **vars(a), **count}, indent=1))


if __name__ == "__main__":
    main()
