def find_second_largest(numbers):
    # Негативну нескінченність можна представити додаванням - до inf.
    largest = -float('inf')
    second_largest = -float('inf')
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

nums = [10, 15, 18, 20, 13, 19, 21]
second_largest_num = find_second_largest(nums)
print(f"The second largest number: {second_largest_num}")