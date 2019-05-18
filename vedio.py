from tkinter import*
import time
import pickle
def pic():
    pass
return True
def breaker(event):
    return False
def save(name_pic):
    save_pic=open('save.dat', 'wb')
    pickle.dump(name_pic, time.time(), save_pic)
    save_pic.close()
def write(event):
    num=0
    while True:
        pic_%s%num=pic()
        save(pic_%s%num)
        time.sleep(15)
        bind_all('KeyPress-Return', breaker)
        num=num+1
def read(start_time, end_time):
    tk=Tk()
    canvas=Canvas(tk, height=1366, width=768)
    canvas.pack()
    for i in range(end_time-start_time*20):
        tk.update()
        
