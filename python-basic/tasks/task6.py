name = input('Enter file: ')
text_file = open(f'data/{name}', 'r')

counts = dict()
for line in text_file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

big_count = None
big_word = None
for word, count in counts.items():
    if big_count is None or count > big_count:
        big_word = word
        big_count = count

print(big_word, big_count)
text_file.close()
