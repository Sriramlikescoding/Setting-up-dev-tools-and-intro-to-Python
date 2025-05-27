try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result  = num1/num2
    print("The result is", result)

except ZeroDivisionError:

    print("No Dividing By zero")

except SyntaxError:
    print("Comma is missing. Please enter 2 numbers separated by a comma")

except:
    print("Wrong Input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")