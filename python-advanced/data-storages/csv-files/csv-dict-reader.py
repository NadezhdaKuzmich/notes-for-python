import csv

with open('data/example1.csv', 'r') as f:
    # аналогічно виклику csv.reader(f)
    # але DictReader дозволяємо перетворювати CSV рядки в словники, для більш
    # зручної роботи на Python
    reader = csv.DictReader(f)
    print('Line nums', reader.line_num)
    print('Dialect', reader.dialect)
    for row in reader:
        print(row)
        # для звернення до конкретного стовпця рядка використовуємо
        # звернення по ключу `row['name'] --> row[0]`
