# +=
num = 0
num += 2  # num = num + 2
print(num)

# if умова:
#     оператори
counter = 0
if counter < 10:
    counter += 1
print(counter)

x = int(input('x = '))
if x > 5:
    print('x > 5')

# Однорядкова форма (небажана для використання):
# Тут оператори, якщо їх кілька, поділяються символом крапки з комою.
# if умова: оператори

# Блок операторів не може бути порожнім. Якщо така необхідність виникає, можна
# скористатися оператором pass, який нічого не робить.
# if value is not None:
#     pass           # TODO: add logic

# if & else:
counter = 10
if counter < 10:
    counter += 1
else:
    counter += 100
print(counter)

temperature = 4
if temperature < 10:
    print("Вдягаєте шапку")
else:
    print("Не вдягаєте шапку")

# if & elif & else:
animal = "cat"
if animal == "cat":
    print("Meo")
elif animal == "dog":
    print("Wof")
elif animal == "snake":
    print("Shshsh")
else:
    print("I don't know this animal.")

# input()
# user_name = input("Fill up your name \n")
# user_age = int(input("Fill up your age, please \n"))
#
# if user_name == "Mark" and user_age >= 21:
#     print("Hello Mark")
#     print("Your age is more then 21")
# elif user_name == "Bob" or user_age < 21:
#     print(f"Hello user")
# else:
#     print(f"Hello dear user {user_name}")

# len()
# print(len("loooooooooong name"))
#
# user_name = input("Fill up your name \n")
# if len(user_name) > 9:
#     print("Your name is too long.")

print('''Меню:
1. Файл
2. Вид
3. Вихід''')
choice = int(input('Ваш вибір: '))

if choice == 1:
    print('Ви вибрали пункт меню "Файл"')
elif choice == 2:
    print('Ви відкрили меню "Вид"')
elif choice == 3:
    print('Завершення.')
else:
    print('Некоректний вибір')

# Тернарні оператори:
# Синтаксис умовного виразу у Python:
# 'вираз1' if 'умова' else 'вираз2'
a = 1
b = 2
result = a if a > b else b
print(result)

books = 5
print("You have", books, ("books" if books > 1 else "book"))

# Задачки:
# cost = int(input("Fill up your price \n"))
# if cost > 1000:
#     cost = cost - cost * 0.1
# elif cost > 500:
#     cost = cost - cost * 0.05
# elif cost > 100:
#     cost = cost - cost * 0.03
# print(cost)

is_ready = True
state_msg = 'Ready' if is_ready else 'Not ready yet'
print(state_msg)

is_ready = False
print(is_ready and 'Ready' or 'Not ready yet')

line = input("Enter any line \n")
# print(line if bool(line) else None)
print('You entered:', line if line else None)
