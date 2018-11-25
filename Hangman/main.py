# Modules
import outputDisplay





# try running the code. If error occors we will print out message to inform user
try:
    app = outputDisplay.MainMenu()
    app.title("Game")
    app.geometry("800x500")
    # Main Loop
    app.mainloop()

except:
    print("An error has occured!. Please ensure you have installed the required packages.")

