# Limit the length of the string to a maximum of 79 characters.
long_variable1 = 1
long_variable2 = 2
long_variable3 = 3
long_variable4 = 4
long_variable5 = 5
long_variable6 = 6

income1 = (long_variable1 + long_variable2 + (long_variable3 - long_variable4) - long_variable5 - long_variable6)

income2 = (long_variable1 +
           long_variable2 +
           (long_variable3 - long_variable4) -
           long_variable5 -
           long_variable6)

# best practice
income3 = (long_variable1
           + long_variable2
           + (long_variable3 - long_variable4)
           - long_variable5
           - long_variable6)

print(income1, income2, income3)
