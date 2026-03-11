# Mastering Linux Commands

## File and Directory Management 

### `ls` command
> Used to List files

```bash
$ ls
linux		README.md

$ ls -l
total 8
drwxr-xr-x  3 eswarmaganti  staff  96 24 Feb 09:15 linux
-rw-r--r--@ 1 eswarmaganti  staff  70 24 Feb 09:14 README.md

$ ls -la
total 8
drwxr-xr-x@  5 eswarmaganti  staff  160 24 Feb 09:15 .
drwxr-xr-x@ 18 eswarmaganti  staff  576 24 Feb 09:14 ..
drwxr-xr-x@ 13 eswarmaganti  staff  416 24 Feb 09:17 .git
drwxr-xr-x   3 eswarmaganti  staff   96 24 Feb 09:15 linux
-rw-r--r--@  1 eswarmaganti  staff   70 24 Feb 09:14 README.md

# The first column describes the file permissions
# the second column describes the number of hard links. For . there are 5 hard links
# The third column describes the Owner (user) of the file
# The fourth column describes the Group Owner of the file
# The fifth column describes the size of file in bytes. For files its the total size in bytes, for directories it's total size of directory metadata
# Column 6,7,8 describes the last modified timestamp
# The last column describes the file/directory name

$ ls -lh
total 8
drwxr-xr-x  3 eswarmaganti  staff    96B 24 Feb 09:15 linux
-rw-r--r--@ 1 eswarmaganti  staff    70B 24 Feb 09:14 README.md

```

### `pwd` command
> Used to print the present working directory

```bash
$ pwd
/Users/eswarmaganti/Developer/Projects/devops-interview-prep
```

### `cd` command
> Used to change directory

```bash
# changing to a sepcific directory
$ cd /var/log

# changing to parent directory of current directory
$ cd ..

# changing to the user home directory
$ cd ~

# changing to the parent of current directory
$ cd -
```

### `touch` command
> Used to create files

```bash

# Creating a single file using touch

$ touch names.txt
$ ll names.txt
-rw-r--r--  1 eswarmaganti  staff  0 24 Feb 11:25 names.txt

# Creating multiple files 

$ touch names1.txt names2.txt names3.txt
$ ls names*.txt
names.txt	names1.txt	names2.txt	names3.txt	

# Creating multiple files dynamically 
$ touch names{4..6}.txt
$ ls names*.txt
names.txt	names1.txt	names2.txt	names3.txt	names4.txt	names5.txt	names6.txt

# creating multiple files of different file types
$ touch {script.py,config.yaml,data.json}
$ ls -t
data.json	config.yaml	script.py	
```

### `mkdir` command
> Used to create directories
```bash
# Creating a directory 
mkdir data

# Creating nested directories
mkdir -p data/config/test


# Creating a dir and assigning permissions
$ mkdir -m 700 config

$ ls -l | grep config
drwx------  2 eswarmaganti  staff  64 24 Feb 11:39 config

# Creating multiple directories
$ mkdir {dir1,dir2,dir3}
$ mkdir dir{1..3}

# Creating nested directories
$ mkdir -p dir1/{dir11/{dir111,dir112},dir12,dir13}

$ tree dir1
dir1
├── dir11
│   ├── dir111
│   └── dir112
├── dir12
└── dir13

6 directories, 0 files
```

### `mv` command
> Used to move / rename files

```bash

# Renaming a file
$ mv data.txt mydata.txt

# Moving a file to a different path
$ mv mydata.txt ~/

$ ls ~/ | grep mydata.txt
mydata.txt

```

### `rm` command
> Used to delete files/dirs

```bash
# deleting the files / dirs
$ rm mydir/myfile
$ rm -r mydir

# force deleting 
$ rm -f dir/file

```

#### What is the result of `rm -rf /`
> It usually fails or is blocked because of built-in protection.

The output will be like
```
$ sudo rm -rf /
rm: it is dangerous to operate recursively on '/'
rm: use --no-preserve-root to override this failsafe
```

If we run `rm -rf --no-preserve-root /` The system will start deleting everything, we need to reinstall OS.


### `stat` command
> Used to display detailed status information (metadata) about files and file systems

```bash

# status information about a file
/mydir$ stat data.txt 
  File: data.txt
  Size: 12        	Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d	Inode: 786825      Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/ vagrant)   Gid: ( 1000/ vagrant)
Access: 2026-02-24 06:57:58.433666687 +0000
Modify: 2026-02-24 06:57:58.433666687 +0000
Change: 2026-02-24 06:58:15.013952696 +0000
 Birth: 2026-02-24 06:57:58.433666687 +0000

# status information of a directory
 $ stat mydir
  File: mydir
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: fd00h/64768d	Inode: 917506      Links: 2
Access: (0775/drwxrwxr-x)  Uid: ( 1000/ vagrant)   Gid: ( 1000/ vagrant)
Access: 2026-02-24 06:59:17.701280725 +0000
Modify: 2026-02-24 06:58:15.013952696 +0000
Change: 2026-02-24 06:58:15.013952696 +0000
 Birth: 2026-02-24 06:57:40.328618679 +0000
```

### `file` command: 
> Used to determine the type of a file based on its contents

```bash
$ file mydir/data.txt 
mydir/data.txt: ASCII text

$ echo 'print("Hello World!!!")' > mydir/script.py

$ file mydir/script.py 
mydir/script.py: ASCII text

```



### `find` command
> used to recursively search for files and directories within a specified directory hierarchy based on a wide range of criteria.

> Syntax: `find <path> <expression>`

#### Search file by name
```bash
$ sudo find /etc -name nginx.conf
/etc/nginx/nginx.conf

# Case in-sensitive
$ sudo find /etc -iname nginx.conf
/etc/nginx/nginx.conf

# find all the log files 

$ find /var/log -name *.log 2>/dev/null
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/cloud-init.log
/var/log/installer/subiquity-server-info.log
/var/log/installer/cloud-init.log
/var/log/installer/cloud-init-output.log
/var/log/installer/subiquity-client-info.log
/var/log/installer/block/discover.log
/var/log/installer/curtin-install.log
/var/log/installer/subiquity-client-debug.log
/var/log/installer/subiquity-server-debug.log
/var/log/cloud-init-output.log
/var/log/dpkg.log
/var/log/kern.log
/var/log/landscape/sysinfo.log
/var/log/alternatives.log
/var/log/bootstrap.log
/var/log/ubuntu-advantage.log
/var/log/auth.log
/var/log/nginx/access.log
/var/log/nginx/error.log
```

#### Search files by type
```bash

# finding all the files in current dir
$ find . -type f
./mydir/data.txt
./mydir/script.py
./.ssh/authorized_keys
./.bash_history
./.profile
./.bash_logout
./.vbox_version
./.lesshst
./.cache/motd.legal-displayed
./.sudo_as_admin_successful
./.bashrc

# finding all the dirs in current dir
$ find . -type d
.
./mydir
./.ssh
./.config
./.config/procps
./.cache

# Finding the symlink files

$ find . -type l
./script.py
```

#### Search Files by Size

```bash

# Finding files with size more than 1KB
$ find . -type f -size +1k
./.bashrc

# finding files with size more then 100MB
$ find . -type f -size +100M

# finding files with size less than 1KB
$ find . -type f -size -1k
./.cache/motd.legal-displayed
./.sudo_as_admin_successful

```

#### Search files by last modified time / accessed time / metadata changed time (`-mtime/-atime/-ctime`)

```bash
# find files changed in last 1 days
$ find . -mtime -1
.
./mydir
./mydir/data.txt
./mydir/script.py
./.lesshst
./script.py

# find files which are changed in last 30 mins
$ find . -mmin -30
.
./script.py

```
#### Search files by Owner user & group
```bash
$ find . -user vagrant 
.
./mydir
./mydir/data.txt
./mydir/script.py
./.ssh
./.ssh/authorized_keys
./.bash_history
./.profile
./.bash_logout
./.vbox_version
./.lesshst
./.config
./.config/procps
./.cache
./.cache/motd.legal-displayed
./script.py
./.sudo_as_admin_successful
./.bashrc

$ find . -group vagrant
.
./mydir
./mydir/data.txt
./mydir/script.py
./.ssh
./.ssh/authorized_keys
./.bash_history
./.profile
./.bash_logout
./.vbox_version
./.lesshst
./.config
./.config/procps
./.cache
./.cache/motd.legal-displayed
./script.py
./.sudo_as_admin_successful
./.bashrc
```

