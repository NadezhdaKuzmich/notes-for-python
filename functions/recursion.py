# Recursion
# Рекурсія – це коли функція викликає сама себе. У рекурсії обов'язково має бути кінцева глибина для того,
# щоб не було зациклювання.
# def foo():
#     return foo()
#
# foo()  # => RecursionError: maximum recursion depth exceeded
# print(globals())


def foo(x: int) -> None:
    if x < 10:
        x += 1
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
