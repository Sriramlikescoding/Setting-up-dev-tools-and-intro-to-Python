medical_problem = input("Are you missing the exam due to virus N or virus Y? (Ex. Y)")
attendance = input("What is your attendance percent? (Ex. 82)")

if medical_problem == 'Y':
    print("You are allowed")
else:
    if attendance >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")