---
title: How to add admonition from obisidian to mkdocs
description: A little how-to showing how to add cool drop down boxes from obsidian to mkdocs
date: 2026-07-08
icon: material/language-markdown
---


There's a neat trick with obsidian where you can add little expandable text boxes.

It looks like this:

```markdown
> [!info]- Click to Expand Me!
> > Hello!!!
```

> [!info]- Click to Expand Me!
> > Hello!!!

With html, that would look something like this:

```html
<details>
  <summary>Click to Expand Me!</summary>
  <blockquote>Hello!!!</blockquote>
</details>
```

By default, with mkdocs (no `callouts` plugin), that same Obsidian markdown syntax renders as this instead. Plain Markdown has no idea what `[!info]-` means, so it just falls back to a plain nested blockquote with that text sitting there literally, not styled or collapsible at all:

```html
<blockquote>
  <p>[!info]- Click to Expand Me!</p>
  <blockquote>
    <p>Hello!!!</p>
  </blockquote>
</blockquote>
```


So to render the obsidian style in mkdocs, we just need to add a little plugin.

1. Install it (into your venv):
```sh
venv/bin/pip install mkdocs-callouts
```

2. Add to `mkdocs.yml` — the plugin plus the markdown extensions the output relies on:
```yaml
plugins:
  - search
  - callouts          # converts Obsidian > [!note] → Material admonition

markdown_extensions:
  - admonition        # renders the callout boxes
  - pymdownx.details  # needed for collapsible callouts
  - pymdownx.superfences
```

With that in place, the exact same Obsidian syntax at the top of this page renders as the real, styled, collapsible box.