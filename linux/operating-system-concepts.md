# Operating System Concepts

## Filesystem Hierarchy Standard
The linux file system hierarchy is a standard, tree-like structure starting from a **single root directory (/)**, defined bu the Filesystem Hierarchy Standard (FHS). This united structure ensures consistency across different linux distributions

Key directories and their purposes include
- `/ (root)`: The base of the entire filesystem, containing all other files and directories
- `/bin`: Essential command binaries required for basic system operation and maintenance in single-user mode, available for all users.
- `/sbin`: Essential System binaries for system administration tasks, typically requiring root privileges
- `/dev`: Contains special files that represents hardware devices (e.g., `/dev/sda1` for hard disk partition, `/dev/null` for a null device)
- `/etc`: Host-specific system-wide configuration files for applications, services and system settings (e.g., `/etc/passwd`, `/etc/fstab`)
- `/proc`: A virtual file system exposing kernel and device information, allowing interaction with hardware and kernel features
- `/sys`: Another virtual file system exposing kernel and device information, allowing interaction with hardware and kernel features.
- `/home`: Contains the personal home directories for regular users, where they store their files, documents and user-specific configurations.
- `/root`: The home directory of the superuser
- `/usr`: A secondary hierarchy for read-only user data, containing most user utilities and applications, including subdirectories like `/usr/bin`, `/usr/lib` and `/usr/share` for documentation and shared data
- `/var`: Stores variable data files whose content is expected to change frequently during normal system operation, such as log files (`/var/log`), mail data, and caches
- `/tmp`: A location for temporary files created by users and applications. Contents are typically not preserved across system reboots
- `/boot`: Contains the files required to start the system, including the Linux Kernel image and boot loader (GRUB) configuration files.
- `/lib` and `/lib64`: House essential shared libraries required by the binaries in `/bin` and `/sbin`
- `/mnt` and `/media`: Used as temporary mount points for manual or automatically mounting external storage devices like USB devices, CDs or network shares
- `/opt`: Reserved for optional or third-party software packages not part of the core distribution such as proprietary applications.
- `/run`: Stores run-time variable data that is cleared at the beginning of the boot process (e.g., process IDs, logged-in users info)

```bash
$ tree / -L 1
/
├── bin -> usr/bin
├── boot
├── cdrom
├── dev
├── etc
├── home
├── lib -> usr/lib
├── lost+found
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin -> usr/sbin
├── snap
├── srv
├── swap.img
├── sys
├── tmp
├── usr
├── vagrant
└── var

```

---

## `/proc` FileSystem
The `/proc` filesystem is a virtual, RAM based filesystem in Linux/unix operating systems that provide a realtime hierarchical interface to kernel data structures, system information and running processes.
It acts as a control and information center, with directories for each PID and system file like `cpuinfo`

### Key Aspects of the Proc FileSystem
- **Virtual Nature**: `/proc` files so not exist on the disk; they are generated on-the-fly by the kernel in memory
- **Process Information**: Each running process has a directory named ny its process ID (e.g., `/proc/1234/`), containing details like command line arguments, memory usage, and file descriptors.
- **System Metrics**: `/proc` provides system-wide information, including:
  - `/proc/cpuinfo`: CPU details
  - `/proc/meminfo`: memory usage statistics
  - `/proc/loadavg`: System load average
  - `/proc/uptime`: System uptime
- **Kernel Tuning**: The `/proc/sys` directory allows viewing and modifying kernel parameters at runtime 
- **Permissions**: Most files are read-only, but `/proc/sys` is writable for configuration
- **Kernel Interface**: It acts as a bridge between *user space* and *kernel space*, allowing users and tools (`ps`, `top` or `free`) to query system information without special system calls

---

## Kernel vs Shell Interaction

### Kernel
The linux kernel is the core component of an operating system. It's the part of system that interacts directly with the computer's hardware such as the CPU, memory, and input/output devices.
The kernel manages system resources, controls the execution processes, and provides a layer of security between different programs

### Shell
A shell is a user interface that allows you to interact with your computer's operating system. It's a program that takes commands from the user and executes them on the operating system.
The shell provides a way for users to issue commands to the operating system, like creating a new file, deleting a directory, or running a program.

### Key differences and Interaction
- **Role**: The kernel directly controls hardware, whereas the shell acts as an intermediary for user-to-kernel communication.
- **Operation**: The shell operates at a high level, translating commands like `ls` or `cd` into actions, while the kernel works at low level.
- **Communication**: The shell uses system calls to request services from the kernel, such as file access or process management
- **Process**: When a user enters a command, the shell interprets it, send it to the kernel, the kernel executes it, and the output is returned to the shell.

