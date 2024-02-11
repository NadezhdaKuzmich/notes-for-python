# Моя маленька шпаргалка по Python:
name = 'Vadim'
print('Hello', name)

# Зміна значення змінної:
name = 'Nadiia'
print('Hello', name)
# id() - метод для того, щоб подивитись адресу в змінній
print(id(name))
# help(...) - позволяє подивитись що робить той чи інший метод
# help(id)

# Не можна іменувати змінні таким чином:
# 2name = 'Error 1'
# ?name = 'Error 2'
# new name = 'Error 3'
# and = 'and' (ключові слова)

# Код для того, щоб подивитись ключові слова
# from keyword import kwlist
# print(kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
#  'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
#  'else', 'except', 'finally', 'for', 'from', 'global', 'if',
#  'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass',
#  'raise', 'return', 'try', 'while', 'with', 'yield']

# Можна іменувати таким чином:
# camelCase
# snake_case
# UPPERCASE - для константи (можна змінюватию, бо це звичайна змінна,
# але це як флажок що цього робити не треба)
full_name = 'Nadiia Kuzmich'
__my_age = '27'  # не більше двох символів
print('Hello!', 'My name', full_name, 'I\'m', __my_age)

# Можна так писати, але не треба:
моя_змінна = 'Доброго вечора'
print(моя_змінна)

# print – це функція, яка виводить інформацію на екран
# параметри (аргументи) функцій беруться у круглі дужки
print("Hello, World!")

# input — функція, яка призупиняє виконання програми, поки користувач не введе
# значення та натисне клавішу Enter. Функція повертає введене значення.
text = input('Enter some text: ')
print(text)
