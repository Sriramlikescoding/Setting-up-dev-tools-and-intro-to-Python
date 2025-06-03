import random
user = input("Enter" \
" R for Rock," \
" P for Paper," \
"and S for Scizzors")
computer = random.choice("RPS")

if user == computer:
    print("Looks like this game ended in a draw")
elif user == "R" and computer == "P":
    print("Computer won: Paper beats Rock")
elif user == "R" and computer == "S":
    print("You won: Rock beats Scizzors")
elif user == "S" and computer == "R":
    print("Computer won: Rock beats Scizzors")
elif user == "S" and computer == "P":
    print("You won: Paper beats Scizzors")
elif user == "P" and computer == "S":
    print("Comoputer won: Scizzors beats Paper")
elif user == "P" and computer == "R":
    print("You won: Paper beats Rock")