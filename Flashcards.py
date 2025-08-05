f1 = input("What would you like on the front side of your flashcard: ")
b1 = input("What would you like on the back side of your flashcard: ")

Check = input("Would you like to quiz yourself? Enter: y/n")

if Check == 'Y' or 'y':
    print(f1)
    answer = input("Enter what you said on the back: ")
    if answer == b1:
        print("You got it!")
    else:
        print("Not quite the answer, here's what was the correct answer:", b1)
elif Check == "N" or 'n': 
    print("No problem type y when you're ready to start")
