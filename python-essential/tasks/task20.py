def reverse_v1(text):
    split_arr = text.split()
    result = []
    for word in split_arr:
        result.insert(0, word)
    return " ".join(result)


def reverse_v2(text):
    split_arr = text.split()
    return " ".join(split_arr[::-1])


def reverse_v3(text):
    split_arr = text.split()
    return " ".join(reversed(split_arr))


def reverse_v4(text):
    split_arr = text.split()
    split_arr.reverse()
    return " ".join(split_arr)


test1 = input("Enter a sentence: ")
print(reverse_v1(test1))
print(reverse_v2(test1))
print(reverse_v3(test1))
print(reverse_v4(test1))