#### Search files by their permissions
```bash

# find files that all users can access with full permissions
$ find . -perm 777
./script.py

# find files which are having full user permissions
$ find . -perm 700
./.ssh
./.config
./.config/procps
./.cache

# find all the files can  write by all users
$ find . -perm -002
./script.py
```

#### Search files with combine conditions

```bash

# Find all log files having more than 1KB size
$ find /var -name *.log -size +1k 2>/dev/null
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/cloud-init.log
/var/log/cloud-init-output.log
/var/log/dpkg.log
/var/log/kern.log
/var/log/auth.log
/var/log/nginx/access.log

# Find all log and text files having 1KB of size

$ find /var \( -name *.log -o -name *.txt \) -size +1k  2>/dev/null
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/cloud-init.log
/var/log/cloud-init-output.log
/var/log/dpkg.log
/var/log/kern.log
/var/log/auth.log
/var/log/nginx/access.log

# Find all the .txt and .log files
$ find /var -name *.log -o -name *.txt  2>/dev/null
/var/lib/cloud/instances/iid-datasource-none/vendor-data.txt
/var/lib/cloud/instances/iid-datasource-none/cloud-config.txt
/var/lib/cloud/instances/iid-datasource-none/user-data.txt
/var/lib/cloud/instances/iid-datasource-none/vendor-data2.txt
/var/log/apt/history.log
/var/log/apt/term.log
/var/log/cloud-init.log
/var/log/installer/subiquity-server-info.log
/var/log/installer/cloud-init.log
/var/log/installer/cloud-init-output.log
/var/log/installer/subiquity-client-info.log
/var/log/installer/block/discover.log
/var/log/installer/installer-journal.txt
/var/log/installer/curtin-install.log
/var/log/installer/subiquity-client-debug.log
/var/log/installer/subiquity-server-debug.log
/var/log/cloud-init-output.log
/var/log/dpkg.log
/var/log/kern.log
/var/log/landscape/sysinfo.log
/var/log/alternatives.log
/var/log/bootstrap.log
/var/log/ubuntu-advantage.log
/var/log/auth.log
/var/log/nginx/access.log
/var/log/nginx/error.log
```

#### Executing commands with find

```bash
# Delete all the log files which are older than 30 days and sire larger than 10MB
$ find /var -name *.log -mtime +30 -size +10M -delete  2>/dev/null


# Find the symbolic link file created today and delete it

# method 1
$ find . -name script.py -type l -mtime 0 -exec rm {} \;

# method 2
$ find . -name script.py -type l -mtime 0 -delete

# method 3
$ ln -s mydir/script.py $(pwd)/script.py
$ find . -name script.py -type l -mtime 0 -exec rm {} +
```

We can use `{} \;` or `{} +` to run the command on searched files. 
- `\;` : runs once per file
- `+` : batches files (a faster way)


#### using xargs with find
```bash
# printing the content of each file using find with xargs
$ find . -type f -name *.py | xargs cat
print("Hello World!!!")
print(f"Welcome!!! Eswar Maganti")

# executing multiple python files using find
$ find . -type f -name *.py -exec python3 {} \;
Hello World!!!
Welcome!!! Eswar Maganti

```

#### Search all empty files & dirs 
```bash
# finding empty files
$ find . -type f -empty 
./.cache/motd.legal-displayed
./temp.log
./.sudo_as_admin_successful

# finding empty dirs
$ find . -type d -empty 
./.config/procps

```

---

## Text Processing 

### `less` : 
> A terminal pager used to view the contents of a file or the output of a command one screen at a time, allowing for both forward and backward navigation

```bash
$ less /etc/nginx/nginx.conf 
```

### `more`: 
> A utility used to view text files one screen (or page) at a time. It allows only forward movement only

```bash
$ more /etc/nginx/nginx.conf 
```

### `head` command
> Used to display the initial lines or bytes of a file

```bash

# using the head command without any options
$ head /etc/nginx/nginx.conf 
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

# using head command to print specific number of lines 

$ head -n 20 /etc/nginx/nginx.conf 
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	types_hash_max_size 2048;
	# server_tokens off;
```

### `tail` command
> Used to display the last few lines or bytes of a file

```bash
# using tail command without any options
$ tail /etc/nginx/nginx.conf 
#		protocol   pop3;
#		proxy      on;
#	}
#
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}

# using tail command to print last 20 lines in a file
$ tail -n 20 /etc/nginx/nginx.conf 
#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
#
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
```

### `grep` Command
> Used for searching and filtering text based on specified patterns within files or data streams (Global Regular Expression Print)

```bash
# Count total lines using grep

$ grep -c "" /var/log/nginx/access.log 
124

# Finding failed requests from nginx log
$ grep "404" /var/log/nginx/access.log  
127.0.0.1 - - [24/Feb/2026:07:31:56 +0000] "GET /abc HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:00 +0000] "GET /abc/dca HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"

# Find the count of failed requests
$ grep -c "404" /var/log/nginx/access.log  
22

# Find all the IP addresses from nginx access log
$ grep -oE '^[0-9.]+' /var/log/nginx/access.log  
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1
127.0.0.1


# Find all the GET Requests
$ grep "\"GET" /var/log/nginx/access.log 
127.0.0.1 - - [24/Feb/2026:07:26:37 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:31:52 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:31:56 +0000] "GET /abc HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:00 +0000] "GET /abc/dca HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:53 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"

# Find all the requests which are made 1 minute ago
$ grep "$(date -d '1 minute ago' '+%d/%b/%Y:%H:%M')" /var/log/nginx/access.log 
127.0.0.1 - - [24/Feb/2026:07:56:13 +0000] "GET / HTTP/1.1" 200 612 "-" "curl/7.81.0"

# Unmatching the specific patterns
$ grep -v '200' /var/log/nginx/access.log
127.0.0.1 - - [24/Feb/2026:07:31:56 +0000] "GET /abc HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:32:00 +0000] "GET /abc/dca HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0"
127.0.0.1 - - [24/Feb/2026:07:34:44 +0000] "GET /profile HTTP/1.1" 404 162 "-" "curl/7.81.0" 


# Finding running processes
$ ps aux | grep nginx
root        3341  0.0  1.2  55072 10628 ?        S    07:10   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    3344  0.0  0.7  55768  6436 ?        S    07:10   0:00 nginx: worker process
vagrant     3753  0.0  0.2   5912  1912 pts/0    S+   08:43   0:00 grep --color=auto nginx

# Working with processes
$ ps aux | grep [n]ginx
root        3341  0.0  1.2  55072 10628 ?        S    07:10   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    3344  0.0  0.7  55768  6436 ?        S    07:10   0:00 nginx: worker process
```

### `awk` Command
> Used for text processing, data extraction, and report generation.

> Syntax: `awk 'pattern { action }' file`

Builtin Variables
- `$0` : Entire Line
- `$1`: First Column
- `$2`: Second Column
- `NF`: Number of fields
- `NR`: Number of rows
- `FS`: Field Separator
- `OFS`: Output field separator

```bash

# Extracting the filesystem mounts, type and used %

$ df -Th | awk 'BEGIN {OFS=" - "} NR > 1 { print $NF,$2,$(NF-1) }'
/run - tmpfs - 2%
/ - ext4 - 27%
/dev/shm - tmpfs - 0%
/run/lock - tmpfs - 0%
/boot - ext4 - 7%
/boot/efi - vfat - 1%
/vagrant - vboxsf - 63%
/run/user/1000 - tmpfs - 1%


# Extracting the 404 requests from nginx log and printing the count of each request

$ awk '$9=404 { print $1, $6 }' /var/log/nginx/access.log | sort | uniq -c
    104 127.0.0.1 /
      1 127.0.0.1 /abc
      1 127.0.0.1 /abc/dca
     20 127.0.0.1 /profile


# Find all the pods which are not in running state
$ kubectl get pods --all-namespaces | awk 'NR>1 && $4!="Running" { print $2, $4 }'
ingress-nginx-admission-create-5glrx Completed
ingress-nginx-admission-patch-cs8fj Completed

# Finding the count of pods running in each namespace
$ kubectl get pods --all-namespaces | awk 'NR>1 {print $1}' | sort | uniq -c
   2 app2
   7 argocd
   3 cert-manager
   3 ingress-nginx
   7 kube-system
   1 portfolio

# Finding the sum of all files in a directory
$ ls -la /etc/nginx/ | awk '{sum += $5} END { print sum}' 
49963
```

#### BEGIN and END in awk

