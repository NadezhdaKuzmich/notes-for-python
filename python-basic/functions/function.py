# Функція - це іменована ділянка коду, до якої можна неодноразово звертатися
# з інших місць програми. Функції можуть приймати параметри (аргументи) і
# повертати значення. У Python будь-яка підпрограма є функцією. Якщо функція
# явно не повертає жодного значення, автоматично повертається None.

# Функція – це об'єкт, який приймає та повертає значення. Функцію можна
# викликати з будь-якого місця в коді повторного використання. Ця концепція
# допомагає уникнути повторюваних ділянок коду, а також розбивати програму
# на підпрограми, що покращує читання коду.

# Створення функції:
# Щоб створити функцію, потрібно скористатися спеціальним словом def.
# Синтаксис:
# def my_function(params?):
#     тіло функції...

# В тілі функції обов'язково щось має бути
# def example_error():
# example_error()  # => IndentationError: expected an indented block after
# function definition on line 14

# Якщо ви ще не знаєте що буде в функції, то можна поставити заглушку,
# щоб не виводило помилку
# v1
# def example(): pass  # заглушка

# example()

# v2
# def example2():
#     ...  # заглушка

# example2()

# v3
# def example3():
#     """Docstring for information"""  # заглушка (інформативний опис)

# example3()
# print(help(example3))  # => Docstring for information

def hello_world():
    print('Hello, World!')


hello_world()

# Головну функцію бажано викликати так
# (таким чином функція буде викликана тільки якщо
# цей файл був запущений як головний; це важливо
# для додатків, що складаються з декількох модулів)
if __name__ == '__main__':
    hello_world()


def print_sum():
    print(2 + 2)


print_sum()  # => 4


def print_sum(a, b):
    print(a + b)


print_sum(4, 4)  # => 8
print_sum(6, 8)  # => 14


def print_numbers(limit):
    for i in range(limit):
        print(i)


print_numbers(2)


def print_numbers(limit):
    for i in range(limit):
        print(i)


n = int(input('Введіть n: '))
print_numbers(n)


def printing_positional_arguments(first, second):
    print(f'{first=} {second=}')


printing_positional_arguments('FIRST', 'SECOND')
# => first='FIRST' second='SECOND'
printing_positional_arguments('SECOND', 'FIRST')


# => first='SECOND' second='FIRST'
# printing_positional_arguments('SECOND', 'FIRST', 'THIRD')  # => TypeError:
# printing_positional_arguments() takes 2 positional arguments but 3 were given

def printing_positional_arguments(first, second, third, *args):
    print(f'{first=} {second=} {third=}', args)


# => first='SECOND' second='FIRST' third='THIRD' ('fourth', 'fifth', '...',
# [], {}, 2)
printing_positional_arguments('SECOND', 'FIRST', 'THIRD',
                              'fourth', 'fifth', '...', [], {}, 2)


def print_sum(a, b, *nums):
    print(a + b + sum(nums))


print_sum(1, 2, 3, 4, 5, 6, 7, 8, 9)  # => 45


def make_pizza(*toppings):
    for topping in toppings:
        print(f'-{topping}')


make_pizza('mushrooms', 'sausages', 'cheese')


# Ключові аргументи
# Функція, яка приймає три аргументи
def info(obj, color, price):
    print('Об\'єкт:', obj)
    print('Колір:', color)
    print('Ціна:', price)
    print()


# передача параметрів у прямому порядку
info('ручка', 'синій', 1)
# передача параметрів у довільному порядку
info(price=5, obj='чашка', color='помаранчевий')
# можна змішувати обидва способи, але спочатку повинні йти параметри,
# які передаються в прямому порядку
info('кава', price=10, color='чорний')


def printing_positional_arguments(first, second, third):
    print(f'{first=} {second=} {third=}')


# => first='FIRST' second='SECOND' third='THIRD'
printing_positional_arguments(second='SECOND', first='FIRST', third='THIRD')


def hello_user(name, surname, middlename):
    print(f'Hello {name} {surname} {middlename}!')


hello_user(surname='Dil', middlename='Mon', name='Mark')
# hello_user(surname='Dil', name='Mark')  # => TypeError: hello_user()
# missing 1 required positional argument: 'middlename'

# *args - упаковка для позиційних аргументів
# **kwargs - упаковка для ключових аргументів
def hello_user(position_job, name, surname, middlename='', **kwargs):
    # або None
    print(kwargs)  # => {'country': 'Ukraine', 'work_car': 'CAT'}
    print(f'Hello {name} {surname} {middlename}! '
          f'Your job position is {position_job}.')


hello_user('developer', surname='Dil', name='Mark',
           country="Ukraine", work_car='CAT')
# => Hello Mark Dil ! Your job position is developer.
