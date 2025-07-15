import random

real_num = random.randint(0, 200)#Generating number from 0-200 for user to guess
GameDone = False

user_guess = int(input("Number generated, take a guess at what you think the number is.")) #Asking the user for their guess and assigning the variable to user_guess
while GameDone == False:
    if user_guess == real_num:
        print("Congratulations you guessed the number correctly. \n")
        GameDone = True

    else:
        if user_guess > real_num:
            print("Not quite, go lower \n" )
        else:
            print("Not quite, go higher \n")
        user_guess = int(input("Try again\n"))
        