from abc import ABC, abstractmethod

class ABsclass(ABC):
    def print(self,x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside ABC class tak")

class test_Class(ABsclass):
    def task(self):
        print("We are inside test_Class")

test_obj = test_Class()
test_obj.task()
test_obj.print(100)