from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()

# search value
# вибірка тегів first_name із тегів person з атрибутом pk = 21
first_name = root.findall('./person[@pk="21"]/first_name')
# вибірка тегів last_name з тегів person з атрибутом pk = 21
last_name = root.findall('person[@pk="21"]/last_name')
# вибірка тегів age з тегів person з атрибутом pk = 21
age = root.findall('person/[@pk="21"]/age')

for values in zip(first_name, last_name, age):
    row = {value.tag: value.text for value in values}
    print(row)

# вибірка тексту у тега first_name у person з атрибутом pk та індексом 1 у DOM
name = root.find('./person/age/..[@pk][1]/first_name').text
print(name)

# вибірка тексту у тега first_name у person з атрибутом pk та індексом 2 у DOM
name = root.find('./person/age/..[@pk][2]/first_name').text
print(name)

# вибірка тексту у тега first_name у person з атрибутом pk та індексом 3 в DOM
name = root.find('./person/age/..[@pk][3]/first_name').text
print(name)
