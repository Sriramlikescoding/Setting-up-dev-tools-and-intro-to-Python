class Base():
    __private_var = 27

    def privMeth(self):
        print("I'm inside the Class")
    
    def    hello(self):
        print("Private Variable is : ", Base.__private_var)

Obj = Base()
Obj.hello()
Obj.__private_var
