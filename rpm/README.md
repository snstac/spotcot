# Build RPM
```
[root@6157c14fe292 spotcot]# cd rpm
[root@6157c14fe292 rpm]# make #yum install -y make
rm -rf ~/rpmbuild
yum install -y rpmdevtools rpmlint git
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: centos.mirrors.estointernet.in
 * extras: centos.mirrors.estointernet.in
 * updates: centos.mirrors.estointernet.in
Package rpmdevtools-8.3-8.el7_9.noarch already installed and latest version
Package rpmlint-1.5-4.el7.noarch already installed and latest version
Package git-1.8.3.1-23.el7_8.x86_64 already installed and latest version
Nothing to do
rpmdev-setuptree
cd ~/rpmbuild/BUILD && git clone https://github.com/ampledata/spotcot.git spotcot-0.0.1
Cloning into 'spotcot-0.0.1'...
remote: Enumerating objects: 126, done.
remote: Counting objects: 100% (126/126), done.
remote: Compressing objects: 100% (87/87), done.
remote: Total 126 (delta 56), reused 106 (delta 36), pack-reused 0
Receiving objects: 100% (126/126), 2.44 MiB | 2.87 MiB/s, done.
Resolving deltas: 100% (56/56), done.
cd ~/rpmbuild/BUILD && tar --create --file spotcot-0.0.1.tar.gz spotcot-0.0.1 && mv -f spotcot-0.0.1.tar.gz ../SOURCES/
cp spotcot.spec ~/rpmbuild/SPECS
rpmbuild -bb ~/rpmbuild/SPECS/spotcot.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.DsCcYO
+ umask 022
+ cd /root/rpmbuild/BUILD
+ cd /root/rpmbuild/BUILD
+ rm -rf spotcot-0.0.1
+ /usr/bin/tar -xf /root/rpmbuild/SOURCES/spotcot-0.0.1.tar.gz
+ cd spotcot-0.0.1
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.1txiaU
+ umask 022
+ cd /root/rpmbuild/BUILD
+ '[' /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64 '!=' / ']'
+ rm -rf /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
++ dirname /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
+ mkdir -p /root/rpmbuild/BUILDROOT
+ mkdir /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
+ cd spotcot-0.0.1
+ rm -rf /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
+ python3 setup.py install
running install
running bdist_egg
running egg_info
creating spotcot.egg-info
writing spotcot.egg-info/PKG-INFO
writing dependency_links to spotcot.egg-info/dependency_links.txt
writing entry points to spotcot.egg-info/entry_points.txt
writing requirements to spotcot.egg-info/requires.txt
writing top-level names to spotcot.egg-info/top_level.txt
writing manifest file 'spotcot.egg-info/SOURCES.txt'
reading manifest file 'spotcot.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'spotcot.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/spotcot
copying spotcot/constants.py -> build/lib/spotcot
copying spotcot/__init__.py -> build/lib/spotcot
copying spotcot/functions.py -> build/lib/spotcot
copying spotcot/classes.py -> build/lib/spotcot
copying spotcot/commands.py -> build/lib/spotcot
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/spotcot
copying build/lib/spotcot/constants.py -> build/bdist.linux-x86_64/egg/spotcot
copying build/lib/spotcot/__init__.py -> build/bdist.linux-x86_64/egg/spotcot
copying build/lib/spotcot/functions.py -> build/bdist.linux-x86_64/egg/spotcot
copying build/lib/spotcot/classes.py -> build/bdist.linux-x86_64/egg/spotcot
copying build/lib/spotcot/commands.py -> build/bdist.linux-x86_64/egg/spotcot
byte-compiling build/bdist.linux-x86_64/egg/spotcot/constants.py to constants.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/spotcot/__init__.py to __init__.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/spotcot/functions.py to functions.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/spotcot/classes.py to classes.cpython-36.pyc
byte-compiling build/bdist.linux-x86_64/egg/spotcot/commands.py to commands.cpython-36.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/not-zip-safe -> build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying spotcot.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
creating dist
creating 'dist/spotcot-2.0.2-py3.6.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing spotcot-2.0.2-py3.6.egg
removing '/usr/lib/python3.6/site-packages/spotcot-2.0.2-py3.6.egg' (and everything under it)
creating /usr/lib/python3.6/site-packages/spotcot-2.0.2-py3.6.egg
Extracting spotcot-2.0.2-py3.6.egg to /usr/lib/python3.6/site-packages
spotcot 2.0.2 is already the active version in easy-install.pth
Installing spotcot script to /usr/bin

Installed /usr/lib/python3.6/site-packages/spotcot-2.0.2-py3.6.egg
Processing dependencies for spotcot==2.0.2
Searching for aiohttp==4.0.0a1
Best match: aiohttp 4.0.0a1
Processing aiohttp-4.0.0a1-py3.6-linux-x86_64.egg
aiohttp 4.0.0a1 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/aiohttp-4.0.0a1-py3.6-linux-x86_64.egg
Searching for pytak==3.5.2
Best match: pytak 3.5.2
Processing pytak-3.5.2-py3.6.egg
pytak 3.5.2 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/pytak-3.5.2-py3.6.egg
Searching for pycot==2.5.0
Best match: pycot 2.5.0
Processing pycot-2.5.0-py3.6.egg
pycot 2.5.0 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/pycot-2.5.0-py3.6.egg
Searching for yarl==1.7.2
Best match: yarl 1.7.2
Processing yarl-1.7.2-py3.6-linux-x86_64.egg
yarl 1.7.2 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/yarl-1.7.2-py3.6-linux-x86_64.egg
Searching for typing-extensions==4.1.1
Best match: typing-extensions 4.1.1
Processing typing_extensions-4.1.1-py3.6.egg
typing-extensions 4.1.1 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/typing_extensions-4.1.1-py3.6.egg
Searching for multidict==4.7.6
Best match: multidict 4.7.6
Processing multidict-4.7.6-py3.6-linux-x86_64.egg
multidict 4.7.6 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/multidict-4.7.6-py3.6-linux-x86_64.egg
Searching for idna-ssl==1.1.0
Best match: idna-ssl 1.1.0
Processing idna_ssl-1.1.0-py3.6.egg
idna-ssl 1.1.0 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/idna_ssl-1.1.0-py3.6.egg
Searching for chardet==3.0.4
Best match: chardet 3.0.4
Processing chardet-3.0.4-py3.6.egg
chardet 3.0.4 is already the active version in easy-install.pth
Installing chardetect script to /usr/bin

Using /usr/lib/python3.6/site-packages/chardet-3.0.4-py3.6.egg
Searching for attrs==21.4.0
Best match: attrs 21.4.0
Processing attrs-21.4.0-py3.6.egg
attrs 21.4.0 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/attrs-21.4.0-py3.6.egg
Searching for async-timeout==3.0.1
Best match: async-timeout 3.0.1
Processing async_timeout-3.0.1-py3.6.egg
async-timeout 3.0.1 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/async_timeout-3.0.1-py3.6.egg
Searching for gexml==1.2.0
Best match: gexml 1.2.0
Processing gexml-1.2.0-py3.6.egg
gexml 1.2.0 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/gexml-1.2.0-py3.6.egg
Searching for idna==3.3
Best match: idna 3.3
Processing idna-3.3-py3.6.egg
idna 3.3 is already the active version in easy-install.pth

Using /usr/lib/python3.6/site-packages/idna-3.3-py3.6.egg
Finished processing dependencies for spotcot==2.0.2
+ '[' noarch = noarch ']'
+ case "${QA_CHECK_RPATHS:-}" in
+ /usr/lib/rpm/check-buildroot
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
+ /usr/lib/rpm/redhat/brp-compress
/usr/lib/rpm/redhat/brp-compress: line 8: cd: /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64: No such file or directory
+ /usr/lib/rpm/redhat/brp-strip /usr/bin/strip
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
+ /usr/lib/rpm/redhat/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
Can't list /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
+ /usr/lib/rpm/redhat/brp-python-hardlink
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
+ /usr/lib/rpm/redhat/brp-java-repack-jars
find: '/root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64': No such file or directory
Processing files: spotcot-0.0.1-1.el7.noarch
Provides: spotcot = 0.0.1-1.el7
Requires(rpmlib): rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1 rpmlib(CompressedFileNames) <= 3.0.4-1
Checking for unpackaged file(s): /usr/lib/rpm/check-files /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
Wrote: /root/rpmbuild/RPMS/noarch/spotcot-0.0.1-1.el7.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.5KqCl8
+ umask 022
+ cd /root/rpmbuild/BUILD
+ cd spotcot-0.0.1
+ rm -rf /root/rpmbuild/BUILDROOT/spotcot-0.0.1-1.el7.x86_64
+ exit 0
echo

**********************************************************************************************
Use below command to install RPM using yum package manage
yum install /root/rpmbuild/RPMS/noarch/spotcot-0.0.1-1.el7.noarch.rpm
**********************************************************************************************
```

