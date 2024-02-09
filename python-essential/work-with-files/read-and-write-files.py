import random

# READ:
# v1
filename = 'my-files/my_text'

text_file = open(filename, 'r')
txt = text_file.read()
text_file.close()  # !!!
print(txt)

# v2
filename_uk = 'my-files/my_text_2'
# without .close()
with open(filename_uk, 'r', encoding='utf-8') as text_file:
    text1 = text_file.read(6)
    text2 = text_file.read(6)
    text_file.seek(13)
    text3 = text_file.read()
print(f'{text1=} {text2=}')
print(f'{text3=}')

filename_lines = 'my-files/my_text_lines'

with open(filename_lines, 'r') as text_file:
    text = text_file.readlines()
    print(text)
    # text1 = text_file.readline()
    # print(text1)
    # text2 = text_file.readline()
    # print(text2)
    # for row in text:
    #     print(row)
    #     for letter in row:
    #         print(letter)

# WRITE:
filename2 = 'my-files/my_text_3'

# v1
text_file = open(filename2, 'w')
txt2 = 'Hello world ! 12345'
text_file.write(txt2)
# text_file.write([1, 2, 3]) => ERROR - можна передавати тільки рядок символів
text_file.close()

# v2
with open(filename2, 'a') as text_file:
    text = '\nHello world ! 54321'
    text_file.write(text)

# Task
letters = "abcdefghijklmnopqrstuvwxyz"

random_letters = ""
random_count = 25

while len(random_letters) < random_count:
    random_letter = letters[random.randint(0, len(letters) - 1)]
    random_letters += random_letter

print(random_letters)

with open('my-files/random_string', 'w') as text_file:
    text_file.write(random_letters)
