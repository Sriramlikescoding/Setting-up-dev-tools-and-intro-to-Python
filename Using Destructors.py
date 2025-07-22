class Employee:
    def __init__ (self):
        print("Emplyee Created")

    def __del__ (self):
        print("Destructor Called")
def CreateObj():
        print("Making Obj...")
        obj = Employee()
        print('Function End...')
        return obj

print('Calling Create Obj() Function...')
obj = CreateObj()
print('Program end...')
