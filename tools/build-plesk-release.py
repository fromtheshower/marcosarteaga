#!/usr/bin/env python3
"""Build the public-file tree for a separate Plesk deployment branch."""

from pathlib import Path
import shutil
import subprocess
import sys


root = Path(__file__).resolve().parents[1]
output = root / "build" / "plesk-release"

# Keep the WordPress templates in sync with the editable HTML before packaging.
subprocess.run([sys.executable, str(root / "tools/build-wordpress-template.py")], check=True)

files = [
    "styles.css",
    "script.js",
    "config.js",
    "submit.php",
    "assets/favicon.svg",
    "assets/fhios.png",
    "assets/future.png",
    "assets/groupe-dynamite.svg",
    "assets/hippoc.png",
    "assets/marcos-portrait.png",
    "assets/mindgeek.png",
    "assets/mobile-nations.png",
    "lib/phpmailer/LICENSE",
    "lib/phpmailer/src/Exception.php",
    "lib/phpmailer/src/PHPMailer.php",
    "lib/phpmailer/src/SMTP.php",
]
wordpress_files = [
    "marcos-audit-home.php",
    "marcos-audit-home/template.php",
    "marcos-audit-home/privacy-template.php",
    "marcos-audit-home/fr-template.php",
    "marcos-audit-home/fr-privacy-template.php",
]

if output.is_symlink():
    raise SystemExit(f"Refusing to replace symlink: {output}")
if output.exists():
    shutil.rmtree(output)
output.mkdir(parents=True)

for relative in files:
    source = root / relative
    target = output / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)

for relative in wordpress_files:
    source = root / "wordpress/mu-plugins" / relative
    target = output / "wp-content/mu-plugins" / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)

print(f"Built {len(files) + len(wordpress_files)} public files in {output.relative_to(root)}")
print("This tree is for a deploy-only Git branch; do not deploy the source branch to httpdocs.")
