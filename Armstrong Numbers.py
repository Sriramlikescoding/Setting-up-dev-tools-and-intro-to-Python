num = int(input("Enter a number to check if it's an armstrong number: "))
temp = num
ans = 0


while temp > 0:
    hope = temp%10
    ans += hope**3
    temp = temp//10

if num != ans:
    print("Your number is not an armstrong number")
elif num == ans:
    print("Your number is an armstrong number")
