import re
import math
import datetime

t = ("I want to be a professor, but only one thing I can solve is x=exp("
     "8)+sqrt(17)+log(5)")


def process(text):
    re_match = re.search('x=', text)
    print(re_match.span())

    equation = text[re_match.span()[1]:]
    print(equation)

    ops = {'exp': math.exp, 'sqrt': math.sqrt, 'log': math.log}
    actions = equation.split('+')
    print(actions)

    result = 0
    for action in actions:
        action = action.replace('(', ' ').replace(')', '')
        print(action)

        op, value = action.split(' ')
        result += ops[op](int(value))

    report = (f"Result = {result}; "
              f"Date {datetime.datetime.now().strftime('%d/%m/%y')}")
    print(report)


process(t)
