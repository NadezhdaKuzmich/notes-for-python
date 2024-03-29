# task 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# v1
res_dict = dict(zip(keys, values))
print(res_dict)

# v2
res_dict = dict()
# dict.update([other]) - оновлює словник, додаючи пари (ключ, значення) з
# other. Наявні ключі перезаписуються.
for i in range(len(keys)):
    res_dict.update({keys[i]: values[i]})
print(res_dict)

# task 2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

# v1
# Оператор ** використовується для пакування та розпакування словників.
# У разі використання перед словником під час виклику функції оператор **
# розпаковує пари ключ-значення словника в аргументи ключових слів, що можуть
# бути передані у функцію:
dict3 = {**dict1, **dict2}
print(dict3)

# v2
# dict.copy() повертає неглибоку копію словника:
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

# task 3
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sample_dict['class']['student']['marks']['history'])

# task 4
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# dict.fromkeys(seq[, value]))
# - створює словник із ключами з seq і значенням value (за замовчуванням None).
# - це швидкий і зручний спосіб створення словника без використання зайвих
# ітерацій і створення об'єктів.
res = dict.fromkeys(employees, defaults)
print(res)
print(res["Kelly"])

# task 5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]

# v1
new_dict = {key: sample_dict[key] for key in keys}
print(new_dict)

# v2
res = dict()

for key in keys:
    res.update({key: sample_dict[key]})
print(res)

# task 6
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

# v1
# dict.pop(key, default) - видаляє ключ і повертає значення. Якщо ключа немає,
# повертає default (за замовчуванням кидає виняток).
for key in keys:
    sample_dict.pop(key)
print(sample_dict)

# v2
sample_dict = {key: sample_dict[key] for key in sample_dict.keys() - keys}
print(sample_dict)

# task 7
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')

# task 8
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# task 9
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
# У функціях min() і max() можна вказати необов'язковий іменний параметр key.
# Йому присвоюється одноаргументна функція, яка виконує якусь попередню дію над
# елементами списку:
print(min(sample_dict, key=sample_dict.get))

# task 10
sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)
