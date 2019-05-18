from tkinter import*
import random
scoreboard=[0, 0, 0]
pick_random=random.randint(1, 1000)
tk=Tk()
canvas=Canvas(tk, height=500, width=500)
canvas.pack()
canvas.create_text(220, 300, text=str(pick_random), font=('Courier', 22), color=colorchooser.askcolor())
