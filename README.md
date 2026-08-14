# docs.jjserver.sh

Personal docs/wiki site (Obsidian vault) built with [MkDocs](https://www.mkdocs.org/) +
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Setup

Requires Debian's `python3-venv`. From the project root:

```bash
python3 -m venv venv
venv/bin/pip install --upgrade pip
venv/bin/pip install mkdocs mkdocs-material mkdocs-callouts
```

This installs mkdocs 1.6.x (not the older apt-packaged `mkdocs` 1.4.2 — that one lacks
the `material` theme and the `tags`/`callouts` plugins that `mkdocs.yml` requires, so
don't rely on the system `mkdocs` binary).

> **Note:** the venv is not portable — it's created with absolute paths baked into its
> shebangs/activate scripts. If you move or rename the project directory, delete `venv/`
> and recreate it rather than trying to reuse it.

## Usage

Run from the project root (where `mkdocs.yml` lives), not from `docs/`.

```bash
# live-reloading dev server at http://127.0.0.1:8000
venv/bin/mkdocs serve

# build the static site into ./site/
venv/bin/mkdocs build
```

## Project layout

- `mkdocs.yml` — active config (Material theme, `tags` + `callouts` plugins).
- `mkdocs.yml.custommill` — alternate/experimental config using the custom
  `themes/mkdocs_custommill` theme. Not currently used; run with
  `venv/bin/mkdocs serve -f mkdocs.yml.custommill` to try it.
- `docs/` — page content (Markdown source, Obsidian vault).
- `site/` — build output (generated, gitignored/ignorable).
