from tkinter import *

m = Tk()
m.geometry("400x400")


def change_color():
    w.config(bg = "blue")
    w.config(text = "w's color is" + w.cget("bg"))



w = Button(m, bg = "red", width = 10, height = 5, text = "red")
w.pack()





w.config(command = change_color)






m.mainloop()