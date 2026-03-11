'''
Write a python script that runs the command "dh -h"
Parse the output, identify the filesystems which usage is > 80%

Log format:
Filesystem                        Type    Size  Used Avail Use% Mounted on
tmpfs                             tmpfs    84M  944K   83M   2% /run
/dev/mapper/ubuntu--vg-ubuntu--lv ext4     30G  7.8G   21G  28% /
tmpfs                             tmpfs   418M     0  418M   0% /dev/shm
tmpfs                             tmpfs   5.0M     0  5.0M   0% /run/lock
/dev/sda2                         ext4    2.0G  125M  1.7G   7% /boot
/dev/sda1                         vfat    1.1G  6.4M  1.1G   1% /boot/efi
vagrant                           vboxsf  461G  282G  180G  62% /vagrant
tmpfs                             tmpfs    84M  8.0K   84M   1% /run/user/1000
'''

import shlex
import subprocess
import traceback
from pathlib import Path

# filesytem_log = subprocess.run(shlex.split('df -h'))

logfile = Path.cwd() / "filesystem.log"

try:
  with open(logfile) as f:
    data = f.readlines()

except FileNotFoundError as f:
  traceback.print_exc()

data = [item.split() for item in data[1:]]
filtered = sorted(data, key= lambda item: int(item[-2][0:-1]), reverse=True)

for i in range(0,4):
  print(f"File System - {filtered[i][0]} is {filtered[i][-2]}")