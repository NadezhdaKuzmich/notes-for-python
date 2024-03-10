def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x


print("Removing characters from a string")
print(remove_chars("Python", 2))
print(remove_chars("JavaScript", 4))