---

## Kernel Space and User Space
In Linux, kernel space and user space are two separate and protected areas of virtual memory that enforce security and stability by dividing the system operations based on privilege levels.
The core operating system runs in the kernel space with full privileges, while applications runs in the restricted user space.

### Kernel Space
Kernel space is privileged memory area where the core of the operating system resides and executes in kernel mode
- **Access Level**: Has unrestricted, direct access to all hardware resources, including the CPU, memory, and I/O devices.
- **Key Functions**: Manages crucial system tasks such as: 
  - Process management and scheduling
  - Memory allocation and management
  - Device drivers and hardware communication
  - Security enforcement and access control
- **Stability**: A Crash in kernel space is severe and can bring down the entire operating system.

### User Space
User Space is the unprivileged memory area where all user applications, libraries, and daemons run. Each process typically has its own isolated virtual address space.
- **Access Level**: Has limited access to system resources and cannot interact with hardware directly
- **Key Functions**: Operations performed here include:
  - Running application software
  - Utilizing standard libraries
  - Data processing and user interface management
- **Stability**: A crash in a user-space application does not effect the kernel or other user programs, enhancing system stability.

---
## How Linux handles Interrupts

An interrupt is a signal from hardware or software that temporarily stops the CPU's current task and forces the kernel to execute a specific handler to respond to an event. Without interrupts, CPU would need to constantly poll devices.

Examples:
- Keyboard press
- Network packet arrival
- Disk I/O completion

### Types
#### Hardware Interrupt (IRQ)
Triggered by hardware devices

Example:
- Keyboard
- Disk
- Network Card

#### Software Interrupt (SoftIRQ)
Used by kernel to defer work that doesn't need immediate handling.

Example:
- Network packet processing split into:
  - Hardware IRQ -> minimal work
  - SoftIRQ -> full processing

#### System Call Interrupt (User -> Kernel)
User processes interrupts kernel to request service

Example:
- read()
- write()
- open()

#### Non-Maskable Interrupt (NMI)
Critical Interrupts that cannot be ignored. These are highest priority interrupts

Examples:
- Hardware failures
- CPU errors

### Where to see interrupts
we can get the detailed information about interrupts from  the file `/proc/interrupts`

```bash
$ cat /proc/interrupts 
           CPU0       
 10:    1454276     GICv3  27 Level     arch_timer
 13:      60496     GICv3  37 Level     virtio0
 14:         46     GICv3  36 Level     xhci-hcd:usb1
 15:     240805     GICv3  34 Level     eth0
 16:          0  ARMH0061:00   3 Edge      power
 17:          0  ARMH0061:00   4 Edge      unknown
 18:      50409     GICv3  35 Level     vboxguest
IPI0:         0       Rescheduling interrupts
IPI1:         0       Function call interrupts
IPI2:         0       CPU stop interrupts
IPI3:         0       CPU stop (for crash dump) interrupts
IPI4:         0       Timer broadcast interrupts
IPI5:         0       IRQ work interrupts
IPI6:         0       CPU wake-up interrupts
Err:          0
```

---

## I/O redirection & Piping
Linux I/O redirection and piping allow users to control input/output sources and connect commands, moving away from default keyboard/screen usage.
Use `>`, `>>`, `<` to redirect output/input to/from files, and pipes `|` to chain command outputs as inputs for others.

Key tools include `2>` for error redirection and `2>&1` to merge output streams

### I/O redirection operators
Redirection allows changing the source (input) or destination (output) of a command's data stream.
- `>` **(stdout Redirection)**: Redirects standard output to a file, overwriting the file content
  - Ex: `ls -l > files.txt`
- `>>` **(stdout append)**: Redirects standard output to a file, appending to existing content.
  - Ex: `echo "New Line" > log.txt`
- `<` **(stdin Redirection)**: Takes input from a file instead of the keyboard.
  - Ex: `wc -l < input.txt`
- `2>` **(stderr Redirection)**: Redirects error messages to a file, keeping standard output on the screen.
  - Ex: `find / -type f 2> error.log `
- `2>&1` **(Merge Streams)**: Redirects standard error (2) to the same location as standard output (1)
  - Ex: `command > output.txt 2>&1`
- `/dev/null`: Discards standard output by sending it to a null device: "black hole".

