# for
def remove_duplicates_v1(x):
    new_arr = []
    for el in x:
        if el not in new_arr:
            new_arr.append(el)
    return new_arr


# set
def remove_duplicates_v2(x):
    return list(set(x))


a = [1, 2, 3, 4, 3, 2, 1, 4, 5]
print(a)
print(remove_duplicates_v1(a))
print(remove_duplicates_v2(a))
