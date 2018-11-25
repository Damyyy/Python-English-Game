from tkinter import *
def clear_search(event):
    b.delete(0, END)
obj = Tk()
b = Entry(obj,width=100)
b.insert(0,"Enter the value to search")
b.bind("<Button-1>", clear_search)
b.pack()
mainloop()