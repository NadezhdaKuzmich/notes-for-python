import decimal

# Декоратор у Python - функція, яка приймає як параметр іншу функцію (або клас)
# і повертає нову, модифіковану функцію (або клас), яка її замінює.
# Крім того, поняття функцій вищого порядку часто застосовується і для
# створення декораторів: часто потрібно, щоб декоратор приймав ще якісь
# параметри, крім модифікованого об'єкта. У такому разі створюється функція,
# що створює і повертає декоратор, а під час застосування декоратора замість
# вказівки імені функції-декоратора ця функція викликається.

# Приклад створення декоратора
def decorator(fn):
    """Приклад декоратора"""

    def decorated_fn(*args, **kwargs):
        """Модифікована функція"""

        print('Decorated function says:')
        fn(*args, **kwargs)  # виклик початкової функції
        print()

    return decorated_fn


@decorator
def hello():
    print('Hello!')


# Виклик декорованої функції
hello()


def cast_result(type_):
    """Приклад створення декоратора з параметром"""

    def cast_decorator(function):
        """Сам декоратор"""

        def decorated_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return type_(result)

        return decorated_function

    return cast_decorator


@cast_result(float)
def add(x, y):
    return x + y


print(add(2, 3))


@cast_result(repr)
@cast_result(decimal.Decimal)
def div(x, y):
    return x / y


print(div(3, 2))
