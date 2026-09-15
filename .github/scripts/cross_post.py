import os
import re
import sys
import yaml
import requests

# --- CROSS-POSTING: dev.to, Mastodon ---
# Hashnode was dropped: as of 2026, their GraphQL API (read AND write) is
# gated behind a paid Pro plan on the publication ($5/mo or $50/yr), so
# free-tier auto-posting there isn't possible anymore.
# Each remaining platform is skipped gracefully (not a hard failure) if its
# secret isn't configured yet, so this script is safe to run before every
# secret has been set up in the repo.

SITE_URL = "https://www.adambourg.com"

DEVTO_API_KEY = os.environ.get("DEVTO_API_KEY")
MASTODON_INSTANCE_URL = os.environ.get("MASTODON_INSTANCE_URL")
MASTODON_ACCESS_TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")


def parse_post(path):
    """Split a Jekyll post into (frontmatter dict, body markdown, canonical_url)."""
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    parts = raw.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path} doesn't look like a Jekyll post (no frontmatter)")

    frontmatter = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()

    filename = os.path.basename(path)
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$", filename)
    if not match:
        raise ValueError(f"{filename} doesn't match YYYY-MM-DD-slug.md")
    year, month, day, slug = match.groups()
    canonical_url = f"{SITE_URL}/{year}/{month}/{day}/{slug}.html"

    return frontmatter, body, canonical_url


def devto_tags(categories):
    """dev.to allows up to 4 tags: lowercase, alphanumeric only, no spaces/dots."""
    if isinstance(categories, str):
        categories = categories.split()
    tags = []
    for c in categories or []:
        cleaned = re.sub(r"[^a-z0-9]", "", str(c).lower())
        if cleaned and cleaned not in tags:
            tags.append(cleaned)
        if len(tags) == 4:
            break
    return tags


def post_to_devto(title, body, categories, canonical_url):
    if not DEVTO_API_KEY:
        print("Skipping dev.to: DEVTO_API_KEY not found in environment.")
        return

    try:
        response = requests.post(
            "https://dev.to/api/articles",
            headers={"api-key": DEVTO_API_KEY, "content-type": "application/json"},
            json={
                "article": {
                    "title": title,
                    "body_markdown": body,
                    "published": True,
                    "tags": devto_tags(categories),
                    "canonical_url": canonical_url,
                }
            },
        )
        if response.status_code == 201:
            print(f"Posted to dev.to: {response.json().get('url')}")
        else:
            print(f"Error posting to dev.to ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error posting to dev.to: {e}")


def post_to_mastodon(title, canonical_url):
    if not MASTODON_INSTANCE_URL or not MASTODON_ACCESS_TOKEN:
        print("Skipping Mastodon: MASTODON_INSTANCE_URL or MASTODON_ACCESS_TOKEN not found in environment.")
        return

    status = f"New post: {title}\n\n{canonical_url}"

    try:
        response = requests.post(
            f"{MASTODON_INSTANCE_URL.rstrip('/')}/api/v1/statuses",
            headers={"Authorization": f"Bearer {MASTODON_ACCESS_TOKEN}"},
            data={"status": status, "visibility": "public"},
        )
        if response.status_code == 200:
            print(f"Posted to Mastodon: {response.json().get('url')}")
        else:
            print(f"Error posting to Mastodon ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error posting to Mastodon: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cross_post.py _posts/2026-01-01-some-post.md [more files...]")
        sys.exit(0)

    for path in sys.argv[1:]:
        if not os.path.exists(path):
            print(f"Skipping {path}: file not found")
            continue

        frontmatter, body, canonical_url = parse_post(path)
        title = frontmatter.get("title", "")
        categories = frontmatter.get("categories", [])

        print(f"--- Cross-posting: {title} ---")
        post_to_devto(title, body, categories, canonical_url)
        post_to_mastodon(title, canonical_url)
