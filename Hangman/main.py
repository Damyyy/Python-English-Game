import random
import randomwordgenerator
import userInput as UI
import outputDisplay as OD
import process as P


file = open("wordlist.txt","r")
wordList = file.read().split(",")
file.close()
print(wordList)

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

play = UI.Menu()

if play == "y":
    UI.Menu()
