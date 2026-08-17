---
title: dns
date: 2026-07-07T18:36:12-04:00
draft: true
tags:
  - linux
  - networking
description: ""
icon: material/lan-connect
---

# DNS

DNS = phonebook: **hostname → IP**.

- On Linux, name resolution isn't *only* DNS. `/etc/nsswitch.conf` sets the order — usually `files` (`/etc/hosts`) **then** `dns`. That's why `getent` and `dig` can disagree.
- **Resolver** (recursive: `8.8.8.8`, systemd-resolved) answers by asking around. **Authoritative** server actually owns the record.
- **TTL** = how long an answer is cached before it's re-fetched.
- Most modern Debian/Ubuntu run **systemd-resolved**: a stub resolver at `127.0.0.53`, which is what `/etc/resolv.conf` usually points at.

### Record types

| Type    | Meaning                       |
| ------- | ----------------------------- |
| `A`     | hostname → IPv4               |
| `AAAA`  | hostname → IPv6               |
| `CNAME` | alias → another hostname      |
| `MX`    | mail server                   |
| `TXT`   | free text (SPF, verification) |
| `NS`    | nameserver for the zone       |
| `PTR`   | IP → hostname (reverse)       |


## Lookup tools

| Command                     | What it does                                       |
| --------------------------- | ------------------------------------------------- |
| `nslookup <hostname>`       | simple lookup (uses configured resolver)          |
| `dig <hostname>`            | detailed lookup, full DNS answer                  |
| `dig +short <hostname>`     | just the IP, no noise                             |
| `dig <hostname> MX`         | query a specific record type (A/AAAA/MX/TXT/NS)   |
| `dig @8.8.8.8 <hostname>`   | ask a specific server (bypass your resolver)      |
| `dig -x <ip>`               | reverse lookup (IP → name)                        |
| `dig +trace <hostname>`     | follow delegation from root → authoritative       |
| `host <hostname>`           | quick one-line lookup                             |
| `getent hosts <hostname>`   | resolves via nsswitch (files + dns, like apps do) |
| `resolvectl query <host>`   | query through systemd-resolved                    |


## systemd-resolved / status

| Command                   | What it does                    |
| ------------------------- | ------------------------------- |
| `resolvectl status`       | which DNS servers per interface |
| `resolvectl flush-caches` | clear the resolver cache        |
| `resolvectl statistics`   | cache hits/misses               |


## Config files

| File                         | Purpose                                       |
| ---------------------------- | --------------------------------------------- |
| `/etc/resolv.conf`           | which resolver(s) to use (often → 127.0.0.53) |
| `/etc/hosts`                 | static hostname → IP overrides                |
| `/etc/nsswitch.conf`         | resolution order (`files dns`)                |
| `/etc/systemd/resolved.conf` | systemd-resolved settings                     |


## Troubleshooting

| Symptom / need                     | Check                                          |
| ---------------------------------- | ---------------------------------------------- |
| `getent` vs `dig` mismatch         | it's `/etc/hosts` or nsswitch, not DNS itself  |
| Stale record after a change        | `resolvectl flush-caches` (or check TTL)       |
| Which server am I even using?      | `resolvectl status` or `cat /etc/resolv.conf`  |
| Works with `@8.8.8.8`, not default | your configured resolver is the problem        |
