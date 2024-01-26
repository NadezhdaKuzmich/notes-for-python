# while:
counter = 5
while counter > 0:
    print('Iteration, counter =', counter)
    counter -= 1
print("-" * 20)

# range():
range(6)  # => range(0, 6) => [0, 1, 2, 3, 4, 5]

# for:
for number in range(6):
    print(number)
print("-" * 20)

# break:
counter = 10
while True:
    counter -= 1
    print(counter)
    if counter == 5:
        break
        # print("Текст після break не друкується! Всі операції після нього -
        # не спрацюють.")
print("-" * 20)

# continue
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print(counter)
print("-" * 20)

# Задачки:
# for number in range(102):
#     if number != 0 and number % 2 == 0:
#         print(number)
# print("-" * 20)

# word = "hello"
# answer = ""
# for char in word:
#     if char == "l":
#         answer += "s"
#     else:
#         answer += char
# print(answer)
print('hello'.replace('l', 's'))
print("-" * 20)

for num in reversed(range(100)):
    if num % 5 == 0:
        print(num)
        break

# for num in range(-99, 0):
#     if num % 5 == 0:
#         print(abs(num))
#         break
