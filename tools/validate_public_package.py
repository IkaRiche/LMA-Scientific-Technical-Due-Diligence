"""Validate schema, provenance references and internal Markdown links.

This is not a patent, confidentiality or independent scientific audit.
"""
import csv
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", "README_RU.md", "LEGAL.md", "SECURITY.md",
    "docs/00_START_HERE.md", "docs/INDEX.md",
    "docs/10_EVIDENCE_STANDARDS.md",
    "docs/01_EXECUTIVE_OVERVIEW.md", "docs/02_LMA_FORMAL_SCOPE.md",
    "docs/03_TMC_VISION.md", "docs/04_GUARDIAN_VEIL.md",
    "docs/05_REVIEW_PROTOCOL.md", "docs/06_PRODUCT_SELECTION.md",
    "docs/07_DISCLOSURE_BOUNDARY.md",
    "docs/08_MATHEMATICAL_REVIEW_CHECKLIST.md",
    "docs/09_SOURCE_NAVIGATION.md",
    "evidence/CLAIMS_REGISTER.csv", "evidence/INDEX.md",
]
for path in required:
    assert (root / path).is_file(), f"Missing required file: {path}"


with (root / "evidence/CLAIMS_REGISTER.csv").open(newline="", encoding="utf-8") as f:
    claims = list(csv.DictReader(f))
ids = [x["claim_id"] for x in claims]
assert len(ids) == len(set(ids))
assert len(claims) >= 12
for entry in claims:
    assert entry["status"] and entry["scope"] and entry["source_id"]

markdown = list(root.rglob("*.md"))
for md in markdown:
    text = md.read_text(encoding="utf-8")
    for url in re.findall(r"\]\(([^)]+)\)", text):
        if "://" in url or url.startswith("#") or url.startswith("mailto:"):
            continue
        target = (md.parent / url.split("#", 1)[0]).resolve()
        assert target.is_file(), f"Broken link in {md.relative_to(root)}: {url}"

print(f"PUBLIC_PACKAGE_STRUCTURE_OK: {len(required)} required, {len(claims)} public claims, {len(markdown)} Markdown files")
print("NOTE: Integrity validation does not establish scientific correctness or disclosure clearance.")
