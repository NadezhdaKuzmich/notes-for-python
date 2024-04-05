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
num = int(input("Enter a number: "))
print("This is an odd number." if num % 2 > 0 else "This is an even number.")


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
print(list_count_4([1, 4, 6, 4, 7, 4]))


# task 4
def substring_copy(text, n):
    rlen = 2

    if rlen > len(text):
        rlen = len(text)

    substr = text[:rlen]
    return substr * n


print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))


# task 5
def is_vowel(char):
    all_vowels = 'aeiou'
    return char.lower() in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))
print(is_vowel('A'))
