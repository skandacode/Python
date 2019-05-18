from tkinter import*
tk=Tk()
canvas=Canvas(tk, height=136*2, width=204*2)
canvas.pack()
tk.update()
ind=PhotoImage(file='C:\\Users\\aruns\\Desktop\\skanda pro programs\\photos\\indian_flag.gif')
ind.zoom(2, 2)
canvas.create_image(0, 0, anchor=NE, image=ind)
