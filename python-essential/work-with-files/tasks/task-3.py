import datetime
from xml.etree import ElementTree
import csv

with open(f'./files/users_data_{datetime.datetime.now().strftime('%d-%m-%y')}'
          f'.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    data = [row for row in reader]
    print(data)

columns = data[0]
print(columns)
users = data[1:]
print(users)

xml_data = ElementTree.Element('data')
items_holder = ElementTree.SubElement(xml_data, 'users')
items = [ElementTree.SubElement(items_holder, 'user')
         for i in range(len(users))]
for j in range(len(users)):
    item = items[j]
    for k in range(len(columns)):
        item.set(columns[k], users[j][k])

xml_file = ElementTree.tostring(xml_data)
with open('./files/users.xml', 'wb') as file:
    file.write(xml_file)
