---
title: Install Things Over HTTP
date: 2025-10-24
icon: material/penguin
tags:
  - linux
---


```bash
ssh -R 30001 juuj@<system-ip>
```


```bash
sudo http_proxy=socks5h://localhost:30001 https_proxy=socks5h://localhost:30001 apt update
sudo http_proxy=socks5h://localhost:30001 https_proxy=socks5h://localhost:30001 apt install <packages>
```


