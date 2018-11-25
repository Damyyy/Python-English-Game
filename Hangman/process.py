from random_words import RandomWords
from pygame import mixer


class logic(object):

    def __init__(self):
        # Word Related
        self.word = ""
        self.blanked = ""
        self.wordLength = 0
        # Guess Related
        self.guessed = []
        self.correct = []
        self.wrong = []
        self.points = 0
        self.wrongCount = 0
        self.triesLeft = 10
        self.totalTested = ""
        self.requiredPoints = 0
        self.abcd = "abcdefghijklmnopqrstuvwxyz-"

    # Gets Random Word
    def get_word(self):
        rw = RandomWords()
        word = rw.random_word()
        self.word = word.lower()

        # To show word on terminal for demo purposes only
        print(self.word)

    # Makes Blanked word version

    def process_word(self):
        self.wordLength = len(self.word)
        emptyWord = []
        for i in range(self.wordLength):
            emptyWord.append("_ ")

        processedWord = "".join(emptyWord)

        self.blanked = processedWord

    # Check if letter guessed is in the word
    # If yes then points added
    # If wrong, tries will be deducted
    def check_letter(self, letterGuess):
        if letterGuess not in self.wrong and letterGuess not in self.correct:
            if letterGuess in self.word:
                mixer.init()
                mixer.music.load('correct.mp3')
                mixer.music.play()
                self.correct.append(letterGuess)
                self.points += 1
            else:
                self.wrong.append(letterGuess)
                mixer.init()
                mixer.music.load('wrong.mp3')
                mixer.music.play()
                self.wrongCount += 1
                self.triesLeft -= 1

        self.rebuild_blankedWord()

    # Rebuilds blank word after a new letter is guessed
    def rebuild_blankedWord(self):

        toList = list(self.blanked)
        wordToList = list(self.word)

        for i in range(self.wordLength):
            if wordToList[i] in self.correct:
                toList[i * 2] = wordToList[i]

        self.blanked = "".join(toList)
    # Make a string to show users what inout they have tried
    def tested_letters(self):
        self.totalTested = "".join(self.correct) + "".join(self.wrong)
    # Count required points to win
    def count_required_points(self):
        toList = list(self.abcd)

        for i in range(self.wordLength):
            if self.word[i] in self.abcd:
                self.requiredPoints += 1
                toList.remove(self.word[i])
                self.abcd = "".join(toList)

    # Reset all values
    def reset(self):

        # Word Related
        # self.word = ""
        # self.blanked = ""
        self.wordLength = 0
        # Guess Related
        self.guessed = []
        self.correct = []
        self.wrong = []
        self.points = 0
        self.wrongCount = 0
        self.triesLeft = 10
        self.totalTested = ""
        self.requiredPoints = 0
        self.get_word()
        self.process_word()
        self.abcd = "abcdefghijklmnopqrstuvwxyz-"
        self.count_required_points()


# This class is use to give the correct answer to user if they lose
class ShowAnswer(object):

    def __init__(self):
        self.correctWord = ''

    def correctAnswer(self, word):
        self.correctWord = word

    def getCorrectAnswer(self):
        return self.correctWord
