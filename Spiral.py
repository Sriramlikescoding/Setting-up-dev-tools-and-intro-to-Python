import turtle
Pen = turtle.Turtle()
turtle.Screen().bgcolor("red")
turtle.Screen().setup(400,300)
spiral_Number=10

size = 0

while True :
    for i in range(4):
        Pen.fd(size+1)
        Pen.left(90)
        size = size-5
    size = size + 1
    
