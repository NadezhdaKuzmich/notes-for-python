import sys
import json

# task 1
print("Float value information: ", sys.float_info)
print("Integer value information: ", sys.int_info)
print("Maximum size of an integer: ", sys.maxsize, "\n")

# task 2
str1 = "A8238i823acdeOUEI"
print(any(i.islower() for i in str1))

# task 3
str1 = "122.22"
print("\nAdded trailing zeros:")
str1 = str1.ljust(8, "0")
print(str1)
str1 = str1.ljust(10, "0")
print(str1)

print("\nAdded leading zeros:")
str1 = "122.22"
str1 = str1.rjust(8, "0")
print(str1)
str1 = str1.rjust(10, "0")
print(str1, "\n")

# task 4
data = {'Alex': 1, 'Suresh': 2, 'Agnesa': 3}
json_string = json.dumps(data)
print(json_string)
