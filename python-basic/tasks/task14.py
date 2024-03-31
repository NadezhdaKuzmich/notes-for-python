# task 0
# Create a class without any variables and methods
class Some:
    pass


# task 1
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return (f"The seating capacity of a {self.name} is {capacity} "
                f"passengers")


model = Vehicle("BMW", 240, 18)
print(model.name, model.max_speed, model.mileage)


# task 2
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


school_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", school_bus.name, "\nSpeed:", school_bus.max_speed,
      "\nMileage:", school_bus.mileage)

# task 3
school_bus = Bus("School Volvo", 180, 12)
print(school_bus.seating_capacity())
