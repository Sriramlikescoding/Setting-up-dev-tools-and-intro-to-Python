import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #Importing and assigning to var

num_sides = 6
side_Length=70
angle = 360.0 / num_sides
#Iterate in loop
for i in range(num_sides):
    polygon.forward(side_Length)
    polygon.right(angle)