```bash
# Basic Syntax
awk '
BEGIN { ... }
{ ... }          # runs for each line
END { ... }
' file
```
Use `BEGIN` when you need:
- Initialization
- Set Variables
- Define FS, OFS
- Print Header
- Print Starting Message

Use `END` when you
- Summary
- Totals
- Average
- Final Result
- Footer


### `sed` command
> A powerful, non-interactive text manipulation tool used for filtering and transforming text from an input stream

> Syntax `sed <command> file`

#### Replacing text
```bash
$ cat data.txt 
Hello World
Welcome to DevOps
I Love DevOps

# Replacing the first occurrence 
$ sed 's/Hello/Hai/' data.txt 
Hai World
Welcome to DevOps
I Love DevOps

# Replacing all occurrences
$ sed 's/DevOps/Cloud \ \& \DevOps/g' data.txt 
Hello World
Welcome to Cloud  & DevOps
I Love Cloud  & DevOps
```

#### modifying the file
```bash
# replacing a word in a file
$ sed -i 's/Hello/Hai/' data.txt 

$ cat data.txt 
Hai World
Welcome to DevOps
I Love DevOps

# removing a line from a file
$ cat data.txt 
Hai World
Welcome to DevOps
I Love DevOps
Dummy Line

$ sed -i 4d data.txt 

$ cat data.txt 
Hai World
Welcome to DevOps
I Love DevOps

# Delete lines containing a specific work
$ cat data.txt 
Hai World
Welcome to DevOps
I Love DevOps

$ sed -i '/DevOps/d' data.txt 

$ cat data.txt 
Hai World
```

#### Replacing only specific line numbers
```bash
$ sed '5s/DevOps/DEVOPS/' data.txt 
Hai World
Welcome to DevOps
DevOps is a culture which automates the Dev and Ops 
DevOps include automating manual process, IaC, Configuration Management, Container Orchestration.
Few most popular DEVOPS tools are Kubernetes, Ansible, Terraform, Docker e.t.c
```

#### Replace only matching lines
```bash
$ sed '/Few/s/DevOps/DEVOPS/' data.txt 
Hai World
Welcome to DevOps
DevOps is a culture which automates the Dev and Ops 
DevOps include automating manual process, IaC, Configuration Management, Container Orchestration.
Few most popular DEVOPS tools are Kubernetes, Ansible, Terraform, Docker e.t.c
```

#### Inserting data 
```bash
# Inserting text at line number 1
$ sed '1i Hello World!!!' data.txt 
Hello World!!!
Hai World
Welcome to DevOps
DevOps is a culture which automates the Dev and Ops 
DevOps include automating manual process, IaC, Configuration Management, Container Orchestration.
Few most popular DevOps tools are Kubernetes, Ansible, Terraform, Docker e.t.c


# Appending text after line number 3
sed '3a I love scripting in Python' data.txt 
Hai World
Welcome to DevOps
DevOps is a culture which automates the Dev and Ops 
I love scripting in Python
DevOps include automating manual process, IaC, Configuration Management, Container Orchestration.
Few most popular DevOps tools are Kubernetes, Ansible, Terraform, Docker e.t.c
```

#### Printing specific lines of a file
```bash
# Printing a specific line
$ sed -n '2p' data.txt 
Welcome to DevOps

# printing a range of lines
$ sed -n '2,5p' data.txt 
Welcome to DevOps
DevOps is a culture which automates the Dev and Ops 
DevOps include automating manual process, IaC, Configuration Management, Container Orchestration.
Few most popular DevOps tools are Kubernetes, Ansible, Terraform, Docker e.t.c

# Printing lines matching a pattern
$ sed -n '/DevOps/p' data.txt 
Welcome to DevOps
DevOps is a culture which automates the Dev and Ops 
DevOps include automating manual process, IaC, Configuration Management, Container Orchestration.
Few most popular DevOps tools are Kubernetes, Ansible, Terraform, Docker e.t.c
```

#### Removing comments from a file
```bash
$ sed '/^[[:space:]]*#/d' /etc/nginx/nginx.conf 

user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
}

http {


	sendfile on;
	tcp_nopush on;
	types_hash_max_size 2048;


	include /etc/nginx/mime.types;
	default_type application/octet-stream;


	ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;


	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;


	gzip on;



	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}
```

---

## Permissions in Linux

### Understanding permissions

```bash
$ ls -l data.txt 
-rw-rw-r-- 1 vagrant vagrant 258 Feb 24 14:39 data.txt
```

```
- rwx r-x r--
│ │   │   │
│ │   │   └── Others
│ │   └────── Group
│ └────────── Owner
└──────────── File type
```

File Types
- `-` : Regular file
- `d` : Directory
- `l` : Symlink
- `c` : Character device
- `b` : Block device

Permission Meaning
- `r (4)` : read
- `w (2)` : write
- `x (1)` : execute

### `chmod` command
> used to change the access permissions (or mode) of files and directories.

#### Changing the permissions of a file using Numeric mode
```bash
$ ls -l greet.py 
-rw-rw-r-- 1 vagrant vagrant 23 Feb 25 02:47 greet.py

$ chmod 755 greet.py 

$ ls -l greet.py 
-rwxr-xr-x 1 vagrant vagrant 23 Feb 25 02:47 greet.py
```

#### Changing file permissions using symbolic mode
```bash
# adding execute permissions to owner
$ chmod u+x greet.py 

# adding execute permission to the group
$ chmod g+x greet.py 

# removing read permission to others
$ chmod o-r greet.py 

$ ls -l greet.py 
-rwxrwx--- 1 vagrant vagrant 23 Feb 25 02:47 greet.py
```

#### Recusrively change the permissions to all the files in a directory

```bash
$ ls -l mydir
total 12
-rw-rw-r-- 1 vagrant vagrant 12 Feb 24 06:57 data.txt
-rw-rw-r-- 1 vagrant vagrant 35 Feb 24 11:02 hello.py
-rw-rw-r-- 1 vagrant vagrant 24 Feb 24 07:07 script.py

$ chmod -R 775 mydir

$ ls -l mydir
total 12
-rwxrwxr-x 1 vagrant vagrant 12 Feb 24 06:57 data.txt
-rwxrwxr-x 1 vagrant vagrant 35 Feb 24 11:02 hello.py
-rwxrwxr-x 1 vagrant vagrant 24 Feb 24 07:07 script.py
```

### `chown` command
> Used to change the user and/or group ownership of a specified file or directory.

Basic Syntax
```bash
chown user file
chown user:group file
```

#### changing the owern of a file
```bash
$ ls -l /var/www/html/index.nginx-debian.html 
-rw-r--r-- 1 root root 612 Feb 24 07:10 /var/www/html/index.nginx-debian.html

$ sudo chown nginx:nginx /var/www/html/index.nginx-debian.html 

$ ls -l /var/www/html/index.nginx-debian.html 
-rw-r--r-- 1 nginx nginx 612 Feb 24 07:10 /var/www/html/index.nginx-debian.html
```

#### recusrively changing the ownership of a directory
```bash
$ ls -l /var/www/
total 4
drwxr-xr-x 2 root root 4096 Feb 24 07:10 html

$ sudo chown -R nginx:nginx /var/www

$ ls -l /var/www/
total 4
drwxr-xr-x 2 nginx nginx 4096 Feb 24 07:10 html
```

### Special Permissions (SUID, SGID)

`SUID` allows an executable file to run with the privileges of the file's owner rather than the user who execute it.
```bash
$ chmod 4755 greet.py 
# chmod u+s greet.py  - works the same way

$ ls -l greet.py 
-rwsr-xr-x 1 vagrant vagrant 23 Feb 25 02:47 greet.py

$ sudo python3 greet.py 
Hello World!!
```

`SGID` forces new files/subdirectories to inherit the directory's group ownership rather than the creator's primary group
```bash
$ chmod 2755 mydir
# chmod g+s mydir - works the same way

$ ls -l | grep mydir
drwxr-sr-x 2 vagrant nginx   4096 Feb 25 03:27 mydir

$ touch mydir/test2.log

$ ls -l mydir/test2.log 
-rw-rw-r-- 1 vagrant nginx 0 Feb 25 03:26 mydir/test2.log
```

### `sudo` command
> `sudo` stands for "Superuser Do". It allows a permitted user to execute a command as another user (by default roo) according to the security policy defined in `/etc/sudoers`

#### How the `sudo` works
When we run any command with prefixed with `sudo` the systems will check
- The user listed in `/etc/sudoers` or not
- The user can run this command or not
- Prompts for user password
- executes the command

