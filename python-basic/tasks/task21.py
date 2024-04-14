import sys
import json
import os.path
from timeit import default_timer
import struct

# task 1
print("Float value information: ", sys.float_info)
print("Integer value information: ", sys.int_info)
print("Maximum size of an integer: ", sys.maxsize, "\n")

# task 2
str1 = "A8238i823acdeOUEI"
print(any(i.islower() for i in str1))

# task 3
str1 = "122.22"
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, "0")
print(str1)
str1 = str1.ljust(10, "0")
print(str1)

print("\nAdded leading zeros:")
str1 = "122.22"
str1 = str1.rjust(8, "0")
print(str1)
str1 = str1.rjust(10, "0")
print(str1, "\n")

# task 4
data = {'Alex': 1, 'Suresh': 2, 'Agnesa': 3}
json_string = json.dumps(data)
print(json_string, "\n")

# task 5
var_list = ['a', 'b', 'c', 'd', 'e']
a, b, c, d, e = var_list
print(a, b, c, d, e, "\n", sep=", ")

# task 6
print(os.path.expanduser('~'), "\n")


# task 7
def timer(n):
    start = default_timer()
    sum_n = 0

    for num in range(1, n + 1):
        sum_n += num

    print(f"Sum: {sum_n}")
    print(default_timer() - start)


timer(5)
timer(15)

# task 8
# v1
a, b = [int(a) for a in input("\nInput the value of a & b: ").split(", ")]
print(f"The value of a & b are: {a=}, {b=}", "\n")
# v2
# x, y = map(int, input("\nInput the value of x & y: ").split(", "))
# print(f"The value of x & y are: {x=}, {y=}", "\n")

# task 9
d = {'Red': 'Green'}
(c1, c2), = d.items()
print(c1)
print(c2, "\n")

# task 10
print(struct.calcsize("P") * 8, "\n")

# task 11
# v1
print(isinstance(25, int))
print(isinstance("25", str), "\n")


# v2
def check_type(nums):
    if isinstance(x, tuple):
        return 'The variable x is a tuple'
    elif isinstance(x, list):
        return 'The variable x is a list'
    elif isinstance(x, set):
        return 'The variable x is a set'
    else:
        return 'Neither a list or a set or a tuple.'


x = ['a', 'b', 'c', 'd']
print(check_type(x))

x = {'a', 'b', 'c', 'd'}
print(check_type(x))

x = ('tuple', False, 3.2, 1)
print(check_type(x))

x = 100
print(check_type(x))

# v3
x = ('tuple', False, 3.2, 1)

if type(x) is list:
    print('x is a list')
elif type(x) is set:
    print('x is a set')
elif type(x) is tuple:
    print('x is a tuple')
else:
    print('Neither a list nor a set nor a tuple.')

print()


# task 12
def multiple(m, n):
    return m % n == 0


print(multiple(20, 5))
print(multiple(7, 2))
