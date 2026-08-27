---
title: Linux Variables
icon: material/penguin
date: 2026-07-19
---

# Linux Variables

## Overview

- A **shell variable** lives only in the current shell. `export` promotes it to an **environment variable** so child processes inherit it. That's the whole distinction.
- `VAR=value` → shell only. `export VAR=value` → inherited by anything you launch.
- Inheritance is one-way (parent → child). A child can't change the parent's env — which is why a script can't `cd` your shell for you.


## Setting & inspecting

| Command            | What it does                                 |
| ------------------ | -------------------------------------------- |
| `VAR=value`        | set a shell variable (this shell only)       |
| `export VAR=value` | set + export (children inherit)              |
| `VAR=value cmd`    | set for just that one command's run          |
| `unset VAR`        | remove it                                    |
| `echo $VAR`        | print one value                              |
| `printenv` / `env` | list **exported** (environment) variables    |
| `set`              | list **all** shell vars (incl. non-exported) |
| `declare -p VAR`   | show a var + its attributes                  |


## Common variables

| Variable              | Meaning                                                              |
| --------------------- | -------------------------------------------------------------------- |
| `$HOME`               | your home directory                                                  |
| `$USER`               | current username                                                     |
| `$PATH`               | dirs searched for commands (colon-separated)                         |
| `$SHELL`              | your login shell (not necessarily current one)                       |
| `$PWD` / `$OLDPWD`    | current / previous directory                                         |
| `$LANG`               | locale (language/encoding)                                           |
| `$EDITOR`             | default editor (git, crontab, etc. use it)                           |
| `$TERM`               | terminal type                                                        |
| `$DISPLAY`            | which X display to draw to (see [[display-basics]])                  |
| `$XDG_SESSION_TYPE`   | `x11` vs `wayland` (see [[display-basics]])                          |
| `XDG_CURRENT_DESKTOP` | set by display managers and full desktop sessions (GNOME, KDE, XFCE) |
| `DESKTOP_SESSION`     | set by display managers and full desktop sessions (GNOME, KDE, XFCE) |


## Shell special variables

| Variable | Meaning                            |
| -------- | ---------------------------------- |
| `$?`     | exit code of last command (0 = ok) |
| `$$`     | PID of the current shell           |
| `$!`     | PID of the last backgrounded job   |
| `$0`     | name of the script/shell           |
| `$#`     | number of args passed to a script  |
| `$@`     | all args                           |


## Persistence — where to define them

| File                             | When it loads                                           |
| -------------------------------- | ------------------------------------------------------- |
| `~/.bashrc`                      | every interactive **non-login** bash shell              |
| `~/.bash_profile` / `~/.profile` | **login** shells                                        |
| `~/.zshrc`                       | interactive zsh                                         |
| `/etc/environment`               | system-wide, all users (simple `KEY=val`, no scripting) |

> Login vs non-login is the classic "my var works in one terminal but not another" gotcha. A common fix is to `source ~/.profile` from `~/.bashrc`.
