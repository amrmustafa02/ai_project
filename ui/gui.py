from tkinter import *

import customtkinter

listAlgorithms = ["Min max", "Alpha Beta"]

frame = Tk()


def initScreen():
    frame.title("Connect 4")
    setScreenLocation()
    frame['background'] = 'white'
    addAlgorithmsMenu()
    addLevelMenu()
    frame.mainloop()


def moveWindow(event):
    frame.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


def setScreenLocation():
    window_height = 600
    window_width = 600
    # get the screen dimension
    screen_width = frame.winfo_screenwidth()
    screen_height = frame.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


def button_event():
    print("button pressed")
    frame.destroy()


def addAlgorithmsMenu():
    # add label and set location
    label = Label(frame, text='Select Algorthm', width=15, background="white")
    label.grid(row=1, column=2)

    # add menu options
    options = StringVar(frame)
    options.set("Min max")  # default value

    menu = OptionMenu(frame, options, listAlgorithms[0], listAlgorithms[1])
    menu.grid(row=1, column=3)


def addLevelMenu():
    # add label and set location
    label = Label(frame, text='Select Level', width=15, background="white")
    label.grid(row=3, column=2)

    # add menu options
    options = StringVar(frame)
    options.set("easy ")  # default value

    menu = OptionMenu(frame, options, "easy", "meduim", "hard")
    menu.grid(row=3, column=3)


def addButton():
    button = customtkinter.CTkButton(master=frame, text="Min max algorithm", command=button_event)
    button.pack(padx=10, pady=50)


initScreen()
