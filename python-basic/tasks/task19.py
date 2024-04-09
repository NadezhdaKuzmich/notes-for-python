from __future__ import print_function
import sys
import time

# task 1
n = '246.2458'
print(float(n))
print(int(float(n)), '\n')

# task 2
for _ in range(0, 10):
    print('*', end='')

print('\n')


# task 3
def sum_of_n_numbers(num):
    start_time = time.time()
    s = 0

    for i in range(1, num + 1):
        s = s + i

    end_time = time.time()
    return s, end_time - start_time


print("Time to sum of 1 to 5 and required time to calculate is:",
      sum_of_n_numbers(5))

print("\nTime to sum of 1 to 10 and required time to calculate is:",
      sum_of_n_numbers(10))

# task 4
nums = [7, 12, 4]
a1 = min(nums)
a3 = max(nums)
a2 = sum(nums) - a1 - a3
print("\nNumbers in sorted order:", a1, a2, a3)

# task 5
print("\nPython Copyright Information:")
print(sys.copyright, "\n")


# task 6
def eprint(*args, **kwargs):
    # sys.stderr - повідомлення про помилки та власні запити перекладача.
    print(*args, file=sys.stderr, **kwargs)


eprint('abc', 'efg', 'xyz', sep='--')
