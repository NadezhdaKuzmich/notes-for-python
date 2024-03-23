import json
from json import JSONEncoder

# task 1
data = {"key1": "value1", "key2": "value2"}
jsonData = json.dumps(data)
print(jsonData)

# task 2
sampleJson = """{"key1": "value1", "key2": "value2"}"""
data = json.loads(sampleJson)
print(data['key2'])

# task 3
sampleJson = {"key1": "value2", "key2": "value2", "key3": "value3"}
# indent - використовується для відступу кожного рівня.
# separators має бути кортежем (item_separator, key_separator)
prettyPrintedJson = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(prettyPrintedJson)

# task 4
sampleJson = {"id": 1, "name": "value2", "age": 29}
print("Started writing JSON data into a file")
with open("data/sample-json.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
print("Done writing JSON data into a file")

# task 5
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data['company']['employee']['payable']['salary'])


# task 6
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


class VehicleEncoder(JSONEncoder):
    # default(obj) - реалізує метод у підкласі JSONEncoder так,
    # щоб він повертав об'єкт, що серіалізується, для obj або
    # викликав базову реалізацію.
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print("Encode Vehicle Object into JSON")
# Щоб використовувати власний підклас JSONEncoder (наприклад, той, який
# перевизначає метод default() для серіалізації додаткових типів), вкажіть
# його за допомогою cls kwarg; інакше використовується JSONEncoder.
vehicleJson = json.dumps(vehicle, indent=2, cls=VehicleEncoder)
print(vehicleJson)


# task 7
def vehicle_decoder_func(obj):
    return Vehicle(obj['name'], obj['engine'], obj['price'])

# object_hook - являє собою користувацьку функцію і якщо вказана, то буде
# викликатися з результатом декодування кожного об'єкта JSON dict, а її
# значення, що повертається, буде використовуватися замість відповідного
# словника dict. Цю поведінку можна використовувати для забезпечення
# настроюваної десеріалізації.
vehicleObj = json.loads(
    '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }',
    object_hook=vehicle_decoder_func)

print("Type of decoded object from JSON Data")
print(type(vehicleObj))
print("Vehicle Details:")
print(vehicleObj.name, vehicleObj.engine, vehicleObj.price)
