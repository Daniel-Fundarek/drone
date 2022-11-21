import tkinter
import asyncio
from djitellopy import Tello
# from tello_asyncio import Tello
from enum import Enum
import threading


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
        self.drone = Tello()

        self.button1 = tkinter.Button(self.window, text=DroneCommand.TAKEOFF, command=lambda: self.start_onclick_thread(1))
        self.button1.grid(row=1, column=0)

        self.button2 = tkinter.Button(self.window, text=DroneCommand.FLIP, command=lambda: self.start_onclick_thread(2))
        self.button2.grid(row=2, column=0)

        self.button3 = tkinter.Button(self.window, text=DroneCommand.CONNECT, command=lambda: self.start_onclick_thread(3))
        self.button3.grid(row=3, column=0)
        self.button1 = tkinter.Button(self.window, text=DroneCommand.LAND, command=lambda: self.start_onclick_thread(4))
        self.button1.grid(row=1, column=1)

        self.button2 = tkinter.Button(self.window, text='Battery status', command=lambda: self.start_onclick_thread(5))
        self.button2.grid(row=2, column=1)

        self.window.mainloop()

    def set_name_button(self, text):
        self.button1.config(text=text)

    def start_onclick_thread(self, num):
        threading.Thread(target=lambda: self.onclick(num)).start()

    def onclick(self, button_num):

        if button_num == 1:

            self.drone.takeoff()
            # self.takeoff(True)

        elif button_num == 2:
            # self.drone.flip_back()

            self.drone.flip_right()

            # self.flip()

        elif button_num == 3:

            self.drone.connect()
            # self.connect(True)

        elif button_num == 4:
            self.drone.land()
            # self.takeoff(False)

        elif button_num == 5:
            battery = self.drone.get_battery()
            print(f'battery percentage: {battery}%')
        # self.disconnect(False)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def get_command(self):
        return self.command

    def set_command(self, command):
        self.command = command
