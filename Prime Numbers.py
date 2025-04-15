lower_range = int(input("Enter the lower value you want"))
higher_range = int(input("Enter the higher value you want"))

print("Prime numbers between ", lower_range, "and", higher_range, "are: ")

for num in range(lower_range, higher_range+1):
    if num > 1:
        for  i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num)