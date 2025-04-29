rowSize = int(input("Enter number of rows you would like"))
if rowSize%2 == 0: #Conditions
    halfDaimRow = int(rowSize/2)
else:
    halfDaimRow = int(rowSize/2)+1
space = halfDaimRow-1
#Loop for upper part only
for i in range(1, 1 + halfDaimRow): #loop for rows
    for j in range(1, space + 1): # loop for columns
        print(end= " ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
       #incerementing each number at each column
        num = num + 1
    print()
space = 1
#loop for lower part

for i in range(1, halfDaimRow):
    for j in range(1, space+1):
        print(end=" ")
    space = space+1
    num = 1
    for j in range(1, 2*(halfDaimRow-i)):
        print(end = str(num)) #display result
        #incerementing each number at each column
        num = num+1
    print()
