from tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="green")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="red", width=3)
w.create_line(0, 100, 50, 80, fill="yellow", width=3)
w.create_line(150,20, 200, 0, fill="green", width=3)
w.create_line(150, 80, 200, 100, fill="pink", width=3)

mainloop()