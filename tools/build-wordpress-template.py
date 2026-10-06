#!/usr/bin/env python3
"""Copy the reviewed static pages into WordPress-only PHP templates."""

from pathlib import Path
import subprocess
import sys


root = Path(__file__).resolve().parents[1]
# The translated pages follow the English HTML structure and must be rebuilt
# before copying them into WordPress templates.
subprocess.run([sys.executable, str(root / "tools/build-localizations.py")], check=True)
guard = "<?php\nif (!defined('ABSPATH')) { http_response_code(404); exit; }\n?>\n"
for source_name, target_name in (
    ("index.html", "template.php"),
    ("privacy/index.html", "privacy-template.php"),
    ("fr/index.html", "fr-template.php"),
    ("fr/privacy/index.html", "fr-privacy-template.php"),
):
    source = root / source_name
    target = root / "wordpress/mu-plugins/marcos-audit-home" / target_name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(guard + source.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Updated {target.relative_to(root)} from {source.relative_to(root)}")
