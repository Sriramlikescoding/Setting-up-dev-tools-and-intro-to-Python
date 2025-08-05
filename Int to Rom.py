x = int(input("Enter a number"))
units = x%10
tens = x//10
unitsN = "" 
TensN = '' 


while units > 0:
    unitsN += "I"
    units -= 1

while tens > 0:
    TensN += "X"
    units -= 1