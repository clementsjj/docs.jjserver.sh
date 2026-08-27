---
title: Use mkdocs-material theme
description: How to setup and use the material theme for mkdocs
date: 2026-08-17
icon: material/language-markdown
---





### Frontmatter

| Frontmatter     |                                                         |
| --------------- | ------------------------------------------------------- |
| title           | overrides page title                                    |
| description     | `<meta name="description">`                             |
| tags            | need plugin for tags in mkdocs.yml                      |
| icon            | icons next to page; <br>these come with material mkdocs |
| status          | badge next to nav entry                                 |
| hide            | e.g. hide: [navigation, toc]                            |
| search: exclude | exclude page from search index                          |
| template        | use different jinja template                            |


### Icons

Icons are baked into the theme. There are 3 varietals.

| Set                   | Prefix                                                            | Example                   |
| --------------------- | ----------------------------------------------------------------- | ------------------------- |
| Material Design Icons | material/                                                         | material/bicycle          |
| Font Awesome          | fontawesome/solid/<br>fontawesome/regular/<br>fontawesome/brands/ | fontawesome/brands/github |
| Octicons              | octicons/                                                         | octicons/start-24         |
You can use these in front-matter, mkdocs.yml, and inline (`:material/bicycle:`)

More info on icons can be found here: https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/

- https://fontawesome.com/search
- https://pictogrammers.com/library/mdi/