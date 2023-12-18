# int:
x_10: int = 15  # десяткове число => 15
y_1: str = bin(15)  # двійкове число або бітне => '0b1111'
y_2: int = 0b1111  # двійкове число => 15
z_8: int = 0o17  # вісімкове число => 15
w_16: int = 0xF  # шіснадцяткове число => 15

# Операції з цілими числами:
sum_x_y = 1 + 2
minus_x_y = 2 - 1
mult_x_y = 1 * 2
quotient = 1 / 2
floored_quotient = 11 / 2  # => 5
remainder = 11 % 2  # => 1
exp1 = 2 + 3 * 4  # => 14
exp2 = (2 + 3) * 4  # => 20

# float:
x: float = 5.5
y: float = 5.  # => 5.0 (можна опустити 0 після крапки)

# Корисні функції:
absolute_n = abs(-5)  # Абсолютне значення
rounded_n1: int = round(4.23121)  # => 4
rounded_n2: float = round(4.23121, 2)  # => 4.23
rounded_n3: int = round(4.8888)  # => 5 (округлює)

# Зміна типу:
float(1)  # => 1.0
int(1.0)  # => 1
print(int(1.99))  # => 1 просто обрізає все після крапки (НЕ округлює)

# Об'єкт також не змінюваний: (адреса змінилася)
age = 27
print(id(age))  # => 4368421192
age = 32
print(id(age))  # => 4368421352

# type()
int_n = 2
float_n = 4.8
name = 'Dima'
print(type(int_n))  # => <class 'int'>
print(type(float_n))  # => <class 'float'>
print(type(name))  # => <class 'str'>