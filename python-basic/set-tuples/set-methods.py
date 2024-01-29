some_set = {'a', 1, 3, 4, 5, 2, 8}
empty_set = set()

# pop() – видаляє перший елемент множини і повертає його. Так як множини не
# впорядковані, не можна точно сказати, який елемент буде першим.
print('pop:', some_set.pop())  # => 1
print('pop:',
      some_set)  # => {2, 3, 4, 5, 8, 'a'} але відповідь може бути й інша

# print(empty_set.pop())  # => KeyError: 'pop from an empty set'

# discard(elem) – видаляє елемент із множини, не повертає нічого (None) та
# не виводить помилок (None).
print('discard:', some_set.discard(8))  # => None
print('discard:', some_set)  # => {2, 3, 4, 5, 'a'}
# print(empty_set.discard('any'))  # => None

# remove(elem) – видаляє елемент із множини. Якщо такого елемента немає,
# видає помилку.
new_some_set = {'a', 1, 3, 4, 5, 2, 8}
new_some_set.remove('a')  # => {1, 2, 3, 4, 5, 8}
print('remove:', new_some_set)
# some_set.remove('b')  # => KeyError: 'b'

# add(elem) – додає елемент у множину.
some_set.add('new element')
print('add:', some_set)  # => {'new element', 2, 3, 4, 5, 'a'}
# some_set.add([])  # => TypeError: unhashable type: 'list'

# union(another_set) – поєднує множини.
first_set = {'one', 'two'}
second_set = {'three', 'four'}
print('union:',
      first_set.union(second_set))  # => {'three', 'one', 'four', 'two'}

# v2
print(
    first_set | some_set)  # => {'new element', 2, 3, 4, 5, 'two', 'one', 'a'}

# v3
# Не повертає нову множину, а працює з першою
some_set |= second_set
print(some_set)  # => {'new element', 2, 3, 4, 5, 'four', 'three', 'a'}

# intersection(another_set) – знаходить перетин двох множин.
print(some_set.intersection(second_set))  # => {'three', 'four'}
some_set1 = {'a', 0, 2, 4, 6, 8}
some_set2 = {1, 3, 5, 7, 8, 'a'}
print(some_set1.intersection(some_set2))  # => {8, 'a'}
print(some_set1.intersection(some_set2, first_set))  # => set()

# v2
print(some_set1 & some_set2)  # => {8, 'a'}
print(some_set & some_set1 & some_set2)  # => {'a'}

# difference(another_set) – різниця множин. Повертає різницю двох або більше
# множин у вигляді нової множини.
print(some_set1.difference(some_set2))  # => {0, 2, 4, 6}
print(some_set2.difference(some_set1))  # => {1, 3, 5, 7}
a = {1, 2, 3, 4}
b = {3, 4}
print(a.difference(b))  # => {1, 2}
print(b.difference(a))  # => set()

# isdisjoint()
# Перевірка того, що множина не має спільних елементів з іншою множиною
print(some_set1.isdisjoint(some_set2))  # => False
print(first_set.isdisjoint(second_set))  # => True

# issubset()
# Перевірка того, що усі елементи множини є елементами іншої множини
print(some_set1.issubset(some_set2))  # => False

# v1
print({1, 2}.issubset({1, 2, 3}))  # => True

# v2
print({1, 2} <= {1, 2, 3})  # => True

# symmetric_difference()
# Створення нової множини, яка є симетричною різницею даних множин
# v1
print({1, 2}.symmetric_difference({1, 2, 3}))  # => {3}

# v2
print({1, 2} ^ {1, 2, 3})  # => {3}
# АЛЕ! Бінарні оператори потребують щоб другий операнд також був множиною:
# print({1, 2}.symmetric_difference([1, 2, 3]))  # => (Все спрацює) {3}
# print({1, 2} ^ [1, 2, 3])  # => (Видасть помилку) TypeError: unsupported
# operand type(s) for ^: 'set' and 'list'

# clear() – очищає множину.
some_set.clear()
print(some_set)  # => set()
