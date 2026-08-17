---
title: Random Linux
description: random pieces of linux knowledge
tags:
  - linux
icon: material/linux
date: 2026-08-15
---

# Random Linux

## Shell / history tricks

| Command              | What it does                                              |
| -------------------- | --------------------------------------------------------- |
| `sudo !!`            | re-run the last command with sudo                         |
| `!$`                 | last arg of previous command                              |
| `cd -`               | jump back to previous directory                           |
| `Ctrl+R`             | reverse-search command history                            |
| `watch -n1 <cmd>`    | re-run a command every 1s (live view)                     |
| `<cmd> \| column -t` | align whitespace columns into a table                     |
| `^oldword^newword`   | this replaces the last command with the word substitution |


## Useful Programs


|         |                                               |
| ------- | --------------------------------------------- |
| [[xev]] | Allows you to see the metadata of a key press |
|         |                                               |


## Processes

| Command              | What it does                         |
| -------------------- | ------------------------------------ |
| `pgrep -af <name>`   | find PIDs by name, with full cmdline |
| `pkill -f <pattern>` | kill by matching the whole cmdline   |
| `lsof -p <pid>`      | every file/socket a process has open |
| `strace -p <pid>`    | watch a running process's syscalls   |
| `nohup <cmd> &`      | run detached, survives logout        |


## Disk & files

| Command              | What it does                                    |
| -------------------- | ----------------------------------------------- |
| `chattr +i <file>`   | make immutable (deeper than chmod)              |
| `ncdu`               | interactive disk-usage explorer                 |
| `du -sh *`           | size of each item in current dir                |
| `df -h` / `df -i`    | free space / free **inodes**                    |
| `readlink -f <path>` | resolve a symlink to its real absolute path     |
| `stat <file>`        | full metadata (perms, timestamps, inode)        |
| `chattr`             | set/alter low-level file attributes; can make files immutable |


## systemd / logs

| Command                        | What it does                     |
| ------------------------------ | -------------------------------- |
| `journalctl -u <svc> -f`       | follow a service's logs live     |
| `journalctl -b -p err`         | this boot's errors only          |
| `systemctl status <svc>`       | is it running? recent log tail   |
| `systemctl enable --now <svc>` | enable at boot **and** start now |


## Gotchas

| Symptom                                 | Fix                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------ |
| `df` shows full but `du` doesn't add up | a deleted file is still held open — `lsof +L1` to find it; restart that process |
