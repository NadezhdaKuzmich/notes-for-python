some_tuple = (1, 2, 3)
some_tuple2 = tuple("Hello")
print(len(some_tuple))  # => 3
print('H' in some_tuple2)  # => True
print(some_tuple2.count('l'), 'count')  # => 2 count
print(some_tuple2.index('e'), 'index')  # => 1 index

a, b, c = (1, 2, 3)
print(a, b, c)  # => 1 2 3
# a, b, c = 1, 2, 3
# print(a, b, c)  # => 1 2 3
a = (1, 2)
x, y = a
print(f'{x=} {y=}')  # => x=1 y=2

# Кортежам властиві всі методи списків, які його не змінюють. Дуже часто
# зустрічається випадок використання кортежів у тому, щоб поміняти елементи
# місцями. Для цього достатньо прописати: a, b = b, a swapping
a = 1
b = 2

c = a
a = b
b = c
del c
print(f'{a=} {b=}')  # => a=2 b=1

a = 'One'
b = 'Two'
c = 'Three'
a, b = b, a
print(f'{a=} {b=}')  # => a='Two' b='One'
# a, b = (b, a, c)  # => ValueError: too many values to unpack (expected 2)
# Не можна так робити!

a, b, *anything = (b, a, c, 1, 3, 4, 'hello')
print(f'{a=} {b=} {anything=}')  # => a='One' b='Two' anything=['Three', 1,
# 3, 4, 'hello']

first, *middle, last = ('Igor', 'Mark', 'Lena', 'Zurab')
print(f'{first=}, {middle=}, {last=}')  # => first='Igor', middle=['Mark',
# 'Lena'], last='Zurab'

# Також, при проходженні за списком кортежів, цикл for може набувати стільки
# значень, скільки елементів у tuple. Синтаксис: for elem1, elem2 in [(1,2),
# (2,4)]:
class_school = (('Igor', 10), ('Mark', 12), ('Lena', 8), ('Zurab', 11))
for st, mark in class_school:
    print(f'Student: {st}, mark: {mark}')
