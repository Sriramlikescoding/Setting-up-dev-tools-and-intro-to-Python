n = int(input("How many rows would you like in your triangle?"))
print("Here is your triangle made of stars")

for i in range(n):
    for j in range(i + 1):
        print("* ", end = "")
    
    print()