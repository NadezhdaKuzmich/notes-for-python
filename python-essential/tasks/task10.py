def char_frequency(str1):
    dictionary = {}
    for n in str1:
        keys = dictionary.keys()

        if n in keys:
            dictionary[n] += 1
        else:
            dictionary[n] = 1

    return dictionary


print(char_frequency('hello world'))
