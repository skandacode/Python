from tkinter import*
import random
import time

class Game:
    def __init__(self):
        self.tk=Tk()
        self.tk.title("Mr.Stick man races for the exit")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas=Canvas(self.tk, height=700, width=900
                           , highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height=700
        self.canvas_width=900
        self.sprites=[]
        self.running=True
    def mainloop(self):
        while True:
            if self.running==True:
                for sprite in self.sprites:
                    sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)

#class Coords:
    #def __init__(self, x1=0, y1=0, x2=0, y2=0):
g=Game()

g.mainloop()
