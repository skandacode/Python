import turtle
turtle.setup(width=500, height=500)
t=turtle.Pen()
close=int(input())
for i in 360/close/5:
    t.color(0, 0, 0)
    t.forward(100)
    for m in close:
        t.left(1)
    t.color(1, 1, 1)
    t.goto(0, 0)
    t.forward(100)
    for m in close:
        t.left(1)
    t.color(1, 0, 0)
    t.goto(0, 0)
    t.forward(100)
    for m in close:
        t.left(1)
    t.color(0, 1, 0)
    t.goto(0, 0)
    t.forward(100)
    for m in close:
        t.left(1)
    t.color(0, 0, 1)
    t.goto(0, 0)
