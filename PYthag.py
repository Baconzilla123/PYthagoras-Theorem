from ast import Str
import math
import time
import turtle
import os

import tkinter as tk
from tkinter import ttk

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("PYthag")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10, padx=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()



turtle.right(180)

Side1 = 0
Side2 = 0
Square = 0
Hyp = 0

Type = turtle.textinput("PYthag","Hyp (H) | Side (S)")
if Type.lower() == "h":

    Side1 = turtle.numinput("PYthag","side one ")
    Side2 = turtle.numinput("PYthag","side two ")
    
    Square = ((Side1) * (Side1)) + ((Side2) * (Side2))
    Hyp = math.sqrt(Square)

if  Type.lower() == "s":

    Side1 = turtle.numinput("PYthag","side one ")
    Hyp = turtle.numinput("PYthag","hypotenuse ")
    
    if (Hyp) >> (Side1):
        Square = ((Hyp) * (Hyp)) - ((Side1) * (Side1))

    if (Hyp) << (Side1):
        Square = ((Side1) * (Side1)) - ((Hyp) * (Hyp))
    Side2 = math.sqrt((Square))

print("side 1:")
print(Side1)
print("side 2:")
print(Side2)
print("hypotenuse:")
print(Hyp)

x = turtle.xcor()
y = turtle.ycor()

turtle.forward((Side1 * 2))
turtle.right(90)
turtle.forward((Side2 * 2))
turtle.goto(x=(x), y=(y))

message = ("Hypotenuse: " + str(Hyp) + " | Side 1: " + str(Side1) + " | Side 2: " + str(Side2))

popupmsg(message)