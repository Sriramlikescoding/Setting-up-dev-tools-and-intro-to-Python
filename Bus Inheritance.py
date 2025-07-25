class Vehicle():
    def __init__(self, name, speed, mileage):
        self.speed = speed
        self.mileage = mileage
        self.name = name

class Bus(Vehicle):
    pass

School_Bus = Bus("School Volvo", 120, 12)
print("Vehicle Name:", School_Bus.name, "\n Vehicle speed:", School_Bus.speed, "\n Vehicle mileage: ", School_Bus.mileage)