# Install Built RPM
```
[root@6157c14fe292 rpm]# yum install /root/rpmbuild/RPMS/noarch/spotcot-0.0.1-1.el7.noarch.rpm
Loaded plugins: fastestmirror, ovl
Examining /root/rpmbuild/RPMS/noarch/spotcot-0.0.1-1.el7.noarch.rpm: spotcot-0.0.1-1.el7.noarch
Marking /root/rpmbuild/RPMS/noarch/spotcot-0.0.1-1.el7.noarch.rpm to be installed
Resolving Dependencies
There are unfinished transactions remaining. You might consider running yum-complete-transaction, or "yum-complete-transaction --cleanup-only" and "yum history redo last", first to finish them. If those don't work you'll have to try removing/installing packages by hand (maybe package-cleanup can help).
--> Running transaction check
---> Package spotcot.noarch 0:0.0.1-1.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

==============================================================================================================================================================================================================================================================
 Package                                                 Arch                                                   Version                                                     Repository                                                                   Size
==============================================================================================================================================================================================================================================================
Installing:
 spotcot                                                 noarch                                                 0.0.1-1.el7                                                 /spotcot-0.0.1-1.el7.noarch                                                 0.0

Transaction Summary
==============================================================================================================================================================================================================================================================
Install  1 Package

Installed size: 0
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : spotcot-0.0.1-1.el7.noarch                                                                                                                                                                                                                 1/1
  Verifying  : spotcot-0.0.1-1.el7.noarch                                                                                                                                                                                                                 1/1

Installed:
  spotcot.noarch 0:0.0.1-1.el7

Complete!

[root@6157c14fe292 rpm]# cat /etc/centos-release
CentOS Linux release 7.9.2009 (Core)

[root@6157c14fe292 rpm]# spotcot -h
lusage: spotcot [-h] -U COT_URL [-S COT_STALE] -k API_KEY [-i INTERVAL]
               [-p PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -U COT_URL, --cot_url COT_URL
                        URL to CoT Destination.
  -S COT_STALE, --cot_stale COT_STALE
                        CoT Stale period, in seconds
  -k API_KEY, --api_key API_KEY
                        Spot API Key ("XML Feed Id").
  -i INTERVAL, --interval INTERVAL
                        Spot API Query Interval.
  -p PASSWORD, --password PASSWORD
                        Spot Feed Password for private feeds.
```
