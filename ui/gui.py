from tkinter import *
from lab_code import game

listAlgorithms = ["Min max", "Alpha Beta"]
listLevel = ["Easy", "Medium", "Hard"]

values = {
    "Easy": 2,
    "Medium": 4,
    "Hard": 7,
    "Min max": 1,
    "Alpha Beta": 2
}
frame = Tk()


class Gui:
    def __init__(self):
        self.algoOptions = StringVar
        self.levelOptions = StringVar

    def initScreen(self):
        frame.title("Connect 4")
        self.setScreenLocation()
        frame['background'] = 'white'
        self.addAlgorithmsMenu()
        self.addLevelMenu()
        self.addButton()
        frame.mainloop()

    def setScreenLocation(self):
        window_height = 600
        window_width = 600
        # get the screen dimension
        screen_width = frame.winfo_screenwidth()
        screen_height = frame.winfo_screenheight()
        # find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def addAlgorithmsMenu(self):
        # add label and set location
        label = Label(frame, text='Select Algorthm', width=15, background="white")
        label.grid(row=1, column=2)

        # add menu options
        self.algoOptions = StringVar(frame)
        self.algoOptions.set("Select one")  # default value

        menu = OptionMenu(frame, self.algoOptions, *listAlgorithms)
        menu.grid(row=1, column=3)

    def addLevelMenu(self):
        # add label and set location
        label = Label(frame, text='Select Level', width=15, background="white")
        label.grid(row=3, column=2)

        # add menu options
        self.levelOptions = StringVar(frame)
        self.levelOptions.set("select one")  # d
        # efault value

        menu = OptionMenu(frame, self.levelOptions, *listLevel)
        menu.grid(row=3, column=3)

    def addButton(self):
        label = Label(frame, text='Start game', width=15, background="white")
        label.grid(row=4, column=2)
        btn = Button(frame, text="ok", command=lambda: self.clickOnButton())
        btn.grid(row=4, column=3)

    def clickOnButton(self):
        algo = values.get(self.algoOptions.get())
        level = values.get(self.levelOptions.get())
        print('test')
        frame.destroy()
        game.main(algo, level)


gui = Gui()
gui.initScreen()
