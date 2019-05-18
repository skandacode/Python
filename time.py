from tkinter import*
import time
import sys
def close(sys):
    sys.exit()
tk=Tk()
canvas=Canvas(tk, height=500, width=700)
canvas.pack()
tk.update()
thetime=0
times=[]
#b=Tk()
btn=Button(tk, height=5, width=20, text='Stop')
btn.pack()
btn.place(x=100, y=300)

start=Button(tk, height=5, width=20, text='Start')
start.pack()
start.place(x=300, y=300)
print('''The time is:
''')

while True:
    print(thetime)
    #time.sleep(1)
    thetime=thetime+1
    stop=Button(tk, height=5, width=20, text='Stop')
    stop.place(x=100, y=300)
    tk.update()
