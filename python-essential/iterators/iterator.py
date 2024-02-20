# Функція обходу ітерабельного об'єкта
def traverse(iterable):
    print(f'Traversing {type(iterable).__name__}:')
    for element in iterable:
        print(element)
    print()


# Оголошення списку
my_list = [1, 2, 3, 5, 8]

# Отримання його ітератора
list_iterator = iter(my_list)

# Обхід списку
traverse(my_list)

# Обхід ітератора списку
traverse(list_iterator)

# Черговий обхід списку - працює коректно, оскільки створюється
# новий об'єкт-ітератор
traverse(my_list)

# Черговий обхід ітератора - не виводиться нічого, оскільки
# елементи в ітераторі вже вичерпані
traverse(list_iterator)

# next:
it = iter(my_list)
print('next(iter): ')
print(next(it), next(it), next(it), next(it), next(it))
print()


# custom func
def my_for(iterable, callback):
    itr = iter(iterable)
    while True:
        try:
            value = next(itr)
            callback(value)
        except StopIteration:
            break


def loop_body(val):
    print(f'Value is {val}')


print("My func")
my_for(range(10), loop_body)