### Linux Piping (|):
Piping uses the vertical bar `|` to take the standard output of the command on the left and connect it directly as the standard input for the command on the right. This allows for complex data processing chains.
> Syntax: `command1 | command2`

Examples
```bash
$ df -Th | grep ext4
/dev/mapper/ubuntu--vg-ubuntu--lv ext4     30G  7.8G   21G  28% /
/dev/sda2                         ext4    2.0G  125M  1.7G   7% /boot

$ ps aux | grep [n]ginx
root        5134  0.0  0.6  55204  5520 ?        Ss   Feb27   0:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    5141  0.0  0.7  55892  6216 ?        S    Feb27   0:00 nginx: worker process
```

---

## Environment Variables in Linux
Environment variables in Linux are dynamic key-value pairs used to store configuration data that controls how the shell and applications behave.
They provide information to processes, such as the search path for executables, user details, and system settings

### Common environment variables
- `PATH`: A colon-separated list of directories where the shell looks for executable commands
- `HOME`: The path to the current user's home directory
- `USER`: The username of the currently logged-in user.
- `SHELL`: The path to the current user's default shell interpreter (e.g., `/bib/bash`)
- `PWD`: The present working directory
- `EDITOR`: The system's default text editor
- `LANG`: The current language and locale settings

### Managing Environment Variables
You can view, set, and unset environment variables using specific commands in the terminal

You can use `printenv` or `env` commands to view all environment variables

```bash
# To view all environment variables
$ printenv
SHELL=/bin/bash
PWD=/home/vagrant
LOGNAME=vagrant
XDG_SESSION_TYPE=tty
MOTD_SHOWN=pam
HOME=/home/vagrant
LANG=en_US.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SSH_CONNECTION=10.0.2.2 56582 10.0.2.15 22
LESSCLOSE=/usr/bin/lesspipe %s %s
XDG_SESSION_CLASS=user
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=vagrant
SHLVL=1
XDG_SESSION_ID=40
XDG_RUNTIME_DIR=/run/user/1000
SSH_CLIENT=10.0.2.2 56582 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
SSH_TTY=/dev/pts/1
_=/usr/bin/printenv

$ env
SHELL=/bin/bash
PWD=/home/vagrant
LOGNAME=vagrant
XDG_SESSION_TYPE=tty
MOTD_SHOWN=pam
HOME=/home/vagrant
LANG=en_US.UTF-8
LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
SSH_CONNECTION=10.0.2.2 56582 10.0.2.15 22
LESSCLOSE=/usr/bin/lesspipe %s %s
XDG_SESSION_CLASS=user
TERM=xterm-256color
LESSOPEN=| /usr/bin/lesspipe %s
USER=vagrant
SHLVL=1
XDG_SESSION_ID=40
XDG_RUNTIME_DIR=/run/user/1000
SSH_CLIENT=10.0.2.2 56582 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
SSH_TTY=/dev/pts/1
_=/usr/bin/env

```
To view a specific environment variable, we can use `echo` command with a `$` prefix
```bash
$ echo $SHELL
/bin/bash
```

To set a temporary environment variable: use the `export` command.
```bash
$ export image=myapp:12

$ echo $image
myapp:12
```

To unset a variable: use the `unset` command
```bash
$ unset image
$ echo $image

```

### The `export` command
The `export` command marks a shell variable to be an environment variable, making it available to any new *child* processes or sub shells created from the current shell
> Syntax: `export VAR_NAME=value`

Variables set directly in the terminal with `export` are only temporary and last for the duration of that specific terminal session. They will be lost when the terminal is closed

You can view all exported environment variables using `env` or `export -p` commands

### The `~/.bashrc` and `~/.zshrc` files
These are user specific configuration files that run every time a new interactive non-login shell is started.

- **Purpose**: They are used to set up a personalized environment, including defining aliases, functions, and permanent environment variables for the specific shell
- **Usage**: To make an environment variable permanent for all future sessions of your chosen shell, ass the export command line to the appropriate file
  - For bash users `~/.bashrc`
  - For Zsh users `~/.zshrc`

---

## Process vs Threads in Linux

### Process
A process is a computer program under execution. Linux is running many processes at any given time. We can monitor them on the terminal using the `ps` command
As we run commands/applications or the old commands complete, we can see the number of processes grow and shrink dynamically. Linux processes are isolated and do not interrupt each other's execution.
With a **PID**, we can identify any process in Linux. Internally, the kernel uniquely allocates this number and releases it for reuse after the process exists.

