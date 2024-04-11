import os

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
x = b'Abc'  # b - bytes object
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
    print("The input value is numbers.")
except (ValueError, TypeError):
    print("Not numeric.")
