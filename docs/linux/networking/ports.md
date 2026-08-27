---
title: Ports
description: A brief overview of ports and how to view in Linux
icon: material/lan-connect
date: 2026-08-01
---


# Ports


A port is a number (0–65535) tagging traffic so the kernel routes it to the right process. 
- IP → machine
- Port → program



| Protocol | Description                     | Services         | `ss` |
| -------- | ------------------------------- | ---------------- | ---- |
| TCP      | Connection, handshake, reliable | ssh, http        | -t   |
| UDP      | Fire and forget, no handshake   | dns, dhcp, video | -u   |

|        |                                |         |
| ------ | ------------------------------ | ------- |
| LISTEN | server waiting for connections | `ss -l` |
| ESTAB  | an active connection           | `ss`    |

| Bind Address     |                                           |
| ---------------- | ----------------------------------------- |
| `127.0.0.1:8000` | local only                                |
| `0.0.0.0:8000`   | (shown as `*`) reachable from the network |


### Port ranges

| Range         | Name                | Notes                                        |
| ------------- | ------------------- | -------------------------------------------- |
| 0–1023        | well-known          | privileged, need root to bind (22, 80, 443)  |
| 1024–49151    | registered          | apps (8080, 5432)                            |
| 49152–65535   | ephemeral / dynamic | random source port for outbound connections  |


## Listing (ss)

| Command                           | What it does                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| `ss -ltnp \| grep :8000`          | See what is listening on port 8000                                                         |
| `sudo ss -autnp \| grep ':40006'` | see whats using 40006, tcp and udp<br>-a all; -u udp; -t tcp; -n numeric ports; -p process |
| `ss -tlnp`                        | all TCP listeners + process (main go-to)                                                   |
| `ss -tulnp`                       | TCP + UDP listeners                                                                        |
| `ss -tanp`                        | all TCP, incl. established connections                                                     |
| `ss -tp state established`        | who's actually connected right now                                                         |
| `ss -tnp 'dport = :443'`          | connections to a remote port                                                               |
| `ss -s`                           | summary counts by socket type                                                              |

Find open ports in range:
```
sudo ss -aun | grep -oE ':40[0-9]{3}' | tr -d ':' | sort -un | awk '{u[$1]=1} END{for(e=40000;e<=40500;e+=2) if(!u[e]&&!u[e+1]) print e" (rtcp "e+1")"}'
```


## Other tools

| Command                              | What it does                          |
| ------------------------------------ | ------------------------------------- |
| `sudo lsof -i :8000`                 | what's on 8000 (shows user + fd)      |
| `sudo lsof -iTCP -sTCP:LISTEN -P -n` | all TCP listeners                     |
| `sudo fuser 8000/tcp`                | PID using the port                    |
| `sudo fuser -k 8000/tcp`             | kill whatever holds it (careful)      |

> `netstat` is the old command you'll see in docs — `ss` replaced it (faster). Same `-tulnp` flags carry over.


## Testing reachability

| Command                                              | What it does                      |
| ---------------------------------------------------- | --------------------------------- |
| `nc -zv host 22`                                     | is a TCP port open? (-z scan, -v) |
| `nc -zvu host 53`                                    | UDP variant                       |
| `curl -v telnet://host:5432`                         | quick TCP probe without nc        |
| `timeout 2 bash -c '< /dev/tcp/host/22' && echo open` | probe with no tools installed     |


## Common ports

| Port    | Service     |     | Port    | Service   |
| ------- | ----------- | --- | ------- | --------- |
| 22      | SSH         |     | 5432    | Postgres  |
| 53      | DNS         |     | 6379    | Redis     |
| 80      | HTTP        |     | 8080    | alt-HTTP  |
| 443     | HTTPS       |     | 123     | NTP (udp) |
| 3306    | MySQL       |     | 67/68   | DHCP      |

`grep 5432 /etc/services` looks any of these up locally.


## Firewall

A service can be listening but the firewall still blocks it — listening ≠ reachable. See [[ip tables]].

| Command                | What it does                    |
| ---------------------- | ------------------------------- |
| `sudo ufw status`      | Debian/Ubuntu simple firewall   |
| `sudo iptables -L -n`  | see rules                       |


## Troubleshooting

| Symptom / need               | Command                                      |
| ---------------------------- | -------------------------------------------- |
| "Address already in use"     | `sudo ss -tlnp \| grep :PORT` then kill it   |
| Running out of source ports  | `cat /proc/sys/net/ipv4/ip_local_port_range` |
| TIME_WAIT pileup             | `ss -tan state time-wait \| wc -l`           |


## Fun Facts

ICMP does not use port numbers. It is a Network Layer (Layer 3) protocol, whereas ports belong to Transport Layer (Layer 4) protocols like TCP and UDP
