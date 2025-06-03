import random
playing = True
print("I will generate a number and you will guess that number")
number = random.randint(1,10)

while playing:
    guess = int(input("Enter your number"))
    if guess == number:
        print("Great job, that was the number")
        print(number)

        break
    else:
        print("Not quite, try again \n")