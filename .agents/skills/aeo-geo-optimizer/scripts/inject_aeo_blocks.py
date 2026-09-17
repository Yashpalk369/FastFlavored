#!/usr/bin/env python3
"""
AEO & GEO Injection & Validation Helper CLI
Inspects HTML articles for AEO answer targets, BLUF formatting, and Wikidata entity schemas.
"""

import os
import sys
import re
import argparse

def check_aeo_health(html_content):
    score = 0
    checks = []

    # 1. Check for direct answer box / BLUF block
    has_answer_box = "aeo-answer-box" in html_content or "key-takeaways" in html_content
    if has_answer_box:
        score += 35
        checks.append("[+] Direct Answer / Key Takeaways block present")
    else:
        checks.append("[-] Missing direct answer / BLUF block (e.g. .aeo-answer-box)")

    # 2. Check for Table of Comparison / Data Matrix
    has_table = "<table" in html_content
    if has_table:
        score += 25
        checks.append("[+] Structured comparison table / data matrix present")
    else:
        checks.append("[-] Missing structured comparison table (critical for GEO citation)")

    # 3. Check for FAQPage or Q&A Schema
    has_faq = "FAQPage" in html_content or "Question" in html_content
    if has_faq:
        score += 20
        checks.append("[+] FAQ schema microdata present")
    else:
        checks.append("[-] Missing FAQPage schema")

    # 4. Check for Entity sameAs or Wikidata/Wikipedia references
    has_entities = "sameAs" in html_content or "wikidata.org" in html_content or "wikipedia.org" in html_content
    if has_entities:
        score += 20
        checks.append("[+] Knowledge Graph entity references (Wikidata/Wikipedia) present")
    else:
        checks.append("[-] Missing Knowledge Graph entity links (about/mentions with sameAs)")

    return score, checks

def inject_aeo_block(filepath, answer_text, entity_name, entity_wiki):
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Create AEO answer box HTML
    answer_box = f"""
      <!-- AEO / AI Overview Direct Answer Target -->
      <div class="aeo-answer-box" style="background: var(--bg-secondary); border-left: 4px solid var(--accent-color); padding: 1.25rem 1.5rem; border-radius: 0 var(--radius-md) var(--radius-md) 0; margin: 1.75rem 0;">
        <p style="margin: 0; font-size: 1.05rem; line-height: 1.7; color: var(--text-primary);">
          <strong style="color: var(--accent-color);"><i class="fa-solid fa-sparkles"></i> Direct Answer:</strong> {answer_text}
        </p>
      </div>
"""
    # Insert after H1 or first paragraph
    h1_pos = content.find("</h1>")
    if h1_pos != -1:
        insert_idx = content.find(">", h1_pos) + 1
        content = content[:insert_idx] + "\n" + answer_box + content[insert_idx:]
        print(f"[+] Injected AEO Direct Answer Box into: {filepath}")

    # Inject entity sameAs if requested and schema exists
    if entity_name and entity_wiki and "@type\": \"BlogPosting\"" in content:
        entity_fragment = f""",
        "about": {{
          "@type": "Thing",
          "name": "{entity_name}",
          "sameAs": "{entity_wiki}"
        }}"""
        content = content.replace('"@type": "BlogPosting"', '"@type": "BlogPosting"' + entity_fragment, 1)
        print(f"[+] Linked Knowledge Graph entity '{entity_name}' ({entity_wiki})")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print("[+] Article updated successfully for AEO/GEO!")

def main():
    parser = argparse.ArgumentParser(description="Audit or inject AEO/GEO answer targets and entity schemas.")
    parser.add_argument("--file", required=True, help="Path to HTML article")
    parser.add_argument("--check", action="store_true", help="Audit AEO readiness score")
    parser.add_argument("--answer", help="Direct answer text to inject")
    parser.add_argument("--entity", help="Primary entity name (e.g. 'Sourdough')")
    parser.add_argument("--wiki", help="Wikidata or Wikipedia URL")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"[-] Error: {args.file} does not exist.")
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        html = f.read()

    score, checks = check_aeo_health(html)
    print(f"\n--- AEO/GEO Audit for {os.path.basename(args.file)} ---")
    print(f"Score: {score}/100")
    for c in checks:
        print(f"  {c}")
    print("-------------------------------------------\n")

    if args.answer:
        inject_aeo_block(args.file, args.answer, args.entity, args.wiki)

if __name__ == "__main__":
    main()
