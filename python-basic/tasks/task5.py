# task 1
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set, '\n')

# task 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
print(set2.intersection(set1), '\n')

# task 3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2), '\n')

# task 4
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1, '\n')

# task 5
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1, '\n')

# task 6
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.symmetric_difference(set2))
print(set1.difference(set2))
print(set2.difference(set1), '\n')

# task 7
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Метод set.isdisjoint() дає змогу перевірити множину set1 на відсутність
# спільних елементів із послідовністю set2. Метод повертає True, якщо множина
# set1 не має спільних елементів з ітеруємим об'єктом set2, якщо є спільні
# елементи, то поверне False.
if set1.isdisjoint(set2):
    print("Two sets have no items in common", '\n')
else:
    print("Two sets have items in common")
    print(set1.intersection(set2), '\n')

# task 8
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1, '\n')

# task 9
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)
