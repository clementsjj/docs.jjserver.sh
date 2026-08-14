# systemctl

## Mental model

- systemd manages **units**. Most are `.service`, but also `.socket`, `.timer` (cron replacement), `.target` (runlevels), `.mount`, `.device`.
- Two **independent** axes — this is the #1 confusion:
  - **enabled** = starts at boot?
  - **active** = running right now?
  - `enable` ≠ `start`. Use `--now` to do both at once.
- Unit files: `/lib/systemd/system/` (shipped by packages) and `/etc/systemd/system/` (your overrides — **wins**). Don't edit the shipped ones directly; use `systemctl edit`.
- `--user` targets units in your own login session instead of system-wide.


## Everyday

| Command                          | What it does                        |
| -------------------------------- | ----------------------------------- |
| `systemctl status <unit>`        | running? + recent log tail          |
| `systemctl start <unit>`         | start now                           |
| `systemctl stop <unit>`          | stop now                            |
| `systemctl restart <unit>`       | stop + start                        |
| `systemctl reload <unit>`        | re-read config without full restart |
| `systemctl enable <unit>`        | start at boot (doesn't start now)   |
| `systemctl disable <unit>`       | don't start at boot                 |
| `systemctl enable --now <unit>`  | enable **and** start now            |


## Inspecting

| Command                            | What it does                       |
| ---------------------------------- | ---------------------------------- |
| `systemctl list-units --type=service` | active services                 |
| `systemctl list-unit-files`        | all units + their enabled state    |
| `systemctl --failed`               | what's broken                      |
| `systemctl is-active <unit>`       | quick active check (scriptable)    |
| `systemctl is-enabled <unit>`      | quick boot check                   |
| `systemctl cat <unit>`             | show the unit file                 |
| `systemctl show <unit>`            | every property                     |
| `systemctl list-dependencies <unit>` | what it pulls in                 |


## Editing units

| Command                         | What it does                              |
| ------------------------------- | ----------------------------------------- |
| `systemctl edit <unit>`         | create a drop-in override (recommended)   |
| `systemctl edit --full <unit>`  | edit a full copy into `/etc`              |
| `systemctl daemon-reload`       | reload after editing any unit file        |
| `systemctl revert <unit>`       | throw away your overrides                 |
| `systemctl mask <unit>`         | fully disable — can't even be started     |


## Timers (cron replacement)

| Command                    | What it does                        |
| -------------------------- | ----------------------------------- |
| `systemctl list-timers`    | all timers + next/last run          |
| `systemctl status <t>.timer` | one timer's schedule + state      |


## Targets & power

| Command                            | What it does                          |
| ---------------------------------- | ------------------------------------- |
| `systemctl get-default`            | boot target (`graphical` / `multi-user`) |
| `systemctl set-default multi-user.target` | boot to CLI, no GUI            |
| `systemctl reboot` / `poweroff`    | restart / shut down                   |
| `systemctl suspend`                | sleep                                 |


## Gotchas

- **`enable` ≠ `start`.** Enabling only affects boot; the service isn't running until you `start` it (or use `--now`).
- **`daemon-reload` after editing unit files** — otherwise systemd runs the old version.
- A **masked** unit can't be started at all until `unmask` — different from merely disabled.


## See also

- [[journalctl]] — read a unit's logs (`journalctl -u <unit>`)
