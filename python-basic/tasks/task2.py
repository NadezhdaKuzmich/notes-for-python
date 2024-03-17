# task 1
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")
print()

# task 2
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

# task 3
str1 = "PYthON"
print('Original String:', str1)
lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)


# task 4
def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    print(f"chars: {char_count}; digits: {digit_count}; "
          f"symbols: {symbol_count}.")


string = "P@yt2h&#o5n"
print("Total counts of chars, digits, and symbols:")
find_digits_chars_symbols(string)
