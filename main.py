# step1 Importing
import tkinter as tk 
from tkinter import *


# step 2 GUI intrection

window=tk.Tk()
window.geometry("400x400")
window.title("Calculator")

# step 3. Adding input

input_box=Entry(window, width=57, borderwidth=5)
input_box.place(x=20, y=20)

# click functionlaity

def button_click(number):
    current=input_box.get()
    input_box.delete(0, END)
    input_box.insert(0, str(current) + str(number))

# Buttons

button_1=Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_1.place(x=10, y=70)
button_2=Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_2.place(x=100, y=70)
button_3=Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_3.place(x=190, y=70) 
button_4=Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_4.place(x=10, y=140) 
button_5=Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_5.place(x=100, y=140)
button_6=Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_6.place(x=190, y=140)
button_7=Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_7.place(x=10, y=210)
button_8=Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_8.place(x=100, y=210)
button_9=Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_9.place(x=190, y=210)
button_0=Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_0.place(x=100, y=280)
button_add=Button(window, text="+", padx=40, pady=20, command=lambda: button_click("+"))
button_add.place(x=280, y=70)
button_subtract=Button(window, text="-", padx=40, pady=20,  command=lambda: button_click("-"))
button_subtract.place(x=280, y=140)
button_multiply=Button(window, text="*", padx=40, pady=20, command=lambda: button_click("*"))
button_multiply.place(x=280, y=210)
button_divide=Button(window, text="/", padx=40, pady=20, command=lambda: button_click("/"))
button_divide.place(x=280, y=280)

button_clear=Button(window, text="C", padx=40, pady=20, command=lambda: input_box.delete(0, END))
button_clear.place(x=10, y=280)


# Mathematical functionality
def button_equal():
    expression=input_box.get()
    try:
        result=eval(expression)
        input_box.delete(0, END)
        input_box.insert(0, str(result))
    except:
        input_box.delete(0, END)
        input_box.insert(0, "Error")
button_equal=Button(window, text="=", padx=40, pady=20, command=button_equal)
button_equal.place(x=190, y=280)


# step 4 main loop

window.mainloop()