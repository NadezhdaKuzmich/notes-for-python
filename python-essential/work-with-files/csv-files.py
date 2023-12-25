import csv

with open('my-files/data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv_reader]
    for row in data:
        print(row)

data.append(['Mike', '35', 'male'])
print(data)

with open('my-files/data2.csv', 'w') as data_file:
    csv_writer = csv.writer(
        data_file,
        delimiter=','
    )
    for row in data:
        csv_writer.writerow(row)
