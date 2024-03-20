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

# task 4
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

# task 5
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)

# task 6
list1 = [5, 20, 15, 20, 25, 50, 20]

# v1
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]


result = remove_value(list1, 20)
print(result)


# v2
def remove_value2(sample_list, val):
    while val in list1:
        sample_list.remove(val)
    return sample_list


result = remove_value2(list1, 20)
print(result)

# task 7
list1 = ["M", "na", "i", "Na"]
list2 = ["y", "me", "s", "diia"]
list3 = [i + j for i, j in zip(list1, list2)]
print(" ".join(list3))

# task 8
numbers = [1, 2, 3, 4, 5, 6, 7]

result = []
for num in numbers:
    result.append(num * num)

print(result)
