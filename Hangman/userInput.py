def Introduction():
    print("Hello there!")

    while True:
        name = input("Please enter your name: ")

        if name == '':
            print("You can't have blank as a name")
    print("Thanks!")
    return name

def Menu():
    print("~~Welcome to Hangman!~~")
    print("Hangman is a game where you guess the word by using letters")
    play = input("Would you want to start playing? (y/n) ").lower()
    return play
