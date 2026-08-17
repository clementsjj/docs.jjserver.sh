---
title: apt
draft: false
tags:
  - debian
description: Some useful commands for use with apt
icon: material/debian
date: 2026-08-16
---

# apt

## Overview

- **`apt`** = friendly frontend for interactive use. **`apt-get`/`apt-cache`** = stable interface for **scripts** (don't use `apt` in scripts — its output isn't guaranteed). **`dpkg`** = low-level `.deb` tool, **no dependency resolution**.
- `apt update` refreshes the local **index** (what's available) — it installs nothing. `apt upgrade` is what actually installs. People conflate these constantly.
- Packages come from repos in `/etc/apt/sources.list` and `/etc/apt/sources.list.d/`.


## Everyday

| Command                  | What it does                                    |
| ------------------------ | ----------------------------------------------- |
| `apt update`             | refresh package index (installs nothing)        |
| `apt upgrade`            | upgrade installed packages                      |
| `apt full-upgrade`       | upgrade, allowing removals to resolve deps      |
| `apt install <pkg>`      | install                                         |
| `apt install ./file.deb` | install a local .deb **with** dependency fixup  |
| `apt remove <pkg>`       | remove, keep config files                       |
| `apt purge <pkg>`        | remove **+** config files                       |
| `apt autoremove`         | remove orphaned dependencies                    |


## Search & info

| Command                       | What it does                                       |
| ----------------------------- | -------------------------------------------------- |
| `apt search <term>`           | search package names/descriptions                  |
| `apt show <pkg>`              | package details                                    |
| `apt list --installed`        | what's installed                                   |
| `apt list --upgradable`       | what has updates pending                           |
| `apt-cache policy <package>`  | installed vs candidate version + repo priorities   |
| `apt-cache madison <package>` | all available versions across repos                |
| `apt-mark hold <pkg>`         | pin — prevent it from upgrading (`unhold` to undo) |


## dpkg (low-level)

| Command                                                           | What it does                                |
| ----------------------------------------------------------------- | ------------------------------------------- |
| `dpkg -l`                                                         | list installed packages                     |
| `dpkg -L <pkg>`                                                   | list files a package installed              |
| `dpkg -S <file>`                                                  | which package **owns** a given file         |
| `dpkg -i <file.deb>`                                              | install a .deb (no deps → `apt install -f`) |
| `dpkg-query -W -f='${Package}\t${Version}\n' 'jj-*' \| column -t` | view packages and versions cleanly          |


## Troubleshooting

| Symptom / need             | Fix                                                        |
| -------------------------- | --------------------------------------------------------- |
| Broken dependencies        | `apt install -f` (a.k.a. `apt --fix-broken install`)      |
| Install a specific version | `apt install <pkg>=<version>`                             |
| "Packages kept back"       | `apt full-upgrade`                                        |
| What changed / when        | `/var/log/apt/history.log`  or the `zcat dpkg.log*` trick |


## History digging

| Command                                | What it does                          |
| -------------------------------------- | ------------------------------------- |
| `zcat /var/log/dpkg.log* \| grep ___`  | Find last package upgrade and version |
