# Важливо розуміти, що input повертає рядок.
x = float(input('Введіть перше число: '))
y = float(input('Введіть друге число: '))
operation = input('Введіть символ арифметичної операції: ')

result = None
# (None - це спеціальне значення, що вказує, що
# значення об'єкта невідомо)

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
elif operation == '^':
    result = x ** y
else:
    print('Непідтримувана операція')

if result is not None:
    print(result)
