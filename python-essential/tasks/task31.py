list1 = [10, 20, 30, 40, 50]

# v1:
new_list = reversed(list1)
for item in new_list:
    print(item)

# v2:
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])
