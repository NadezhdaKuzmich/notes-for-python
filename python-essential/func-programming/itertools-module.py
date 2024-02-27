from itertools import (product,
                       permutations,
                       combinations,
                       combinations_with_replacement,
                       chain,
                       takewhile,
                       dropwhile
                       )

# Модуль itertools містить функції для роботи з ітераторами та створення
# ітераторів. Деякі з них:
# - product - декартовий добуток ітераторів (для уникнення вкладених циклів
# for);
for a, b in product(range(2), range(3)):
    print(a, b)

print()

# - permutations - генерація перестановок;
print(list(permutations('ABC', 2)))
print()

# - combinations - генерація сполучень;
print(list(combinations('ABC', 2)))
print()

# - combinations_with_replacement - генерація розміщень;
print(list(combinations_with_replacement('ABC', 2)))
print()

# - chain - з'єднання декількох ітераторів в один;
for i in chain(range(2), range(3)):
    print(i)

print()

# - takewhile - отримання значень послідовності, доки значення функції-
# предиката для її елементів істинне;
numbers = [1, 4, 6, 4, 1]

for value in takewhile(lambda x: x < 5, numbers):
    print(value)

print()

# - dropwhile - отримання значень послідовності, починаючи з елемента, для
# якого значення функції-предиката перестане бути істинним.
for value in dropwhile(lambda x: x < 5, numbers):
    print(value)
