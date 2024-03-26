# task 1
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# res = num1 * num2
# print("Multiplication is", res)

# task 2
print('My', 'name', 'is', 'Nadiia', sep=' ** ')

# task 3
num = 8
# '%o' - число у вісімковій системі числення.
print('%o' % num)

# task 4
num = 3.141592654
# .2 - вказівка того, що виводиться 2 знаки після '.';
# f - вказівка того, що виводиться речове число в десятковому поданні.
print('%.2f' % num)

# task 5
numbers = []
for i in range(1, 6):
    item = float(input(f"Enter number at location {i}: "))
    numbers.append(item)

print("User List:", numbers)
