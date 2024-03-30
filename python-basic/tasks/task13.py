# task 1
some_tuple = (10, 20, 30, 40, 50)
some_tuple = some_tuple[::-1]
print(some_tuple)

# task 2
some_tuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(some_tuple[1][1])

# task 3
some_tuple = (50,)
print(some_tuple)

# task 4
some_tuple = (10, 20, 30, 40)
a, b, c, d = some_tuple
print(a)
print(b)
print(c)
print(d)

# task 5
some_tuple1 = (11, 22)
some_tuple2 = (99, 88)
some_tuple1, some_tuple2 = some_tuple2, some_tuple1
print(some_tuple2)
print(some_tuple1)

# task 6
some_tuple1 = (11, 22, 33, 44, 55, 66)
some_tuple2 = some_tuple1[3:-1]
print(some_tuple2)

# task 7
some_tuple = (11, [22, 33], 44, 55)
some_tuple[1][0] = 222
print(some_tuple)

# task 8
some_tuple = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
# sorted - це функція, яка створює новий список, що містить відсортовані
# елементи вихідного списку або ітерованої послідовності. Вона не змінює
# вихідний список.
# sort - це метод, який змінює вихідний список, сортуючи його елементи в
# певному порядку. Він не створює новий список.
some_tuple = tuple(sorted(some_tuple, key=lambda x: x[1]))
print(some_tuple)

# task 9
some_tuple = (50, 10, 60, 70, 50)
# .count(sub[, start[, end]])) - повертає кількість разів, коли вказане
# значення з'являється в кортежі. Параметри:
# - sub - str, рядок або символ;
# - start - int, індекс початку пошуку, за замовчуванням 0, необов'язково;
# - end - int, індекс кінця пошуку, за замовчуванням len, необов'язково.
print(some_tuple.count(50))


# task 10
def check(tuple_param):
    # all(iterable) - перевіряє, чи всі елементи в ітерованому об'єкті,
    # що ітерується, є істинними (дорівнюють True)
    return all(item == tuple_param[0] for item in tuple_param)


some_tuple = (45, 45, 45, 45)
some_tuple2 = (42, 44, 42, 42)
print(check(some_tuple))
print(check(some_tuple2))
