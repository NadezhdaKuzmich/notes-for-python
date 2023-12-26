import json
import datetime
import csv

with open('files/users_data_{current_date}.json'.format(current_date=datetime.datetime.now().strftime('%d-%m-%y')),
          'r') as file:
    data = json.load(file)
print(data)

rows = []
for user in data['data']:
    rows.append(list(user.values()))
    print(list(user.values()))

rows = [list(data['data'][0].keys())] + rows
print([list(data['data'][0].keys())])

with open('files/users_data_{date}.csv'.format(date=data['current_date']), 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for row in rows:
        csv_writer.writerow(row)
