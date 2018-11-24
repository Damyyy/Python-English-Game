import tkinter as tk

from tkinter import *

import process
import file_io

LARGE_FONT = ("Verdana", 12)


class MainMenu(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.user = file_io.User()
        self.scoresObject = file_io.IO()
        self.correctWord = process.showAnswer()

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack()

        self.frames = {}

        # Add Pages here
        for F in (StartPage, PageOne, PageTwo, UserNamePage, GamePlay, LoosingPage, WinningPage, ViewScores):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="THE HARDEST WORD GAME EVER", font=LARGE_FONT, fg="green")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Play Game",
                           command=lambda: controller.show_frame(UserNamePage), fg="white", bg='green', height=2,
                           width=10)
        button.pack(pady=30, padx=30)

        # button2 = tk.Button(self, text="View Scores",
        #                     command=lambda: controller.show_frame(PageTwo), height=2, width=10)

        def multifunction():
            controller.scoresObject.readFromText()
            controller.show_frame(ViewScores)

        button2 = tk.Button(self, text="View Scores",
                            command=lambda: multifunction(), height=2, width=10, fg="white", bg='green')
        button2.pack(pady=30, padx=30)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage), height=2, width=10, bg="#00ffff")
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne), height=2, width=10)
        button2.pack()


class UserNamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="ENTER YOUR NAME", font=LARGE_FONT, fg="green")
        label.pack(pady=10, padx=10)

        e = Entry(self)
        e.pack(pady=10, padx=10)

        def e_delete():
            e.delete(first=0, last=22)

        def multiFunction():
            # user = file_io.User()
            if e.get() != '':
                controller.user.setName(e.get())
                e_delete()
                controller.user.test()
                controller.show_frame(GamePlay)

        button = tk.Button(self, text="Continue", command=multiFunction, fg="green", height=2, width=10)

        button.pack(padx=5, pady=5)


class GamePlay(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="GUESS THE WORD IF U CAN!", font=LARGE_FONT, fg="green")
        label.pack(pady=10, padx=10)
        # Instance

        logic = process.logic()
        logic.get_word()
        logic.process_word()
        logic.count_required_points()
        print(logic.blanked)

        # label = tk.Label(self, text=logic.blanked, fg="blue")
        # label.pack()
        v = StringVar()
        Label(self, textvariable=v, font=("Helvetica", 32)).pack(pady=30, padx=30)

        v.set(logic.blanked)

        e = Entry(self, width=20)

        e.pack(pady=30, padx=30)

        triesLeft = StringVar()
        triesLeft.set(logic.triesLeft)

        lettersTested = StringVar()
        lettersTested.set(logic.totalTested)

        def e_delete():
            e.delete(first=0, last=22)

        def rebuild():
            if logic.triesLeft <= 1:
                controller.user.setPoints(logic.points)
                controller.correctWord.correctAnswer(logic.word)
                file_io.IO.saveToText(self, controller.user.name, controller.user.points)
                logic.reset()
                controller.show_frame(LoosingPage)
                e_delete()
                v.set(logic.blanked)
                lettersTested.set(logic.totalTested)
                triesLeft.set(logic.triesLeft)

            if logic.triesLeft >= 0:
                if e.get() != "":
                    logic.check_letter(e.get().lower())
                    e_delete()
                    # label = tk.Label(self, text=logic.blanked, fg="blue")
                    # label.pack()
                    v.set(logic.blanked)
                    triesLeft.set(logic.triesLeft)
                    logic.tested_letters()
                    lettersTested.set(logic.totalTested)

            if logic.points == logic.requiredPoints:
                controller.user.setPoints(logic.points)
                logic.reset()
                controller.show_frame(WinningPage)
                v.set(logic.blanked)
                lettersTested.set(logic.totalTested)
                triesLeft.set(logic.triesLeft)

        submitButton = Button(self, text="Submit", command=lambda: rebuild(), height=2, width=10, fg="white",
                              bg='green')
        submitButton.pack(pady=10, padx=10)

        tested = Label(self, textvariable=lettersTested, font=("Helvetica", 20))
        tested.pack()

        triesLeftLable = Label(self, textvariable=triesLeft, font=("Helvetica", 20))
        triesLeftLable.pack()

        def multifunction():
            controller.user.setPoints(logic.points)
            controller.correctWord.correctAnswer(logic.word)
            file_io.IO.saveToText(self, controller.user.name, controller.user.points)
            logic.reset()
            controller.show_frame(LoosingPage)
            v.set(logic.blanked)
            lettersTested.set(logic.totalTested)
            triesLeft.set(logic.triesLeft)

        quitButton = Button(self, text="Quit", height=2, width=10, command=lambda: multifunction(), fg="white",
                            bg='red')
        quitButton.pack(pady=10, padx=10)


class LoosingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="YOU LOOSE! HAHAHAHAHAHA", font=LARGE_FONT, fg="red")
        label.pack(pady=10, padx=10)
        # correctAnswer = tk.Label(self, text="", font=LARGE_FONT, fg="red")
        # label.pack(pady=10, padx=10)

        v = StringVar()
        v.set(controller.correctWord.correctWord)

        labe12 = tk.Label(self, textvariable=v, font=LARGE_FONT, fg="red")
        labe12.pack(pady=10, padx=10)

        buttonAnswer = tk.Button(self, text="Show Answer", command=lambda: getWord(), fg="white",
                                 bg='green')
        buttonAnswer.pack()

        def getWord():
            v.set(controller.correctWord.correctWord)

        button = tk.Button(self, text="Continue", command=lambda: clearAndNavigate(), fg="white",
                           bg='green')
        button.pack()

        def clearAndNavigate():
            v.set('')
            controller.show_frame(StartPage)


class WinningPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="YOU WIN YAY!", font=LARGE_FONT, fg="green")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Continue", command=lambda: controller.show_frame(GamePlay), fg="white",
                           bg='green')
        button.pack()


class ViewScores(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.scoresObject.readFromText()

        v = StringVar()
        v.set(controller.scoresObject.scores)
        label = tk.Label(self, textvariable=v, font=LARGE_FONT, fg="black")

        label.pack(pady=10, padx=10)

        buttonRebuild = tk.Button(self, text="Click To See Score Updates", command=lambda: rebuld(), fg="white",
                                  bg='green')
        buttonRebuild.pack(pady=5, padx=5)
        button = tk.Button(self, text="Back To Homepage", command=lambda: controller.show_frame(StartPage), fg="white",
                           bg='green')
        button.pack(pady=5, padx=5)

        def rebuld():
            v.set(controller.scoresObject.scores)
