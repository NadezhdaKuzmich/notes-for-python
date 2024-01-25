import math

SOME_CONSTANT = 1  # UPPERCASE FOR CONST

# 1 space
value1 = {'test': 1, 'key': 2, 'value': 3}
value2 = [1, 2, 3, 4]
value3 = pow(2, 10)


# 2 spaces
class User:
    # 1 space / without space
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # 1 space
    def full_name(self):
        """Returns full name of user using first_name, last_name concat."""
        return ''.format(self.first_name, self.last_name)

    # 1 space
    # short name function
    def short_name(self):
        """
        Returns short name of user using first_name, last_name's first letter.
        Example:
            # >>> self.short_name()
        :return: str
        """
        return ''.format(self.first_name, self.last_name[0])

    # 1 space
    def send_mail(self):
        """instance.send_mail() -> list"""
        return ''.format(self.first_name, self.last_name[0])


# 2 spaces
tuple1 = 1,  # unclear
tuple2 = (1,)  # without whitespace

result1 = '1234567'[1:3]
result3 = '1234567'[1 + tuple1[0]: 5 + 10]

user1 = User('t1', 't2')
user1.send_mail()
value1['key'] = tuple1[0]


# 2 spaces
def some_function(argument: str) -> str:
    return argument[:10]


# 2 spaces
value4 = dict(t=1, p=2)

if value4['t'] == 1:
    some_function('*' * 10)

some_function('0' * 10)
some_function('+' * 10)
some_function('-' * 10)

values = [
    1,
    902,
    312,
    431,
    521,
    619,
    722,
    8209,
    912
]


# bad practice
# class Super_Instructor:
#     def testName(self):
#         pass
#
#     def testNameValue(self):
#         pass
#
#     def TestNameValue(self):
#         pass
#
#     def Test_Name_Value(self):
#         pass


# best practice
# class SuperInstructor:
#     def test_name(self):
#         pass
#
#     def test_name_value(self):
#         pass
#
#     def test_name_value1(self):
#         pass
#
#     def test_name_value2(self):
#         pass


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    return None


def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)


# if type(value1) is type(value2):
#     print('Done')

if isinstance(1, int) and isinstance(2, int):
    print('Done')
