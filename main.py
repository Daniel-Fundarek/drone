# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
from tello_asyncio import Tello

from window import Window
from window import FlightState
from window import DroneCommand


async def main():
    window = Window()
    drone = Tello()
    state = FlightState.IDLE
    command = DroneCommand.IDLE
    while state != FlightState.DISCONNECTED:
        state = window.get_state()
        command = window.get_command()

        if state == FlightState.IDLE and command == DroneCommand.CONNECT:
            await drone.connect()
            state = FlightState.CONNECTED
        if state == FlightState.CONNECTED and command == DroneCommand.DISCONNECT:
            await drone.disconnect()
            state = FlightState.DISCONNECTED

        if state == FlightState.CONNECTED and command == DroneCommand.TAKEOFF:
            await drone.takeoff()
            state = FlightState.FLYING

        if state == FlightState.FLYING and command == DroneCommand.LAND:
            await drone.land()
            state = FlightState.CONNECTED

        if state == FlightState.FLYING and command == DroneCommand.FLIP:
            await drone.flip_forward()

        command = DroneCommand.IDLE
        window.set_state(command)
        window.set_command(command)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
