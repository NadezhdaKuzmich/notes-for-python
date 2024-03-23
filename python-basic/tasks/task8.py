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
vehicleJson = json.dumps(vehicle, indent=2, cls=VehicleEncoder)
print(vehicleJson)
