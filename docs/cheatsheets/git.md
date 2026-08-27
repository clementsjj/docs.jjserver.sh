---
title: Git Cheatsheet
date: 2026-09-22
icon: material/git
---


### Initialize a New Repository
#### Init Git
```sh
git init
git add .
git commit -m "Initial Commit"
```

#### Push to Github
```sh
gh auth login
gh repo create REPO-NAME --public --source=. --remote=origin --push
```

Without `gh`, create the repository on Github website, and connect local to remote:
```sh
git remote add origin git@github.com:USERNAME/REPO-NAME.git
git branch -M main          
git push -u origin main
```