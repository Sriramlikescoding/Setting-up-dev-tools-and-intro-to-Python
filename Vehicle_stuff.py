class Vehicle:
    def __init__(self, mileage, speed):
        self.mileage = mileage
        self.speed = speed
    
modelx = Vehicle(50, 120)
print("Modelx mileage = ", modelx.mileage)
print("Modelx speed = ", modelx.speed)