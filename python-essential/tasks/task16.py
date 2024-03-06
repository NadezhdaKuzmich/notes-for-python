# Сортування бульбашкою(Bubble Sort) - це простий алгоритм, який порівнює кожну
# пару сусідніх елементів у списку і міняє їх місцями, якщо вони розташовані в
# неправильному порядку.
def bubble_sort(numbers):
    n = len(numbers) - 1

    for i in range(n):
        for j in range(n - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


nums = [7, 6, 5, 3, 2, 8, 1, 9, 4]
bubble_sort(nums)
print(nums)
