# Словники – це впорядковані колекції формату ключ:значення. Значенням може
# бути будь-який об'єкт, ключем може бути лише незмінний об'єкт.

# Синтаксис словників: { ‘key’ : ‘value’ }
# Де key – це ключ, за яким доступний елемент value. Для того щоб отримати наше
# значення по ключу, достатньо після назви словника в квадратних дужках вказати
# назву ключа. Також можна використовувати метод get(), який у разі відсутності
# елемента за таким ключем поверне None.

example_dict = {
    "key": "value"
}

# Ключі мають бути унікальними
# example_dict = {
#     'hello': 'world',
#     'hello': 'everybody',
# }
# print(example_dict)  # => {'hello': 'everybody'}

# Створення списків:
# v1 { }
my_dict = {
    'name': 'Nadia',
    'age': 27
}
print('v1:', my_dict)

# v2 (список списків)
my_dict = dict([['name', 'Nadia'], ['age', 27]])
print('v2:', my_dict)

# v3 (список (key, value))
my_dict = dict([('name', 'Nadia'), ('age', 27)])
print('v3:', my_dict)

# v4 (за допомогою аргументів)
my_dict = dict(name="Nadia", age=27)  # Але таким чином не можна додати ключ
# з типом int (числа) my_dict2 = dict(18="hi", 32='by')
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print('v4:', my_dict)

# get value from dict
print(my_dict["name"])  # => Nadia
# print(example_dict["key_no_exist"])  # => KeyError: 'key_no_exist'

print(my_dict.get("age"))  # => 27
print(example_dict.get("key_no_exist"))  # => None
print(my_dict.get("age", 0))  # => 27
print(example_dict.get("key_no_exist", "Doesn't exist"))  # => Doesn't exist

# empty dictionary
# empty_dict = {}
city_dict = dict()

# put values in dict
city_dict['Kharkiv'] = 1654
city_dict['Chuhuiv'] = 1638
print(city_dict)

# dictionaries support
city_dict['Kharkiv'] = {'Year of foundation': 1654, 'Main rivers': ['Kharkiv',
                                                                    'Lopan']}
print(city_dict)
print('~' * 40)

# for in dict
# v1
for city in city_dict:
    print('v1', city, city_dict[city])
print('~' * 40)

# v2
for city in city_dict:
    print(f'v2: {city}: {city_dict[city]}')
print('~' * 40)

# v3
for key, value in city_dict.items():
    # print(f'v3: {key}: {value}')
    print(f'v3: {key=} {value=}')  # => ... key='Chuhuiv' value=1638
print('~' * 40)

# del
del city_dict['Chuhuiv']
print(city_dict)
