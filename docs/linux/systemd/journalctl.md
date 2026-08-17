---
icon: material/bash
date: 2026-08-16
---

# journalctl

## Mental model

- The **journal** is systemd's centralized log — kernel, boot, and every service in one place. It replaces hunting through scattered `/var/log/*.log` files.
- It's **structured**: each entry has fields (`_SYSTEMD_UNIT`, `_PID`, `PRIORITY`…). So you *filter*, you don't `grep`.
- **Persistence:** if `/var/log/journal/` exists, logs survive reboot. If only `/run/log/journal/`, they're wiped on reboot (volatile). Make it persistent with `Storage=persistent` in `/etc/systemd/journald.conf` + create that dir.


## Viewing & following

| Command                  | What it does                           |
| ------------------------ | -------------------------------------- |
| `journalctl -u <svc> -f` | follow one service live (daily driver) |
| `journalctl -f`          | follow everything (like `tail -f`)     |
| `journalctl -e`          | jump to the end                        |
| `journalctl -r`          | newest first                           |
| `journalctl -n 50`       | last 50 lines                          |


## Filtering (the point of the journal)

| Command                           | What it does                   |
| --------------------------------- | ------------------------------ |
| `journalctl -u <svc>`             | one service's logs             |
| `journalctl -b`                   | this boot only                 |
| `journalctl -b -1`                | the **previous** boot          |
| `journalctl --list-boots`         | list boots you can reference   |
| `journalctl --since "1 hour ago"` | time window (also `--until`)   |
| `journalctl --since today`        | since midnight                 |
| `journalctl -k`                   | kernel messages (like `dmesg`) |
| `journalctl -p err`               | priority err **and worse**     |
| `journalctl _PID=1234`            | by a structured field          |

Combine freely: `journalctl -u nginx -b -p err --since today`.


## Priority levels

`-p` takes a level; it shows that level **and everything more severe**:

```
0 emerg  1 alert  2 crit  3 err  4 warning  5 notice  6 info  7 debug
```
So `-p warning` = 4 and lower numbers.


## Disk usage / cleanup

| Command                         | What it does                     |
| ------------------------------- | -------------------------------- |
| `journalctl --disk-usage`       | how much space the journal uses  |
| `journalctl --vacuum-time=2d`   | delete entries older than 2 days |
| `journalctl --vacuum-size=500M` | trim journal down to 500M        |
| `journalctl --verify`           | check journal integrity          |


## Output formats

| Command                     | What it does                                |
| --------------------------- | ------------------------------------------- |
| `journalctl -o cat`         | message only, no metadata (good for piping) |
| `journalctl -o json-pretty` | full structured entry as JSON               |
| `journalctl -o short-iso`   | ISO timestamps                              |


## See also

- [systemctl](../systemctl) — managing the units whose logs you're reading
