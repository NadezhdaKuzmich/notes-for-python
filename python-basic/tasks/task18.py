import struct
# 'struct' module provides pack and unpack functions for working with
# variable-length binary data.
import platform
import os
import sys
import sysconfig
import site
import multiprocessing

# task 1
# v1
# struct- це модуль для пакування та розпакування даних у подання C і назад.
# Ця функція обчислює і повертає розмір рядкового представлення структури із
# заданим форматом. Розмір розраховується в байтах.
# P - представляє void * (загальний покажчик). У 32-бітних системах розмір
# покажчика становить 4 байти, а в 64-бітній системі для покажчика потрібно 8.
# struct.calcsize('P') обчислює кількість байтів, необхідну для зберігання
# одного покажчика, повертаючи 4 у 32-бітній системі та 8 у 64-бітній системі.
print(struct.calcsize("P") * 8)
# v2
architecture = platform.architecture()[0]
print(architecture)

# task 2
# v1
print("\nName of the operating system:   ", os.name)
# 'Darwin' (macOS)
print("Name of the OS system:          ", platform.system())
print("Version of the operating system:", platform.release())
# v2
print("\nos.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()[0]  ", platform.architecture()[0], '\n')

# task 3
# 'site.getsitepackages()' retrieves site packages' paths.
print(site.getsitepackages())

# task 4
# 'os.path.realpath(__file__)' gets the full path of the current Python script.
print("\nCurrent File Name: ", os.path.realpath(__file__), '\n')

# task 5
# 'multiprocessing.cpu_count()' determines the number of available CPU cores.
cpu_count = multiprocessing.cpu_count()
print(cpu_count, '\n')

# task 6
# The environ attribute of the os module is a dictionary-like object that
# represents the environment variables in the current process.
# The code that uses square brackets ([]) to access specific environment
# variables by their names:
# v1
print(os.environ, '\n')
print(os.environ['HOME'], '\n')
print(os.environ['PATH'], '\n')
# v2
for data in os.environ:
    print(data)
    print('-' * 30)
    print(os.environ[data])
    print('=' * 30)