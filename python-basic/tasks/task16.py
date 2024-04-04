import sys
import datetime
from math import pi
import calendar
from datetime import date

# task 1
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp "
      "above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, "
      "twinkle, little star, \n\tHow I wonder what you are!")

# task 2
# Напишіть програму, щоб дізнатися, яку версію Python ви використовуєте.
print("\nPython version")
print(sys.version)
print("Version info.")
print(sys.version_info)

# task 3
now = datetime.datetime.now()
print("\nCurrent date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# task 4
r = float(input("\nInput the radius of the circle : "))
area = pi * r ** 2
print(f"The area of the circle with radius {r} is: {area}")

# task 5
values = input("\nInput some comma-separated numbers: ")
some_list = values.split(",")
some_tuple = tuple(some_list)
print('List : ', some_list)
print('Tuple : ', some_tuple)

# task 6
filename = input("\nInput the Filename: ")
f_extns = filename.split(".")
# repr() повертає формальне строкове представлення зазначеного об'єкта.
print("The extension of the file is : " + repr(f_extns[-1]))

# task 7
color_list = ["Red", "Green", "White", "Black"]
print("\n%s %s" % (color_list[0], color_list[-1]))

# task 8
# v1
# a = input("\nInput an integer: ")
# n1 = int("%s" % a)
# n2 = int("%s%s" % (a, a))
# n3 = int("%s%s%s" % (a, a, a))
# print(n1 + n2 + n3)

# v2
a = input("\nInput an integer: ")
n1 = int(a)
n2 = int(a * 2)
n3 = int(a * 3)
print(n1 + n2 + n3)

# task 9
# A docstring is a string literal that occurs as the first statement in a
# module, function, class, or method definition. Such a docstring becomes the
# __doc__ special attribute of that object.
print(f'\n{abs.__doc__}')

# task 10
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

# task 11
f_date = date(2024, 3, 2)
l_date = date(2024, 4, 1)
delta = l_date - f_date
# days - повертає кількість днів
print(delta.days)


# task 12
def new_string(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text


print(new_string("Array"))
print(new_string("IsEmpty"))
