from random_word import RandomWords
import random

#
# # Return a single random word
# r.get_random_word()
# # Return list of Random words
# r.get_random_words()
# # Return Word of the day
# r.word_of_the_day()


def get_word():
    r = RandomWords()
    w = r.get_random_word()
    return w


def process_word(word):
    word = word
    length = len(word)
    toList = list(word)

    emptyWord = []

    for i in range(length):
        emptyWord.append("_ ")

    processedWord = "".join(emptyWord)

    return processedWord, word



def check_word(word, guess):
    marks = 0

    if guess in word:
        marks += 1

    print(marks)
    return marks





