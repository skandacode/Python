from tkinter import*
def start(evt):
    import time
    import random
    class Goal:
        def init(self, canvas):
            make_goal=canvas.create_oval(20, 20, 50, 50, fill=color)
            tk.update()
            make.move(450, 450)
        def up(self, evt):
            self.y=5
        def down(self, evt):
            self.y=-5
    class Ball1:
        def __init__(self, canvas, color):
            make_ball1=canvas.create_oval(10, 10, 25, 25, fill=color)
            make_ball1.move(350, 400)
        def shoot(self, evt):
            pass
    tk=Tk()
    canvas=Canvas(tk, height=700, width=900)
    canvas.pack()
    while True:
        tk.update()

#canvas.bind_all('KeyPress-Return', start)
len('''eggggrebgebrehpwhfuiwvhihfievifupehwviufhvufehwivuehpfivuhuwhurvhphhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhuiuphuhrihtfuwrhuwh9u0rehwg0thwgu0whuth5uch9uc0hucchuigpcgugwtphgmcpguuuuuuuhiuhgiuhwiphieguwhirphwgiurheiwhruiehgwpierhgwiuhwuihpuigrhiuwhieuwgiprheuwguerhpgwiuerhpiwguerhwguiwhpwurihuwrephrtigrhwgewhwupghrguwphiwphihgriughpirghuiqqqqqqqqqrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrtyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwweeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeetttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttrrrrrrrrrrtttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr''')
