#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk
from tkinter import *

win= tk.Tk()

s1=IntVar()
s2=IntVar()
s3=IntVar()
s4=IntVar()
s5=IntVar()
s6=IntVar()
s7=IntVar()
s8=IntVar()
entered = StringVar()

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal


    pass
    #return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    n1 = 0
    n2 = 0
    n4 = 0
    n8 = 0
    n16 = 0
    n32 = 0
    n64 = 0
    n128 = 0
    b = int(decimal)
    if b >= 128:
        n128 = 1
        b = b - 128
    if b >= 64:
        n64 = 1
        b = b - 64
    if b >= 32:
        n32 = 1
        b = b - 32
    if b >= 16:
        n16 = 1
        b = b - 16
    if b >= 8:
        b8 = 1
        b = b - 8
    if b >= 4:
        n4 = 1
        b = b - 4
    if b >= 2:
        n2 = 1
        b = b - 2
    if b >= 1:
        n1 = 1
        b = b -1
    binary = (n128+n64+n32+n16+n8+n4+n2+n1)
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = decimal_to_binary(entered.get)
    binary = binary_to_decimal(decimal)
    binary = (binary(0) + binary(1) + binary(2) + binary(3) + binary(4) + binary(5) + binary(6) + binary(7))
    s1.set(binary(0))
    s2.set(binary(1))
    s3.set(binary(2))
    s4.set(binary(3))
    s5.set(binary(4))
    s6.set(binary(5))
    s7.set(binary(6))
    s8.set(binary(7))

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    decimal = binary_to_decimal(binary)


title = tk.Label(win, text="Binary / Decimal converter", font="system")
e1 = tk.Checkbutton(win, variable=s1)
e2 = tk.Checkbutton(win, variable=s2)
e3 = tk.Checkbutton(win, variable=s3)
e4 = tk.Checkbutton(win, variable=s4)
e5 = tk.Checkbutton(win, variable=s5)
e6 = tk.Checkbutton(win, variable=s6)
e7 = tk.Checkbutton(win, variable=s7)
e8 = tk.Checkbutton(win, variable=s8)
b1 = tk.Button(win, text="Convert to Binary", command=get_binary)
b2 = tk.Button(win, text="Convert to Decimal", command=get_decimal)
entry = tk.Entry(win, bd=4, textvariable=entered)

title.grid(row=1, column=1, columnspan=8)
b1.grid(row=3, column=1, columnspan=4)
b2.grid(row=3, column=5, columnspan=8)
e1.grid(row=2, column=1)
e2.grid(row=2, column=2)
e3.grid(row=2, column=3)
e4.grid(row=2, column=4)
e5.grid(row=2, column=5)
e6.grid(row=2, column=6)
e7.grid(row=2, column=7)
e8.grid(row=2, column=8)
entry.grid(row=4,column=1,columnspan=8)

win.mainloop()