All the sudo commands are logged under
> `/var/log/auth.log` (Ubuntu)
> `/var/log/secure` (RHEL)

Difference between `sudo su -` & `sudo -i`

> Using `sudo su -` opens full root shell, harder to audit and can tun dangerous commands accidentally

> Using `sudo -i` starts root login shell

---

## Process Management

### What is a process
A process is a running instance of a program
Each process has:
- PID (Process ID)
- PPID (Parent PID)
- User
- CPU Usage
- Memory
- State

### Zombie Process
A zombie process is a terminated child process that remains in the system's process table because its parent has not yet read its exit status using the `wait()` system call
While it consumes no CPU or memory resources, it occupies a PID

### `ps` process snapshot command
> shows the snaphot of running processes (not real-time)

we can use `ps aux` or `ps -ef (RHEL)`
```
# Show all the processes running 
$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  1.2 102420 11080 ?        Ss   Feb24   0:05 /sbin/init autoinstall
root           2  0.0  0.0      0     0 ?        S    Feb24   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   Feb24   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   Feb24   0:00 [rcu_par_gp]
.
.
.


# To show process tree
$ ps -ef --forest
UID          PID    PPID  C STIME TTY          TIME CMD
root           2       0  0 Feb24 ?        00:00:00 [kthreadd]
root           3       2  0 Feb24 ?        00:00:00  \_ [rcu_gp]
root           4       2  0 Feb24 ?        00:00:00  \_ [rcu_par_gp]
root           5       2  0 Feb24 ?        00:00:00  \_ [slub_flushwq]
root           6       2  0 Feb24 ?        00:00:00  \_ [netns]
root           8       2  0 Feb24 ?        00:00:00  \_ [kworker/0:0H-events_highpri]
root          10       2  0 Feb24 ?        00:00:00  \_ [mm_percpu_wq]
root          11       2  0 Feb24 ?        00:00:00  \_ [rcu_tasks_rude_]
root          12       2  0 Feb24 ?        00:00:00  \_ [rcu_tasks_trace]
root          13       2  0 Feb24 ?        00:00:00  \_ [ksoftirqd/0]
root          14       2  0 Feb24 ?        00:00:00  \_ [rcu_sched]
root          15       2  0 Feb24 ?        00:00:00  \_ [migration/0]
root          16       2  0 Feb24 ?        00:00:00  \_ [idle_inject/0]
root          18       2  0 Feb24 ?        00:00:00  \_ [cpuhp/0]
root          19       2  0 Feb24 ?        00:00:00  \_ [kdevtmpfs]
root          20       2  0 Feb24 ?        00:00:00  \_ [inet_frag_wq]
root          21       2  0 Feb24 ?        00:00:00  \_ [kauditd]
root          22       2  0 Feb24 ?        00:00:00  \_ [khungtaskd]
root          23       2  0 Feb24 ?        00:00:00  \_ [oom_reaper]
root          24       2  0 Feb24 ?        00:00:00  \_ [writeback]
root          25       2  0 Feb24 ?        00:00:07  \_ [kcompactd0]
root          26       2  0 Feb24 ?        00:00:00  \_ [ksmd]
root          27       2  0 Feb24 ?        00:00:00  \_ [khugepaged]
root          73       2  0 Feb24 ?        00:00:00  \_ [kintegrityd]
root          74       2  0 Feb24 ?        00:00:00  \_ [kblockd]
root          75       2  0 Feb24 ?        00:00:00  \_ [blkcg_punt_bio]
root          76       2  0 Feb24 ?        00:00:00  \_ [tpm_dev_wq]
root          77       2  0 Feb24 ?        00:00:00  \_ [ata_sff]
root          78       2  0 Feb24 ?        00:00:00  \_ [md]
root          79       2  0 Feb24 ?        00:00:00  \_ [edac-poller]
root          80       2  0 Feb24 ?        00:00:00  \_ [devfreq_wq]
root          81       2  0 Feb24 ?        00:00:00  \_ [watchdogd]
root          83       2  0 Feb24 ?        00:00:00  \_ [kworker/0:1H-kblockd]
root          84       2  0 Feb24 ?        00:00:00  \_ [kswapd0]
root          85       2  0 Feb24 ?        00:00:00  \_ [ecryptfs-kthrea]
root          87       2  0 Feb24 ?        00:00:00  \_ [kthrotld]
root          88       2  0 Feb24 ?        00:00:00  \_ [acpi_thermal_pm]
root          90       2  0 Feb24 ?        00:00:00  \_ [mld]
root          91       2  0 Feb24 ?        00:00:00  \_ [ipv6_addrconf]
root         100       2  0 Feb24 ?        00:00:00  \_ [kstrp]
root         103       2  0 Feb24 ?        00:00:00  \_ [zswap-shrink]
root         104       2  0 Feb24 ?        00:00:00  \_ [kworker/u3:0]
root         107       2  0 Feb24 ?        00:00:00  \_ [cryptd]
root         145       2  0 Feb24 ?        00:00:00  \_ [charger_manager]
root         181       2  0 Feb24 ?        00:00:00  \_ [scsi_eh_0]
root         182       2  0 Feb24 ?        00:00:00  \_ [scsi_tmf_0]
root         253       2  0 Feb24 ?        00:00:00  \_ [kdmflush]
root         284       2  0 Feb24 ?        00:00:00  \_ [raid5wq]
root         335       2  0 Feb24 ?        00:00:00  \_ [jbd2/dm-0-8]
root         336       2  0 Feb24 ?        00:00:00  \_ [ext4-rsv-conver]
root         437       2  0 Feb24 ?        00:00:00  \_ [kaluad]
root         442       2  0 Feb24 ?        00:00:00  \_ [kmpath_rdacd]
root         444       2  0 Feb24 ?        00:00:00  \_ [kmpathd]
root         445       2  0 Feb24 ?        00:00:00  \_ [kmpath_handlerd]
root         474       2  0 Feb24 ?        00:00:00  \_ [iprt-VBoxWQueue]
root         569       2  0 Feb24 ?        00:00:00  \_ [jbd2/sda2-8]
root         570       2  0 Feb24 ?        00:00:00  \_ [ext4-rsv-conver]
root        4307       2  0 06:46 ?        00:00:00  \_ [kworker/0:7-inode_switch_wbs]
root        4308       2  0 06:46 ?        00:00:05  \_ [kworker/0:8-events]
root        4822       2  0 08:16 ?        00:00:00  \_ [kworker/u2:0-events_unbound]
root        4826       2  0 08:35 ?        00:00:00  \_ [kworker/u2:1-ext4-rsv-conversion]
root        4874       2  0 09:04 ?        00:00:00  \_ [kworker/u2:2-events_power_efficient]
root           1       0  0 Feb24 ?        00:00:05 /sbin/init autoinstall
root         408       1  0 Feb24 ?        00:00:01 /lib/systemd/systemd-journald
root         443       1  0 Feb24 ?        00:00:00 /lib/systemd/systemd-udevd
root         446       1  0 Feb24 ?        00:00:08 /sbin/multipathd -d -s
systemd+     642       1  0 Feb24 ?        00:00:00 /lib/systemd/systemd-networkd
systemd+     644       1  0 Feb24 ?        00:00:00 /lib/systemd/systemd-resolved
message+     659       1  0 Feb24 ?        00:00:12 @dbus-daemon --system --address=systemd: --nofork 
root         666       1  0 Feb24 ?        00:00:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --ru
root         667       1  0 Feb24 ?        00:00:00 /usr/libexec/polkitd --no-debug
syslog       669       1  0 Feb24 ?        00:00:00 /usr/sbin/rsyslogd -n -iNONE
root         673       1  0 Feb24 ?        00:00:04 /lib/systemd/systemd-logind
root         674       1  0 Feb24 ?        00:00:00 /usr/libexec/udisks2/udisksd
root         707       1  0 Feb24 ?        00:00:00 /usr/sbin/cron -f -P
root         712       1  0 Feb24 tty1     00:00:00 /sbin/agetty -o -p -- \u --noclear tty1 linux
root         728       1  0 Feb24 ?        00:00:00 /usr/sbin/ModemManager
root        1011       1  0 Feb24 ?        00:00:18 /usr/sbin/VBoxService --pidfile /var/run/vboxadd-s
root        1055       1  0 Feb24 ?        00:00:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 sta
root        1505    1055  0 Feb24 ?        00:00:00  \_ sshd: vagrant [priv]
vagrant     1545    1505  0 Feb24 ?        00:00:06      \_ sshd: vagrant@pts/0
vagrant     1546    1545  0 Feb24 pts/0    00:00:02          \_ -bash
vagrant     4875    1546  0 09:05 pts/0    00:00:00              \_ ps -ef --forest
vagrant     1509       1  0 Feb24 ?        00:00:00 /lib/systemd/systemd --user
vagrant     1510    1509  0 Feb24 ?        00:00:00  \_ (sd-pam)
root        1880       1  0 Feb24 ?        00:00:01 /usr/libexec/packagekitd
root        2162       1  0 Feb24 ?        00:00:16 /snap/snapd/current/usr/lib/snapd/snapd
root        3341       1  0 Feb24 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on
www-data    3344    3341  0 Feb24 ?        00:00:00  \_ nginx: worker process
```

