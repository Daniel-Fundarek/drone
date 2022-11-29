# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import asyncio
#from tello_asyncio import Tello

from window import Window
from window import FlightState
from window import DroneCommand
from serialCom import SerialCom

def main():
    #window = Window()
    serial = SerialCom()
    #dgfg
    serial.continous_read()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
