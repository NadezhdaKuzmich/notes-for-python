import operator


def input_operation():
    operation = input('Enter operation (+, -, *, /, ^) or type "exit" '
                      'to quit: ')
    if operation == 'exit':
        exit()
        # Функція exit() - здійснює вихід з поточного програмного блоку.
    elif operation == '+':
        return operator.add
    elif operation == '-':
        return operator.sub
    elif operation == '*':
        return operator.mul
    elif operation == '/':
        return operator.truediv
    elif operation == '^':
        return operator.pow
    else:
        raise NotImplementedError('unsupported operation')


def main():
    while True:
        try:
            operation = input_operation()
            first_number = float(input('Enter first number: '))
            second_number = float(input('Enter second number: '))
            result = operation(first_number, second_number)
        except (ValueError, ArithmeticError, NotImplementedError) as error:
            print('Error:', error)
        else:
            print('Result:', result)
        finally:
            print()


if __name__ == '__main__':
    main()
