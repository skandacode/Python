from tkinter import*
import time
import random
import sys
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-1
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos)==True:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3

class Paddle:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0, 0, 150, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)            
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] <= self.canvas_width:
            self.x = 0
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
    def turn_left(self, evt):
        self.x=-20
        
    def turn_right(self, evt):
        self.x=20    
            
tk=Tk()
tk.title("bounce")
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas=Canvas(tk, width=800, height=700, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle=Paddle(canvas, 'blue')
ball=Ball(canvas, paddle, 'red')
while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    paddle.draw()
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if canvas.bind_all('<KeyPress-x>')==True:
        sys.close()
    print(bool(ball.hit_bottom))

