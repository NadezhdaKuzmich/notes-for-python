# Поліморфізм - різна поведінка одного й того методу в різних класах.

# Поліморфізм досягається шляхом перевантаження чи перевизначення методу.
# Таким чином досягається додаткова гнучкість програми. А також, значно
# скорочується дублювання коду, що дуже важливо для хорошого та
# підтримуваного проекту.

# Поліморфізм досягається 2 методами:
# - Перевантаження:
# Перевантаження методу або overloading - це заздалегідь визначений алгоритм
# усередині самого методу, завдяки якому при різній комбінації задіяних
# аргументів функція веде себе по-різному. Перевантажуючи метод,
# ви заздалегідь визначаєте аргументи, у разі використання яких, функція
# поводиться інакше.
class Base:
    def __init__(self, a):
        self.__a = a

    def print_a(self, square=False, multiplier=None):
        if square and not multiplier:
            print(self.__a ** 2)
        elif not square and multiplier:
            print(self.__a * multiplier)
        elif square and multiplier:
            print((self.__a ** 2) * multiplier)
        else:
            print(self.__a)


base = Base(4)
base.print_a(True)  # => 16
base.print_a(False, 2)  # => 8
base.print_a(True, 2)  # => 32
base.print_a()  # => 4


# - Перевизначення:
# Перевизначаючи метод, у дочірнього класу ви можете повністю змінити його.
# Ви не зможете перевизначити аргументи методу дочірнього класу (тільки якщо
# це не конструктор). Але ви можете змінювати внутрішню логіку самого методу
# (це і є перевизначення або overwriting).
class Multiplier:
    def __init__(self, a):
        self._a = a

    def print_a(self, x):
        print(self._a * x)


class Exponent(Multiplier):
    def print_a(self, x):
        print(self._a ** x)


m = Multiplier(5)
m.print_a(2)  # => 10
e = Exponent(4)
e.print_a(2)  # => 16


# Приклади:
class Car:
    def __init__(self, name):
        self._speed_name_map = {
            "BMW": 250,
            "Mercedes": 350
        }
        self._max_speed = self._define_max_speed(name)

    def _define_max_speed(self, name):
        return self._speed_name_map.get(name, 0)

    def distance_on_max_speed(self, distance):
        if self._max_speed == 0:
            print(
                f"Speed = 0, select valid car "
                f"brand: {list(self._speed_name_map.keys())}"
            )
            return 0
        return distance / self._max_speed


car1 = Car('BMW')
car2 = Car('Mercedes')
car3 = Car('ABC')

print(car1.distance_on_max_speed(100))
print(car2.distance_on_max_speed(100))
print(car3.distance_on_max_speed(100))


class Animal:
    def __init__(self, name):
        self._name = name

    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        print("Meow")


class Dog(Animal):
    def voice(self):
        print("Bark")


animal = Animal('?')
cat = Cat('Sarah')
dog = Dog('Rex')
animal.voice()
cat.voice()  # => Meow
dog.voice()  # => Bark


class Animal2:
    def __init__(self, name):
        self._name = name

    def voice(self):
        if self._name == 'cat':
            print('Meow')
        elif self._name == "dog":
            print('Bark')
        else:
            print("...")


cat = Animal2('cat')
dog = Animal2('dog')
dinosaur = Animal2('dinosaur')
cat.voice()  # => Meow
dog.voice()  # => Bark
dinosaur.voice()  # => ...


class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length


class Square(Parallelogram):
    def get_area(self):
        return self._width * self._width


p = Parallelogram(2, 3)
s = Square(2, 3)
print(p.get_area())  # => 6
print(s.get_area())  # => 4


def function(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


print(function({1, 5, 3}, 4))  # => {1, 3, 4, 5}
print(function([1, 5, 3, 4], 6))  # => [1, 5, 3, 4, 6]
print(function('hel', 'lo'))  # => hello

# ПОГАНИЙ ПРИКЛАД:
# class Messenger:
#     def __init__(self, connection):
#         self._connection = connection
#
#     def send_message(self, text, option=None):
#         self._connection.send(text)
#
# class ExtendedMessenger(Messenger):  # Bad example !
#     def send_message(self, text, option=None):
#         if option == 'message':
#             self._connection.send(text)
#         elif option == 'image':
#             self._connection.send(text)
#         elif option == 'math':
#             print('2+2=4')
#         else:
#             print('...')
