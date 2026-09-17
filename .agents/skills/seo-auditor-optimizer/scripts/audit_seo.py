#!/usr/bin/env python3
"""
Static Blog SEO Auditor CLI
Audits HTML files for title lengths, meta descriptions, headings, image alts, schemas, and orphan pages.
"""

import os
import sys
import re
import glob
import json
import argparse

def audit_html_file(filepath):
    issues = []
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    rel_path = os.path.relpath(filepath)

    # 1. Title Tag
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if not title_match:
        issues.append("Missing <title> tag")
    else:
        title = title_match.group(1).strip()
        if len(title) < 30:
            issues.append(f"Title too short ({len(title)} chars): '{title}'")
        elif len(title) > 65:
            issues.append(f"Title too long ({len(title)} chars, ideal is 50-60): '{title[:45]}...'")

    # 2. Meta Description
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', content, re.IGNORECASE)
    
    if not desc_match:
        issues.append("Missing meta description tag")
    else:
        desc = desc_match.group(1).strip()
        if len(desc) < 100:
            issues.append(f"Meta description too short ({len(desc)} chars, ideal is 130-160)")
        elif len(desc) > 170:
            issues.append(f"Meta description too long ({len(desc)} chars, ideal is 130-160)")

    # 3. H1 Tags
    h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if len(h1_matches) == 0:
        issues.append("Missing <h1> tag")
    elif len(h1_matches) > 1:
        issues.append(f"Multiple <h1> tags found ({len(h1_matches)})")

    # 4. Image Alt Attributes
    img_tags = re.findall(r'<img\s+[^>]*>', content, re.IGNORECASE)
    missing_alt_count = 0
    for img in img_tags:
        if 'alt=' not in img.lower() or re.search(r'alt=["\']\s*["\']', img, re.IGNORECASE):
            missing_alt_count += 1
    if missing_alt_count > 0:
        issues.append(f"{missing_alt_count} image(s) missing or have empty alt attributes")

    # 5. Schema.org JSON-LD
    if "<script type=\"application/ld+json\">" not in content and "<script type='application/ld+json'>" not in content:
        # About/contact/legal pages don't strictly require schema, but articles should have it
        if "articles" in rel_path:
            issues.append("Article missing Schema.org JSON-LD structured data")

    # 6. Viewport
    if "name=\"viewport\"" not in content and "name='viewport'" not in content:
        issues.append("Missing responsive viewport meta tag")

    return {
        "file": rel_path,
        "issues": issues,
        "links": re.findall(r'href=["\']([^"\']+)["\']', content, re.IGNORECASE)
    }

def run_site_audit(root_dir):
    print(f"==================================================")
    print(f"  STATIC BLOG SEO AUDIT: {os.path.abspath(root_dir)}")
    print(f"==================================================")

    html_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        # ignore git and node_modules if any
        if ".git" in dirpath:
            continue
        for f in filenames:
            if f.endswith(".html"):
                html_files.append(os.path.join(dirpath, f))

    if not html_files:
        print("[-] No HTML files found.")
        return

    results = []
    all_internal_targets = set()

    for path in html_files:
        res = audit_html_file(path)
        results.append(res)
        for link in res["links"]:
            if not link.startswith("http") and not link.startswith("#") and not link.startswith("mailto:"):
                # Normalize link
                clean_target = os.path.basename(link.split("?")[0].split("#")[0])
                if clean_target.endswith(".html"):
                    all_internal_targets.add(clean_target)

    # Check for orphan articles
    total_issues = 0
    for r in results:
        file_base = os.path.basename(r["file"])
        if "articles" in r["file"] and file_base not in all_internal_targets:
            r["issues"].append(f"Orphan page warning: No internal links point to {file_base}")

        if r["issues"]:
            total_issues += len(r["issues"])
            print(f"\n[!] {r['file']}")
            for issue in r["issues"]:
                print(f"    - {issue}")
        else:
            print(f"[+] {r['file']}: 100% SEO Clean")

    print(f"\n--------------------------------------------------")
    print(f"Scanned {len(html_files)} HTML pages.")
    if total_issues == 0:
        print(f"Score: 100/100! All pages conform to best practices.")
    else:
        print(f"Found {total_issues} SEO recommendation(s) across {len([r for r in results if r['issues']])} page(s).")
    print(f"--------------------------------------------------\n")

def main():
    parser = argparse.ArgumentParser(description="Audit static blog HTML files for SEO health.")
    parser.add_argument("--root", default=".", help="Root directory of the blog")
    args = parser.parse_args()
    run_site_audit(args.root)

if __name__ == "__main__":
    main()
