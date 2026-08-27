---
title: display
date: 2026-07-07T18:37:05-04:00
draft: true
tags:
  - linux
description: ""
icon: material/monitor-small
---

# Display

- **`xrandr` is X11-only.** On Wayland it won't work — check your session first: `echo $XDG_SESSION_TYPE` (`x11` vs `wayland`).
- **Output** = a physical connector: `eDP-1` (laptop panel), `HDMI-1`, `DP-1`. **Mode** = resolution + refresh rate.
- Software vs hardware brightness: `xrandr --brightness` dims the *signal* (fake); real backlight control is `brightnessctl` / `/sys/class/backlight`.


## xrandr — outputs & modes

| Command                                             | What it does                           |
| --------------------------------------------------- | -------------------------------------- |
| `xrandr`                                            | list outputs + available modes         |
| `xrandr --query \| grep " connected"`               | just the connected outputs             |
| `xrandr --output HDMI-1 --mode 1920x1080`           | set resolution                         |
| `xrandr --output HDMI-1 --mode 1920x1080 --rate 60` | set resolution + refresh               |
| `xrandr --output HDMI-1 --primary`                  | make it the primary display            |
| `xrandr --output HDMI-1 --auto`                     | enable at preferred mode               |
| `xrandr --output HDMI-1 --off`                      | disable an output                      |
| `xrandr --output HDMI-1 --right-of eDP-1`           | position (also `--left-of`, `--above`) |
| `xrandr --output HDMI-1 --rotate left`              | rotate (normal/left/right/inverted)    |
| `xrandr --output HDMI-1 --scale 1.5x1.5`            | scale (software)                       |


## Add a custom resolution

| Step                  | Command                          |
| --------------------- | -------------------------------- |
| generate a modeline   | `cvt 1920 1080 60`               |
| register it           | `xrandr --newmode "<modeline>"`  |
| attach to an output   | `xrandr --addmode HDMI-1 <name>` |


## Wayland equivalents

| Environment          | Command                   |
| -------------------- | ------------------------- |
| wlroots (Sway, etc.) | `wlr-randr`               |
| Hyprland             | `hyprctl monitors`        |
| GNOME / KDE          | Settings → Displays (GUI) |


## Brightness (real backlight)

| Command                                 | What it does        |
| --------------------------------------- | ------------------- |
| `brightnessctl set 50%`                 | set backlight       |
| `brightnessctl g` / `brightnessctl m`   | current / max value |
| `cat /sys/class/backlight/*/brightness` | raw value           |


## Troubleshooting

| Symptom                            | Check                                             |
| ---------------------------------- | ------------------------------------------------- |
| Monitor not detected               | `xrandr` to see if listed; reseat cable; `--auto` |
| `xrandr` says "can't open display" | you're on Wayland (or no `$DISPLAY` set)          |
| Wrong refresh rate                 | `xrandr --output X --rate 60`                     |


See [[window-managing]] for compositors, tearing, and WMs.

For a real-world case (XFCE's display GUI doing nothing under a bare Openbox session, `autorandr`, and a toggle script), see [[hdmi-tv-openbox]].
