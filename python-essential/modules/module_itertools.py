import itertools

combs = itertools.combinations([1, 2, 3, 4], 2)
print(list(combs))

print(list(itertools.combinations_with_replacement([1, 2, 3, 4], 2)))

permutations = itertools.permutations([1, 2, 3, 4], 2)
print(list(permutations))

print(list(itertools.accumulate([1, 2, 3, 4, 5])))

print(list(itertools.accumulate([1, 2, 3, 4, 5], lambda a, b: a - b)))

print(list(itertools.filterfalse(lambda x: x % 2, range(11))))
