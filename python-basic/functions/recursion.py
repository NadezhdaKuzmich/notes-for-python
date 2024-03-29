# Рекурсія – це коли функція викликає сама себе. У рекурсії
# обов'язково має бути кінцева глибина для того, щоб не було зациклювання.
# Рекурсія
# • Пам'ять під локальні змінні виділяється під час кожного виклику функції.
# Це уможливлює рекурсію.
# • Рекурсія - виклик функції з неї самої, безпосередньо (проста рекурсія) або
# через інші функції (складна або непряма рекурсія), наприклад, функція A
# викликає функцію B, а функція B - функцію A.
# • Кількість вкладених викликів функції або процедури називається глибиною
# рекурсії.
# • Рекурсивна програма дозволяє описати повторюване чи навіть потенційно
# нескінченне обчислення, причому без явних повторень частин програми та
# використання циклів.

# def foo():
#     return foo()
# foo()  # => RecursionError: maximum recursion depth exceeded
# print(globals())


def foo(x: int) -> None:
    if x < 10:
        x += 1
        print(x)
        foo(x)
        print(x)


foo(1)


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(1 * 2 * 3 * 4 * 5)
