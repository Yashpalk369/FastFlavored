#!/usr/bin/env python3
"""
Article Registration Helper CLI
Registers a newly published article (listicle or single article) into:
1. articles_database.json
2. index.html (as a responsive card in #articleGrid)
3. sitemap.xml
"""

import os
import sys
import json
import re
import argparse
from datetime import date

def register_article(root_dir, title, slug, category, author, read_time, excerpt, image, article_type, base_url):
    db_path = os.path.join(root_dir, "articles_database.json")
    index_path = os.path.join(root_dir, "index.html")
    sitemap_path = os.path.join(root_dir, "sitemap.xml")

    cat_slug = category.lower().replace(" ", "-")
    cat_str = f"all {cat_slug}"
    today_str = date.today().isoformat()

    # 1. Update articles_database.json
    db = []
    if os.path.exists(db_path):
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                db = json.load(f)
        except Exception:
            db = []

    # Check if entry already exists
    existing = next((item for item in db if item.get("slug") == slug or item.get("id") == slug), None)
    entry_data = {
        "id": slug,
        "slug": slug,
        "title": title,
        "category": category,
        "categories_str": cat_str,
        "read_time": read_time,
        "author": author,
        "type": article_type,
        "date": today_str,
        "image": image,
        "excerpt": excerpt
    }

    if existing:
        existing.update(entry_data)
        print(f"[*] Updated existing article in database: {slug}")
    else:
        db.insert(0, entry_data)
        print(f"[+] Added new article to database: {slug}")

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

    # 2. Update index.html
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            index_content = f.read()

        card_link = f"./articles/{slug}.html"
        if card_link not in index_content:
            card_html = f"""      <!-- Article Card: {title} -->
      <article class="article-card" data-categories="{cat_str}">
        <div class="card-image-wrap">
          <span class="card-badge">{category}</span>
          <img src="{image}" alt="{title}" loading="lazy">
        </div>
        <div class="card-content">
          <div class="card-meta">
            <span><i class="fa-regular fa-calendar"></i> {today_str}</span>
            <span>&bull;</span>
            <span><i class="fa-regular fa-clock"></i> {read_time}</span>
          </div>
          <h2 class="card-title">
            <a href="{card_link}">{title}</a>
          </h2>
          <p class="card-excerpt">{excerpt}</p>
          <div class="card-footer">
            <span>By {author}</span>
            <a href="{card_link}" class="read-link">Read Full Guide <i class="fa-solid fa-arrow-right"></i></a>
          </div>
        </div>
      </article>
"""
            # Insert after <div class="article-grid" id="articleGrid">
            grid_marker = re.search(r'(<div[^>]*class="[^"]*article-grid[^"]*"[^>]*>)', index_content, re.IGNORECASE)
            if grid_marker:
                insert_pos = grid_marker.end()
                index_content = index_content[:insert_pos] + "\n" + card_html + index_content[insert_pos:]
                with open(index_path, "w", encoding="utf-8") as f:
                    f.write(index_content)
                print(f"[+] Injected article card into index.html: {title}")
            else:
                print("[-] Notice: Could not locate .article-grid container in index.html to auto-inject card.")

    # 3. Update sitemap.xml
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()

        target_url = f"{base_url.rstrip('/')}/articles/{slug}.html"
        if target_url not in sitemap_content and "</urlset>" in sitemap_content:
            new_url_entry = f"""  <url>
    <loc>{target_url}</loc>
    <lastmod>{today_str}</lastmod>
    <priority>0.8</priority>
  </url>
</urlset>"""
            sitemap_content = sitemap_content.replace("</urlset>", new_url_entry)
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(sitemap_content)
            print(f"[+] Added URL to sitemap.xml: {target_url}")

    print("[+] Article successfully registered across all systems!")

def main():
    parser = argparse.ArgumentParser(description="Register a new article in the blog ecosystem.")
    parser.add_argument("--root", default=".", help="Root directory of the blog")
    parser.add_argument("--title", required=True, help="Article title")
    parser.add_argument("--slug", required=True, help="Slug/filename without extension")
    parser.add_argument("--category", default="Guides", help="Article category")
    parser.add_argument("--author", default="Editorial Staff", help="Author name")
    parser.add_argument("--read-time", default="6 min read", help="Read time (e.g. 7 min read)")
    parser.add_argument("--excerpt", default="", help="Short excerpt snippet")
    parser.add_argument("--image", default="./assets/placeholder.webp", help="Featured image path")
    parser.add_argument("--type", default="listicle", choices=["listicle", "single_article"], help="Article format type")
    parser.add_argument("--base-url", default="https://yoursite.com", help="Live website domain")

    args = parser.parse_args()
    register_article(
        root_dir=args.root,
        title=args.title,
        slug=args.slug,
        category=args.category,
        author=args.author,
        read_time=args.read_time,
        excerpt=args.excerpt,
        image=args.image,
        article_type=args.type,
        base_url=args.base_url
    )

if __name__ == "__main__":
    main()
