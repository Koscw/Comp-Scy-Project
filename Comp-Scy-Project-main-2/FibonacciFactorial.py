import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

win=Tk()
win.title("fibonacci sequence and factorial calculator")
win.geometry("400x200")
win.resizable(width=True,height=True)
title=ttk.Label(win,text="Enter a number, Then click on the function you want.")
title.pack()
entry=ttk.Entry(win,width=10)
entry.pack()


def Fibonacci ():

  try:
    x = int(entry.get())
    if x<=0:
      t.set("Input invalid")
    else:
      x=int(x)
      if x==1:
        t.set("Answer: [0]")
      elif x==2:
        t.set("Answer: [0,1]")
      else:
        y = [0, 1]
        for i in range(2, x):
          y.append(y[i - 1] + y[i - 2])
        t.set(f"Answer: {y}")
  except Exception as e:
    messagebox.showerror("Input Is Invalid", "Please enter a valid integer")

def factorial(x):
  x=int(x)
  if x<=1:
    return 1
  else:
    return x*factorial(x-1)

def fac2():
  try:
    x = float(entry.get())
    ngt = 0
    if x < 0:
      x = x * -1
      ngt = 1
    t.set(f"Answer: {factorial(x)}")
    if ngt == 1:
      t.set(f"Answer: -{factorial(x)}")
  except Exception as e:
    messagebox.showerror("Input Is Invalid", "Please enter a valid number")






boton_1=ttk.Button(win,text="Fibonacci", command=Fibonacci)
boton_2=ttk.Button(win,text="Factorial", command=fac2)
boton_1.pack()
boton_2.pack()
t = tk.StringVar()
l = tk.Label(win,textvariable=t)
l.pack()
t.set("Enter a number")

win.mainloop()
