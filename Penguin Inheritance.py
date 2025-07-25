class Bird():
    def __init__(self, height, wingspan, speed):
        self.height = height
        self.wingspan = wingspan
        self.speed = speed
    def display(self):
        print("Height: ", self.height)
        print("Wingspan: ", self.wingspan)
        print("Speed: ", self.speed)
    def isbird(self):
        print("This animal is a bird")

class Penguin(Bird):
    def __init__(self, height, wingspan, speed, water_speed):
        self.water_speed = water_speed
        Bird.__init__(self, height, wingspan, speed)
    

Larry = Penguin("3ft 5 in.",  "2ft", 4, 20)
Larry.display()