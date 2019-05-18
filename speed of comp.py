from tkinter import*
import time
t_one=time.time()
nums=[]
for i in range(1, 1001):
    nums.append([i])
    print(nums[i-1])
    #tk=Tk()
    #canvas=Canvas(tk, height=500, width=500)
    #canvas.pack()
t_two=time.time()
time_take=t_two-t_one
speed=time_take
print(speed)
