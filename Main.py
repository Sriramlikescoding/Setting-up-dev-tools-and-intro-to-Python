import numpy as np
import matplotlib.pyplot as p
from numpy import asarray
from numpy import arange
from numpy.random import rand

def objective(x):
    return x**2.0
def derivative(x):
    return x*2.0
def gradient_descendant(objective, derivative, bonds, niteration, stepsize):
    solutions, scores = list(), list()
    solution = bonds[:, 0] + rand(len(bonds))*(bonds[:, 1] - bonds[:,0])
    for i in range(niteration):
        gradient = derivative(solution)
        solution = solution - stepsize * gradient
        solution_evaluation = objective(solution)
        solutions.append(solution)
        scores.append(solution_evaluation)
        print('>%d f(%s) = %.5f'%(i, solution, solution_evaluation))
    return [solutions, scores]
bonds = asarray([[-1.0 , 1.0]])
niteration = 30
stepsize = 0.1
solutions, score = gradient_descendant(objective, derivative, bonds, niteration, stepsize)
inputs = arange(bonds[0, 0], bonds[0,1]+0.1, 0.1)
results = objective(inputs)
p.plot(input, results)
p.plot(solutions, score, ".-", color = "red")
p.show()