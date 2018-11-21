# Modules
import outputDisplay
from pygame import mixer



# Other Modules

mixer.init()
mixer.music.load('sound.mp3')
mixer.music.play(loops=-1)


app = outputDisplay.MainMenu()
app.title("Game")
app.geometry("800x500")
# app.configure(background="black")
app.mainloop()