### `top` command
> It's used to monitor the realtime processes. It shows the CPU usage, Memory usage, Load average, Running processes

```bash
$ top

top - 09:06:58 up  9:26,  1 user,  load average: 0.07, 0.02, 0.00
Tasks:  89 total,   1 running,  88 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.3 sy,  0.0 ni, 99.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :    834.1 total,    127.8 free,    162.0 used,    544.4 buff/cache
MiB Swap:   5722.0 total,   5714.7 free,      7.3 used.    576.0 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                       
   4876 vagrant   20   0    9988   3348   2756 R   0.3   0.4   0:00.03 top                           
      1 root      20   0  102420  11080   7228 S   0.0   1.3   0:05.69 systemd                       
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.08 kthreadd 
```

### `htop` command
> works simillar to top command and provides features like Colored UI, Scrollable, Easier Killing and Tree View

![Htop](../images/htop.png)


### LInux Signals

Signals in Linux are software interrupts used for inter-process communication (IPC), allowing the operating system ot other processes to notify a runnning program of an event.
Process can be instructed to terminate, stop, continue, ignore the signal, or execute a custom function (signal handler) in response.

### Key Concepts
- **Asynchronous**: Signals can arrive and interrupt a process's normal flow of execution at any time.
- **Identification**: Each signal has a unique name and number
- **Default Action**: Every signal has a system-defined default action, such as terminating the process or ignoring the signal.
- **Handling**: Programs can override default actions by installing a custom signal handler, a specific function that runs upon signal receipt.
- **Uncatchable Signals**: Two signals, `SIGKILL(9)` and `SIGSTOP(19)`, cannot be caught, ignored, or blocked by a process, ensuring the OS can always manage processes.

### Common Signals
| Signal Name | Number | Description | Default Action |
| ----------- | ------ | ----------- | -------------- |
| `SIGHUP`   | 1      | Hangup detected on controlling terminal | Terminate |
| `SIGINT` | 2 | Interrupt from key board | Terminate |
| `SIGQUIT` | 3 | Quit from keyboard | Terminate (core dump) |
| `SIGFPE` | 8 | Floating-point exception (e.g., divide by zero) | Terminate |
| `SIGKILL` | 9 | Kill signal (cannot be caught or ignored) | Terminate |
| `SIGSEGV` | 11 | Invalid memory refrence | Terminate (core dump) |
| `SIGPIPE` | 13 | Write to pipe with no reader | Terminate |
| `SIGTERM` | 15 | Software termination signal (default of the kill command) | Terminate | 
| `SIGSTOP` | 19 | Stop process (cannot be caught or ignored) | Stop the process | 
| `SIGCONT` | 18 | Continue executing if stopped | Continue the process |  

### Difference b/w `SIGTERM`, `SIGKILL` & `SIGSTOP`
- `SIGTERM` is a polite request to exit, allowing the process a change to clean up its resources and exit
- `SIGKILL` is an immediate, inescapable termination command issued by the operating system kernal, used when a process is unresponsive.
- `SIGSTOP` does not terminate the process but instead freezes its execution entirely, allowing it to be resumed later with a SIGCONT signal

### `kill` command
> send signal to process, `kill` does NOT always mean "terminate" it sends a signal.

Basic Usage
> kill <PID>

#### Terminating a process using kill command
```bash
$ ps aux | grep [n]ginx
root        3341  0.0  1.1  55072  9500 ?        S    Feb24   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    3344  0.0  0.7  55768  6372 ?        S    Feb24   0:00 nginx: worker process

$ sudo kill -9 3341

$ ps aux | grep [n]ginx
```

#### Stopping ans resuming a service using kill command
```bash
$ ps aux | grep [n]ginx
root        4996  0.0  0.1  55068  1620 ?        Ss   09:42   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    4997  0.0  0.7  55764  6136 ?        S    09:42   0:00 nginx: worker process

# Stopping the master and worker process
$ sudo kill -SIGSTOP 4996 4997

# The process state is `T` which means stopped
$ ps aux | grep [n]ginx
root        4996  0.0  0.1  55068  1620 ?        Ts   09:42   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    4997  0.0  0.7  55764  6136 ?        T    09:42   0:00 nginx: worker process

# Resuming the process using SIGCONT signal
$ sudo kill -SIGCONT 4996 4997

$ ps aux | grep [n]ginx
root        4996  0.0  0.2  55068  2456 ?        Ss   09:42   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    4997  0.0  0.7  55764  6460 ?        S    09:42   0:00 nginx: worker process
```

### `nice` and `renice` commands
> Used to manage the CPU scheduling priority of processes, known as the niceness value. The niceness value ranges from -20 (highest priority) to +19 (lowest priority), with a default value of 0.

#### Start a process with priority
```bash
nice -n 10 python3 script.py
```

#### Change the priority of running process
```bash
renice -n 5 -p <PID>
```

## `systemctl` command
> is a powerful command-line utility to control the `systemd` system and service manager in modern Linux distributions.

```bash
# checking the status of a service
$ systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2026-02-25 09:42:37 UTC; 2h 56min ago
       Docs: man:nginx(8)
    Process: 4994 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, s>
    Process: 4995 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/S>
   Main PID: 4996 (nginx)
      Tasks: 2 (limit: 837)
     Memory: 2.5M
        CPU: 18ms
     CGroup: /system.slice/nginx.service
             ├─4996 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─4997 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >

Feb 25 09:42:37 ubuntulvmlab0101 systemd[1]: Starting A high performance web server and a reverse pro>
Feb 25 09:42:37 ubuntulvmlab0101 systemd[1]: Started A high performance web server and a reverse prox

# stopping a running service
$ sudo systemctl stop nginx

# starting a service
$ sudo systemctl start nginx

# restarting a service
$ sudo systemctl restart nginx

# reloading a service (graceful)
$ sudo systemctl reload nginx

# enabling a service at boot
$ sudo systemctl enable nginx
Synchronizing state of nginx.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable nginx

# disabling a service
$ sudo systemctl disable  nginx
Synchronizing state of nginx.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install disable nginx
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.

```

---

## Disk & File System Usage

### `df` command
> Used to display the amount of availabe and used disk space on mounted file system

```bash
# human readable format
$ df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                               84M  972K   83M   2% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   30G  7.7G   21G  28% /
tmpfs                              418M     0  418M   0% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          2.0G  125M  1.7G   7% /boot
/dev/sda1                          1.1G  6.4M  1.1G   1% /boot/efi
vagrant                            461G  288G  173G  63% /vagrant
tmpfs                               84M  8.0K   84M   1% /run/user/1000

# Show specific filesystem usage
$ df -h /dev/sda2
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       2.0G  125M  1.7G   7% /boot

# Show filesystem type
$ df -Th
Filesystem                        Type    Size  Used Avail Use% Mounted on
tmpfs                             tmpfs    84M  972K   83M   2% /run
/dev/mapper/ubuntu--vg-ubuntu--lv ext4     30G  7.7G   21G  28% /
tmpfs                             tmpfs   418M     0  418M   0% /dev/shm
tmpfs                             tmpfs   5.0M     0  5.0M   0% /run/lock
/dev/sda2                         ext4    2.0G  125M  1.7G   7% /boot
/dev/sda1                         vfat    1.1G  6.4M  1.1G   1% /boot/efi
vagrant                           vboxsf  461G  288G  173G  63% /vagrant
tmpfs                             tmpfs    84M  8.0K   84M   1% /run/user/1000
```

### `du` command
> A standard linux utility used to estimate and display the disk space consumed by files and directories

> Syntax: `du <directory>`

