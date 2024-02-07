import collections

# from collections import Counter

a = [1, 1, 2, 3, 3, 3]
counts = collections.Counter(a)
# counts = Counter(a)
print(counts)

dict_of_lists = collections.defaultdict(list)
for value in range(1, 13):
    if value % 2 == 0:
        dict_of_lists['even'].append(value)
    else:
        dict_of_lists['odd'].append(value)
print(dict(dict_of_lists))

counts = collections.defaultdict(int)
for value in a:
    counts[value] += 1
print(counts)

d = collections.deque([1, 2, 3])
d.popleft()
print(d)
d.append(4)
print(d)
d.appendleft(0)
print(d)
d.pop()
print(d)
