# Приклад роботи з функціями як з об'єктами першого класу
# Створення посилання на об'єкт
out = print
out('Hello')


# Збереження посилань на функції в структурі даних
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


operations = {
    '+': add,
    '-': sub
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

# Приклад використання лямбда-виразів
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}

print(operations['+'](2, 1))
print(operations['-'](2, 1))


# Приклад замикання
def make_closure():
    variable = 42

    def closure():
        return variable

    return closure


fn = make_closure()
print(fn())
