"""
mkdocs-macros-plugin module for docs.jjserver.sh.
https://mkdocs-macros-plugin.readthedocs.io/

Provides two macros, usable in any .md page with `render_macros: true`
in its frontmatter:

- {{ latest_pages(n) }}  — the n most recently dated pages (needs `date:`)
- {{ featured_pages() }} — every page with `featured: true`, newest first
"""
import datetime
import os
import re

import yaml

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)


def _read_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def _file_to_url(docs_dir, path):
    """Mirror MkDocs' own file->URL rule (use_directory_urls, the default)."""
    rel = os.path.relpath(path, docs_dir).replace(os.sep, "/")
    if rel == "index.md":
        rel = ""
    elif rel.endswith("/index.md"):
        rel = rel[: -len("index.md")]
    else:
        rel = rel[: -len(".md")] + "/"
    return "/" + rel


def _all_pages(docs_dir):
    """Yield (path, meta, title, url, date_key) for every markdown page.

    date_key is the ISO-ish sort key for `date:` if it's a real date
    (datetime.date/datetime, as PyYAML parses an unquoted ISO date into),
    else "" — so undated pages sort last, and placeholder/template text
    like the literal string "{{date}}" in scaffold files can't slip in
    just because it's truthy.
    """
    for root, _, files in os.walk(docs_dir):
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            meta = _read_frontmatter(path)
            date = meta.get("date")
            date_key = str(date) if isinstance(date, (datetime.date, datetime.datetime)) else ""
            title = meta.get("title") or name[:-3].replace("-", " ").title()
            yield path, meta, title, _file_to_url(docs_dir, path), date_key


def define_env(env):
    docs_dir = env.conf["docs_dir"]

    @env.macro
    def latest_pages(n=5):
        dated = [
            (date_key, title, url)
            for _, meta, title, url, date_key in _all_pages(docs_dir)
            if date_key
        ]
        dated.sort(key=lambda p: p[0], reverse=True)
        top = dated[:n]
        if not top:
            return "*(no dated pages yet)*"
        return "\n".join(f"- [{title}]({url}) — {date}" for date, title, url in top)

    @env.macro
    def featured_pages():
        featured = [
            (date_key, title, url, meta.get("description"))
            for _, meta, title, url, date_key in _all_pages(docs_dir)
            if meta.get("featured")
        ]
        # Two-pass stable sort: title A-Z first (the tiebreaker), then
        # date_key newest-first (the primary key) — Python's sort is
        # stable, so undated pages (date_key == "", which sorts last
        # since "" < any real date string) keep their title order.
        featured.sort(key=lambda p: p[1])
        featured.sort(key=lambda p: p[0], reverse=True)
        if not featured:
            return "*(nothing featured yet — add `featured: true` to a page's frontmatter)*"
        lines = []
        for _, title, url, description in featured:
            line = f"- **[{title}]({url})**"
            if description:
                line += f" — {description}"
            lines.append(line)
        return "\n".join(lines)
