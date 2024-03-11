def first_last_same(number_list):
    print("Given list:", number_list)

    if number_list[0] == number_list[-1]:
        return True
    else:
        return False


numbers1 = [1, 2, 3, 4, 1]
print("Result is", first_last_same(numbers1))

numbers2 = [7, 6, 3, 7, 2]
print("Result is", first_last_same(numbers2))
