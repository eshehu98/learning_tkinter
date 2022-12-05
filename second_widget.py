from tkinter import *

# this creates the root window
root = Tk()

# this creates a frame inside the root window
frame = Frame(root)

# method of placing the widget
frame.pack()

# creates a button and places it inside frame which is inside root
button = Button(frame, text = "Geek")
button.pack()

#standard tkinter event loop
root.mainloop()