Since many processes are running at any given time in Linux, they have to share the CPU. The process of switching between two executing processes on the CPU is called process context switching. **Process context switching is expensive because the kernel has to save old registers and load current registers, memory maps, an other resources**

### Thread
**A thread is a lightweight process**. A process can do more than one unit of work concurrently by creating one or more threads. These threads, being lightweight, can be spawned quickly.

Lets see an example and identify the process and its thread in Linux using `ps -efL` command.
- `PID`: unique process identifier
- `LWP`: unique thread identifier
- `NLWP`: Number of threads for a given process

```bash
$ ps -efL
UID          PID    PPID     LWP  C NLWP STIME TTY          TIME CMD
root           1       0       1  0    1 Feb27 ?        00:00:16 /sbin/init autoinstall
root         446       1     446  0    7 Feb27 ?        00:00:03 /sbin/multipathd -d -s
root         446       1     449  0    7 Feb27 ?        00:00:00 /sbin/multipathd -d -s
root         446       1     451  0    7 Feb27 ?        00:00:00 /sbin/multipathd -d -s
root         446       1     452  0    7 Feb27 ?        00:00:00 /sbin/multipathd -d -s
root         446       1     453  0    7 Feb27 ?        00:00:00 /sbin/multipathd -d -s
root         446       1     454  0    7 Feb27 ?        00:00:25 /sbin/multipathd -d -s
root         446       1     455  0    7 Feb27 ?        00:00:00 /sbin/multipathd -d -s
```

## Virtual Memory concept in Linux
Virtual memory in Linux is a memory management technique that abstracts physical RAM into a large, continuous address. space for each process. This allows applications to operate as if they have access to more memory than is physically installed on the system by using disk space as a supplement.

### Core Mechanisms
- **Paging**: Linux divides memory into fixed-size blocks called **Pages** (typically 4KB). These map to **page frames** in physical RAM via hierarchical **Page Tables** managed by the kernel and CPUs Memory Management Unit (MMU)
- **Demand Paging**: The kernel only loads pages into RAM when a process actually attempts to access them. If the page is not in RAM, a **page fault** occurs, and the kernel fetches it from disk
- **Swapping**: When physical RAM is full, the kernel moves inactive memory pages to a designated **swap space** (a partition or file) on the disk to free up RAM for active tasks.
- **Copy-on-Write (COW)**: An optimization where child process share the same physical memory pages as their parent until once process modifies a page, at which point a private copy is created.

### Key Benefits
- **Isolation & Security**: Each process has its own private address space, preventing it from accessing or corrupting the memory of other processes or the kernel.
- **Overcommitment**: Linux can allocate more virtual memory to processes than the total physical RAM + swap available, based on the assumption that most processes don't use all their memory simultaneously.
- **Efficient Sharing**: Multiple processes can share a single copy of common data (like shared libraries) in physical memory by mapping it into their respective virtual address spaces.

---

## Inode and File Descriptors
In Linux, an inode is a filesystem data structure that stores file metadata and data block locations on disk, while a file descriptor (FD) is a per-process integer handle used to access an open file or I/O resource in memory.
The file descriptor acts as an index into a process's open file table, which in turn points to the file's inode.

### Inode
An inode (index node) is a fundamental data structure for Unix-style filesystem that describes a filesystem object, such as a file, directory, or device.
- **Persistence**: Inodes are stored on disk and persists across system reboots
- **Metadata**: An inode stores all file attributes except its name and actual data. This includes:
  - File Type
  - Permissions
  - Ownership
  - File Size
  - Timestamps
  - A link count
  - Pointers to actual data blocks on the disk
- **Identification**: Each file on a given filesystem has a unique inode number. The filename itself is stored in a directory entry, which maps the name to the inode number
- **Usage**: You can check a file's inode number using the `ls -l` command

```bash
$ ls -il
total 56
786830 -rw-rw-r-- 1 vagrant vagrant   258 Feb 24 14:39 data.txt
786829 -rw-rw-r-- 1 vagrant vagrant 40076 Feb 28 16:36 error.log
786444 -rwsr-xr-x 1 vagrant vagrant    72 Feb 25 12:34 greet.py
917506 drwxr-sr-x 2 vagrant nginx    4096 Feb 25 03:27 mydir
786826 -rw------- 1 vagrant vagrant     0 Feb 25 12:34 nohup.out
786828 -rw-rw-r-- 1 vagrant vagrant     0 Feb 24 12:04 temp.log
786832 -rw-rw-r-- 1 vagrant vagrant   448 Feb 26 09:26 wget-response
```

