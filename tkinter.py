from tkinter import *
from tkinter import ttk
def Prov(*args) :
	mag_label.set(mag-entry.get())
	mag_entry.set("")

root=Tk()
root.title("bestemminetor-2000")

mainframe=ttk.Frame(root, padding="12 20 12 20")
mainframe.grid(column=0,row=0)

mag_entry= StringVar()
mag_label=StringVar()
ttk.Entry(mainframe,width=8,textvariable=msg_entry).grid(column=0,row=0)

ttk.Label(mainframe, text="ella", textvariable=msg_label).grid(column=0, row=1)

root.mainloop()