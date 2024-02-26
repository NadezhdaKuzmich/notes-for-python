from functools import reduce

# Трьома класичними функціями вищого порядку, що з'явилися ще в мові
# програмування Lisp, які приймають функцію і послідовність, є map, filter і
# reduce.

# - map
# застосовує функцію до кожного елемента послідовності, у Python2 повертає
# список, у Python 3 - об'єкт-ітератор.
string = '2 4 8 15 42'
numbers = map(lambda num: int(num) + 1, string.split())
print(list(numbers))

# - filter
# залишає лише ті елементи послідовності, для яких задана функція істинна.
# У Python 2 повертає список, у Python 3 - об'єкт-ітератор.
numbers = [3, 2, -1, 0, 15, -8, -7, 3, -3, 8]
positive_numbers = filter(lambda x: x > 0, numbers)
print(list(positive_numbers))

# - reduce (у Python2 вбудована, у Python3 міститься в модулі functools)
# приймає функцію від двох аргументів, послідовність і опціональне початкове
# значення та обчислює згортання (fold) послідовності як результат послідовного
# застосування цієї функції до поточного значення (так званого акумулятора) і
# наступного елемента послідовності.
numbers = [3, 2, 1, 8, -3, -2]
product = reduce(lambda acc, num: acc * num, numbers)
print(product)
