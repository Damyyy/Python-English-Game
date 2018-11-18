from tkinter import *


def display():


    root = Tk()
    frame1 = Frame(root)
    frame1.pack()
    frame2 = Frame(root)
    frame2.pack(side=BOTTOM)
    theLabel = Label(frame1, text="This is hangman", fg="red")
    theLabel.pack(fill=X)


    button1 = Button(frame2, text="Start Game", fg="red")
    button2 = Button(frame2, text="View High scores", fg="red")
    button3 = Button(frame2, text="Instructions", fg="red")

    button1.pack()
    button2.pack()
    button3.pack()
    root.mainloop()



