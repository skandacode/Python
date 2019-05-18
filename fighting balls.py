from tkinter import

if int(input('how many people'))>5:
    name()
else:
    
def name(name1, name2, name3, name4):
    pass
class P1:
    def up(self):
        self.y=5
    def down(self):
        self.y=-5
    def left(self):
        self.x=5
    def right(self):
        self.x=-5
    def move(self, canvas, c1, c2, c3, c4):
        self.canvas.bind_all(c1, up)
        self.canvas.bind_all(c2, down)
        self.canvas.bind_all(c3, left)
        self.canvas.bind_all(c4, right)
class hypnotizer:
    h=PhotoImage('hypno.gif')
    

class Game:
    tk=Tk()
    tk.update()
    canvas=Canvas(tk, height=900, width=1200)
    canvas.pack()
    def loop(self):
        while True:
            p1=P1(canvas, 'red', '<KeyPress-Up>', '<KeyPress-Down>'
                  , '<KeyPress-Left>', '<KeyPress-Right>')
            p1.move()
            tk.update()
game=Game()
game.loop()

            
