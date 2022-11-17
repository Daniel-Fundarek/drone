import tkinter

from enum import Enum


class FlightState(Enum):
    TAKEOFF = 1
    LAND = 2
    LANDING = 3
    FLYING = 4
    IDLE = 5


class Window:




    def __init__(self):
        window = tkinter.Tk()
        window.resizable(True, True)
        window.geometry('500x500')

        button1 = tkinter.Button(window, text=FlightState.TAKEOFF, command= self.onclick())
        button1.place(x=25, y=100)
        button1.up

        button2 = tkinter.Button(window, text="flip")
        button2.place(x=100, y=25)

        button3 = tkinter.Button(window, text="flip")
        button3.place(x=100, y=25)
        window.mainloop()

    def set_name_button(self, text):
        self.button1.config(text=text)

    def onclick(self):

        pass
