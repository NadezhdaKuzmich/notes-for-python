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
show_employee('Kate')


# task 5
def outer_func(a, b):
    def addition(x, y):
        return x + y

    add_value = addition(a, b)
    return add_value + 5


result = outer_func(5, 20)
print(result)


# task 6
def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0


res = addition(10)
print(res)


# task 7
def display_student(name, age):
    print(name, age)


display_student('John', 21)
showStudent = display_student
showStudent('John', 21)

# task 8
print(list(range(4, 30, 2)))

# task 9
x = [4, 6, 8, 24, 12, 2]
print(max(x))
