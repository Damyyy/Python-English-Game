def Introduction():
    print("Hello there!")

    while True:
        name = input("Please enter your name: ")

        if name == '':
            print("You can't have blank as a name")
        else:
            print("Thanks!")
            return name

def Menu(name):
    print("~~Welcome to Hangman,",name,"!~~")
    print("Hangman is a game where you guess the word by using letters")
    play = input("Would you want to start playing? (y/n) ").lower()
    return play