```bash
$ du .
16	./mydir
8	./.ssh
4	./.config/procps
8	./.config/htop
16	./.config
4	./.cache
88	.

# human readable format
$ du . -h
16K	./mydir
8.0K	./.ssh
4.0K	./.config/procps
8.0K	./.config/htop
16K	./.config
4.0K	./.cache
88K	.

```

#### Find the top 10 large files in the system

```bash
# du -ah = will check for all files and returns human readable format
# sort -hr = will sort the records the records in reverse order and prints in human readable format

$ sudo du -ah / | sort -hr | head -10
9.0G	/
5.6G	/swap.img
1.3G	/usr
1.2G	/snap
933M	/usr/lib
861M	/var
729M	/snap/lxd
683M	/var/lib
483M	/usr/lib/modules/5.15.0-160-generic
483M	/usr/lib/modules
```

## Networking Tools

### `ping` command
> checks if a host is reachable and measures latency

> syntax: `ping <ip/hostname>`

```bash
# pinging a IP address
$ ping 142.250.205.110
PING 142.250.205.110 (142.250.205.110) 56(84) bytes of data.
64 bytes from 142.250.205.110: icmp_seq=1 ttl=255 time=83.0 ms
64 bytes from 142.250.205.110: icmp_seq=2 ttl=255 time=81.8 ms
64 bytes from 142.250.205.110: icmp_seq=3 ttl=255 time=124 ms
64 bytes from 142.250.205.110: icmp_seq=4 ttl=255 time=207 ms
^C
--- 142.250.205.110 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3009ms
rtt min/avg/max/mdev = 81.760/124.047/207.343/51.009 ms

# pinging a hostname
$ ping google.com
PING google.com (142.250.205.110) 56(84) bytes of data.
64 bytes from pnmaaa-ao-in-f14.1e100.net (142.250.205.110): icmp_seq=1 ttl=255 time=75.6 ms
64 bytes from pnmaaa-ao-in-f14.1e100.net (142.250.205.110): icmp_seq=2 ttl=255 time=78.8 ms
64 bytes from pnmaaa-ao-in-f14.1e100.net (142.250.205.110): icmp_seq=3 ttl=255 time=73.2 ms
64 bytes from pnmaaa-ao-in-f14.1e100.net (142.250.205.110): icmp_seq=4 ttl=255 time=70.9 ms
64 bytes from pnmaaa-ao-in-f14.1e100.net (142.250.205.110): icmp_seq=5 ttl=255 time=95.0 ms
^C
--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4004ms
rtt min/avg/max/mdev = 70.935/78.707/94.979/8.538 ms

# pinging a IPv6 address/hostname
$ ping6  google.com
PING google.com(pnmaaa-ax-in-x0e.1e100.net (2404:6800:4007:80c::200e)) 56 data bytes
64 bytes from pnmaaa-ax-in-x0e.1e100.net (2404:6800:4007:80c::200e): icmp_seq=1 ttl=255 time=89.6 ms
64 bytes from maa05s02-in-x0e.1e100.net (2404:6800:4007:80c::200e): icmp_seq=2 ttl=255 time=81.6 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 81.565/85.581/89.598/4.016 ms
```

### `curl` command
> send HTTP requests and fetch responses

> Syntax : `curl <url>`

```bash

# send a basic HTTP Get request
$ curl http://127.0.0.1
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

# Send a Get request but only receive headers
$ curl -I http://127.0.0.1
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 26 Feb 2026 09:02:22 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 24 Feb 2026 07:10:06 GMT
Connection: keep-alive
ETag: "699d4ece-264"
Accept-Ranges: bytes

# explicity specifying the HTTP method using -X to send GET and POST requests

$ $ curl -X GET https://jsonplaceholder.typicode.com/todos/1 
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}


$ curl -X POST  https://jsonplaceholder.typicode.com/todos -H "Content-Type: application/json"  -d '{"userId": 2,"id": 2, "title": "dummy", "completed": false}' 
{
  "userId": 2,
  "id": 201,
  "title": "dummy",
  "completed": false
}

$curl -X DELETE  https://jsonplaceholder.typicode.com/todos/1 
{}
```

### `wget` command
> Used to download files

```bash
# downloading a file
$ wget httpbin.org/get
--2026-02-26 09:25:34--  http://httpbin.org/get
Resolving httpbin.org (httpbin.org)... 3.94.221.249, 52.6.202.211, 3.93.97.64, ...
Connecting to httpbin.org (httpbin.org)|3.94.221.249|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 291 [application/json]
Saving to: ‘get’

get                       100%[===================================>]     291  --.-KB/s    in 0s      

2026-02-26 09:25:35 (25.3 MB/s) - ‘get’ saved [291/291]

# specifying a filename with wget
$ wget httpbin.org/get -o wget-response

$ cat wget-response 
--2026-02-26 09:25:59--  http://httpbin.org/get
Resolving httpbin.org (httpbin.org)... 52.200.102.227, 44.195.71.76, 3.93.97.64, ...
Connecting to httpbin.org (httpbin.org)|52.200.102.227|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 291 [application/json]
Saving to: ‘get.1’

     0K                                                       100% 5.93M=0s

2026-02-26 09:26:00 (5.93 MB/s) - ‘get.1’ saved [291/291]


# -S to test the destination url , --spider to test without downloading the file
$ wget httpbin.org/get -S --spider
Spider mode enabled. Check if remote file exists.
--2026-02-26 09:28:39--  http://httpbin.org/get
Resolving httpbin.org (httpbin.org)... 52.200.102.227, 3.93.97.64, 3.94.221.249, ...
Connecting to httpbin.org (httpbin.org)|52.200.102.227|:80... connected.
HTTP request sent, awaiting response... 
  HTTP/1.1 200 OK
  Date: Thu, 26 Feb 2026 09:28:40 GMT
  Content-Type: application/json
  Content-Length: 291
  Connection: keep-alive
  Server: gunicorn/19.9.0
  Access-Control-Allow-Origin: *
  Access-Control-Allow-Credentials: true
Length: 291 [application/json]
Remote file exists.
```

### `ip` command
> utility for displaying and manipulating network interfaces, IP addresses and routing tables

```bash

# To display the IP addresses of all interfaces
~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:d9:fa:93 brd ff:ff:ff:ff:ff:ff
    altname enp0s8
    inet 10.0.2.15/24 metric 100 brd 10.0.2.255 scope global dynamic eth0
       valid_lft 40899sec preferred_lft 40899sec
    inet6 fd17:625c:f037:2:a00:27ff:fed9:fa93/64 scope global dynamic mngtmpaddr noprefixroute 
       valid_lft 86264sec preferred_lft 14264sec
    inet6 fe80::a00:27ff:fed9:fa93/64 scope link 
       valid_lft forever preferred_lft forever

$ ip addr show lo
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever

# To display the route information
$ ip route show
default via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
10.0.2.0/24 dev eth0 proto kernel scope link src 10.0.2.15 metric 100 
10.0.2.2 dev eth0 proto dhcp scope link src 10.0.2.15 metric 100 
49.205.72.130 via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
102.192.249.101 via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 
183.82.243.66 via 10.0.2.2 dev eth0 proto dhcp src 10.0.2.15 metric 100 

# To display NW Interfaces states
$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 08:00:27:d9:fa:93 brd ff:ff:ff:ff:ff:ff
    altname enp0s8

# To display the Interface to MAC resolution
$ ip neigh
10.0.2.2 dev eth0 lladdr 52:55:0a:00:02:02 REACHABLE
fe80::2 dev eth0 lladdr 52:56:00:00:00:02 router STALE
fd17:625c:f037:2::2 dev eth0 lladdr 52:56:00:00:00:02 router STALE
fd17:625c:f037:2::3 dev eth0 lladdr 52:56:00:00:00:03 router STALE
```

### `ss` command (socket statistics)
> utility to display information about network sockets alternative to `netstat`

```bash
# show all listening ports
$ ss -lnt
State        Recv-Q       Send-Q             Local Address:Port              Peer Address:Port       Process       
LISTEN       0            128                      0.0.0.0:22                     0.0.0.0:*                        
LISTEN       0            4096               127.0.0.53%lo:53                     0.0.0.0:*                        
LISTEN       0            511                      0.0.0.0:80                     0.0.0.0:*                        
LISTEN       0            128                         [::]:22                        [::]:*                        
LISTEN       0            511                         [::]:80                        [::]:*       

# show all connections
$ ss -tulnp
Netid     State       Recv-Q      Send-Q            Local Address:Port           Peer Address:Port     Process     
udp       UNCONN      0           0                 127.0.0.53%lo:53                  0.0.0.0:*                    
udp       UNCONN      0           0                10.0.2.15%eth0:68                  0.0.0.0:*                    
tcp       LISTEN      0           128                     0.0.0.0:22                  0.0.0.0:*                    
tcp       LISTEN      0           4096              127.0.0.53%lo:53                  0.0.0.0:*                    
tcp       LISTEN      0           511                     0.0.0.0:80                  0.0.0.0:*                    
tcp       LISTEN      0           128                        [::]:22                     [::]:*                    
tcp       LISTEN      0           511                        [::]:80                     [::]:*  
```

