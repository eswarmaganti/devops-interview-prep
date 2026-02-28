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
