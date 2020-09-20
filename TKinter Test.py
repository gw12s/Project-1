from tkinter import *
from tkinter import messagebox
from data_collection import *


root = Tk()

C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file=r"C:\Users\Owner\OneDrive\Desktop\Project-1\tktestimage.jpg")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.image = background_image


C.pack()

root.mainloop()