# []
my_list = [1, 2, 3, 'hello']
print(my_list)
print(my_list[3])

list_empty = []
# print(list_empty)  # => []

# list()
list_empty2 = list()
# print(list_empty2)  # => []
# Не можна poбити так: list(1, 2, 3)
list2 = list('hello')
print(list2)  # => ['h', 'e', 'l', 'l', 'o']

# len()
print(len(list2))  # => 5
# print(list2[5])  # => IndexError: list index out of range

# [-1]
print(list2[-2])  # => l
list2 += '!'
print(list2)  # => ['h', 'e', 'l', 'l', 'o', '!']

# Зрізи списків:
# Синтаксис: my_list[start:stop:step]
# - Start – індекс, з якого починається підмножина.
# - Stop – індекс, перед яким закінчиться підмножина (якщо він виходить за межі розміру списку - не буде помилки):
# print(list2[2:50:2])  # => ['l', 'o']
# - Step – крок вибору елементів (за замовчувавання "без вказання" - 1).
# list2[1:4:0] => ValueError: slice step cannot be zero
# list2[1:4] === list2[1:4:1]
print(my_list[:])  # => [1, 2, 3, 'hello'] (робить копію)

print(list2[2:5:2])  # => ['l', 'o']

my_list2 = [1, 2, 3, 'hello', 'hi', 'python']
print(my_list2[-1:-6:-2])  # => ['python', 'hello', 2]
