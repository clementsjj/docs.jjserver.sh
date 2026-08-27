---
title: How to setup simple apache directory
draft: false
date: 2025-10-08
tags:
    - apache
tags: 
    - linux
    - how-to
icon: material/book-open-blank-variant-outline
---

(This is using Arch to install, otherwise substitute httpd with apache2)

### Install Apache & Copy Files to Serve
```bash
sudo pacman -S --needed apache
sudo install -d -m 755 /srv/http/audio
sudo chmod 644 /srv/http/audio/*  
```

### Include Apache Index Module
```bash
sudo sed -i 's/^#\?LoadModule autoindex_module/LoadModule autoindex_module/' /etc/httpd/conf/httpd.conf
```

### Create Directory Conf
```bash
sudo tee /etc/httpd/conf/extra/simple-dir.conf >/dev/null <<'EOF'
<Directory "/srv/http">
    Options Indexes
    AllowOverride None
    Require all granted
</Directory>
EOF
```

### Add Hostname to Conf
```bash
echo 'Include conf/extra/simple-dir.conf' | sudo tee -a /etc/httpd/conf/httpd.conf

echo "ServerName $(hostname -f 2>/dev/null || hostname):80" | sudo tee -a /etc/httpd/conf/httpd.conf
```

### Check if Loaded
```bash
httpd -M 2>/dev/null | grep -i autoindex || echo "autoindex NOT loaded"
```


### Test httpd config
```bash
httpd -t
```

### Start httpd
```bash
sudo systemctl enable --now httpd
systemctl --no-pager status httpd
```


### Copy File Over
```bash
cp ~/supremecourt-oralarguments-20251008-hour1.mp3 /srv/http/audio/
```



