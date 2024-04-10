import getpass
import multiprocessing
import os
import os.path
import platform
import pwd
import site
import socket
import struct
import sys
import sysconfig
import time
from pathlib import Path
import glob

# task 1
# v1
# struct- це модуль для пакування та розпакування даних у подання C і назад.
# Ця функція обчислює і повертає розмір рядкового представлення структури із
# заданим форматом. Розмір розраховується в байтах.
# P - представляє void * (загальний покажчик). У 32-бітних системах розмір
# покажчика становить 4 байти, а в 64-бітній системі для покажчика потрібно 8.
# struct.calcsize("P") обчислює кількість байтів, необхідну для зберігання
# одного покажчика, повертаючи 4 у 32-бітній системі та 8 у 64-бітній системі.
print(struct.calcsize("P") * 8)
# v2
architecture = platform.architecture()[0]
print(architecture)

# task 2
# v1
print("\nName of the operating system:   ", os.name)
# "Darwin" (macOS)
print("Name of the OS system:          ", platform.system())
print("Version of the operating system:", platform.release())
# v2
print("\nos.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()[0]  ", platform.architecture()[0], "\n")

# task 3
# "site.getsitepackages()" retrieves site packages" paths.
print(site.getsitepackages())

# task 4
# "os.path.realpath(__file__)" gets the full path of the current Python script.
print("\nCurrent File Name: ", os.path.realpath(__file__), "\n")

# task 5
# "multiprocessing.cpu_count()" determines the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()
print(cpu_count, "\n")

# task 6
# The environ attribute of the os module is a dictionary-like object that
# represents the environment variables in the current process.
# The code that uses square brackets ([]) to access specific environment
# variables by their names:
# v1
print(os.environ, "\n")
print(os.environ["HOME"], "\n")
print(os.environ["PATH"], "\n")
# v2
for data in os.environ:
    print(data)
    print("-" * 30)
    print(os.environ[data])
    print("=" * 30)

print('\n')
# v3
for item, value in os.environ.items():
    print(f"{item}: {value}")

print('\n')

# task 7
# v1
print(getpass.getuser())


# v2
def get_username():
    return pwd.getpwuid(os.getuid())[0]


print(get_username(), '\n')

# task 8
# Step 1: Get the local hostname.
local_hostname = socket.gethostname()

# Step 2: Get a list of IP addresses associated with the hostname.
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

# Step 3: Filter out loopback addresses (IPs starting with "127.").
filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

# Step 4: Extract the first IP address (if available) from the filtered list.
first_ip = filtered_ips[:1]

# Step 5: Print the obtained IP address to the console.
print(first_ip[0])

# task 9
# v1
print("\nAbsolute file path: ", os.path.abspath(__file__), "\n")
# v2
p = Path(__file__).resolve()
print(p)

# task 10
print("\nLast modified: %s" % time.ctime(os.path.getmtime(__file__)))
print("Created: %s" % time.ctime(os.path.getctime(__file__)), "\n")

# task 11
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))

# task 12
path = "task18.py"
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a normal file")
else:
    print("It is a special file (socket, FIFO, device file)")
