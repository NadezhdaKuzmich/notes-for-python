# Структури даних у Python – це способи організації та зберігання даних у
# пам'яті комп'ютера.
# Структури даних – це, власне, і є структури, які можуть зберігати деякі
# дані разом. Іншими словами, вони використовуються для зберігання
# пов'язаних даних. У Python існують чотири вбудовані структури даних:
# список, кортеж, словник та множина.
# Комбінувати можна майже будь-які структури даних між собою, створюючи тим
# самим складні та комплексні об'єкти. Наприклад, ви можете зробити список
# словників або зробити словник зі списками словників, де будуть списки
# рядків і т.д.
user = {
    "name": "JohnDoe",
    "info": {
        "basic": {
            "age": 25,
            "salary": 5000
        },
        "additional": {
            "study": "mathematics",
            "family": "married"
        },
        "special": {
            "projects": [
                {"name": "quantum_computer", "stage": "in_progress"},
                {"name": "laser_gun", "stage": "in_production"}
            ]
        }
    }
}


def get_data(data_dict, keys):
    data = data_dict
    for key in keys:
        data = data[key]
    return data


print(get_data(user, ['info', 'special', 'projects', 0]))


def get_data_rec(data_dict, keys, index=0):
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index + 1)
    return data_dict


print(get_data(user, ['info', 'special', 'projects', 1]))
print(get_data_rec(user, ['info', 'special', 'projects', 1, 'name']))


def func(index, count):
    return {
        "ID": index,
        "values": ["{}_{}".format(index, value) for value in range(count)]
    }


f = func(1, 3)
print(f)


def generate(count):
    return [func(i, j) for i, j in zip(range(count), list(range(count))[::-1])]


r = generate(4)
print(r)

f = [value for sublist in r for value in sublist['values']]
print(f)
