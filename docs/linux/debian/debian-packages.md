---
title: Debian Packages
date: 2025-09-16
icon: material/debian
tags:
  - linux
---

As an example, I will be using a very simple script that prints the Wireless SSID the server is connected to and it's Signal Strength. The goal is to log this information and read it with `journalctl`

The script, `signalstrengthd.sh` looks like this: 
```bash
#!/bin/bash
# a loop that checks wifi status every 10 seconds
while true; do
    awk 'BEGIN{printf strftime("%d/%m/%Y %H:%M:%S UTC -- ", systime())}'
    echo -n $(networkctl status vwsta -n0 | grep -i "Wifi access point")
    awk 'NR==3 {print " | WiFi Signal Strength = " $3 "00 %"}' /proc/net/wireless 
    sleep 10
done
```

There are two types of packages: source & binary. 

<!-- <details><summary><h4>Source Packages - <code>.dsc</code> </h4></summary>
Built from the original source code. 
A source package that provides us with all the necessary files to compile or otherwise build the desired piece of software.
  
Requires 3 files: 
- Original Source (xxx.orig.tar.xz)
- Debian Source (xxx.debain.tar.xz)
- Source Control (dsc)
</details> -->

#### Source Packages 
###### `.dsc`

Built from the original source code. 
A source package that provides us with all the necessary files to compile or otherwise build the desired piece of software.
Requires 3 files: 
- Original Source (xxx.orig.tar.xz)
- Debian Source (xxx.debain.tar.xz)
- Source Control (dsc)


#### Binary Packages
###### `.deb`

  Binary packages use a `DEBIAN` directory
  
  Consists of the following:
  - debian-binary
    - version of the deb file format
 	- control.tar.gz
  	- metadata about the package
  - data.tar.gz
  	- data files of the package


---

## Required Files
```bash
mkdir -p debian/source

touch debian/changelog
touch debian/compat
touch debian/control
touch debian/rules
touch /debian/source/format
```

##### 1. `rules` - instructions for debhelper

