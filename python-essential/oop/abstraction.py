# Абстракція - це спосіб представити кінцевий продукт таким чином, щоб користувачеві не потрібно було знати,
# як саме продукт працює, але користувач міг би їм легко користуватися.
# Основна ідея полягає в тому, щоб відокремити спосіб використання складових об'єктів даних від деталей їх
# реалізації у вигляді більш простих об'єктів..

# Абстракція в ООП - це приховування складності реалізації програмного продукту від кінцевого користувача шляхом
# створення простих і зрозумілих інтерфейсів (мова про так звані класи).  Основну ідею абстракції можна легко
# переплутати з інкапсуляцією. Адже приховування даних користувача з'являється в обох визначеннях. У разі
# інкапсуляції – це просте приховування атрибутів та методів, а абстракція – це приховування цілих класів чи
# груп класів шляхом побудови архітектури програмного продукту (саме за рахунок ООП).
class Core:
    def __init__(self):
        self._types = {
            "A": 100,
            "B": 300
        }

    def get_salary(self, class_name):
        return self._types.get(class_name, 0)


class AccountingInterface:
    def __init__(self, data):
        self._core = Core()
        self._database = data

    def get_salary(self, name):
        class_of_employee = self._database.get(name)
        salary = self._core.get_salary(class_of_employee)
        return salary


db = {"John": "A", "Mike": "B"}
interface = AccountingInterface(data=db)
print(f"John's salary is: {interface.get_salary(name="John")}")
print(f"Mike's salary is: {interface.get_salary('Mike')}")


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __convert_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parse(self, expression):
        packed_values = tuple(expression.split(' '))
        if len(packed_values) < 3:
            print("Wrong indentation, check your expression")
            return 0, 0, '+'
        a, op, b = packed_values
        return self.__convert_type(a), self.__convert_type(b), op


class Core:
    def __init__(self):
        self._parser = Parser()
        self._functions = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }

    def calculate(self, expression):
        a, b, op = self._parser.parse(expression)
        result = self._functions.get(op)(a, b)
        return result


class Interface:
    def __init__(self):
        self._core = Core()

    def run_calculator(self):
        while True:
            print("Enter your expression: eg. '2 + 2' ")
            expression = input()
            result = self._core.calculate(expression)
            print(f"Result: {result}")
            print("=" * 10)


if __name__ == "__main__":
    calculator = Interface()
    calculator.run_calculator()
