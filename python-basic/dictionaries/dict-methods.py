# Методи словників:
# help({})
# help(dict)
# dir(dict)

capital_cities = {
    'Venezuela': 'Caracas',
    'Nicaragua': 'Managua',
    'Ukraine': 'Kiev',
    'Georgia': 'Tbilisi',
    'Moldova': 'Kishinev',
    'China': 'Beijing',
    'USA': 'Washington',
}

# items() – повертає пару ключ – значення.
print(capital_cities.items())
# dict_items([('Venezuela', 'Caracas'), ('Nicaragua', 'Managua'),
# ('Ukraine', 'Kiev'), ('Georgia', 'Tbilisi'), ('Moldova', 'Kishinev'),
# ('China', 'Beijing'), ('USA', 'Washington')])
for element in capital_cities.items():
    print(element)  # => ('Venezuela', 'Caracas')...
print('~' * 40)

# Розпаковка:
# first_value, second_value = 1, 2
# country, capital = 'Georgia', 'Tbilisi'

for country, capital in capital_cities.items():
    print(f'{country}: {capital}')  # => Venezuela: Caracas...
print('~' * 40)

# pop(key) – видаляє ключ і повертає відповідне значення.
print(capital_cities.pop('China'))  # => Beijing
print(capital_cities)
print('~' * 40)

# popitem() – видаляє останнє значення та повертає його у форматі
# ключ-значення. Не приймає аргументів.
print(capital_cities.popitem())  # => ('USA', 'Washington')
print(capital_cities)
print('~' * 40)

# update({‘key’: ‘value’}) – додає нове ключ-значення
capital_cities.update({'Brazil': 'Brasilia'})
print(capital_cities)
print('~' * 40)
# або словник:
usa = {'USA': 'Washington'}
capital_cities.update(usa)
print(capital_cities)
print('~' * 40)

# keys() – повертає всі ключі у словнику.
print(capital_cities.keys())
# => dict_keys(['Venezuela', 'Nicaragua', 'Ukraine', 'Georgia', 'Moldova',
# 'Brazil', 'USA'])
print('~' * 40)

# values() – повертає всі значення у словнику.
print(capital_cities.values())
# => dict_values(['Caracas', 'Managua', 'Kiev', 'Tbilisi', 'Kishinev',
# 'Brasilia', 'Washington'])
print('~' * 40)

# setdefault() - Повертає значення, або як що ключа немає то повертає
# значення із аргументу.
print('GET =>', capital_cities.get('Romania'))  # => None
print('SETDEFAUL =>', capital_cities.setdefault('Romania', 'Bucharest'))
# => Bucharest
print('~' * 40)

# fromkeys - будує новий словник.
any_dictionary = {}
days_name_list = ['Monday', 'Tuesday', 'Wednesday']
new_dictionary = any_dictionary.fromkeys(days_name_list)
print(new_dictionary)  # => 'Monday': None, 'Tuesday': None, 'Wednesday':
# None
new_dictionary = any_dictionary.fromkeys(days_name_list, 'Day')
print(f'{any_dictionary=}')  # => any_dictionary={}
print(f'{new_dictionary=}')  # => new_dictionary={'Monday': 'Day',
# 'Tuesday': 'Day', 'Wednesday': 'Day'}
print('~' * 40)

# clear() – очищає словник.
capital_cities.clear()
print('clear =>', capital_cities)  # => {}
print('~' * 40)

# Задачки: 1. Порахувати за допомогою словника скільки разів елемент
# повторюється у списку.
classmates_name = ['Sergey', 'Igor', 'Tanya', 'Sergey', 'Mikhael', 'Sergey',
                   'Lena']
# v0
# answer = {}
# for name in classmates_name:
#     if name in answer:
#         answer[name] += 1
#     else:
#         answer[name] = 1
# print(answer)
# print('~' * 40)

# v1
# answer = {}
# for name in classmates_name:
#     if name in answer.keys():
#         answer[name] += 1
#     else:
#         answer[name] = 1
# print(answer)
# print('~' * 40)

# v2
answer = {}
for name in classmates_name:
    answer[name] = classmates_name.count(name)

print(answer)
print('~' * 40)

# 2. Пройтися за словником і вивести всі значення, які мають парний ключ.
data_dict = {1: 'one', 8: 'any text', 2: '2', 6: '6', 9: 'end'}
for key, value in data_dict.items():
    if key % 2 == 0:
        print(value)
print('~' * 40)

# range_none: dict = dict().fromkeys(range(10), 'any value')
# for k in range_none.keys():
#     if k % 2 == 0:
#         print(k)

# 3. Видалити всі ключі, значення яких починається з літери.
# v1
# DO NOT delete element in the collection during cycle
# only_int_keys: dict = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}
# for k in only_int_keys:
#     if type(k) == str:
#         del only_int_keys[k]
#
# print(only_int_keys)  # => RuntimeError: dictionary changed size during
# iteration

# v 2
# Видалити всі ключі, значення яких починається з літери.
only_int_keys: dict = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}
copy_only_int_keys = only_int_keys.copy()
for k in only_int_keys:
    if type(k) is str:
        del copy_only_int_keys[k]

print(copy_only_int_keys)