### File Descriptor (FD)
A file descriptor is a small, non-negative integer that the kernel assigns to a process when a file or other I/O resource is opened.
- **Scope**: File descriptors are specific to each process and exist only in memory while the file is open.
- **Handle**: Processes use the FD as a handle to perform I/O operations (e.g., `read()`, `write()`, `close()`) on the open file, without needing to know the underlying implementation details.
- **Standard FDs**: By default, every process starts with three standard file descriptors automatically opened by shell:
- `0`: Standard Input (stdin), typically the keyboard
- `1`: Standard Output (stdout), typically the terminal screen
- `2`: Standard Error (stderr), also typically the terminal screen.
- **Usage**: You can view the open file descriptors for a running process using the `lsof` command or by inspecting the `/proc/<PID>/fd` directory

```bash
# inspecting the fds the nginx process is using
$ ps -ef | grep [n]ginx
root        5134       1  0 Feb28 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data    5141    5134  0 Feb28 ?        00:00:00 nginx: worker process

$ sudo ls -l /proc/5134/fd
total 0
lrwx------ 1 root root 64 Feb 28 06:10 0 -> /dev/null
lrwx------ 1 root root 64 Feb 28 06:10 1 -> /dev/null
l-wx------ 1 root root 64 Feb 28 06:10 2 -> /var/log/nginx/error.log
lrwx------ 1 root root 64 Feb 28 06:10 4 -> 'socket:[83730]'
lrwx------ 1 root root 64 Feb 28 06:10 5 -> 'socket:[83731]'
lrwx------ 1 root root 64 Feb 28 06:10 6 -> 'socket:[83662]'
lrwx------ 1 root root 64 Feb 28 06:10 7 -> 'socket:[83663]'
l-wx------ 1 root root 64 Mar  1 11:38 8 -> /var/log/nginx/access.log
l-wx------ 1 root root 64 Feb 28 06:10 9 -> /var/log/nginx/error.log

```

---


## Linux Boot Process
The Linux boot process involves six key stages: BIOS/UEFI initializes hardware (POST), MBR or EFI locates the GRUB bootloader, GRUB loads the kernel and initramfs into memory, the kernel initializes hardware and mounts the root file system, and finally, systemd (PID 1) starts system services and user space.

```mermaid
flowchart LR
  A[BIOS/UEFI] --> B[MBR] --> C[GRUB] --> D[Kernel] --> E[Init] --> F[Runlevels]
  
```
### BIOS
BIOS stands for Basic Input/Output System. In simple terms the BIOS loads and executes the Master Bootloader Record (MBR)

The BIOS search for, loads and executes the boot loader program, which can be found in the MBR. The MBR sometimes on a USB stick or CD-ROM such as with live installation of Linux

Once the boot loader program is detected, it's then loaded into memory and the BIOS gives control of the system to it.

### MBR
MBR stands for Master Boot Record, and is responsible for loading and executing the GRB boot loader.
The MBR is located in the 1st selector of the bootable disk, which is typically `/dev/hda` or `/dev/sda` depending on your hardware.

### GRUB
Sometimes called GNU GRUB, which is short for GNU GR and Unified Bootloader, is the typical boot loader for most modern Linux systems

In many systems you can find the GRUB configuration file at `/boot/grub/grub.conf` or `/etc/grub.conf`

```bash
$ sudo cat /etc/default/grub
# If you change this file, run 'update-grub' afterwards to update
# /boot/grub/grub.cfg.
# For full documentation of the options in this file, see:
#   info -f grub -n 'Simple configuration'

GRUB_DEFAULT=0
GRUB_TIMEOUT_STYLE=hidden
GRUB_TIMEOUT=0
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="autoinstall ds=nocloud-net;s=http://10.0.2.2:8340/ubuntu/"
GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0 "

# Uncomment to enable BadRAM filtering, modify to suit your needs
# This works with Linux (no patch required) and with any kernel that obtains
# the memory map information from GRUB (GNU Mach, kernel of FreeBSD ...)
#GRUB_BADRAM="0x01234567,0xfefefefe,0x89abcdef,0xefefefef"

# Uncomment to disable graphical terminal (grub-pc only)
#GRUB_TERMINAL=console

# The resolution used on graphical terminal
# note that you can use only modes which your graphic card supports via VBE
# you can see them in real GRUB with the command `vbeinfo'
#GRUB_GFXMODE=640x480

# Uncomment if you don't want GRUB to pass "root=UUID=xxx" parameter to Linux
#GRUB_DISABLE_LINUX_UUID=true

