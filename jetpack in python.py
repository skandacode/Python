from tkinter import*
class Player:
    def up(self, evt):
        self.y=10
    def small(self, evt):
        self.size=25
    def __init__(self, canvas):
        make_player=PhotoImage('fish.gif', ('-topmost', 1), 250, 0)
