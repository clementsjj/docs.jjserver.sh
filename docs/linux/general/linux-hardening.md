---
title: "Linux Hardening"
icon: material/penguin
tags:
    - linux
date: 2025-10-20
---

## Setup SSH Keys
`ssh-keygen -t rsa -b 4096 -C "xxx@yyy.com"`

## Edit sshd

`sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.original`
<details open>
<summary><code>sudo vim /etc/ssh/sshd_config</code></summary>
  
```bash
Port 2222
ChallengeResponseAuthentication no
UsePAM no
PasswordAuthentication no
PermitRootLogin no
PermitRootLogin prohibit-password
```
</details>

`sudo systemctl reload sshd`

## UFW

- `sudo ufw allow 2222`
- `sudo ufw allow 80/tcp`
- `sudo ufw allow 443/tcp`
- `sudo ufw deny 22`
- `sudo ufw status`
- `sudo ufw reload`

## fail2ban / sshguard / crowdsec

```bash
sudo apt install fail2ban
sudo systemctl start fail2ban
sudo systemctl enable fail2ban
```


## log all ssh commands
  
Add to /etc/bash.bashrc:  
`readonly PROMPT_COMMAND='history -a >(logger -t "commandlog $USER[$PWD] $SSH_CONNECTION")'`

can configure syslog to forward logs elsewhere

## Block Ping
```
sudo vim /etc/ufw/before.rules
```

Add under `# ok icmp codes for INPUT`:  
Add:
```
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP
```

```
sudo reboot
```

## Check System

```bash
sudo ss -tulpn
```

```bash
# From external computer
ping xx.xx.xx.xx -t
```