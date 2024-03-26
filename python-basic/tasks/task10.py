import os

# task 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
res = num1 * num2
print("Multiplication is", res)

# task 2
print('My', 'name', 'is', 'Nadiia', sep=' ** ')

# task 3
num = 8
# '%o' - число у вісімковій системі числення.
print('%o' % num)

# task 4
num = 3.141592654
# .2 - вказівка того, що виводиться 2 знаки після '.';
# f - вказівка того, що виводиться речове число в десятковому поданні.
print('%.2f' % num)

# task 5
numbers = []
for i in range(1, 6):
    item = float(input(f"Enter number at location {i}: "))
    numbers.append(item)

print("User List:", numbers)

# task 6
# Метод readlines використовується для читання всіх рядків з файлу і повертає
# їх у вигляді списку рядків. Кожен рядок з файлу буде окремим елементом
# списку.
with open("data/text.txt", "r") as file:
    lines = file.readlines()

with open("data/new_text.txt", "w") as file:
    count = 0
    for line in lines:
        if count == 5:
            count += 1
            continue
        else:
            file.write(line)
        count += 1

# task 7
str1, str2, str3 = input("Enter three strings: ").split()
print('String 1:', str1)
print('String 2:', str2)
print('String 3:', str3)

# task 8
quantity = 2
totalMoney = 1100
price = 450
statement = "I have {1} dollars so I can buy {0} item\\s for {2:.2f} dollars."
print(statement.format(quantity, totalMoney, price))

# task 9
# Функція stat() модуля os отримує статистичну інформацію файлу або дескриптора
# файлу. Ця функція повертає об'єкт os.stat_result, який містить різні атрибути
# файлу, включно з його розміром.
# st_size - розмір файлу.
size = os.stat("data/new_text.txt").st_size
if size == 0:
    print('File is empty!')
else:
    print(size)

# task 10
with open("data/text.txt", "r") as file:
    lines = file.readlines()
    print(lines[4])
