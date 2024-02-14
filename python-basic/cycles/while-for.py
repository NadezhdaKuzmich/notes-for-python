# Цикл — це конструкція, призначена для багаторазового виконання
# набору інструкцій.

# while:
counter = 5
while counter > 0:
    print('Iteration, counter =', counter)
    counter -= 1
print("-" * 20)

n = 1
while n <= 5:
    print('n =', n)
    n += 1
print("-" * 20)

x = 0
while x <= 0:
    x = int(input('Enter a positive number: '))
print('You have entered:', x)
print("-" * 20)

# Цикл while з гілкою else
# while умова:
#     блок_операторів_1
# else:
#     блок_операторів_2
# Оператор while також може мати гілку else (за аналогією з if). Спочатку
# кожної ітерації інтерпретатор перевіряє істинність умови виконання циклу,
# і якщо воно істинно, то виконує гілку while, інакше він виконує гілку else
# (якщо вона присутня) і завершує виконання циклу, причому це може статися
# перед першою ітерацією, якщо умова спочатку було хибним.
x = 5
while x:
    print(x)
    x -= 1
else:
    print('Цикл виконано')
    print('Кінцеве значення x:', x)
print("-" * 20)

# Однак якщо цикл був перерваний оператором break, то гілка else не
# виконується.
x = 3
while x:
    x -= 1
    response = input('Введіть stop, щоб зупинити цикл (інакше що завгодно): ')
    if response == 'stop':
        break
else:
    print('Цикл завершився сам')
    print('Кінцеве значення x:', x)
print('Кінець програми')
print("-" * 20)

# range():
range(6)  # => range(0, 6) => [0, 1, 2, 3, 4, 5]

# for:
for number in range(6):
    print(number)
print("-" * 20)

for i in range(5, 10):
    print('i =', i)
print("-" * 20)

for i in range(5, 10, 2):
    print('i =', i)
print("-" * 20)

for i in range(5, 0, -1):
    print('i =', i)
print("-" * 20)

for i in range(3):
    response = input('Введіть stop, щоб зупинити цикл (інакше що завгодно): ')
    if response == 'stop':
        break
else:
    print('Цикл завершився сам')
    print('Кінцеве значення x:', x)
print('Кінець програми')
print("-" * 20)

for i in range(5):
    for j in range(30):
        print('*', end='')
    print()
print("-" * 20)

# break:
counter = 10
while True:
    counter -= 1
    print(counter)
    if counter == 5:
        break
        # print("Текст після break не друкується! Всі операції після нього -
        # не спрацюють.")
print("-" * 20)

while True:
    print("Enter 'exit' to exit loop")
    response = input('> ')
    if response == 'exit':
        break

print('Loops has stopped.')
print("-" * 20)

name = None
while True:
    print('Меню:')
    print('1. Ввести ім\'я')
    print('2. Вивести вітання')
    print('3. Вийти')
    response = input('Виберіть пункт: ')
    print()

    if response == '1':
        name = input('Введіть ваше ім\'я: ')
    elif response == '2':
        if name:
            print('Привіт, ', name, '!', sep='')
        else:
            print('Я не знаю вашого імені.')
    elif response == '3':
        break
    else:
        print('Неправильне введення.')

print("-" * 20)

# continue
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)
print("-" * 20)

# Задачки:
# for number in range(102):
#     if number != 0 and number % 2 == 0:
#         print(number)
# print("-" * 20)

# word = "hello"
# answer = ""
# for char in word:
#     if char == "l":
#         answer += "s"
#     else:
#         answer += char
# print(answer)
print('hello'.replace('l', 's'))
print("-" * 20)

for num in reversed(range(100)):
    if num % 5 == 0:
        print(num)
        break

# for num in range(-99, 0):
#     if num % 5 == 0:
#         print(abs(num))
#         break
