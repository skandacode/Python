from tkinter import*
import time
var_start=False
def do_start():
   var_start=True
class start:
   def __init__(self, tk):
      btn=Button(tk, text="Start", command=do_start)
      btn.pack()
var_menu=False
def do_menu():
   var_menu=True
class menu:
   def __init__(self, tk):
      btn=Button(tk, text="Menu", command=do_menu)
      btn.pack()
def do_bank():
   var_bank=True
class bank:
   def __init__(self, tk):
      btn=Button(tk, text="Bank", command=do_start)
      btn.pack()
     


tk=Tk()
canvas=Canvas(tk, height=500, width=700)
canvas.pack()
while True:
   tk.update()
   img=PhotoImage(file="scene.sprite2")
   canvas.create_image(500, 700, anchor=NW, image=img)
   time.sleep(30)
   tk.update()
   start()
