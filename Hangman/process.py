from random_word import RandomWords
import random

#
# # Return a single random word
# r.get_random_word()
# # Return list of Random words
# r.get_random_words()
# # Return Word of the day
# r.word_of_the_day()







class logic(object):

    word = ""
    blanked = ""
    wordLength = 0

    guessed = []
    correct = []
    wrong = []
    points = 0
    
    def __init__(self):
        # Word Related
        self.word = ""
        self.blanked = ""
        self.wordLength = 0
        # Guess Related
        self.guessed = []
        self.correct = []
        self.wrong = []

    def get_word(self):
        r = RandomWords()
        w = r.get_random_word()
        self.word = w
        print(self.word)


    def process_word(self):
        self.wordLength = len(self.word)
        emptyWord = []
        for i in range(self.wordLength):
            emptyWord.append("_ ")

        processedWord = "".join(emptyWord)

        self.blanked = processedWord




    def check_letter(self, letterGuess):
        if letterGuess not in self.wrong and letterGuess not in self.correct:
            if letterGuess in self.word:
                self.points += 1
                self.correct.append(letterGuess)
            else:
                self.wrong.append(letterGuess)


        print(self.points)














