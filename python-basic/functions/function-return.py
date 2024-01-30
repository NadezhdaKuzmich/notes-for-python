# Для того, щоб повернути результат функції, потрібно скористатися
# спеціальним словом return.
def sum_numbers(a, b):
    return a + b


result = sum_numbers(3, 9)
print(result)  # => 12


def subtraction_numbers(a, b):
    answer = [a - b]
    return answer


result = subtraction_numbers(9, 3)
print(result)  # => [6]


def sum_numbers(a, b, *args):
    answer = a + b + sum(args)
    return answer


result = sum_numbers(2, 3, 1, 3, 6, 2, 1, 8)
print(result)  # => 26
print(type(sum_numbers(2, 4)))  # => <class 'int'>


def external():
    def internal():
        pass

    return internal


print(type(external()))  # => <class 'function'>


def reversing_list_numbers(nums):
    # nums_copy = nums.copy()
    nums_copy = nums[:]
    nums_copy.reverse()
    return nums_copy


numbers = [1, 2, 3]
result = reversing_list_numbers(numbers)
print(numbers)  # => [1, 2, 3]
print(result)  # => [3, 2, 1]


# Задачки:
# 1. Знайдіть максимальне значення в списку, що передається в функцію,
# і поверніть його, якщо воно більше 0, в іншому випадку поверніть
# повідомлення про те, що число менше 0.
# v1
def get_max_from_list(list_values):
    max_value = list_values[0]
    for element in list_values:
        if element > max_value:
            max_value = element
    return max_value if max_value > 0 else "Max value is less then zero"


list_nums = [-45, -2, -5, -7, -78]
max_a = get_max_from_list(list_nums)
max_b = get_max_from_list([1, 12, 18, 5, 9, 102])
print(max_a)  # => Max value is less then zero
print(max_b)  # => 102


# v2
def get_max_from_list(list_values):
    max_value = max(list_values)
    return max_value if max_value > 0 else "Max value is less then zero"


max_a = get_max_from_list([1, 4, 8, 0, 9])  # => 102
max_b = get_max_from_list([-1, -2, -7, -9, -6])
# => Max value is less then zero
print(max_a)
print(max_b)


# 2. Поверніть кількість літер у слові, яке надсилається у параметрах.
def get_string_length(string):
    return len(string)


string_a = 'hello'
string_b = 'bye'
len_a = get_string_length(string_a)
len_b = get_string_length(string_b)
print(f"Str '{string_a}' has {len_a} characters")
print(f"Str '{string_b}' has {len_b} characters")


# 3. Напишіть функцію, яка зводить до ступеня число, яке передається у
# параметрах, якщо ступінь не є негативним. Перший параметр - число, другий –
# ступінь, у якому його необхідно звести.
# v1
def power(number, value_power):
    if value_power >= 0:
        return number ** value_power
    return number


print(power(2, -1))  # => 2


# v2
def power(number, value_power):
    if value_power >= 0:
        return pow(number, value_power)
    return number
    # print('NO PRINT')  # This code is unreachable


print(power(3, 3))  # => 27
