# Генератори:
def fibonacci(max_count):
    """Генерація max_count чисел Фібоначчі"""
    count = 0
    first, second = 0, 1

    while count < max_count:
        count += 1
        yield second
        first, second = second, first + second


for num in fibonacci(15):
    print(num)

print('\n', '* ' * 10, '\n')

# Вирази-генератори:
generator = (x ** 2 + y for x in range(2, 7) for y in range(3) if x != 6)
for number in generator:
    print(number)

print('\n', '* ' * 10, '\n')

print(sum(2 * x for x in range(5)))
print('\n', '* ' * 10, '\n')


# Підгенератори:
def generator():
    yield from (3 * x for x in range(5))
    print('\n', '. ' * 10, '\n')
    yield from (2 * x for x in range(5, 10))


for i in generator():
    print(i)
