word = input('Enter word ')
print("Original String:", word)
size = len(word)

print("Print only even index chars")
for i in range(0, size, 2):
    print("index[", i, "]", word[i])
