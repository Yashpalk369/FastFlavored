#!/usr/bin/env python3
"""
Off-Page Backlink Outreach Campaign Generator CLI
Generates personalized outreach email templates and pitches for link acquisition.
"""

import os
import sys
import argparse
from datetime import date

def generate_broken_link_pitch(article_title, article_url, niche, target_site, your_name, blog_name):
    year = date.today().year
    return f"""Subject: Quick heads up regarding a broken resource on {target_site}

Hi there,

I was reading your {niche} guide on {target_site} today and found it super actionable.

While checking out some of the linked resources, I noticed that one of your reference links appears to be dead (returning a 404 error).

We just published a brand-new, thoroughly tested guide on the exact same topic:
"{article_title}" -> {article_url}

It's updated for {year} with fresh data and clear takeaways. If you are looking for an active, reliable replacement to keep your article fresh for readers, feel free to check it out!

Keep up the great work on {target_site}.

Best regards,
{your_name}
{blog_name}
"""

def generate_guest_post_pitch(article_title, article_url, niche, target_site, your_name, blog_name):
    return f"""Subject: 3 article ideas for {target_site} readers (From {blog_name})

Hi {target_site} Editorial Team,

I've been following your {niche} content for a while and love your depth of coverage.

I noticed a couple of emerging topics in {niche} that haven't been deeply explored on your blog yet. I'd love to write a comprehensive, data-driven guest article for your audience.

Here are 3 specific angles I've mapped out:

1. The Complete Blueprint to [Core Problem in {niche}] (Step-by-step tutorial + checklist)
2. 7 Costly Mistakes Beginners Make in {niche} (And How to Avoid Them)
3. [Trend/Method A] vs [Method B]: Which Delivers Better Results in {date.today().year}?

I write 1,500+ word, zero-fluff, original content formatted cleanly with custom graphics. You can see an example of my writing standard here:
{article_url}

Would any of these three topics resonate with your editorial calendar?

Warm regards,
{your_name}
Founder, {blog_name}
"""

def generate_journalist_pitch(article_title, article_url, query_topic, your_name, blog_name, author_title):
    return f"""Subject: Expert commentary for query: "{query_topic}" - {your_name}

Hi there,

Here is expert commentary regarding your query on {query_topic}:

Soundbite 1:
"The biggest misconception in this space is assuming more complexity equals better results. In our testing, simplifying the core routine yielded a 35% higher success rate."

Soundbite 2:
"Consistency and baseline measurements always outperform trendy shortcuts. Tracking your core metrics over 30 days is what moves the needle."

Key Takeaway:
Focus on the foundational 20% that drives 80% of results before adding advanced techniques.

Credentials:
- Name: {your_name}
- Title: {author_title}, {blog_name}
- Reference Guide: {article_url} ("{article_title}")

Feel free to quote any of the above verbatim or reach out if you'd like additional commentary or data!

Best,
{your_name}
"""

def main():
    parser = argparse.ArgumentParser(description="Generate backlink outreach campaigns.")
    parser.add_argument("--type", choices=["broken_link", "guest_post", "journalist"], default="broken_link", help="Campaign type")
    parser.add_argument("--article-title", required=True, help="Title of your published article")
    parser.add_argument("--article-url", required=True, help="URL of your published article")
    parser.add_argument("--niche", default="our niche", help="Niche topic")
    parser.add_argument("--target-site", default="AuthoritySite.com", help="Target website name")
    parser.add_argument("--your-name", default="Alex Morgan", help="Your name")
    parser.add_argument("--blog-name", default="Our Blog", help="Your blog name")
    parser.add_argument("--author-title", default="Lead Editor", help="Your professional title")
    parser.add_argument("--query-topic", default="Industry Best Practices", help="Journalist query topic (for HARO)")

    args = parser.parse_args()

    print("\n========================================================")
    print(f"  BACKLINK OUTREACH CAMPAIGN ({args.type.upper()})")
    print("========================================================\n")

    if args.type == "broken_link":
        print(generate_broken_link_pitch(args.article_title, args.article_url, args.niche, args.target_site, args.your_name, args.blog_name))
    elif args.type == "guest_post":
        print(generate_guest_post_pitch(args.article_title, args.article_url, args.niche, args.target_site, args.your_name, args.blog_name))
    elif args.type == "journalist":
        print(generate_journalist_pitch(args.article_title, args.article_url, args.query_topic, args.your_name, args.blog_name, args.author_title))

    print("========================================================\n")

if __name__ == "__main__":
    main()
