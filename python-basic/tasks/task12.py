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

for k in keys:
    res.update({k: sample_dict[k]})
    
print(res)
