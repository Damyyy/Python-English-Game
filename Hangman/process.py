from random_word import RandomWords
import random


from PyDictionary import PyDictionary

dictionary = PyDictionary()



#
# # Return a single random word
# r.get_random_word()
# # Return list of Random words
# r.get_random_words()
# # Return Word of the day
# r.word_of_the_day()




def random_word():

    r = RandomWords()

    word = r.get_random_word()
    print(word)
    # word2 = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10)
    length = len(word)
    toList = list(word)
    processedWord = ""

    for i in range(length // 2):
        randomNumber = random.randint(1, length)
        toList[randomNumber] = "_"

    processedWord = "".join(toList)

    return processedWord