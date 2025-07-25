class Person():
    def __init__(self, name, ID_number):
        self.name = name
        self.ID_number = ID_number
    def display(self):
        print("Name:", self.name)
        print("ID#:", self.ID_number)

class Employee(Person):
    def __init__(self, name, ID_number, salary, post):
        self.salary = salary
        self.post = post
        Person.__init__(self, name, ID_number)
    
a = Employee("Rahul", 1006, 80000, "Area Director")
a.display()
