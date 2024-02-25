# Анонімні функції – використовуються у випадку, якщо нам їх потрібно кудись
# передати і більше ми їх не будемо використовувати повторно. Такий запис
# буде компактнішим. У такої функції не буде імені.

# Лямбда-вирази
# Звичайне оголошення функції:
# def add(x, y):
#     return x + y
# Використання лямбда-виразу (лямбда-функції, анонімної функції):
# add = lambda x, y: x + y

# Синтаксис:
# lambda x: x
# Де перший x – це параметр, який передається у функцію, а другий – те,
# що повертається.
# Еквівалент звичайної функції:
# def some_name(x): return x

# lambda
def make_something(function):
    for element in global_value:
        print(function(element))


global_value = [1, 2, 3, 4]
make_something(lambda x: x * 10)


def foo(x):
    return x


# In general, I would advise against this, as it goes against the PEP8
# recommendations: l_func = lambda...
l_func = (lambda x: x)
print(foo(1))
print(l_func(2))
print(foo.__name__)  # => foo
print(l_func.__name__)  # => <lambda>

# def power(x, y):
#     return x ** y
#
# print(power(2, 8))  # => 256

p = (lambda x, y: x ** y)
print(p(2, 8))  # => 256

nums = [4, 3, 2, 5, 6, 4, 3, 1]
nums.sort(key=lambda x: -x)
print(nums)  # => [6, 5, 4, 4, 3, 3, 2, 1]

m = list(map(lambda x: x ** 3, nums))
print(m)  # => [216, 125, 64, 64, 27, 27, 8, 1]