1. Makefile that is used in the build process.
2. According to [this](https://www.debian.org/doc/manuals/maint-guide/dreq.en.html#rules), the required targets are:
    - clean
    - build
    - build-arch
    - build-indep
    - binary
    - binary-arch
    - binary-indep
  

  
  If you do this, it will pass to the included Makefile:
  ```bash
  DH_VERBOSE = 1
  #!/usr/bin/make -f  
  # % sign means any target
  %:  
  # calls a single program, dh, with the target name
  # dh is a wrapper script that runs appropriate sequences of dh_*
    dh $@
  ```



##### 2. `control` - package specific information
  Metadata that has at least 2 sections - one for source and one for binary. 
  
  Key Value Pairs grouped into sections.
  
  Mandatory Fields include:
  - Source
  - Maintainer
  - Standards-Version 
  - Package
  - Architecture
  - Description
  
  Highly Recommended:
  - Priority
  - Section



##### 3. `compat` - compatibility level for debhelper
  

##### 4. `changelog` - changes to the package and software
  Metadata explaining the changes of the package, in a very rigid format. 
  It sets the name, version, and distribution of the package.
  
  If distribution name = UNRELEASED, then the package build is not targeted for a particular distribution and does not need to be signed. 
  
  Leaving this empty will precent the package from building. 
  
  Best practice is to use `dch` (debchange)
  

##### 5. format
  I've really only seen/used a format file with this format specified: `3.0 (quilt)`
  
  This means that we can expect three files:
  - original source
  - debian source
  - source control 
  
  For anything >= 2.0, the default compression is xz. 
  For 1.0, default compression is gzip (gz).

 
##### Not Required Files But Excellent Files Nonetheless

- `preinst`
  - Runs before installation
- `postinst`
  - Runs after installation
  


---
# Build
---
 
## Build With `dpkg` suite
https://metebalci.com/blog/a-minimum-complete-example-of-debian-packaging-and-launchpad-ppa-hellodeb/

`dpkg` comes standard on Ubuntu, and contains various tools. We will be using 2 in particular:

  <details><summary><code>dpkg-deb</code></summary>
  Builds a binary package.
  a low-level tool that you should not call by itself (we'll use it in the rules file though), it is what is responsible for actually creating the .deb file. 
 </details>
  
 <details><summary><code>dpkg-buildpackage</code></summary>
  A Perl Script. Can also run various steps, like running `dpkg-source`
  
  Using the flag <code>--build</code> provides these options:
- source
- any
- all
- binary
- full
 </details>

We will also need to install `dpkg-dev` to generate packages. 
  <details><summary><code>dpkg-dev</code></summary>
  ```bash
  sudo apt install dpkg-dev
  ```
 </details>
 
![debian-package-min-tree-2.png](/debian-package-min-tree-2.png)
 
#### Folder Structure
Run `dpkg-buildpackage` in the directory with the source code, which should also contain a directory `debian` with the files mentioned above included.
The .deb output will be in the parent directory of where `dpkg-buildpackage` is run.



#### Build!
Assuming you have everything from the list of required files, you can build the package.
If you run `dpkg-buildpackage` by itself, it will run by default `dpkg-buildpackage --build full`. The build option that you provide corresponds to what you need to have in your `debian/rules` file.
Here are the `--build` options you have with `dpkg-buildpackage`, and the targets that are run from the rules file:
- full
	- clean, build, binary
  - full also builds the source packages, while binary does not
- all
  - clean, build-indep, binary-indep
- any
	- clean, build-arch, binary-arch
- binary
	- clean, build, binary
- source
	- clean

```bash
dpkg-buildpackage 
```

Need to add completed `rules` file that builds the tarball...

---

## Buld With `debmake`
According to this site, `debmake` is currently Broken :/

https://wiki.debian.org/SimplePackagingTutorial

---

## Build With `dh-make`, `debuild`, and a bash script
Using `dh-make`, creating a package can be pretty straight forward. Using this script for our example should be everything we need to create a debian package for the signal strength checker.

`dh-make` -- To prepare the package
`debuild` -- To build the package

```bash
#!/bin/bash

# Set the variables that will be used by dh_make
export DEBEMAIL=""
export DEBFULLNAME="First Last"

mkdir -p signal_strength_pkg/signalstrengthd-0.1
cd signal_strength_pkg/signalstrengthd-0.1

cat>signalstrengthd.sh << EOF 
#!/bin/bash
# a loop that checks wifi status every 10 seconds
while true; do
    awk 'BEGIN{printf strftime("%d/%m/%Y %H:%M:%S UTC -- ", systime())}'
    echo -n $(networkctl status vwsta -n0 | grep -i "Wifi access point")
    awk 'NR==3 {print " | WiFi Signal Strength = " $3 "00 %"}' /proc/net/wireless 
    sleep 10
done
EOF

cat>signalstrengthd.service << EOF
[Unit]
Description=Wifi Signal Strength Logger

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/signal-strength.sh

[Install]
WantedBy=multi-user.target
EOF

chmod +x signal-strength.sh

dh_make --indep --createorig 
# dh_make --createorig -e email@email.com -i -y

cd debian

rm *.ex *.EX
rm README.*

echo "signalstrengthd.sh /usr/local/bin/" > install
echo "signalstrengthd.service /usr/lib/systemd/system/" >> install

# Create .postinst
cat>postinst << EOF
#!/bin/bash
set -e
/usr/bin/systemctl daemon-reload
/usr/bin/systemctl enable signalstrengthd.service
exit 0
EOF

# Build Package
debuild -us -uc
# if this fails, you may need to rebuild the original tar
# dh_make --createorig

cd ..

sudo apt install ./signalstrengthd-0.1.deb
```

#### - `debuild` -
when running `debuild -us -uc`, 
`-us -uc` tells the script not to sign the .dsc and .changes files accordingly.
This is pretty much the standard run. 

You can also fancy it up more with: 
`debuild -us -uc -i -I -b`
-i and -I makes the script ignore common version control files. -b tells debuild to only create binary packages

#### Making Changes
If you make a change, like renaming a file, and try to run debuild again, you will get an error like so:
```bash
dpkg-source: info: local changes detected, the modified files are:
 signalstrengthd-1.5/services/signalstrengthd-log.service
dpkg-source: error: aborting due to unexpected upstream changes, see /tmp/signalstrengthd_1.5-1.diff.JrsnWU
dpkg-source: info: you can integrate the local changes with dpkg-source --commit
```

If you run waht it suggests, `dpkg-source --commit`, you will create a patch. You can then run debuild again successfully.

---

## Build Debian Package with `pbuilder` and a bash script
https://blog.packagecloud.io/building-debian-and-ubuntu-packages-with-pbuilder/


---

