import sys

# task 1
n = "246.2458"
print(float(n))
print(int(float(n)), '\n')

# task 2
for i in range(0, 10):
    print('*', end="")

print("\n")


# task 3
def eprint(*args, **kwargs):
    # sys.stderr - повідомлення про помилки та власні запити перекладача.
    print(*args, file=sys.stderr, **kwargs)


eprint("abc", "efg", "xyz", sep="--")
