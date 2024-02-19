# simple examples
try:
    x = 2 / 0
except ZeroDivisionError:
    print('Division by zero detected')

try:
    x = 3 / 0
except:
    pass

print('Program flow goes further')

try:
    try:
        raise ValueError('Incorrect value')
    except ZeroDivisionError:
        print('Division by zero')
except Exception as e:
    print(e)

try:
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception:', error)
        raise
except ValueError:
    print('ValueError detected')


# my own error
class MyException(Exception):
    # def __str__(self):
    #     return 'My error'
    pass


try:
    raise MyException("My error")
except MyException as e:
    print(e)
except Exception:
    print('Some exception')


# V1
# def divide_numbers():
#     loop = True
#     while loop:
#         try:
#             first_number = float(input('First number: '))
#             second_number = float(input('Second number: '))
#             print('Result:', first_number / second_number)
#             loop = False
#         except (ValueError, ZeroDivisionError) as error:
#             print('Error:', error)
#             print('Please try again')
#             print()
#             loop = True

# V2
def divide_numbers():
    while True:
        try:
            first_number = float(input('First number: '))
            second_number = float(input('Second number: '))
            result = first_number / second_number
        except (ValueError, ZeroDivisionError) as error:
            print('Error:', error)
            print('Please try again')
            print()
        else:
            print('Result:', result)
            break


# finally
def function_that_may_fail():
    response = None
    while response != 'y' and response != 'n':
        response = input('Raise an exception? (y/n) ')
    if response == 'y':
        raise Exception


try:
    function_that_may_fail()
except:
    print('Exception handler')
finally:
    print('Finally block')

# try:
#     2 / 0
# finally:
#     print('Finally block is always executed')

if __name__ == '__main__':
    divide_numbers()


# errors in classes
class MyClass(object):
    def __del__(self):
        raise ZeroDivisionError

# print('Creating object')
# obj = MyClass()
# print('Deleting object')
# del obj
# print('Done')
