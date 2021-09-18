from tkinter import *

canvas_width = 150
canvas_height =150

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

w.create_oval(10,50,140,100)

mainloop()