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

    def __init__(self):

        self.scores = ""


    def saveToText(self, userName, points):

        # Error will occure if text file does not exist
        # Using try catch to evaluate if the text file exist or not
        # If it does not it will create one before being read

        # If no error then it will proceed reading, updating dictionary and writing it back to textfile

        try:
            file = open('scores.txt', 'r')

            # Get existing values from textfile
            read = open('scores.txt', 'r')
            content = read.read()
            contentToDict = eval(content)
            # Add value to dictionary
            contentToDict.update({userName: str(points)})
            read.close()
            file = open('scores.txt', 'w')
            # Write dictinary to textfile in jason format
            file.write(json.dumps(contentToDict))
            file.close()


        except IOError:
            # Due to error of file not existing, create one
            initialize = open('scores.txt', 'w')
            initialize.write(json.dumps({'': ''}))

            initialize.close()

            # Get existing values from textfile
            read = open('scores.txt', 'r')
            content = read.read()
            contentToDict = eval(content)
            # Add value to dictionary
            contentToDict.update({userName: str(points)})
            read.close()
            file = open('scores.txt', 'w')
            # Write dictinary to textfile in jason format
            file.write(json.dumps(contentToDict))
            file.close()


            file = open('scores.txt', 'r')
            # Write dictinary to textfile in jason format
            val = file.read()
            valToDict = eval(val)
            file.close()

            del valToDict[""]


            file = open('scores.txt', 'w')
            # Write dictinary to textfile in jason format
            file.write(json.dumps(valToDict))
            file.close()






    def readFromText(self):
        try:
            file = open('scores.txt', 'r')
            value = file.read()

            toDictionary = eval(value)

            print(toDictionary)

            print(type(toDictionary))
            self.scores = toDictionary

            self.scores = '\n'.join("{}: {}".format(k, v) for k, v in toDictionary.items())

        except IOError:
            print("Error")


