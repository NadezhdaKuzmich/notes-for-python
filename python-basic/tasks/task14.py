# task 0
# Create a class without any variables and methods
class Some:
    pass


# task 1
class Vehicle:
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"The seating capacity of a {self.name} is {capacity} "
                f"passengers")


model = Vehicle("BMW", 240, 18)
print(model.name, model.max_speed, model.mileage, "\n")


# task 2
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


school_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, "\nSpeed:", school_bus.max_speed,
      "\nMileage:", school_bus.mileage, "\n")

# task 3
print(school_bus.seating_capacity(), "\n")


# task 4
class Car(Vehicle):
    pass


print(school_bus.color, school_bus.name, "\nSpeed:",
      school_bus.max_speed, "\nMileage:", school_bus.mileage, "\n")

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "\nSpeed:", car.max_speed, "\nMileage:",
      car.mileage)


# task 5
class Vehicle2:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus2(Vehicle2):
    def fare(self):
        amount = super().fare()
        amount += amount * 0.1
        return amount


school_bus2 = Bus2("School Volvo", 12, 50)
print("\nTotal Bus fare is:", school_bus2.fare())

# task 7
print(type(school_bus))
print(type(school_bus2))
