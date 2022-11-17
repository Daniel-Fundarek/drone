import tkinter

from enum import Enum


class FlightState(Enum):
    LANDING = 1
    FLYING = 2
    IDLE = 3
    CONNECTED = 4
    DISCONNECTED = 5


class DroneCommand(Enum):
    CONNECT = 1
    DISCONNECT = 2
    TAKEOFF = 3
    LAND = 4
    FLIP = 5
    IDLE = 6


class Window:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry('500x500')
        self.command = DroneCommand.IDLE
        self.state = FlightState.IDLE

        self.button1 = tkinter.Button(self.window, text=DroneCommand.TAKEOFF, command=lambda: self.onclick(1))
        self.button1.grid(row=1, column=0)

        self.button2 = tkinter.Button(self.window, text=DroneCommand.FLIP, command=lambda: self.onclick(2))
        self.button2.grid(row=2, column=0)

        self.button3 = tkinter.Button(self.window, text=DroneCommand.CONNECT, command=lambda: self.onclick(3))
        self.button3.grid(row=3, column=0)
        self.window.mainloop()

    def set_name_button(self, text):
        self.button1.config(text=text)

    def onclick(self, button_num):

        if button_num == 1:
            if self.button1['text'] == DroneCommand.TAKEOFF:
                if self.state == FlightState.CONNECTED:
                    self.button1['text'] = DroneCommand.LAND
                    self.command = DroneCommand.TAKEOFF
            else:
                if self.state.FLYING:
                    self.button1['text'] = DroneCommand.TAKEOFF
                    self.command = DroneCommand.LAND

        elif button_num == 2:
            if self.state == FlightState.FLYING:
                self.command = DroneCommand.FLIP


        elif button_num == 3:
            if self.state == FlightState.IDLE:
                self.command = DroneCommand.CONNECT
                self.button3['text'] = DroneCommand.DISCONNECT
                return
            if self.state == FlightState.CONNECTED:
                self.command = DroneCommand.DISCONNECT
                self.button3['text'] = DroneCommand.CONNECT




    def set_state(self, state):
        self.state = state


    def get_state(self):
        return self.state


    def get_command(self):
        return self.command


    def set_command(self, command):
        self.command = command
