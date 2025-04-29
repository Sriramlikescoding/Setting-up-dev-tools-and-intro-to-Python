rows = int(input("Enter the number of rows you would like on your triangle: "))
number = 1

print("Here is Your floyd's triangle")

for i in range(1, rows + 1):
    for j in range(1, i+1):
        print(number, end= '  ')
        number = number + 1
    print()
