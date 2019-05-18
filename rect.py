import random
tk=Tk()
canvas=Canvas(tk, height=700, width=900)
canvas.pack()
def rect(width, height):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=y1+random.randrange(width)
    canvas.create_rectangle(x1, y1, x2, y2)

rect(500, 500)
