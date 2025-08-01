from abc import ABC

class India():
    def capital(self):
        print("The Capital of ")
    def language(self):
        print("The most commonly spoke language of India happens to be Hindi")
    def type(self):
        print("India is a developing country.")

class France():
    def capital(self):
        print("The capital of France is Paris")
    def language(self):
        print("The language of France is French")
    def type(self):
        print("France is a developed country.")


class Mexico():
    def capital(self):
        print("Mexico city is the capital of Mexico")
    def language(self):
        print("Spanish/Espagnole is the official language of Mexico.")
    def type(self):
        print("Mexico is a developing country")

class USA():
    def capital(self):
        print("The capital of USA is washington DC")
    def language(self):
        print("The language of the USA is English")
    def type(self):
        print("The USA is a developed country.")

obj_Ind = India()
obj_U = USA()
obj_F = France()
obj_M = Mexico()

for country in (obj_Ind, obj_U, obj_F, obj_M):
    country.capital()
    country.language()
    country.type()