### `netstat` command
> Used to monitor network connections, view routing tables, and display network interface statistics
> Same as `ss` command

```bash
$ netstat -tulnp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.0.2.15:68            0.0.0.0:*                           -         
```

### `traceroute` command
> a network diagnostic tool used to display the path that data packates take to a specific destination and measure transit delays at each hop (router) along the way

```bash
$ traceroute google.com
traceroute to google.com (142.250.66.14), 30 hops max, 60 byte packets
 1  _gateway (10.0.2.2)  0.130 ms  0.102 ms  0.129 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
 6  * * *
 7  *^C
```

### `dig` command
> `dig` Domain Information Grouper command is used for querying DNS servers to retrieve information about the hostname addresses, mail exchanges, name servers and other related data.

```bash
$ dig google.com

; <<>> DiG 9.18.39-0ubuntu0.22.04.2-Ubuntu <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 46792
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		37	IN	A	142.250.66.14

;; Query time: 4 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Sat Feb 28 05:34:55 UTC 2026
;; MSG SIZE  rcvd: 55

# Only retrive A record
$ dig google.com A

; <<>> DiG 9.18.39-0ubuntu0.22.04.2-Ubuntu <<>> google.com A
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8049
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;google.com.			IN	A

;; ANSWER SECTION:
google.com.		33	IN	A	142.250.66.14

;; Query time: 4 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Sat Feb 28 05:35:00 UTC 2026
;; MSG SIZE  rcvd: 55

# Retrieve name server information
$ dig google.com NS

; <<>> DiG 9.18.39-0ubuntu0.22.04.2-Ubuntu <<>> google.com NS
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29767
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;google.com.			IN	NS

;; ANSWER SECTION:
google.com.		600	IN	NS	ns2.google.com.
google.com.		600	IN	NS	ns1.google.com.
google.com.		600	IN	NS	ns3.google.com.
google.com.		600	IN	NS	ns4.google.com.

;; ADDITIONAL SECTION:
ns2.google.com.		600	IN	A	216.239.34.10
ns2.google.com.		600	IN	AAAA	2001:4860:4802:34::a
ns1.google.com.		600	IN	A	216.239.32.10
ns1.google.com.		600	IN	AAAA	2001:4860:4802:32::a
ns3.google.com.		600	IN	A	216.239.36.10
ns3.google.com.		600	IN	AAAA	2001:4860:4802:36::a
ns4.google.com.		600	IN	A	216.239.38.10
ns4.google.com.		600	IN	AAAA	2001:4860:4802:38::a

;; Query time: 8 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Sat Feb 28 05:35:03 UTC 2026
;; MSG SIZE  rcvd: 287
```

### `nslookup` command
> Used for querying the DNS to obtain the domain names or IP address mappings

```bash
$ nslookup google.com
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	google.com
Address: 142.250.66.14
Name:	google.com
Address: 2404:6800:4007:804::200e

$ nslookup localhost
Server:		127.0.0.53
Address:	127.0.0.53#53

Name:	localhost
Address: 127.0.0.1
Name:	localhost
Address: ::1
```

### `nmap` command
> Used for network exploration and security auditing

```bash
# scan open ports 
utdated hypervisor (qemu) binaries on this host.
$ nmap localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-28 05:43 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000042s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds

# scan specific ports
$ nmap -p 80 localhost
Starting Nmap 7.80 ( https://nmap.org ) at 2026-02-28 05:45 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00069s latency).

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.04 seconds
```

### `tcpdump` command
> Used to capturing and analyzing network packets in realtime

```bash
$ sudo tcpdump -i eth0
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
05:47:35.111870 IP ubuntulvmlab0101.ssh > _gateway.58687: Flags [P.], seq 47313006:47313098, ack 11907200, win 65535, length 92
05:47:35.111968 IP _gateway.58687 > ubuntulvmlab0101.ssh: Flags [.], ack 92, win 65535, length 0
05:47:35.111990 IP ubuntulvmlab0101.ssh > _gateway.58687: Flags [P.], seq 92:128, ack 1, win 65535, length 36
05:47:35.112015 IP _gateway.58687 > ubuntulvmlab0101.ssh: Flags [.], ack 128, win 65535, length 0
05:47:35.112049 IP ubuntulvmlab0101.ssh > _gateway.58687: Flags [P.], seq 128:172, ack 1, win 65535, length 44
05:47:35.112106 IP _gateway.58687 > ubuntulvmlab0101.ssh: Flags [.], ack 172, win 65535, length 0
05:47:35.112141 IP ubuntulvmlab0101.ssh > _gateway.58687: Flags [P.], seq 172:232, ack 1, win 65535, length 60
05:47:35.112166 IP _gateway.58687 > ubuntulvmlab0101.ssh: Flags [.], ack 232, win 65535, length 0
05:47:35.112195 IP ubuntulvmlab0101.ssh > _gateway.58687: Flags [P.], seq 232:292, ack 1, win 65535, length 60
05:47:35.112234 IP _gateway.58687 > ubuntulvmlab0101.ssh: Flags [.], ack 292, win 65535, length 0
05:47:35.112258 IP ubuntulvmlab0101.ssh > _gateway.58687: Flags [P.], seq 292:328, ack 1, win 65535, length 36
05:47:35.112285 IP _gateway.58687 > ubuntulvmlab0101.ssh: Flags [.], ack 328, win 65535, length 0
05:47:35.209137 IP6 ubuntulvmlab0101.56952 > fd17:625c:f037:2::3.domain: 38755+ [1au] PTR? 15.2.0.10.in-addr.arpa. (51)
```

### `host` command
> used for DNS lookup works simillar to nslookup

```bash
$ host google.com
google.com has address 142.250.66.14
google.com has IPv6 address 2404:6800:4007:804::200e
google.com mail is handled by 10 smtp.google.com.

$ host yahoo.com
yahoo.com has address 74.6.231.21
yahoo.com has address 98.137.11.163
yahoo.com has address 74.6.143.26
yahoo.com has address 74.6.143.25
yahoo.com has address 98.137.11.164
yahoo.com has address 74.6.231.20
yahoo.com has IPv6 address 2001:4998:44:3507::8000
yahoo.com has IPv6 address 2001:4998:24:120d::1:1
yahoo.com has IPv6 address 2001:4998:24:120d::1:0
yahoo.com has IPv6 address 2001:4998:124:1507::f001
yahoo.com has IPv6 address 2001:4998:124:1507::f000
yahoo.com has IPv6 address 2001:4998:44:3507::8001
yahoo.com mail is handled by 1 mta7.am0.yahoodns.net.
yahoo.com mail is handled by 1 mta6.am0.yahoodns.net.
yahoo.com mail is handled by 1 mta5.am0.yahoodns.net.

$ host localhost
localhost has address 127.0.0.1
localhost has IPv6 address ::1
```

### `hostname`
> used to display the hostname related information

```bash
# displaying the IP address
$ hostname -i
127.0.2.1

# Displaying the hostname
$ hostname
ubuntulvmlab0101
```

### `nc` command
> netcat command is used for readling from and writing data across network connections, using either the TCP or UDP protocols

```bash
$ nc -zv localhost 80
Connection to localhost (127.0.0.1) 80 port [tcp/http] succeeded!

$ nc -zv localhost 22
Connection to localhost (127.0.0.1) 22 port [tcp/ssh] succeeded!

$ nc -zv localhost 443
nc: connect to localhost (127.0.0.1) port 443 (tcp) failed: Connection refused

```

### `telnet` command
> Used to test network services and port connectivity

```bash
$ telnet localhost 80
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
^CConnection closed by foreign host.

$ telnet localhost 443
Trying 127.0.0.1...
telnet: Unable to connect to remote host: Connection refused

$ telnet localhost 22
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.13
^]
Invalid SSH identification string.
Connection closed by foreign host.
```
### `arp` command
> Used to display and modify the kernel's address resilution protocol cache

