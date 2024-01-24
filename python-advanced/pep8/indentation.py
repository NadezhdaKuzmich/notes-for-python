# Don't use tab
def foo(value):
    # 4 spaces
    if value == 10:
        # 4 spaces
        raise ValueError('Incorrect value: {}'.format(value))
    return pow(10, value)


# 2 spaces
def bar(value):
    return pow(10, value)
