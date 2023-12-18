# +=
num = 0
num += 2  # num = num + 2
print(num)

# if:
counter = 0
if counter < 10:
    counter += 1
print(counter)

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

# Тернарні оператори:
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

line = input("Any line \n")
# print(line if bool(line) else None)
print(line if line else None)
