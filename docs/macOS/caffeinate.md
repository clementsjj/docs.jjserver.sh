---
title: Caffeinate
draft: false
date: 2025-01-05
icon: fontawesome/brands/apple
tags:
  - macOS
---

<div style="position:relative;width:min(600px, 100%);height:100px;margin:2rem auto;display:flex;align-items:center;justify-content:center;border-radius:.375rem;overflow:hidden;background-image:url('https://picsum.photos/600/100?random=1&grayscale');background-repeat:no-repeat;background-size:cover;background-position:center;">
    <div style="position:absolute;inset:0;background:rgba(253, 21, 21, 0.15);z-index:0;"></div>
    <img src="/img/apple/apple-dark-grey.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
    <img src="/img/apple/apple-rainbow.svg" alt="linux" style="position:relative;z-index:1;width:5rem;margin:.5rem;opacity:.8;"/>
    <img src="/img/apple/apple-light-grey.svg" alt="linux" style="position:relative;z-index:1;height:4rem;width:auto;max-width:5rem;margin:.5rem;opacity:.8;"/>
</div>

Need a quick and painless way to keep your mac from going to lockscreen or screensaver? 

Use caffeinate!

This became an issue where I wanted to run a script for work from my mac where I would continually query and restart a remote server.
Due to work required software, I am unable to run it continually if I want to step away from the computer for a while, as the mandated screensaver would kick in, and would kill my fortinet vpn session, causing the script to basically timeout. 


Enter Caffeinate. 

As far as I can tell, it already comes pre installed on macOS. And running it is as simple as:

```bash
caffeinate -d
```

Simply put, this command prevents the display from sleeping. 



You can see more information with this via tldr: 


```bash
√ juuj@JJs-MacBook-Pro:~ % tldr caffeinate

caffeinate

Prevent macOS from sleeping.
More information: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Prevent the display from sleeping:
    caffeinate -d

- Prevent from sleeping for 1 hour (3600 seconds):
    caffeinate -u -t 3600

- Fork a process, exec "make" in it, and prevent sleep as long as that process is running:
    caffeinate -i make

- Prevent from sleeping until a process with the specified PID completes:
    caffeinate -w pid

- Prevent disk from sleeping (use `<Ctrl c>` to exit):
    caffeinate -m
```