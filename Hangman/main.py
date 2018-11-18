import random
import pygame as py
import randomwordgenerator as rwg
import userInput as ui
import outputDisplay as od
import process as p

num_words = 20
x = rwg.generate_random_words(n = num_words)
print(x)

file = open("wordlist.txt","r")
wordList = file.read().split(",")
file.close()
print(wordList)

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

play = ui.Menu()

if play == "y":
    ui.Menu()
