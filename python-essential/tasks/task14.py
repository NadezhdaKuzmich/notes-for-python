def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers


nums = [1, 2, 3, 1, 2, 3, 4, 5, 4, 5]
unique_nums = remove_duplicates(nums)
print(unique_nums)
