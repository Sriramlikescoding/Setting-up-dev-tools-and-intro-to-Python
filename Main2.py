Even = {2, 4, 6}
Greater_than_2 = {3, 4, 5, 6}
allrolls = {1, 2, 3, 4, 5, 6}

print("Probability of getting an even number greater than 2 is ")
ProbabilityOfA = len(Even)/len(allrolls)
ProbabilityOfB = len(Greater_than_2)/len(allrolls)

I = Even.intersection(Greater_than_2)
probabilityOfI = len(I)/len(allrolls)
print("Adding all probabilities")
print(probabilityOfI)