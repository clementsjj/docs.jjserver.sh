---
title: Use Local Computer as a Proxy for Apt
description: A brief overview of using your local computer as a proxy for apt on a remote system
icon: material/debian
date: 2026-08-16
---

# Overview

I was once on a remote system that had apt sources blocked. I tried different mirrors. I tried https mirrors (since ubuntu mirrors by default are http). There was no hope. 
However, I realized I could use an apt proxy, with that proxy being my local computer I was working on. 
This was done from macOS, so the process includes using brew package manager.


# Process

#### Local Computer
```sh
brew install tinyproxy
```


Open `/opt/homebrew/etc/tinyproxy/tinyproxy.conf` to edit the conf

```sh
Port 8888
Listen 127.0.0.1
Allow 127.0.0.1
Timeout 600
ConnectPort 443
```

```sh
tinyproxy -d -c /opt/homebrew/etc/tinyproxy/tinyproxy.conf
```


```sh
ssh -R 13142:127.0.0.1:8888 <RemoteSystem>
```


#### Remote Computer

On the remote, you need to pass in an option to `apt-get` to use a proxy address, and since you set up a reverse tunnel, you can hit that via localhost, and it should be all systems go from there.

```sh
sudo -S apt-get -o Acquire::http::Proxy="http://127.0.0.1:13142" -o Acquire::https::Proxy="http://127.0.0.1:13142" update
```

You can also set this option in `/etc/apt` so you don't need to pass -o all the time.


  On the remote, confirm the listener exists:
```sh
ss -lnt | grep 13142      # expect 127.0.0.1:13142 LISTEN
```
  



#### Local Computer
  On your Mac, confirm tinyproxy is up:
```sh
lsof -nP -iTCP:8888 -sTCP:LISTEN
```
  