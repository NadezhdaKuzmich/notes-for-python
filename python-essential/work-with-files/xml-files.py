from xml.dom import minidom
from xml.etree import ElementTree

my_doc = minidom.parse('./my-files/my_file.xml')
items = my_doc.getElementsByTagName('item')
print(items)
print(len(items))
# print(items[0].attributes['name'].value)
for s in items:
    print(s.attributes['name'].value)

data = ElementTree.Element('data')
items = ElementTree.SubElement(data, 'items')
item1 = ElementTree.SubElement(items, 'item')
item2 = ElementTree.SubElement(items, 'item')
item1.set('name', 'item1')
item2.set('name', 'item2')
item1.text = 'item1-1'
item2.text = 'item2-2'

my_data = ElementTree.tostring(data)
with open('./my-files/items2.xml', 'wb') as my_file:
    my_file.write(my_data)
