from tkinter import *

canvas_width = 800
canvas_height =500

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="C:\\Users\\Admin\\Pictures\\stiven-gaviria-bP1mA1s26vk-unsplash.jpg")
canvas.create_image(20,30, anchor=NW, image=img)

mainloop()
