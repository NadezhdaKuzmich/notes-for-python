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
