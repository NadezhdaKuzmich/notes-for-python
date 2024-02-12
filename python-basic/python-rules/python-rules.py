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
# моя_змінна = 'Доброго вечора'
# print(моя_змінна)

# print – це функція, яка виводить інформацію на екран
# параметри (аргументи) функцій беруться у круглі дужки
print('Hello, World!')
# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
# де:
# • objects – це об'єкти, які потрібно вивести
# • sep – роздільник
# • end – рядок, який потрібно вивести після всіх об'єктів
# • file – файл, до якого потрібно вивести дані
# • flush – чи потрібно одразу після виведення скинути вміст буфера у файл.
# Якщо ви виводите інформацію на одному рядку через тривалі проміжки часу,
# і вона не з'являється на екрані, доки ви не виведете символ нового рядка,
# додайте параметр flush=True.
# Жоден із цих параметрів не є обов'язковим.
# вказуємо роздільник
print(2, 3, 5, sep='; ')
print('he', 'llo', sep='')  # він може бути і порожнім рядком

# вказуємо кінець рядка
print(1, end='')
print(2, end='\n\n')
print('he', end='')
print('llo')

# input — функція, яка призупиняє виконання програми, поки користувач не введе
# значення та натисне клавішу Enter. Функція повертає введене значення.
text = input('Enter some text: ')
print(text)
