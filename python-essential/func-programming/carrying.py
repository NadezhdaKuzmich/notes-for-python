# Приклад каррування функції
def ordinary_add(x, y):
    """Звичайна функція"""
    return x + y


def curryied_add(x):
    """Каррована функція"""

    def do_add(y):
        return x + y

    return do_add


print(ordinary_add(2, 3))
print(curryied_add(2)(3))

# Каррування робить легким часткове застосування функцій
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))
print()

# У вигляді лямбда-виразів
# BUT: PEP 8: E731 do not assign a lambda expression, use a def
ordinary_add = lambda x, y: x + y
curryied_add = lambda x: lambda y: x + y

print(ordinary_add(2, 3))
print(curryied_add(2)(3))
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))
