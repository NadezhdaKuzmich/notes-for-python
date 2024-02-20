# Приклади деяких стандартних ітерабельних об'єктів.
# Список
my_list = [1, 2, 5, 7, 32, 148]

# Обхід списку
for element in my_list:
    print(element)

print('\n', '* ' * 10, '\n')

# enumerate повертає ітерабельний об'єкт, який повертає пари індекс-значення
for index, element in enumerate(my_list):
    print(f'{my_list[index]=}')

print('\n', '* ' * 10, '\n')

# Рядок
string = 'A string'

# Обхід рядка посимвольно
for char in string:
    print(char)

print('\n', '* ' * 10, '\n')

# У Python 3 range -- це ітерабельний об'єкт, який задає діапазон.
# У Python 2 для цього служить xrange, а range є функцією, яка повертає список.
my_range = range(2, 17, 2)

for counter in my_range:
    print(counter)

print('\n', '* ' * 10, '\n')


# Ітерабельні об'єкти мають реалізовувати принаймні один із двох методів:
# 1. __iter__(self)
# 2. __getitem__(self, key)

# Метод __iter__ повертає об'єкт-ітератор.
# Метод __getitem__ повертає елемент контейнера за ключем або індексом.
# Вбудована фукнція iter (автоматично викликається циклом for) викликає метод
# __iter__, якщо він існує. Інакше, якщо існує метод __getitem__, то
# автоматично створюється ітератор, який викликає метод __getitem__ зі
# зростаючими індексами, починаючи від нуля, до виникнення винятку IndexError.
# Якщо об 'єкт не реалізує жоден із цих методів, то цей об 'єкт не є
# ітерабельним і викидається виняток TypeError.
class SimpleIterable(object):
    """"Клас ітерабельного об'єкта з методом __getitem__"""

    def __getitem__(self, ind):
        if 0 <= ind < 5:
            return ind * 2
        else:
            raise IndexError('iterable index out of range')


# Створення об'єкта
iterable = SimpleIterable()

# Виведення деяких значень
print(f'{iterable[0]=}')
print(f'{iterable[3]=}')
print('\n', '* ' * 10, '\n')

# Ітерування
for i in iterable:
    print(i)
