import turtle
turtle.bgcolor("lightblue")

turtle.pensize(3.5)
turtle.speed(0.5)
color=["red","green","yellow","black"]
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(50)
turtle.mainloop()
