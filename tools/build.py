#!/usr/bin/env python3
"""Build deterministic portable and ClawHub skill directory bundles."""
from __future__ import annotations

import hashlib
import shutil
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT / "skills" / "zhongkui-guard"
DIST=ROOT / "dist"

def copy_bundle(destination: Path) -> None:
    if destination.exists(): shutil.rmtree(destination)
    shutil.copytree(SOURCE, destination)
    shutil.copytree(ROOT / "scripts", destination / "scripts")
    shutil.copytree(ROOT / "rules", destination / "rules")
    manifest=[]
    for file in sorted(p for p in destination.rglob("*") if p.is_file()):
        manifest.append(f"{hashlib.sha256(file.read_bytes()).hexdigest()}  {file.relative_to(destination).as_posix()}")
    (destination / "SHA256SUMS").write_text("\n".join(manifest)+"\n", encoding="utf-8")

for channel in ("portable", "clawhub"):
    bundle = DIST / channel / "zhongkui-guard"
    copy_bundle(bundle)
    archive = DIST / channel / "zhongkui-guard-0.1.0.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(p for p in bundle.rglob("*") if p.is_file()):
            zf.write(file, file.relative_to(bundle.parent))
    (archive.with_suffix(".zip.sha256")).write_text(hashlib.sha256(archive.read_bytes()).hexdigest() + "  " + archive.name + "\n", encoding="utf-8")
print("built portable and clawhub bundles")
