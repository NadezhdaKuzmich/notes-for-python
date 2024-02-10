import this


# Beautiful is better than ugly.

# bad example
def MyLongNameIsForToDoSomething(a, b, c, d, e, f, g, x, y, t, v):
    pass


# good example
def get_time():
    return "time is ..."


# Explicit is better than implicit.
# bad
def get_args(a, b):
    s = sum([a, b])
    squares = [x ** 2 for x in [s, s + 2, s + 5]]
    print(squares, 'hello')
    return squares[:1]


# good
def get_sum(a, b):
    return sum([a, b])


def get_squares(sum_result):
    return [x ** 2 for x in [sum_result, sum_result + 2, sum_result + 5]]


def print_result(result):
    print(result, 'hello')


def main(a, b):
    s = get_sum(a, b)
    squares = get_squares(s)
    print_result(squares)
    return squares[:1]


main(2, 4)
