import matplotlib.pyplot as m
import numpy as n
#(0,6), (6,250)
x_points = n.array([1,2,6,8])
y_points = n.array([3,8,1,10])
x_points2=n.array([1,2,3,4])
y_points2=n.array([1,0,10,11])
m.plot(x_points,y_points, color="r", linewidth = "20.5")
m.plot(x_points2,y_points2)
m.show()