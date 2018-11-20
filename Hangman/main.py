# Modules
import outputDisplay
from pygame import mixer



# Other Modules

mixer.init()
mixer.music.load('sound.mp3')
mixer.music.play()

app = outputDisplay.MainMenu()
app.mainloop()


