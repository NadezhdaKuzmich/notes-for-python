import random
import secrets
import string
import time

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


# task 5
def random_string(string_length):
    # Константне перерахування літер із набору ASCII у верхньому та нижньому
    # регістрах. Включає літери, визначені в константах ascii_uppercase й
    # ascii_lowercase.
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(string_length))


print("Random String is ", random_string(6))


# task 6
def random_password():
    # string.digits: '0123456789'
    # string.punctuation: рядок ASCII символів, які вважаються розділовими
    # знаками в локалі мови C: !"#$%&'()*+,-./::;<=>?@[\]^_{|}~
    random_source = string.ascii_letters + string.digits + string.punctuation

    # Функція sample() модуля random повертає список довжини k випадкових
    # елементів, обраних із послідовності або множини population. Початкова
    # послідовність population залишається незмінною.
    password = random.sample(random_source, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    password_list = list(password)

    # Клас random.SystemRandom() - альтернативні клас для випадкових чисел,
    # який бере випадкові числа не з вбудованого алгоритму, а з системного
    # os.urandom.
    # Функція shuffle() модуля random перемішує елементи змінюваної
    # послідовності (список) на місці у випадковому порядку.
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password


print("Password is ", random_password())

# task 7
# random.random() - випадкове число від 0 до 1.
num1 = random.random()
print("First Random float is ", num1)

# random.uniform(A, B) - випадкове число з плаваючою крапкою, A ≤ N ≤ B
# (або B ≤ N ≤ A).
num2 = random.uniform(9.5, 99.5)
print("Second Random float is ", num1)
num3 = num1 * num2
print("Multiplication is ", num3)

# task 8
# Функція secrets.token_hex() повертає випадковий текстовий рядок у
# шістнадцятковому форматі. Рядок містить nbytes випадкових байтів, кожен
# байт перетворюється на дві шістнадцяткові цифри.
print("Random secure Hexadecimal token is ", secrets.token_hex(64))

# Функція secrets.token_urlsafe() повертає випадковий URL-безпечний текстовий
# рядок, що містить nbytes випадкових байтів. Текст у кодуванні Base64, тому в
# середньому кожен байт дає приблизно 1,3 символу.
print("Random secure URL is ", secrets.token_urlsafe(64))

# task 9
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
# Істинно випадкову послідовність повторити неможливо. Але для повторення
# псевдовипадкових чисел в обох основних бібліотеках - random і numpy.random є
# функція seed (), яка відповідає за ініціалізацію ("посів") послідовності.
# У необов'язковому параметрі методу передається число для ініціалізації або
# свого роду маркування згенерованого числа. Тому при повторному застосуванні
# методу random згенероване число не змінюється. Якщо ж параметр залишити
# порожнім, то генеруватиметься щоразу нове число.
for i in range(5):
    random.seed(1)
    print(random.choice(dice))


# task 10
def get_random_date(start_date, end_date):
    print("Printing random date between", start_date, " and ", end_date)
    random_generator = random.random()
    date_format = '%m/%d/%Y'

    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))

    random_time = start_time + random_generator * (end_time - start_time)
    random_date = time.strftime(date_format, time.localtime(random_time))
    return random_date


print("Random Date = ",
      get_random_date("01/01/2016", "12/12/2018"))
