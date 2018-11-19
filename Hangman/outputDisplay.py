import tkinter as tk

from tkinter import *


import  process



# def display():
#
#
#     root = Tk()
#     frame1 = Frame(root)
#     frame1.pack()
#     frame2 = Frame(root)
#     frame2.pack(side=BOTTOM)
#     theLabel = Label(frame1, text="This is hangman", fg="red")
#     theLabel.pack(fill=X)
#
#
#     button1 = Button(frame2, text="Start Game", fg="red")
#     button2 = Button(frame2, text="View High scores", fg="red")
#     button3 = Button(frame2, text="Instructions", fg="red")
#
#     button1.pack()
#     button2.pack()
#     button3.pack()
#     root.mainloop()
#
#
#
# class MainMenu(tkinter.Tk):
#     def __init__(self, master):
#         master = master
#         frame = Frame(master)
#         frame.pack()
#         self.gameTitle = Label(frame, text="Hang Me", fg="red")
#         self.gameTitle.pack()
#         self.button1 = Button(frame, text="Start Game", fg="red", command=self.start_game)
#         self.button1.pack()
#         self.button2 = Button(frame, text="Scores", fg="red", command=self.view_scores)
#         self.button2.pack()
#         self.button3 = Button(frame, text="Instructions", fg="red", command=self.view_instructions)
#         self.button3.pack()
#
#
#     def start_game(self):
#         print("Start game Tapped")
#         run = GamePlay
#
#
#     def view_scores(self):
#         print("view scores tapped")
#
#     def view_instructions(self):
#         print("View instructions tapped")
#
#
#
#
# class GamePlay:
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#         self.gameTitle = Label(frame, text="Game Play Here", fg="red")
#         self.gameTitle.pack()
#



LARGE_FONT= ("Verdana", 12)


class MainMenu(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Add Pages here
        for F in (StartPage, PageOne, PageTwo, UserNamePage, GamePlay):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="HANG FAMILY", font=LARGE_FONT, fg="red")
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Play Game",
                           command=lambda: controller.show_frame(UserNamePage))
        button.pack()

        button2 = tk.Button(self, text="View Scores",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(UserNamePage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()


class UserNamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="ENTER YOUR NAME", font=LARGE_FONT, fg="red")
        label.pack(pady=10,padx=10)

        e = Entry(self)
        e.pack()

        button = tk.Button(self, text="Continue", command=lambda: controller.show_frame(GamePlay), fg="red")
        button.pack()



class GamePlay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="GAME PLAY HERE", font=LARGE_FONT, fg="red")
        label.pack(pady=10,padx=10)

        getWord = process.get_word()

        randomWord = process.process_word(getWord)

        label = tk.Label(self, text=randomWord, fg="blue")
        label.pack()

        e = Entry(self)
        e.pack()

        submitButton = Button(self, text="Submit")

        submitButton.pack()




