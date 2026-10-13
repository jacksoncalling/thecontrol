"""Make blind copies of the control and treatment answers for grading.

For each question, the two responses are shuffled into A and B. Only the
response text is copied; the header (arm, model, time) is left out. The
key that says which letter is which arm is written to --key, which must
be outside grading/ so the grader never sees it until grading is done.

Usage: python scripts/blind.py --key <path-outside-grading>/key.json
"""
import argparse, json, random, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "grading" / "blind"
QUESTIONS = [f"q{i:02d}" for i in range(1, 9)]


def response_text(path):
    text = path.read_text(encoding="utf-8")
    m = re.search(r"^## Response.*?\n(.*)\Z", text, re.S | re.M)
    if not m:
        sys.exit(f"{path}: no '## Response' section")
    body = m.group(1).strip()
    if not body or body == "PASTE HERE":
        sys.exit(f"{path}: response is still empty")
    return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True)
    args = ap.parse_args()
    key_path = Path(args.key).resolve()
    if (ROOT / "grading") in key_path.parents:
        sys.exit("--key must be outside grading/")

    rng = random.SystemRandom()
    OUT.mkdir(parents=True, exist_ok=True)
    key = {}
    for q in QUESTIONS:
        arms = ["control", "treatment"]
        rng.shuffle(arms)
        key[q] = {"A": arms[0], "B": arms[1]}
        for letter, arm in zip("AB", arms):
            body = response_text(ROOT / arm / f"{q}.md")
            (OUT / f"{q}-{letter}.md").write_text(
                f"# {q.upper()} answer {letter}\n\n{body}\n", encoding="utf-8")
    key_path.write_text(json.dumps(key, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(QUESTIONS) * 2} blind files to {OUT}")
    print(f"key written to {key_path} (do not show it to the grader)")


if __name__ == "__main__":
    main()
