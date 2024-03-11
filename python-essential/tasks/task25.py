print("Print current and previous value and their sum in a range(10)")
previous_num = 0

for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Value", i, "Previous Value ", previous_num, " Sum: ",
          x_sum)
    previous_num = i
