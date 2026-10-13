"""Collect the treatment folder's .md files into one flat folder for upload.

A Claude project stores knowledge files without folders, and the operator
has five files all named CONTEXT.md. So each file is copied with its path
built into the name: 01-outcome/CONTEXT.md becomes 01-outcome__CONTEXT.md.
File contents are not changed.

Usage: python scripts/make_upload.py
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "discovery-operator"
OUT = ROOT / "treatment-upload"

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
files = sorted(SRC.rglob("*.md"))
for f in files:
    name = "__".join(f.relative_to(SRC).parts)
    shutil.copyfile(f, OUT / name)
print(f"copied {len(files)} files to {OUT}")
