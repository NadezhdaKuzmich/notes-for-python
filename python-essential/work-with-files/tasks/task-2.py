import json
import datetime
import csv

with open(
        f'files/users_data_{datetime.datetime.now().strftime('%d-%m-%y')}'
        f'.json', 'r') as file:
    data = json.load(file)
print(data)

rows = []
for user in data['data']:
    rows.append(list(user.values()))
    print(list(user.values()))

rows_csv = [list(data['data'][0].keys())] + rows
print([list(data['data'][0].keys())])

with open(f'files/users_data_{data['current_date']}.csv',
          'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for row in rows_csv:
        csv_writer.writerow(row)
