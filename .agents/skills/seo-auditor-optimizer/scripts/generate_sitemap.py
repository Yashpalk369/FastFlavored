#!/usr/bin/env python3
"""
XML Sitemap & Robots.txt Generator CLI
Automatically crawls the blog folder and builds a compliant XML sitemap.
"""

import os
import sys
import argparse
from datetime import date

def generate_sitemap(root_dir, base_url):
    base_url = base_url.rstrip("/")
    today_str = date.today().isoformat()
    sitemap_file = os.path.join(root_dir, "sitemap.xml")
    robots_file = os.path.join(root_dir, "robots.txt")

    entries = []

    # Priority 1.0 for index.html
    if os.path.exists(os.path.join(root_dir, "index.html")):
        entries.append(f"""  <url>
    <loc>{base_url}/</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""")

    # Standard root pages
    for page in ["about.html", "contact.html", "privacy.html", "terms.html"]:
        if os.path.exists(os.path.join(root_dir, page)):
            entries.append(f"""  <url>
    <loc>{base_url}/{page}</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>""")

    # Articles directory
    articles_dir = os.path.join(root_dir, "articles")
    if os.path.exists(articles_dir):
        for f in os.listdir(articles_dir):
            if f.endswith(".html"):
                entries.append(f"""  <url>
    <loc>{base_url}/articles/{f}</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    # Recipes directory (if existing in Recipe blog)
    recipes_dir = os.path.join(root_dir, "recipes")
    if os.path.exists(recipes_dir):
        for f in os.listdir(recipes_dir):
            if f.endswith(".html"):
                entries.append(f"""  <url>
    <loc>{base_url}/recipes/{f}</loc>
    <lastmod>{today_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(entries)}
</urlset>
"""

    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    print(f"[+] Generated sitemap.xml with {len(entries)} URLs at: {sitemap_file}")
    if os.path.exists(robots_file):
        with open(robots_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        has_sitemap = any(l.strip().lower().startswith("sitemap:") for l in lines)
        if not has_sitemap:
            with open(robots_file, "a", encoding="utf-8") as f:
                f.write(f"\nSitemap: {base_url}/sitemap.xml\n")
    print(f"[+] Generated robots.txt pointing to: {base_url}/sitemap.xml")

def main():
    parser = argparse.ArgumentParser(description="Generate sitemap.xml and robots.txt.")
    parser.add_argument("--root", default=".", help="Root directory of the blog")
    parser.add_argument("--base-url", default="https://yoursite.com", help="Domain of the website")
    args = parser.parse_args()

    generate_sitemap(args.root, args.base_url)

if __name__ == "__main__":
    main()
