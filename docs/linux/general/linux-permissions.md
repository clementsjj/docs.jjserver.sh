---
title: "Linux Permissions"
description: "A page about Linux permissions"
icon: material/penguin
date: 2025-12-20
tags:
  - linux
---

I'm not gonna lie, I still struggle with remembering file permissions and their number structure. So I think it's about time for me to make a table and study it a bit, finally commit it to memory.

0: no permission
1: execute
2: write
4: read


| Permission | Number | Permission |
|------------|--------|------------|
| No Permission | 0 | - |
| Execute | 1 | --x |
| Write | 2 | -w- |
| Read | 4 | r-- |


| Permission | Number | Permission|
|------------|--------|-----------|
| All permissions | 7 </br> (1+2+4)| rwx|
| Read and Write | 6 </br> (2+4)| rw- |
| Read and Execute | 5 </br> (1+4)| r-x |
| Write and Execute | 3 </br> (1+2)| -wx |


| Number | Owner-Group-Public | When to use |
|------------|--------|--------|
| 0777 | - rwx rwx rwx | Everyone can read, write, and execute. God Mode. |
| 0755 | - rwx r-x r-x | Everyone can read and execute, but only the owner can write |
| 0644 | - rw- r-- r-- | |
| 0600 | - rw- --- --- | Only the owner can read, write |
| 0555 | - r-x r-x r-x |   |
| 0444 | - r-- r-- r-- |   |
| 0400 | - r-- --- --- | A key |


Here's a fun chmod calculator that will create the number pattern for you. 
(Maybe I'll write my own sometime.)
https://chmod-calculator.com/