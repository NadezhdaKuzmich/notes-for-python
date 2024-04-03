import sys
import datetime
from math import pi

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
values = input("Input some comma-separated numbers: ")
some_list = values.split(",")
some_tuple = tuple(some_list)
print('List : ', some_list)
print('Tuple : ', some_tuple)
