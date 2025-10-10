import matplotlib.pyplot as m
import numpy as n
#(0,6), (6,250)
x_points = n.array([80,85,90,95,100,105,110,115,120,125])
y_points = n.array([240,250,260,270,280, 290, 300, 310, 320, 330])
m.plot(x_points,y_points, )
m.title("PYlab Project")
m.xlabel("Average Pulse")
m.ylabel("Calories per date")
m.show()