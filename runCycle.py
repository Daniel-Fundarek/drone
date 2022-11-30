import time

from window import FlightState
from window import DroneCommand
from window import ConnectionState
from window import ConnectionCommand
import threading
import tkinter
from djitellopy import Tello


class RunCycle:

    def __init__(self):
        self.command = DroneCommand.IDLE
        self.state = FlightState.IDLE
        self.connectionState = ConnectionState.DISCONNECTED
        self.drone = Tello()
        self.connectionCommand = ConnectionCommand.DISCONNECT

    def controlDrone(self):
        remoteControll = 1
        left_right_velocity = 5
        forward_backward_velocity = 5
        up_down_velocity = 0
        yaw_velocity = 0

        if remoteControll == 1:
            self.drone.send_rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity,
                                       yaw_velocity)
        else:
            if self.command.name == DroneCommand.TAKEOFF.name:
                if self.state.name == FlightState.IDLE.name:
                    self.drone.takeoff()
                    self.state = FlightState.FLYING

            elif self.command.name == DroneCommand.LAND.name:
                if self.command.name == FlightState.FLYING.name:
                    self.drone.land()
                    self.state = FlightState.LANDING
                    threading.Thread(time.sleep(7)).start()
                    self.state = FlightState.IDLE

            elif self.command.name == DroneCommand.FLIP.name:
                if self.command.name == FlightState.FLYING.name:
                    self.drone.flip()

    def powerDrone(self):
        connectSwitch = 1
        if self.connectionCommand.name == ConnectionCommand.CONNECT.name:
            if self.connectionState.name != ConnectionState.CONNECTED.name:
                self.drone.connect()
                self.connectionState = ConnectionState.CONNECTED



    '''      
      if self.connectionCommand.name==ConnectionCommand.DISCONNECT.name:
            if self.connectionState.name == ConnectionState.CONNECTED.name:
                if self.state.name==FlightState.IDLE.name:
                    self.drone.
                    self.connectionState= ConnectionState.DISCONNECTED
    '''
