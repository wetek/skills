#!/usr/bin/env python3
"""Run the capture-architecture Markdown link checker from the repo root."""

from pathlib import Path
import runpy

SCRIPT = (
    Path(__file__).resolve().parent.parent
    / "skills"
    / "engineering"
    / "capture-architecture"
    / "scripts"
    / "check-markdown-links.py"
)

runpy.run_path(str(SCRIPT), run_name="__main__")
