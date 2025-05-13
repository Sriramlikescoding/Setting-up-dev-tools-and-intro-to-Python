import turtle
turtle.Screen().bgcolor("Aqua")
board = turtle.Turtle()

board.forward(100) #forms the base of our 1st triangle



board.left(120)
board.forward(100) 
#second stroke making our second side


board.left(120)
board.forward(100)
#third stroke completing our triangle


board.penup()
board.right(150)
board.forward(50)
#Going to the third triangle starting area

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)
