# This is a sample Python script.
import threading

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import asyncio
# from tello_asyncio import Tello
from djitellopy import Tello
from window import Window
from window import FlightState
from window import DroneCommand
from serialCom import SerialCom


def main():
    tello = Tello()
    serial = SerialCom(tello)
    threading.Thread(target=lambda: Window(tello,serial)).start()
    serial.continous_read()


# threading.Thread(target=lambda: Window(tello))
# serial.continous_read()

# dgfg
# serial.continous_read()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
