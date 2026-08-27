---
title: How to format a new disk
date: 2025-10-13
icon: material/book-open-blank-variant-outline
tags:
  - linux
---


## Preflight Checks

```bash
sudo pacman -S --needed exfatprogs
```
```bash
ls -l /dev/disk/by-id | grep -E 'sda|sdc'
```

### Optional
```bash
sudo wipefs -a /dev/sdc
```

## Create GPT + Partition

I prefer Option 1 - Using fdisk. 

### Option 1: Use fdisk
```bash
sudo fdisk /dev/sdc 
```
```
g
n, enter, enter, enter
t
11
w
```
```bash
sudo partprobe /dev/sdc
```

- t/11
    - t = change partion type
    - On GPT disks, this sets the partition type GUID (what other OSes use to guess what’s inside)
    - 11 = fdisk’s index/alias for “Microsoft basic data” → GUID EBD0A0A2-B9E5-4433-87C0-68B6B72699C7. Windows expects this for generic data partitions (NTFS/exFAT).
    - Linux doesn't really need to worry about this, it's more of a windows just in case thing. 

- partprobe
    - partprobe tells the kernel to re-read the partition table of a block device without rebooting.

### Option 2: Use Parted
```bash
sudo parted -s /dev/sdc mklabel gpt
sudo parted -s /dev/sdc mkpart DATA_SDC 0% 100%
sudo partprobe /dev/sdc
```

### Option 3: Use sgdisk
```bash
sudo sgdisk -o /dev/sdc
sudo sgdisk -n 0:0:0 -t 0:0700 -c 0:'VIDEO' /dev/sdc
```

### Option 4: Use sfdisk
```bash
printf ',,L\n' | sudo sfdisk /dev/sdc
```
```bash
sudo partprobe /dev/sdc
```


## Make Filesystem
```bash
sudo mkfs.exfat -n VIDEO /dev/sdc1
```
