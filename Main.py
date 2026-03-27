import random 

list_outcomes = ("Red", "Blue", "Yellow", "Green")

result = random.choice(list_outcomes)

#probability = 100/int(list_outcomes.count(""))
p = list_outcomes.count("Red")/len(list_outcomes)
print(f"probaility of picking red ball is ", p)

if result == "Red":
    print("Result was red")

else:
    print("Better luck next time")