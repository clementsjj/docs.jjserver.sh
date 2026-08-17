---
title: Add mkdocs-macros-plugin to mkdocs
description: How to add macros to mkdocs
icon: material/language-markdown
date: 2026-08-17
---

Why?

Because `mkdocs-macros-plugin` lets you write a small Python function that scans all pages, sorts by frontmatter, and drops the result into any page as a Jinja macro call — e.g. `{{ latest_pages(5) }}`. Used here for two things on `index.md`: a "Recently updated" list and a "Featured" list.

## Install

```sh
venv/bin/pip install mkdocs-macros-plugin
```

Pin it in `requirements.txt` like the other deps:
```
mkdocs-macros-plugin==1.5.0
```

## Wire it up in `mkdocs.yml`

```yaml
plugins:
  - macros:                    # {{ latest_pages(n) }} — see main.py
      render_by_default: false # opt-in only, see gotcha below
```

By default, `module_name` is `main`, so it looks for a `main.py` in the project root (next to `mkdocs.yml`) — that's where the macro functions live.

## `main.py`

```python
def define_env(env):
    docs_dir = env.conf["docs_dir"]

    @env.macro
    def latest_pages(n=5):
        ...
```

- `env.conf` is the whole `mkdocs.yml` config dict — `env.conf["docs_dir"]` gives the absolute path to `docs/`. `docs_dir` is either specified in `mkdocs.yml`, or defaults to `docs/` .
- `env.macro` is a decorator that registers a Python function as a Jinja macro, callable from any page as `{{ latest_pages(5) }}`.
- Both macros (`latest_pages`, `featured_pages`) walk every `.md` file under `docs_dir`, hand-parse the YAML frontmatter, and build a sorted Markdown list string, which gets returned and rendered as real Markdown (so `- [title](url)` becomes an actual `<li><a>` link).

Full code lives in `main.py` at the project root.

## Per-page usage

- Add `date: 2026-08-17` (replace with real date...) to any page's frontmatter and it becomes eligible for `latest_pages()`. 
- Add `featured: true` and it becomes eligible for `featured_pages()`.

To actually call a macro on a page, that page's frontmatter needs:
```yaml
render_macros: true
```


`mkdocs-macros-plugin` defaults to treating **every single page's raw Markdown as a Jinja template**, not just pages that use macros.
This can be a problem if you have anything with { }. 

To fix this, we can add `render_by_default: false` in the plugin config (mkdocs.yml), then explicitly opt in per page with `render_macros: true` in frontmatter. This is great because we really only want anything rendering in `index.md`.



## The two macros, briefly

| Macro | Source field | Behavior |
|---|---|---|
| `{{ latest_pages(n) }}` | `date:` | top *n* pages by date, newest first; undated pages excluded entirely |
| `{{ featured_pages() }}` | `featured: true` | every page flagged, dated ones newest-first, undated ones alphabetical by title, tacked on at the end; also shows `description:` after an em dash when a page has one |

Both are defined in `main.py` via a shared `_all_pages()` generator so the file-walking/frontmatter-parsing logic isn't duplicated between them.

