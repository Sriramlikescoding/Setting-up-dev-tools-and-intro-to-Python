units = int(input("Enter Units of Electricity Used: "))


if units <= 50:
    amount = units * 2.6
    surcharge = 25

elif units <= 100:
    amount = 130 + (units - 50) * 3.25
    subcharge = 35

elif units <= 200:
    amount = 130 + 162.5 + (units - 100) * 5.26
    subcharge = 45

elif units > 200:
    amount = 130 + 162.6 + 526 + (units - 200) * 8.45
    subcharge = 75

print("Amount for electricity:", amount)
print("Tax Amount:", subcharge)