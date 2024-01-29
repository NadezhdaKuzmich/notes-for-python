# Множини – це структура даних, що не містить елементів, що повторюються.
# Множини не підтримують індексацію, тому доступ до елементів можливий
# перебором.
# Синтаксис множин: {1, 4, 2, 3}
print('Множини')

# Створення:
some_set = {'a', 'b', 'c', 'c'}
some_set1 = set(['a', 'b', 'c', 'c'])
some_text = set('Hello')
print(some_set)  # => {'a', 'c', 'b'}
print(some_set1)  # => {'a', 'c', 'b'}
print(some_text)  # => {'H', 'e', 'l', 'o'}

# В множину можна підставляти лише незмінні елементи: some_set2 = {['a',
# 'b'], {'a': 'a'}, 'a', 12, {1, 2, 3, 4}}  # => TypeError: unhashable type:
# 'list'
some_set2 = {'a', 12}
print(some_set2)  # => {'a', 12}

print(len(some_text))  # => 4
print('l' in some_text)  # => True
print('x' in some_text)  # => False
print(2 in [1, 2, 3, 4])  # => True

# колекції
# [], 'line', {'key':'value'}, {1, 2}

some_frozen_set = frozenset('Frozen')  # Не можна редагувати та недоступні
# методи для редагування.
print(some_frozen_set)
print('~' * 50)

# Поняття кортежів
# Кортеж (tuple) – це незмінний перелік.
# Синтаксис кортежів:
# (1, 2, 3) (1,)
print('Кортежі')

# Створення:
some_tuple = (1, 2, 3)
some_tuple1 = ([], {}, set(), ())  # Може зберігатися любий тип елементів
some_tuple2 = tuple(['a', 'b', 'c'])
some_tuple3 = tuple("Hello I am python developer")
print(some_tuple)  # => (1, 2, 3)
print(some_tuple1)  # => ([], {}, set(), ())
print(some_tuple2)  # => ('a', 'b', 'c')
print(some_tuple3)  # => ('H', 'e', 'l', 'l', 'o', ' ', ...)

# empty tuple
empty_tuple = ()
empty_tuple2 = tuple()

# tuple with 1 element
tuple_one = (1,)
print(tuple_one)  # => (1,)
tuple_one = 1,
print(tuple_one)  # => (1,)

# tuple_one = (1) - Неправильно!
# print(tuple_one)  # => 1

# Є 2 множини
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}

# Завдання 1
# Вивести в консоль елементи A, яких немає в B.
print(A.difference(B))  # => {3, 4, -3}

# Завдання 2
# Вивести в консоль загальні елементи А та В.
print(A.intersection(B))  # => {11, 5, 7}

# Завдання 3
# Вивести в консоль об'єднання множин А та В.
print(A.union(B))  # => {1, 3, 4, 5, 7, 8, 10, 11, -3}

# Завдання 4 Є рядок a = “a14b6fh”, як дізнатися, що всі символи унікальні,
# використовуючи множини та списки?
a = 'a14b6fh'
set_a = set(a)  # Множина видалить всі повторювані елементи
print(len(set_a) == len(a))  # порівняємо довжини => True
