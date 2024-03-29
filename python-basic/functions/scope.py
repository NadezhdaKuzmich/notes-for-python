# Scope - область видимості
# Область видимості – це область, де інтерпретатору доступні ваші змінні,
# функції та інше. Область видимості буває локальна та глобальна. Змінні,
# які оголошені поза функцією, називаються глобальними змінними в Python. Ці
# змінні мають велику область видимості та доступні всім функціям,
# що визначені після оголошення глобальної змінної. Коли змінна оголошується
# всередині функції, це локальна змінна. Область дії локальної змінної
# обмежена функцією, де вона створюється. Це означає, що вона доступна у
# функції, де вона оголошена, але не поза цією функцією.

# Глобальна область видимості
def print_x():
    print(x)


x = 1
print_x()  # => 1
print(x)  # => 1


# Локальна область видимості
def print_local_y():
    y = 2
    print(y)


print_local_y()  # => 2
# print(y)  # => NameError: name 'y' is not defined
print('~' * 40)


# Задачки
# Напишіть функцію, де дано натуральне число n. Виведіть усі числа від 1 до n.
def natural_int(n: int) -> None:
    if n >= 1:
        natural_int(n - 1)
        print(n)


natural_int(12)
print('~' * 40)


def generate_numbers(n):
    for value in range(1, n + 1):
        print(value)


generate_numbers(10)  # 1 2 3 ... 10
print('~' * 40)


# Напишіть функцію для прорахунку площі прямокутника, у параметрах
# передаються висота та довжина.
# Always use a def statement instead of an assignment statement that binds a
# lambda expression directly to a name.
# Yes:
def rectangle(height: int, length: int) -> int:
    return height * length


print(rectangle(2, 2))
print('~' * 40)

# No:
# rectangle_l = lambda h, l: h * l
# print(rectangle_l(3, 3))

# But:
# In general I would advise against this, as it goes against the PEP8
# recommendations.
rectangle_l2 = (lambda height, length: height * length)
print(rectangle_l2(3, 3))
