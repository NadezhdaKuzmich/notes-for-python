import csv

with open('data/example1.csv', 'r') as f:
    # передаємо у reader файловий дескриптор
    reader = csv.reader(f)
    print('Line nums', reader.line_num)
    # друкуємо dialect, який відповідає правилам парсингу CSV файла.
    print('Dialect', reader.dialect)
    # запуск цикл і ітеруємося по кожному рядку в CSV-файлі
    for row in reader:
        print(row)
