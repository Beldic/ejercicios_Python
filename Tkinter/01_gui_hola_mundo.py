from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Entrada de datos")
frm = ttk.Frame(root , padding = 10, width="500", height= "500")
frm.grid()
ttk.Entry(root).grid(column = 0, row= 1)
ttk.Label(frm, text ="Bienvenida").grid(column = 0, row= 0)
ttk.Button(frm, text="Quit", command= root.destroy).grid(column = 0, row=3)
root.mainloop()