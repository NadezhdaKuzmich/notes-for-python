import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))
current_year = datetime.datetime.now().year

print(f"{name}, you will be 100 years old in {current_year - age + 100}!")
