
import process
import json

class User(object):
    def __init__(self):
        self.name = ''
        self.wordsCorrect = 0
        self.points = 0
    def setName(self, name):
        self.name = name
    def setPoints(self, points):
        self.points += points
    def test(self):
        print(self.name)
        print(self.points)



class IO():
    def saveToText(self, userName, points):

        info = {userName : str(points)}
        file = open('scores.txt','w')
        # file.write(userName)
        # file.write(str(points))
        file.write(json.dumps(info))
        # file.write(process.logic.points)
        file.close()
    def readFromText(self):
        file = open('scores.txt', 'r')
        print(file.read())
        print(type(file.read()))

