from datetime import datetime, timedelta
from time import gmtime, strftime

# task 0
# v1
# Print date and time
print('task 0:')
print(datetime.now())
# only time
print(datetime.now().time())

# v2
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

# task 1
date_string = "Feb 28 2020 2:40PM"
# Метод strptime() створює об'єкт datetime із заданого рядка.
# %b - скорочена назва місяця.
# %d - день місяця у вигляді десяткового числа.
# %Y - рік із зазначенням століття.
# %I - час (12-годинний формат) у вигляді десяткового числа з додаванням нуля.
# %M - хвилини у вигляді десяткового числа, доповненого нулями.
# %p - регіональний стандарт: AM або PM.
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print('\ntask 1:')
print(datetime_object)

# task 2
given_date = datetime(2024, 3, 22)
print('\ntask 2:')
print("Given date")
print(given_date)

# timedelta - різниця між двома моментами часу, з точністю до мікросекунд.
days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("\nNew Date")
print(res_date)

now = datetime.now()
delta = timedelta(days=7, hours=2, seconds=20)
then = now + delta
print("\nNew Date 2")
print(then)

# task 3
iven_date = datetime.now()
print('\ntask 3:')
print("Given date is")
# strftime() повертає рядок, що представляє дату і час, використовуючи об'єкт
# date, time або datetime.
print(given_date.strftime('%A %d %B %Y'))

# task 4
given_date = datetime(2024, 3, 24)
print('\ntask 4:')
# to get weekday as integer
# weekday() - день тижня у вигляді числа, понеділок - 0, неділя - 6
print(given_date.weekday())
# datetime.isoweekday() - день тижня у вигляді числа, понеділок - 1, неділя - 7
print(given_date.isoweekday())
# to get the english name of the weekday
print(given_date.strftime('%A'))

# task 5
given_date = datetime(2024, 3, 22, 19)
print('\ntask 5:')
print("Given date")
print(given_date)

days_to_add = 7
res_date = given_date + timedelta(days=days_to_add, hours=12)
print("\nNew Date")
print(res_date)
