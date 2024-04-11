import os
import time
import socket
import platform
from functools import reduce

# task 1
# v1
file_size = os.path.getsize(__file__)
print("The size of abc.txt is:", file_size, "Bytes")
# v2
file_size = os.stat(__file__)
print("The size of abc.txt is:", file_size.st_size, "Bytes")
# v3
file = open(__file__)
file.seek(0, os.SEEK_END)  # move file cursor to the end of the file.
print("The size of main.py is:", file.tell(), "bytes")

# task 2
x = b"Abc"  # b - bytes object
print("\nConvert bytes of the said string to a list of integers:")
print(list(x))

# task 3
# v1
text = input("\nInput a word or numbers: ")

if text.isdigit():
    print("The input value is numbers.")
else:
    print("The input value is string.")

# v2
text = "a123"

try:
    i = float(text)
    print("The input value is numbers.\n")
except (ValueError, TypeError):
    print("Not numeric.\n")

# task 4
print(time.ctime(), "\n")

# task 5
# v1
host_name = socket.gethostname()
print("Host name:", host_name)
# v2
host_name = platform.uname()[1]
print("Host name:", host_name)
# v3
host_name = os.uname().nodename
print("Host name:", host_name, "\n")

# task 6
nums = [10, 20, 30]
nums_product = reduce((lambda a, b: a * b), nums)
print("\nProduct of the said numbers (without using a for loop):",
      nums_product)
