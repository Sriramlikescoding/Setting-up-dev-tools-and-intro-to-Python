import matplotlib.pyplot as m
import numpy as n
#(0,6), (6,250)
x_points = n.array([1,2,6,8])
y_points = n.array([3,8,1,10])
m.plot(x_points,y_points,linestyle = "dashed")
m.show()