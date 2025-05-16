def add(p,q):
    return int(p) + int(q)
def subtract(p,q):
    return int(p)-int(q)
def multiply(p,q):
    return int(p)*int(q)
def divide(p,q):
    return int(p)/int(q)

print("Choose which of the following you would like to perform")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
choice = input("Enter the letter corresponding to your choice.")

num_1 = input("Enter your 1st number")
num_2 = input("Enter your 2nd number")

if(choice == "a"):
    print(num_1, "+", num_2, "=", add(num_1,num_2))
elif(choice == "b"):
    print(num_1, "-", num_2, "=", subtract(num_1,num_2))
elif(choice == "c"):
    print(num_1, "*", num_2, "=", multiply(num_1,num_2))
elif(choice == "d"):
    print(num_1, "/", num_2, "=", divide(num_1/num_2))
else:
    print("The letter you entered is invalid. Please enter a b c or d")
