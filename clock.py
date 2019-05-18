from tkinter import*
tk=Tk()
canvas=Canvas(height=900, width=1100)
canvas.pack()
tk.update()
while 1:
    canvas.create_oval(700, 700, 900, 900, fill="cyan")
    tk.update()
    
