import turtle 

t = turtle.Turtle()
t.getscreen().bgcolor("black")
t.penup()
t.goto(-350,100)
t.pendown()
t.color("light green","yellow")
t.speed(50)

def star(turtle,size):
    if size<=10:
        return
    
    else:
        turtle.begin_fill()
        for i in range(10):
            turtle.pensize(3)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()

star(t, 360)
turtle.done()


