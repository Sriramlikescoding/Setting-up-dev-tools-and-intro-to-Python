number = int(input("Enter a number to count down from: "))
n = number + 1


for i in range(n, 0, -1):
    n = n - 1
    print("\n",n)