import random

# task 1
print("Generating 3 random integer number between 100 and 999 divisible by 5")

for num in range(3):
    # randrange(start, stop, step) - повертає випадково вибране
    # число з послідовності.
    print(random.randrange(100, 999, 5), end=', ')

# task 2
lottery_tickets_list = []
print("\ncreating 100 random lottery tickets")

for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

# Метод sample повертає випадкову вибірку елементів із послідовності.
# У першому параметрі методу вказуємо послідовність, у другому параметрі -
# кількість елементів, які ми хочемо вибрати випадковим чином.
winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)
