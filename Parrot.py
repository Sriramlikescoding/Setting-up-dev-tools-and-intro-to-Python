class Parrot:
    grade = 7
    print(grade)
    def __init__(self, name, age):
        self.name = name
        self.age = age

ParrotCopy = Parrot("Sriram", 13)

print(ParrotCopy.name)
print(ParrotCopy.age)