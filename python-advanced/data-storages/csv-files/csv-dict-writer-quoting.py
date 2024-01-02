import csv

# екранування всіх осередків файлу
quoting = csv.QUOTE_ALL

with open('data/output.csv', 'w') as f:
    # використовуємо DictWriter для зручнішої роботи з даними
    # він дозволяє працювати з рядками як зі словником, звертаючись до значень
    # за ключами (назвою колонок)
    writer = csv.DictWriter(
        f,
        fieldnames=['first_name', 'last_name', 'age'],
        quoting=quoting
    )

    writer.writeheader()
    # запис також відбувається з використанням словників як рядків
    # з даними, що більш інтуїтивно, ніж просто плоский список
    writer.writerow({
        'first_name': 'Ivan',
        'last_name': 'Petrov @ ll, Test',
        'age': 20
    })
    writer.writerow({
        'first_name': 'Dmitry',
        'last_name': 'Sidorov',
        'age': 30
    })
    writer.writerow({
        'first_name': 'Alexey',
        'last_name': 'Ivanov',
        'age': 30
    })
