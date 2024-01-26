my_str1 = 'Python'
my_str2 = "Hi"
my_str3 = '''Hi
from 
next line'''
my_str4 = """Hi from 
next 
line"""

print(my_str1)
# print(my_str2)
# print(my_str3)
# print(my_str4)

# Конкатенація:
# print('Hello' 'world')
print('Hello ' 'world')
# print('Hello' + 'world')
# print('Hello' + ' world')

# Дублювання:
letter = 'a'
print(letter * 100)

# Довжина рядка:
print(len('Python'))
# print(len(letter))
# print(len(letter * 10))

# Для перетворення рядка у верхній/нижній регістр можна скористатися методом:
# upper/lower:
print(my_str1.upper())
print(my_str1.lower())

# Рядкові літерали можуть містити екранування:
# \t - вертикальна табуляція
# \n - перенесення рядка
my_str5 = "tab\t and new\n line"
print(my_str5)

# Сирі рядки:
print(r'\path\to_the\file')
# print('\path\to_the\next\file') # error

# Метод, який переводить в Unicode символи:
print(ord('N'))
# і навпаки:
print(chr(86))

# Інші методи:
'hello world'.capitalize()  # => Hello world
'some title'.title()  # => Some Title
'hello world'.count('l')  # => 3
'hello'.replace('e', 'l', 1)  # => "hlllo" замінює перший
# аргумент на другий n раз
'SoMe StR'.swapcase()  # => sOmE sTr

# Методи вирівнювання:
'hello'.ljust(10, '#')  # => hello#####
'hello'.rjust(10, '#')  # => #####hello
'hi'.center(10, '#')  # => ####hi####

# Методи видалення:
'####hi####'.lstrip('#')  # => hi####
'####hi####'.rstrip('#')  # => ####hi
'####hi####'.strip('#')  # => hi

# Методи розділення:
'###some string###'.split()  # => ['###some', 'string###']
'file.name.zip'.rsplit('.', 1)  # => ['file.name', 'zip']
'file.name.zip.bip'.partition('.')  # => ('file', '.', 'name.zip.bip')
'file.name.zip.bip'.rpartition('.')  # => ('file.name.zip', '.', 'bip')

# join() - з'єднує слова списку
"".join('Hi from list'.split())  # => Hifromlist
" ".join('Hi from list'.split())  # => Hi from list

# Оператор in
print('python' in "I'm python developer")  # => True

# Пошук підрядка:
print("I'm python developer".find('python'))  # => 4
print("I'm python developer".find('p', 5, 19))  # => 17

# Заміна підстроки:
print("I'm Python developer".replace('Python', 'Frontend'))
print("I'm Python developer. I love Python."
      .replace('Python', 'Frontend', 2))

# Форматування рядків:
# old:
# print('Hello dear %s %s. Your age is %d' % ('Mark', 'Dillan', 44))
name = 'Mark'
surname = 'Dillan'
age = 44
print('Hello dear %s %s. Your age is %d' % (
    name, surname, age))  # => Hello dear Mark Dillan. Your age is 44

# popular:
# print('Hello dear {0} {1}. Your age is {2}'.format('John', 'Stone', 38))
print('Hello dear {0} {1}. Your age is {2}'
      .format(name, surname, age))
# => Hello dear Mark Dillan. Your age is 44

# new:
print(f'Hello dear {name} {surname}. Your age is {age}')

# Об'єкт рядка не змінюваний: (адреса змінилася)
name = 'Nadia'
print(id(name))  # => 4370183008
name = 'Vadim'
print(id(name))  # => 4370183344
