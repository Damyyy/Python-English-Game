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

    def reset(self):
        self.points = 0


class IO():

    def __init__(self):

        self.scores = ""
        self.temporaryDict = {'': ''}

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
            contentToDict.update({userName: points})
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
            contentToDict.update({userName: points})
            read.close()
            file = open('scores.txt', 'w')
            # Write dictionary to textfile in jason format
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
        # Try to read from text file
        # If no file written yet it will be unable to read
        # If no file available try exception will be use to catch and handle error


        try:
            file = open('scores.txt', 'r')
            value = file.read()
            self.temporaryDict = {'': ''}
            self.scoreString = ''

            toDictionary = eval(value)

            listofTuples = sorted(toDictionary.items(), reverse=True, key=lambda x: x[1])

            # Arranging scores based on values
            for elem in listofTuples:
                self.temporaryDict.update({elem[0]: elem[1]})
                line = '\n' + elem[0] + ' : ' + str(elem[1])
                self.scoreString = self.scoreString + line

            self.scores = self.scoreString



        except IOError:
            print("File will be created")
