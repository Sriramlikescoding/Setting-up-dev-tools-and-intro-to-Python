import math
print("The floor and Ceiling values of 23.56 are" + str(math.ceil(23.56)) + ',' + str(math.floor(23.56)))

x = -15
y = 10

#using copysign
print("The value of y after copying the sign of x is, " + str(math.copysign(y,x)))

print("The absolute value of 95 and -56 are: "+ str(math.fabs(95)), "and "+ str(math.fabs(-56)))
print("And finally, the GCD of 24 and 56 are:"+ str(math.gcd(24,56)))