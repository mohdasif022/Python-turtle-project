import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors = ["red","blue","light green","violet","orange","purple","green","white"]
for x in range(360):
    t.pencolor(colors[x%8])
    t.width(x//100+1)
    t.forward(x)
    t.left(float(44))
    t.speed(50)
