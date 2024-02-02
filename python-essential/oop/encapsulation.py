# ● Інкапсуляція - ще одне з основних понять, на якому будується ООП. Вона
# потрібна для того, щоб організувати рівні доступу до різних архітектурних
# компонентів, які пише розробник.

# Є три можливі рівні доступу:
# 1. private (приватний)
# 2. protected (захищений)
# 3. public (публічний)

# Інкапсуляція - принцип, у якому користувач використовує лише публічну чи
# “інтерфейсну” частину класу і не вникає у його внутрішню реалізацію. Таким
# чином, програміст приховує певні дані, методи, атрибути від наступних
# користувачів.

# ● Інкапсуляція в Python відрізняється від її реалізації в інших мовах
# програмування і носить тут більш неявний характер. Якщо в інших мовах
# використовуються ключові слова на кшталт public, protected і private,
# то Python достатньо додати символ “_” (один символ нижнього підкреслення)
# перед іменем змінної або функції, щоб зробити її protected, а “__ ” (два
# символи нижнього підкреслення) щоб зробити private. Public є всі інші
# імена, без символів “_” перед ними.

# ● У даного підходу є свої переваги та недоліки. Перевагою, безумовно,
# є простота реалізації. Вам не потрібно використовувати ключові слова,
# а достатньо додати “_” або “__” перед ім'ям змінної або функції або
# взагалі не додавати. Недоліком є недосконалість даного підходу. Приватні
# змінні за фактом не є такими. Якщо в інших мовах програмування ви ніяк не
# зможете до них "доступитися" поза класом, то в Python, якщо у вас є клас
# A, у нього є атрибут self._x= 10, то після того, як ви створите об'єкт
# класу a = A(), то якщо ви зробите print(a.x) буде помилка, але якщо ви
# зробите print(a._A_x), то виведеться значення змінної х = 10

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account = BankAccount('Vadim', 10000, 'EK82S49R')
account.print_private_data()  # => Vadim 10000 EK82S49R


# print(account._name)  # => Якщо поле захищене до нього все одно можна
# отримати доступ за межами класу
# print(account._balance)
# print(account._passport)

# print(account.__name)  # => AttributeError: 'BankAccount' object has no
# attribute '__name'
# print(account.__balance)
# print(account.__passport)

# print(dir(account))
# print(account._BankAccount__balance)  # => 10000


# Законним способом працювати з приватними та захищеними змінними є
# використання таких функцій як getters та setters. Це спеціальні функції
# самого класу, які ви самі прописуєте та вирішуєте, як саме вони повинні
# повертати значення приватних/захищених змінних (getters, наприклад за
# паролем або просто так) та як встановлювати значення таких атрибутів (
# setters).
class BankAccount2:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Only number!')
        self.__balance = value


account2 = BankAccount2('Nadia', 5000)
account2.name = "Nadijka"
# print(account2.name)
# print(account2.get_balance())
# account2.set_balance(2000)
# print(account2.get_balance())

print(account2.balance)
account2.balance = 5999
print(account2.balance)


# account2.balance = 'Zero'
# account2.set_balance('Zero')  # => ValueError: Only number!


class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


user = User(name='Alex')
user.name = 'Bob'
print(user.name)


class User2:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Property was called")
        return self.__name


u2 = User2(name='Mike')
print(u2.name)


class Worker:
    RIGHTS = "Equal"
    SALARY_MAP = {
        "A": 100,
        "B": 200,
        "C": 500
    }

    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)

    @staticmethod
    def __get_salary(working_class):
        return Worker.SALARY_MAP.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


w1 = Worker('A')
print(w1.salary)

w2 = Worker('D')
print(w2.salary)


class TextProcessor:
    def __init__(self):
        self._punctuation = '.,!?;:*'

    def __is_punctuation(self, char):
        return char in self._punctuation

    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punctuation(char):
                continue
            clean_text += char
        return clean_text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is: {}".format(self.__clean_string))
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean_string = self.__text_loader.clean_string
            clean_texts.append(clean_string)
        return clean_texts


data_i = DataInterface()
data_texts = ['Hello, I am Nadiia *', 'Hey, what is the weather today ?']
clean_t = data_i.process_texts(data_texts)
print(clean_t)
