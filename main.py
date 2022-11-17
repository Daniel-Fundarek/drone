# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
from tello_asyncio import Tello

from window import Window
from window import FlightState


async def main():
    window = Window()
    drone = Tello()
    state = FlightState.IDLE

    await drone.connect()

    await drone.takeoff()
    await drone.turn_clockwise(360)
    await drone.flip_forward()
    await drone.land()

    await drone.disconnect()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    asyncio.run(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
