from abc import ABC, abstractmethod

class animal(ABC):
    def move(self):
        pass

class human(animal):
    def move(self):
        print("I can walk and talk and run")

class dog(animal):
    def move(self):
        print("I can run on four legs and I can bark")
    
class cat(animal):
    def move(self):
        print("I can eat and meow")

class horse(animal):
    def move(self):
        print("I can run up to 50 miles per hour")

class cheetah(animal):
    def move(self):
        print("I can run up to 70 miles per hour but only for a little bit")

class bird(animal):
    def move(self):
        print("I can fly")

class lion(animal):
    def move(self):
        print("I can roar")