import random
import secrets

# task 1
print("Generating 3 random integer number between 100 and 999 divisible by 5")

for num in range(3):
    # randrange(start, stop, step) - повертає випадково вибране
    # число з послідовності.
    print(random.randrange(100, 999, 5), end=', ')

# task 2
lottery_tickets_list = []
print("\ncreating 100 random lottery tickets")

for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

# Метод sample повертає випадкову вибірку елементів із послідовності.
# У першому параметрі методу вказуємо послідовність, у другому параметрі -
# кількість елементів, які ми хочемо вибрати випадковим чином.
winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)

# task 3
# Модуль secrets забезпечує доступ до найбезпечнішого джерела випадковості,
# яке надає операційна система. Він використовується для генерації
# криптографічно стійких випадкових чисел, придатних для управління такими
# даними, як паролі, автентифікація облікового запису, токени безпеки й
# пов'язані з ними секрети. Зокрема, secrets слід використовувати замість
# генератора псевдовипадкових чисел за замовчуванням у модулі random, який
# призначений для моделювання та симуляції, а не безпеки чи криптографії
secretsGenerator = secrets.SystemRandom()
# Клас secrets.SystemRandom() дає змогу створити екземпляр генератора, що
# використовує найбезпечніше джерело випадковості (ентропії) - ресурси
# операційної системи.
print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)
print("Secure random OTP is ", otp)

# task 4
name = 'python'
# Функція choice() з модуля random повертає випадковий елемент із переданої
# їй послідовності, у ролі якої може виступати рядок, список, кортеж або
# будь-яка інша колекція.
char = random.choice(name)
print("random char is ", char)

# Функція choices() модуля random повертає список елементів довжини k, обраних
# із послідовності population з перестановкою елементів. Інакше кажучи, функція
# використовується, коли потрібно вибрати кілька k випадкових елементів із
# заданої послідовності, елементи не зберігають первісний порядок.
# Параметри:
# population - послідовність (рядок, список тощо)
# weights=None - послідовність з відносними вагами,
# cum_weights=None - послідовність із кумулятивними вагами,
# k=1 - кількість обраних випадкових елементів.
chars = random.choices(name, k=2)
print("random 3 chars is ", chars)
