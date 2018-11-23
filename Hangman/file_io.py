
import process

class User(object):
    def __init__(self):
        self.name = ''
        self.wordsCorrect = 0
        self.points = 0
    def setName(self, name):
        self.name = name
    def setValues(self, points, wordsCorrect):
        self.points = points
        self.wordsCorrect = wordsCorrect
    def test(self):
        print(self.name)
        print(self.points)



class IO():
    def saveToText(self):
        file = open('scores.txt','w')
        # file.write(User.name)
        # file.write(process.logic.points)
        # file.close()