def Cube(number):
    return number*number*number
def byThree(number):
    if Cube(number)%3==0:
        return Cube(number)
    else:
        return False
    
print(byThree(9))
print(byThree(4))
