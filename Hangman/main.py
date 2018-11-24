# Modules
import outputDisplay
from pygame import mixer



# Other Modules

# mixer.init()
# mixer.music.load('sound.mp3')
# mixer.music.play(loops=-1)

# Without Wifi the app will not run properly
# Using try exception to handle the errors of no wifi

try:
    app = outputDisplay.MainMenu()
    app.title("Game")
    app.geometry("800x500")
    # Main Loop
    app.mainloop()

except:
    print("Please Check Your Wifi Connection")

