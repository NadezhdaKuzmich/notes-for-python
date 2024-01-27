# Методи списків:
# help([])
# help(list)
# dir(list)

# append() – додавання нового елемента до кінця списку.
shopping_list = ['milk', 'bread']
print(shopping_list, id(shopping_list))  # => ['milk', 'bread']

shopping_list.append('potatoes')
print(shopping_list, id(shopping_list))  # => ['milk', 'bread', 'potato']

# clear() – видалити всі елементи списку.
shopping_list.clear()
print(shopping_list, id(shopping_list))  # => []

# extend() – розширює список переданої послідовності.
shopping_list_weekly = ['milk', 'bread']
shopping_list_monday = ['potatoes', 'onions']
shopping_list_weekly.extend(shopping_list_monday)
print(shopping_list_weekly)  # => ['milk', 'bread', 'potatoes', 'onions']

shopping_list_tuesday = ['icecream', 'chocolate']
shopping_list_weekly += shopping_list_tuesday
print(shopping_list_weekly)  # => ['milk', 'bread', 'potatoes', 'onions',
# 'icecream', 'chocolate']

# index() – повертає index вказаного елемента, якщо таких елементів кілька –
# поверне перший знайдений.
print(shopping_list_weekly.index('chocolate'))  # => 5

# pop() – видаляє елемент зазначеного індексу та повертає його.
print(shopping_list_weekly.pop())  # => chocolate
print(shopping_list_weekly.pop(4))  # => icecream
print(shopping_list_weekly)  # => ['milk', 'bread', 'potatoes', 'onions']

# reverse() – дзеркально відображає список.
shopping_list_weekly.reverse()  # => нічого не повертає (None)
print(shopping_list_weekly)  # => ['onions', 'potatoes', 'bread', 'milk']

# sort() – сортує перелік. Якщо вказати параметри reverse=True, тоді сортування
# буде у зворотному порядку.
nums = [4, 1, 5, 2, 6, 3]
nums.sort()  # => нічого не повертає (None)
print(nums)  # => [1, 2, 3, 4, 5, 6]

nums.sort(reverse=True)
print(nums)  # => [6, 5, 4, 3, 2, 1]

shopping_list_weekly.sort()
print(shopping_list_weekly)  # => ['bread', 'milk', 'onions', 'potatoes']

# Обхід списків
counter = 1
for item in shopping_list_weekly:
    print(f'{counter}) {item}')
    counter += 1

# index = 0
# while True:
#     if index == len(nums):
#         break
#     else:
#         print(f'num: {nums[index]}')
#         index += 1

for num in nums:
    print(f'num: {num}')
print('~' * 40)

# Задачки:
list_of_nums = [2, 4, 1, 7, 3, 55, 98, 2, 12]
copy_list_of_nums2 = list_of_nums.copy()
for num in list_of_nums:
    if num % 2 == 0:
        copy_list_of_nums2.remove(num)
print(copy_list_of_nums2)
print('~' * 40)

# copy_list_of_nums = list_of_nums.copy()
# index = 0
# while True:
#     if index < len(list_of_nums):
#         if list_of_nums[index] % 2 == 0:
#             copy_list_of_nums.remove(list_of_nums[index])
#         index += 1
#     else:
#         break
# print(copy_list_of_nums)

list_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_nums_squares = list()
for num in list_nums:
    list_nums_squares.append(num ** 2)
print(list_nums_squares)
print('~' * 40)

# for index in range(len(list_nums)):
#     list_nums[index] = list_nums[index] ** 2
# print(list_nums)

list_nums2 = [1, -4, 12, -8, 9, 10, -55, 10, 99]
maximum = list_nums2[0]
minimum = list_nums2[0]
# for i in range(1, len(list_nums2)):
#     if list_nums2[i] > maximum:
#         maximum = list_nums2[i]
# print(maximum)

for num in list_nums2:
    if num > maximum:
        maximum = num
print(maximum)

for num in list_nums2:
    if num < minimum:
        minimum = num
print(minimum)

print(max([1, 4, 12, 8, 9, 10, 55, 10, 99]))
print(sorted(list_nums2)[-1])
# list_nums2.sort()
# print(list_nums2[-1])
