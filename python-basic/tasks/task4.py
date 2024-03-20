# task 1
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [first + second for first in list1 for second in list2]
print(result)

# task 2
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = list(filter(None, list1))
print(result)

# task 3
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)