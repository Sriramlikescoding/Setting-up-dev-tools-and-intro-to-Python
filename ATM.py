amount = int(input("Enter Withdrawal Amount: "))
Rupee100 = amount//100
Rupee50 = (amount%100)//50
Rupee10 = ((amount%100)%50)//10
Rupee1 = (((amount%100)%50)%10)//1

print("100 Bills:", Rupee100)
print("50 Bills:", Rupee50)
print("10 Bills:", Rupee10)
print("1 Bills:", Rupee1)