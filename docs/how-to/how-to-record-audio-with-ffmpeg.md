---
title: How to record audio with ffmpeg
date: 2025-10-10
draft: false
tags: 
    - linux
    - how-to
icon: material/book-open-blank-variant-outline
---


Lets first figure out which source we will be recording from:

```bash
pactl list short sources | grep monitor
```

```bash
ffmpeg -f pulse -i 'alsa_output.usb-Razer_Razer_Leviathan_V2_X_000000000000000-01.analog-stereo.monitor'        -c:a libmp3lame -q:a 2 supremecourt-oralarguments-20251008.mp3
```

or, use default currently in use:
```bash
SINK="$(pactl get-default-sink).monitor"
ffmpeg -f pulse -i "$SINK" -c:a libmp3lame -q:a 2 supremecourt-oralarguments-20251008.mp3
```

Use `pactl` to discover and select the correct monitor.

And use ffmpeg to capture and encode in one shot. 

