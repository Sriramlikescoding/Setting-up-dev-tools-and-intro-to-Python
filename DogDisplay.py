class Dog:
    Number = 7
    print(Number)
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

Doggy = Dog("Roxie", "Golden Retriever", "Gold")
Doggy2 = Dog("Bella", "Chihuahua", "Black and White")

print(Doggy.name)
print(Doggy.breed)
print(Doggy.color)

print(Doggy2.name)
print(Doggy2.breed)
print(Doggy2.color)