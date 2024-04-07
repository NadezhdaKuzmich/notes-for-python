import struct
# 'struct' module provides pack and unpack functions for working with
# variable-length binary data.
import platform

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
print(struct.calcsize("P") * 8)
