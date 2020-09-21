import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

root = Tk()

#Settings of Window
root.title("Prestige Worldwide")
root.geometry("1200x800")
root.resizable(False, False)

#ColumConfig Settings
root.columnconfigure(0, weight=1)

#Setting stock_name to StringVar variable
stock_name = tk.StringVar()

#Input Frame Settings
input_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
input_frame.grid(row=0, column=0, sticky="NW")

#Creating the "Stock: " Label & Entry field. Applying it to the Input Frame
stock_label = ttk.Label(input_frame, text="Stock: ")
stock_label.grid(row=0, column=0, padx=(0,5))
stock_entry = ttk.Entry(input_frame, width=17, textvariable=stock_name)
stock_entry.grid(row=0, column=1)
stock_entry.focus()

#Processing Stock Entry

#Buttons Frame
buttons = ttk.Frame(root, padding=(10,20))
buttons.grid(sticky='W')

#Close Button space & function
add_button = ttk.Button(buttons, text="Add Stock")
close_button = ttk.Button(buttons, text="Close", command=root.destroy)
add_button.grid(row=0, column=1)
close_button.grid(row=0, column=2)

#Buttons Column Configure
buttons.columnconfigure(0, weight=1)

#End
root.mainloop()