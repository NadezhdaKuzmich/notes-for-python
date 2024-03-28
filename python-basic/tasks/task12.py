# task 1
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()
res2 = []

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
# append() приймає один аргумент item і додає його в кінець list. Тип параметра
# може бути будь-яким: числа, рядки, словники тощо.
res.append(odd_elements)
res.append(even_elements)
print(res)  # => [[6, 12, 18], [4, 12, 20, 28]]
# Функція extend() працює як append(), але як параметр приймає ітерований
# об'єкт: список, кортеж або рядки
res2.extend(odd_elements)
res2.extend(even_elements)
print(res2)  # => [6, 12, 18, 4, 12, 20, 28]

# task 2
sample_list = [34, 54, 67, 89, 11, 43, 94]
print("Original list ", sample_list)

# pop() використовується для видалення і повернення останнього елемента зі
# списку або зазначеного індексу в списку.
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

# insert() потрібен для того, щоб додати новий елемент у будь-яке місце списку.
sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)

# append() використовується тільки для додавання елементів у кінець списку.
sample_list.append(element)
print("List after Adding element at last ", sample_list)

# task 3
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original list ", sample_list)

part_size = int(len(sample_list) / 3)
start, end = 0, part_size

for i in range(3):
    list_part = sample_list[start:end]
    print("Chunk ", i, list_part)
    # reversed() повертає розгорнутий ітератор, а не рядок.
    print("After reversing it ", list(reversed(list_part)))
    start = end
    end += part_size

# task 4
sample_list = [1, 2, 8, 1, 2, 4, 2, 8, 7]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

# task 5
first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
# zip() використовується для поєднання двох і більше списків в один. Вона
# повертає ітератор кортежів, де i-ий кортеж містить i-ий елемент з кожного з
# переданих списків.
result = zip(first_list, second_list)
result_set = set(result)
print(result_set)

# task 6
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("First Set after removing common element ", first_set)

# task 7
first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
# set.issubset(other) дає змогу перевірити, чи перебуває кожен елемент множини
# set у послідовності other.
print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of first set - ", second_set.issubset(first_set))
# set.issuperset(other) дає змогу перевірити, чи знаходиться кожен елемент
# послідовності other у множині set. Метод повертає True, якщо множина set є
# надмножиною ітерованого об'єкта other, якщо ні, то поверне False.
print("First set is super set of second set - ",
      first_set.issuperset(second_set))
print("Second set is super set of first set - ",
      second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)