```bash
$ arp -a
_gateway (10.0.2.2) at 52:55:0a:00:02:02 [ether] on eth0
```

### `lsof` command
> It's a short form of list open files used to display information about files and the processes using them.

```bash
# Find the process using a specific port
$ sudo lsof -i :80
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   5134     root    6u  IPv4  83662      0t0  TCP *:http (LISTEN)
nginx   5134     root    7u  IPv6  83663      0t0  TCP *:http (LISTEN)
nginx   5141 www-data    6u  IPv4  83662      0t0  TCP *:http (LISTEN)
nginx   5141 www-data    7u  IPv6  83663      0t0  TCP *:http (LISTEN)

# find all the open ports
$ sudo lsof -i 
COMMAND    PID            USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
systemd-n  642 systemd-network   15u  IPv4 120353      0t0  UDP ubuntulvmlab0101:bootpc 
systemd-r  644 systemd-resolve   13u  IPv4  19951      0t0  UDP localhost:domain 
systemd-r  644 systemd-resolve   14u  IPv4  19952      0t0  TCP localhost:domain (LISTEN)
sshd      1055            root    3u  IPv4  21552      0t0  TCP *:ssh (LISTEN)
sshd      1055            root    4u  IPv6  21563      0t0  TCP *:ssh (LISTEN)
sshd      1505            root    4u  IPv4  22844      0t0  TCP ubuntulvmlab0101:ssh->_gateway:58687 (ESTABLISHED)
sshd      1545         vagrant    4u  IPv4  22844      0t0  TCP ubuntulvmlab0101:ssh->_gateway:58687 (ESTABLISHED)
nginx     5134            root    6u  IPv4  83662      0t0  TCP *:http (LISTEN)
nginx     5134            root    7u  IPv6  83663      0t0  TCP *:http (LISTEN)
nginx     5141        www-data    6u  IPv4  83662      0t0  TCP *:http (LISTEN)
nginx     5141        www-data    7u  IPv6  83663      0t0  TCP *:http (LISTEN)

# Find the process using a specific file
$ sudo lsof /var/log/nginx/access.log
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
nginx   5134     root    9w   REG  253,0       82 1574574 /var/log/nginx/access.log
nginx   5141 www-data    8w   REG  253,0       82 1574574 /var/log/nginx/access.log
```


## OS, CPU & Memory information commands

### `uname` command
> Utility to display fundamental system information, such as the kernel name, version, and hardware architecture

```bash
$ uname 
Linux

$ uname -a
Linux ubuntulvmlab0101 5.15.0-160-generic #170-Ubuntu SMP Wed Oct 1 10:12:04 UTC 2025 aarch64 aarch64 aarch64 GNU/Linux
```

### `/etc/os-release` 
> This fie contains operating system identification data

```bash
$ cat /etc/os-release 
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy
```

### `hostnamectl` command
> Can be used to display all current hostname information
```bash
$ hostnamectl status
 Static hostname: ubuntulvmlab0101
       Icon name: computer
      Machine ID: f1876e823e2f471e831669848e339d25
         Boot ID: 60d694db33de4936865a068d41ab3d62
Operating System: Ubuntu 22.04.5 LTS              
          Kernel: Linux 5.15.0-160-generic
    Architecture: arm64
```

### `lscpu` command
> displays details cpu information

```bash
$ lscpu
Architecture:                aarch64
  CPU op-mode(s):            64-bit
  Byte Order:                Little Endian
CPU(s):                      1
  On-line CPU(s) list:       0
Vendor ID:                   Apple
  Model:                     0
  Thread(s) per core:        1
  Core(s) per cluster:       1
  Socket(s):                 -
  Cluster(s):                1
  Stepping:                  0x0
  BogoMIPS:                  48.00
  Flags:                     fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt f
                             cma lrcpc dcpop sha3 asimddp sha512 asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg 
                             dcpodp flagm2 frint bf16
NUMA:                        
  NUMA node(s):              1
  NUMA node0 CPU(s):         0
Vulnerabilities:             
  Gather data sampling:      Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:                Mitigation; __user pointer sanitization
  Spectre v2:                Mitigation; CSV2, but not BHB
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
```

### `nproc` command
> Used to display the number of processors
```bash
$ nproc
1
```

### `/proc/cpuinfo` file
> contains raw cpu information
```bash
$ cat /proc/cpuinfo 
processor	: 0
BogoMIPS	: 48.00
Features	: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm jscvt fcma lrcpc dcpop sha3 asimddp sha512 asimdfhm dit uscat ilrcpc flagm ssbs sb paca pacg dcpodp flagm2 frint bf16
CPU implementer	: 0x61
CPU architecture: 8
CPU variant	: 0x0
CPU part	: 0x000
CPU revision	: 0
```

### `free` command
> Displays memory usage information

```bash
$ free -h
               total        used        free      shared  buff/cache   available
Mem:           834Mi       133Mi       205Mi       0.0Ki       495Mi       604Mi
Swap:          5.6Gi        15Mi       5.6Gi
```

### `vmstat` command
> Detailed CPU + Memory stats

```bash
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0  15440 210088  28332 478660    0    0    14    19   15   91  0  0 100  0  0
 ```

### `/proc/meminfo` file
> contains raw memory information details

```bash
$ cat /proc/meminfo 
MemTotal:         854160 kB
MemFree:          210088 kB
MemAvailable:     618724 kB
Buffers:           28340 kB
Cached:           413792 kB
SwapCached:         2688 kB
Active:           241876 kB
Inactive:         242384 kB
Active(anon):      10424 kB
Inactive(anon):    39984 kB
Active(file):     231452 kB
Inactive(file):   202400 kB
Unevictable:       26660 kB
Mlocked:           26660 kB
SwapTotal:       5859368 kB
SwapFree:        5843928 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:         67524 kB
Mapped:            60624 kB
Shmem:               852 kB
KReclaimable:      64896 kB
Slab:             105480 kB
SReclaimable:      64896 kB
SUnreclaim:        40584 kB
KernelStack:        1964 kB
PageTables:         2272 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:     6286448 kB
Committed_AS:     422776 kB
VmallocTotal:   133143592960 kB
VmallocUsed:       11572 kB
VmallocChunk:          0 kB
Percpu:              496 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
ShmemHugePages:        0 kB
ShmemPmdMapped:        0 kB
FileHugePages:         0 kB
FilePmdMapped:         0 kB
CmaTotal:          32768 kB
CmaFree:            2312 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
Hugetlb:               0 kB
```

### `lsblk` command
> displays information about disks, partitions and mount points

```bash
$ lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0                       7:0    0 33.7M  1 loop /snap/snapd/21761
loop2                       7:2    0 59.8M  1 loop /snap/core20/2321
loop3                       7:3    0 41.6M  1 loop /snap/snapd/25939
loop4                       7:4    0   81M  1 loop /snap/lxd/36930
loop5                       7:5    0 80.9M  1 loop /snap/lxd/37983
sda                         8:0    0   64G  0 disk 
├─sda1                      8:1    0    1G  0 part /boot/efi
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0 60.9G  0 part 
  └─ubuntu--vg-ubuntu--lv 253:0    0 30.5G  0 lvm  /
sdb                         8:16   0    5G  0 disk 
sdc                         8:32   0    5G  0 disk 
sdd                         8:48   0    5G  0 disk 
```

### `uptime` command
> displays the information about the system uptime and load average

```bash
$ uptime
 06:45:08 up 1 day,  2:20,  1 user,  load average: 0.03, 0.04, 0.01

$ uptime -s
2026-02-27 04:24:22
```

### `who` command
> Displays all the logged in user information

```bash
$ who
vagrant  pts/0        2026-02-24 06:56 (10.0.2.2)
vagrant  pts/1        2026-02-28 06:46 (10.0.2.2)
```

### `dmesg` command
> display or control the kernel ring buffer, which stores the messages produced during the boot process and at runtime

```
$ sudo dmesg
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x610f0000]
[    0.000000] Linux version 5.15.0-160-generic (buildd@bos03-arm64-058) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #170-Ubuntu SMP Wed Oct 1 10:12:04 UTC 2025 (Ubuntu 5.15.0-160.170-generic 5.15.189)
[    0.000000] efi: EFI v2.70 by EDK II
[    0.000000] efi: ACPI 2.0=0x46105018 MEMATTR=0x45edc298 MOKvar=0x47450000 MEMRESERVE=0x45ec9598 
[    0.000000] secureboot: Secure boot disabled
..
..
..
```