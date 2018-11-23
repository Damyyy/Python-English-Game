from random_word import RandomWords
from pygame import mixer



# Other Modules


# from PyDictionary import PyDictionary



class logic(object):

    # word = ""
    # blanked = ""
    # wordLength = 0
    #
    # guessed = []
    # correct = []
    # wrong = []
    # points = 0

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
        self.triesLeft = 15
        self.totalTested = ""
        self.requiredPoints = 0
        self.abcd = "abcdefghijklmnopqrstuvwxyz-"

    def get_word(self):
        r = RandomWords()
        w = r.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=5)
        self.word = w.lower()

        print(self.word)

        # dictionary = PyDictionary()
        # print(dictionary.meaning(self.word, features = "lxml"))


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
                self.correct.append(letterGuess)
                self.points += 1
                print("POINTS" + str(self.points) + "FROM ____" + letterGuess)

            else:
                self.wrong.append(letterGuess)
                self.wrongCount += 1
                self.triesLeft -= 1


        print(self.correct)
        print(self.wrong)
        self.rebuild_blankedWord()

    def rebuild_blankedWord(self):

        toList = list(self.blanked)
        wordToList = list(self.word)

        for i in range(self.wordLength):
            if wordToList[i] in self.correct:
                toList[i * 2] = wordToList[i]



        self.blanked = "".join(toList)
        print(self.blanked)


    def tested_letters(self):

        self.totalTested = "".join(self.correct) + "".join(self.wrong)
        print(self.totalTested)






    def count_required_points(self):
        toList = list(self.abcd)


        for i in range(self.wordLength):
            if self.word[i] in self.abcd:
                self.requiredPoints += 1
                toList.remove(self.word[i])
                self.abcd = "".join(toList)

        print("REQUIRED POINTS" + str(self.requiredPoints))




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
        self.triesLeft = 15
        self.totalTested = ""
        self.requiredPoints = 0
        self.get_word()
        self.process_word()
        self.abcd = "abcdefghijklmnopqrstuvwxyz-"
        self.count_required_points()




