# Uncomment to disable generation of recovery mode menu entries
#GRUB_DISABLE_RECOVERY="true"

# Uncomment to get a beep at grub start
#GRUB_INIT_TUNE="480 440 1"
```

### Kernel
In this stage of the boot process, the kernel that was selected by GRUB first mounts the root file system that's specified in the `grub.conf` file.
Then it executes the `sbin/init` program, which is always the first program to be executed.

The kernel then establish a temporary root file system using initial RAM disk (initrd) until the real file system is mounted.

### Init
At this point, your system executed run level programs. At one point it would look for an init file, usually found at `/etc/inittab` to decide the Linux run level.

Modern linux systems use systemd to choose a run level

### Runlevel
Systemd mounts all filesystems, starts services (networking,GUI) and brings the system to a specific target (runlevel), resulting in the login prompt.

---

## Init Systems (systemd vs SysVinit)
The `init` system in Linux (short for initialization) is the **first user-space process started by the kernel**, always assigned a process ID of 1.
Its primary role is to setup the rest of the operating system by running startup scripts, mounting filesystems, and launching system services and daemons.

### Key responsibilities
- **Process Management**: It is the direct or indirect ancestor of all other processes and automatically "adopts" any orphaned processes
- **Service Orchestration**: It starts, stops, and manages system services (like networking, logging, and GUI) during boot-up and shutdown
- **System State Management**: It manages different operational states, historically knows as "runlevels" or in modern systems, "targets"
- **System Integrity**: If the kernel is unstable to start the `init` process, a kernel panic will occur, demonstrating its critical role in system functionality.

### Evolution of Init Systems
Over time, several `init` systems have been developed to address the limitations of their predecessors, primarily to improve boot speed, dependency management, and overall system control.

#### SysVinit
- The traditional, widely used `init` system for many years
- Relies on sequential shell scripts located in directories like `/etc/init.d`
- Uses runlevels (e.g., runlevel 3 for multi-user mode with networking, runlevel 5 for graphical interface) to define system states.
- Booting is slower due to its strictly sequential nature.
  
#### systemd
- The dominant and default `init` system in most modern Linux distributions (e.g., Ubuntu, Fedora, Debian, Arch Linux)
- Uses a unit-based approach and declarative configuration files instead of shell scripts
- Features parallel service startup and sophisticated dependency management, resulting in significantly faster boot times.
- More than just an `init` system, it is a comprehensive suite of management tools (including integrated logging with `journalctl` and network configuration)

To view the `init` system, we can inspect the process with PID `1`
```bash
$ ps -p 1
    PID TTY          TIME CMD
      1 ?        00:00:16 systemd
```
---

## Load Average
In Linux, load average is a metric that represents the average number of processes that are in a **runnable state** (either using CPU or waiting to use the CPU) or in an **uninterruptible sleep state** (mostly waiting for I/O operations like disk or network) over a period of time.
It helps system administrators assess the overall system performance and demand for resources.

### Interpreting the values
The load average is displayed as three numbers, which represent the moving average over the last one, five and fifteen minutes, respectively:
- **First number**: 1-minute load average (indicates recent system load)
- **Second number**: 5-minute load average (indicates short-term trend)
- **Third number**: 15-minute load average (indicates long-term trend)

By comparing these three numbers, you can determine if the system load is increasing, stable or decreasing:
- If the 1-minute average is higher than the 15-minute average, the load is increasing
- If 1-minute is lower than the 15-minute average, the load is decreasing

### The Role of CPU Cores
To properly interpret the load average, you must compare the values to the number of CPU cores (logical processors) your system has.
- **Load Average < Number of Cores**: The system has sufficient capacity, and processes are generally not waiting for CPU time.
- ** Load Average = Number of Cores**: The system is running at full capacity, with all CPU cores fully utilized. This is considered optimal utilization in some scenarios
- **Load Average > Number of Cores**: The system is overloaded, and processes are waiting in a queue for resources (CPU or I/O).

### How to check load average
We can use the commands like `uptime`, `top`, `htop` and `/proc/loadavg` to find the load average of the system

```bash
$ uptime
 12:42:48 up 1 day, 15:38,  2 users,  load average: 0.00, 0.00, 0.00

$top | grep load
top - 12:43:05 up 1 day, 15:38,  2 users,  load average: 0.00, 0.00, 0.00

$cat /proc/loadavg 
0.00 0.00 0.00 1/126 6842
```