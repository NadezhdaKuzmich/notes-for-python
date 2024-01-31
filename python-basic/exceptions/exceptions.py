# Винятки – це механізм для обробки свідомо відомих помилок та інших
# можливих проблем під час виконання програми. Як приклад – це розподіл на 0.

# Винятки
# print('first step')
# 1/0
# print('second step')
#
# def sum(first_arg, second_arg):
#     return first_arg - second_arg
#
# print(sum('asdf', 1))

# Для чого потрібні винятки
# • Можливість вивести текст, що читається, при виникненні помилки.
# • Програма не падатиме.
# • Прописуючи винятки, ви краще продумуєте логіку вашого коду.

# Для обробки винятків використається блок try-except.
# try:
#     some code
# except:
#     some action

# try:
#     1 / 0
# except:
#     print("You couldn't divide on zero!")

def divide_two_numbers(first, second):
    try:
        answer = first / second
    except ZeroDivisionError:
        return "You couldn't divide on zero"
    except (TypeError, Exception):
        return "You couldn't divide different types of object"
    else:
        print(f'Else if in try anything is OK. Answer: => {answer}')

    return answer

    # finally:
    #     print('FINALLY')
    # return answer  # => This code is unreachable (with finally)


print(divide_two_numbers(1, 0))
print(divide_two_numbers(4, 'str'))
print(divide_two_numbers(4, 2))
print('The code go further')
print('~' * 40)


def bool_return():
    try:
        return True
    finally:
        return False


print(bool_return())  # => False
print('~' * 40)

# Для того, щоб обробка помилок була більш точковою, можна вказувати певний
# тип помилки, який ви очікуєте. Спочатку відловлюються помилки типу
# BaseException, під які потрапляють будь-які помилки.
# try:
#     ...
# except BaseException:
#     ...

# Часто зустрічаються види винятків:
# • NameError – не знайдено змінну з такою назвою.
# • TypeError – неправильний тип об'єкта, до якого застосовується операція.
# • ValueError – помилка, пов'язана зі значенням аргументу.
# • AssertionError - вираз у функції assert хибно.
# • ImportError - не вдалося імпортувати модуль або його атрибут.

# raise
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    print('I catch raised error')

# raise ImportError
print('~' * 40)


# assert
# if 1 != 2:
#     raise AssertionError
# Ідентично цьому запису
# assert 1 == 2
# assert 'False' == 'Falsee'

# ImportError
# import math
# from math import minus

# Практичні задачі
# Task 1
# Реалізувати функцію, яка прийматиме на вхід номер місяця,
# повернути його назву та реалізувати в ньому кілька обробок винятків.
def month_name(month_number):
    months = ['January', 'February', 'March',
              'April', 'May', 'Jun', 'July',
              'August', 'September', 'October',
              'November', 'December']
    try:
        month_index = abs(month_number) - 1
        return months[month_index]
    except TypeError:
        return 'Please use only integers'
    except IndexError:
        return 'Please use integers between 1 and 12'


print(month_name(12))
assert month_name(12) == 'December'
print('~' * 40)


# Task 2
# Потрібно перевірити, чи всі числа в послідовності
# є унікальними і реалізувати кілька обробок винятків
def is_sequence_unique(sequence):
    try:
        return len(sequence[:]) == len(set(sequence))
    except (TypeError, KeyError) as error:
        return (f'You need to use only sequence type(str, list, range, tuple) '
                f'\n Error: {error}')


print(is_sequence_unique({'key': 'value'}))
print('~' * 40)
arr = [1, 2, 3, 4]
print(is_sequence_unique(arr))
print('~' * 40)
arr = [1, 1, 2, 3]
print(is_sequence_unique(arr))
print('~' * 40)


# Custom error
class TurnOffLightError(Exception):
    def __str__(self):
        return 'You forgot to turn off the light'


try:
    raise TurnOffLightError
except TurnOffLightError as e:
    print(f'Error message: {e}')
