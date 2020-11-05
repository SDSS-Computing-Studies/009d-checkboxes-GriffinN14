#!python3

import tkinter as tk 
from tkinter import *

win = tk.Tk()
win.geometry("450x300")
Loc=[250,250]
bgimage = PhotoImage(file="download.png")
background = tk.Label(win, image=bgimage)
background.place(x=0,y=0)

def checkLocations():
    if Loc[0] > 50 and Loc[0] < 70 and Loc[1] <30:
        print("destination!")

def doFunction(event):
    print(event)
    if event.keysym=="Up":
        Loc[1] = Loc[1] - 5
    if event.keysym=="Down":
        Loc[1] = Loc[1] + 5
    if event.keysym=="Left":
        Loc[0] = Loc[0] - 5
    if event.keysym=="Right":
        Loc[0] = Loc[0] + 5
    
    x.place(x=Loc[0],y=Loc[1])

    checkLocations()

x = Label(win, text='0 0\n(_)\n )-( ', bg="lightblue")
x.place(x=Loc[0],y=Loc[1])
win.bind("<Key>", doFunction)






win.mainloop()