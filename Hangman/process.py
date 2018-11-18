from random_word import RandomWords


def set_player_name():
    playerName = input("PlayerName: ")
    return playerName


def random_word():
    r = RandomWords()

    # # Return a single random word
    # r.get_random_word()
    # # Return list of Random words
    # r.get_random_words()
    # # Return Word of the day
    # r.word_of_the_day()
    randomWord = r.get_random_word()
    return randomWord




