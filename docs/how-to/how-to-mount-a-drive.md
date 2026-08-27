---
title: How to Mount a Drive
date: 2025-10-13
tags: 
    - linux
    - how-to
icon: material/book-open-blank-variant-outline
date: 2026-08-17
---

Create mount directory
```bash
sudo mkdir -p /srv/media
```

Find the partition UUID
```bash
blkid /dev/sdc1
```


ext4/xfs (Unix perms available):

```bash
# /etc/fstab (replace UUID)
echo 'UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /srv/media ext4 defaults,noatime 0 2' | sudo tee -a /etc/fstab
sudo mount -a
```

exFAT/NTFS (no Unix perms → use uid/gid):
```bash
JUID=$(id -u jellyfin); JGID=$(id -g jellyfin)
# /etc/fstab (exFAT example; use ntfs-3g for NTFS)
echo "UUID=XXXX /srv/media exfat defaults,uid=$JUID,gid=$JGID,umask=002,noatime 0 0" | sudo tee -a /etc/fstab
sudo mount -a
```