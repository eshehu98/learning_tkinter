from tkinter import *
from tkinter.ttk import *

# create the main window object named root
root = Tk()

# titling the main window object
root.title("First_Program")

# the label "widget" is what the label will be on the screen
label = Label(root, text = "hello world").pack()

# the following function call will telll the code to keep displaying the program
root.mainloop()
