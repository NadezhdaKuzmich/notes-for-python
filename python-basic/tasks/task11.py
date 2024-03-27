# task 1
def print_info(name, age):
    print(f'My name is {name}. I\'m {age}.')


print_info('Nadiia', 27)


# task 2
def print_args(*args):
    for i in args:
        print(i)


print_args(1, 2, 3, 4)
print_args(5, 6)


# task 3
# v1
def calculation1(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


res = calculation1(2, 3)
print(res)


# v2
def calculation2(a, b):
    return a + b, a - b


add, sub = calculation2(3, 2)
print(add, sub)


# task 4
def show_employee(name, salary=9000):
    print(f'Name: {name}. Salary: {salary}.')


show_employee('John', 12000)
show_employee("Kate")
