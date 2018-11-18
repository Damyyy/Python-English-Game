import random
import pygame as py
import randomwordgenerator as rwg
import userInput as ui
import outputDisplay as od
import process as p
import sys

file = open("wordlist.txt","r")
wordList = file.read().split(",")
file.close()
print(wordList)

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

name = ui.Introduction()

while True:
    play = ui.Menu(name)
    if play == "n":
        print("Closing Down Program")
        sys.exit()

    elif play == "y":
        print("Let's Start!")
        continue

    else:
        print("Please enter either y/n.")
        continue
