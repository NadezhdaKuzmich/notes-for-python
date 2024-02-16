# Стандартні функції у Python
# У Python існує безліч вбудованих функцій, які можна і потрібно
# використовувати для спрощення коду:
# print – функція виведення повідомлення в консоль.
# len – функція, яка повертає довжину об'єкта

# Функції перетворення типів – потрібні для того, щоб можна було створювати
# нові об'єкти певного типу.
# int - перетворення на ціле число
a_str = "10"
a_int = int(a_str)

# Функції bin, oct і hex повертають рядки, що становлять
# дане число у відповідних системах числення
number = int(input('Введіть число:'))
print('Двійкова система:', bin(number))
print('Вісімкова система: ', oct(number))
print('Шістнадцяткова система:', hex(number))

# str – перетворення на рядок
b_int = 10
b_str = str(b_int)

# float – перетворення на не ціле число
c_int = 25
c_float = float(c_int)

# list - перетворення на список
# dict – перетворення на словник
# set – перетворення на множини
e_list = [1, 2, 2, 2, 3]
e_set = set(e_list)

# tuple – перетворення на кортеж
# bool – перетворення на True/False
d_list = []
d_bool = bool(d_list)

d_list_2 = [1, 2, 3]
d_bool_2 = bool(d_list_2)

# sum – повертає суму набору чисел.
# min та max – повертає мінімум і максимум із набору чисел відповідно.
my_list = [-35, 2, 3, 10]
print(len(my_list))  # 4 count of values in list
print(len("hello"))  # 5 count of chars in string
print(sum(my_list))  # -20 sum of values in list
print(max(my_list))  # 10 max of values in list
print(min(my_list))  # -35 min of values in list

print(sum(my_list) / len(my_list))  # -5.0 average of values in list

# reversed дозволяє обходити послідовність у зворотному порядку
for i in reversed(range(5)):
    print(i)
