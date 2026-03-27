import random

def d():
    list_outcomes = ("Red", "Blue", "Yellow", "Green")

    result = random.choice(list_outcomes)

#probability = 100/int(list_outcomes.count(""))
    p = list_outcomes.count("Red")/len(list_outcomes)
    print(f"probaility of picking red ball is ", p)

    if result == "Red":
        print("Result was red")
        return("Result was red")

    else:
        print("Better luck next time")
        return("Result not red")

result = d()
print(result)