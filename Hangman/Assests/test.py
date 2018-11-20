from tkinter import *        
from PIL import ImageTk, Image


app_root = Tk()

#Setting it up
hangfamily = ImageTk.PhotoImage(Image.open("Hangfamily.png"))
img = ImageTk.PhotoImage(Image.open("Image 1.png"))
img1 = ImageTk.PhotoImage(Image.open("Image 2.png"))
#Displaying it
imglabel = Label(app_root, image=hangfamily).grid(row=1, column=1)
imglabel = Label(app_root, image=img).grid(row=2, column=1)        
imglabel = Label(app_root, image=img1).grid(row=2, column=2)

app_root.mainloop()
