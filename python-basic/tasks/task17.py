import os.path


# task 1
# v1
def larger_string(text, n):
    result = ""
    for i in range(n):
        result = result + text
    return result


print(larger_string('abc', 2))
print(larger_string('.py', 3))


# v2
def larger_string(text, n):
    return text * n


print(larger_string('abc', 2))
print(larger_string('.py', 3))

# task 2
# v1
# num = int(input("Enter a number: "))
# if num % 2 > 0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")

# v2
num = int(input("\nEnter a number: "))
print("This is an odd number." if num % 2 > 0 else "This is an even number.\n")


# task 3
# v1
def list_count_4(nums):
    result = 0

    for n in nums:
        if n == 4:
            result = result + 1

    return result


print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))


# v2
def list_count_4(nums):
    return nums.count(4)


print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]), '\n')


# task 4
def substring_copy(text, n):
    rlen = 2

    if rlen > len(text):
        rlen = len(text)

    substr = text[:rlen]
    return substr * n


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3), '\n')


# task 5
def is_vowel(char):
    all_vowels = 'aeiou'
    return char.lower() in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))
print(is_vowel('A'))


# task 6
# v1
# def is_group_member(group_data, n):
#     for value in group_data:
#         if n == value:
#             return True
#     return False
#
#
# print(is_group_member([1, 5, 8, 3], 3))
# print(is_group_member([5, 8, 3], -1))


# v2
def is_group_member(group_data, n):
    if n in group_data:
        return True
    return False


print(is_group_member([1, 5, 8, 3], 0))
print(is_group_member([5, 8, 3], 8))


# task 7
def histogram(items):
    for n in items:
        print('*' * n)


histogram([0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0])

# task 8
numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953,
    345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
    687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831,
    445, 742, 717, 958, 743, 527
]

for x in numbers:
    if x == 237:
        print(x)
        break
    elif x % 2 == 0:
        print(x)

# task 9
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print("\nOriginal set elements:")
print(color_list_1)
print(color_list_2)
# v1
print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifference of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
# v2
print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1 - color_list_2)
print("\nDifference of color_list_2 and color_list_1:")
print(color_list_2 - color_list_1, '\n')


# task 10
def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Inputs must be integers!"
    return a + b


print(add_numbers(10, 20))
print(add_numbers(10, 20.23))
print(add_numbers('5', 6))
print(add_numbers('5', '6'))


# task 11
def personal_details(name, age, address):
    print(f"\nName: {name}\nAge: {age}\nAddress: {address}\n")


personal_details('Nadiia', 27, 'Poland, Krakow')

# task 12
# v1
print(os.path.isfile('task17.txt'))
print(os.path.isfile('task17.py'))
# v2
print(os.path.exists('task17.txt'))
print(os.path.exists('task17.py'))
# v3
try:
    my_file = open('task17.txt')
    print("File found!")
    my_file.close()
except FileNotFoundError:
    print("File not found!")
