#!/usr/bin/env python3
"""Install chosen skills/workflows from this repo into ~/.claude (and ~/.codex/skills).
Never overwrites: existing files are moved to ~/.claude-starter-backup/<timestamp>/ first.
Usage: python -I scripts/install.py --skills codex-gpt --workflows deep-research [--codex] [--dry-run]
"""
import argparse
import shutil
import time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
home = Path.home()
ap = argparse.ArgumentParser()
ap.add_argument("--skills", nargs="*", default=[])
ap.add_argument("--workflows", nargs="*", default=[])
ap.add_argument("--codex", action="store_true", help="also copy skills to ~/.codex/skills")
ap.add_argument("--dry-run", action="store_true")
a = ap.parse_args()
backup = home / ".claude-starter-backup" / time.strftime("%Y%m%d-%H%M%S")


def put(src: Path, dst: Path):
    if not src.exists():
        print("missing in repo:", src)
        return
    if dst.exists():
        b = backup / dst.relative_to(home)
        print(f"backup {dst} -> {b}")
        if not a.dry_run:
            b.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dst), str(b))
    print(f"install {src.relative_to(root)} -> {dst}")
    if not a.dry_run:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst) if src.is_dir() else shutil.copy2(src, dst)


for s in a.skills:
    put(root / "skills" / s, home / ".claude" / "skills" / s)
    if a.codex:
        put(root / "skills" / s, home / ".codex" / "skills" / s)
for w in a.workflows:
    put(root / "workflows" / f"{w}.js", home / ".claude" / "workflows" / f"{w}.js")
