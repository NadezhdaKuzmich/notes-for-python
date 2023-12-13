type(False)  # => <class 'bool'>
type(True)  # => <class 'bool'>

# bool() # => true / false
bool(1)  # => true
bool(0)  # => false

# Оператори порівняння:
print(1 == 1)
print(1 != 2)
print(4 > 2)
print(4 < 5)
print(4 >= 4)
print(4 <= 5)

# Логічні оператори:
# and
yes = True
no = False
print(yes and no)  # => False
print(yes and yes)  # => True
# or
print(yes or no)  # => True
print(no or no)  # => False
# not
print(not no)  # => True
print(not yes)  # => False

# Оператори посвідчення особи:
a = 3
b = 4
str1 = 'Hello my dear friend Markus'
str2 = 'Hello my dear friend Markus'
print(a is a)  # => True
print(a is b)  # => False
print(a is not b)  # => True
print(str1 is str2)  # => False (порівнює id())

# Оператори членства:
print("python" in "I'm python developer")  # => True
print("js" not in "I'm python developer")  # => True
