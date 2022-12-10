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

    def controlDrone(self,left_right_command,forward_backward_command,up_down_command,yaw_vel_command,command):
        #print( f'fLIGHTsTATE: {self.state.name}')
        if command == 'rc':
           # print(f'cONTROLLING1')
            if self.state.name==FlightState.FLYING.name:
              #  print(f'cONTROLLING2')
                self.drone.send_rc_control(left_right_command, forward_backward_command, up_down_command,
                                       yaw_vel_command)
               # print(f'cONTROLLING3')

        else:
            if command == DroneCommand.TAKEOFF.name:
                if self.state.name == FlightState.IDLE.name:
                    self.drone.takeoff()
                    self.state = FlightState.FLYING


            elif command == DroneCommand.LAND.name:
              #  print(f'Landing1')
                if self.state.name == FlightState.FLYING.name:
                #    print(f'Landing2')
                    self.drone.land()
                #    print(f'Landing3')
                    self.state = FlightState.LANDING
               #     print(f'Landing4')
                    threading.Thread(target=lambda:self.landingControll()).start()
               #     print(f'Landing5')

            elif command == DroneCommand.fFlip.name:
                if self.state.name == FlightState.FLYING.name:
                    self.drone.flip_forward()

            elif command == DroneCommand.bFlip.name:
                if self.state.name == FlightState.FLYING.name:
                    self.drone.flip_back()

            elif command == DroneCommand.rFlip.name:
                if self.state.name == FlightState.FLYING.name:
                    self.drone.flip_right()

            elif command == DroneCommand.lFlip.name:
                if self.state.name == FlightState.FLYING.name:
                    self.drone.flip_left()

   # def powerDrone(self):
    #    connectSwitch = 1
     #   if self.connectionCommand.name == ConnectionCommand.CONNECT.name:
      #      if self.connectionState.name != ConnectionState.CONNECTED.name:
       #         self.drone.connect()
        #        self.connectionState = ConnectionState.CONNECTED

    def landingControll(self):
        time.sleep(4)
        self.state = FlightState.IDLE
        return
    '''      
      if self.connectionCommand.name==ConnectionCommand.DISCONNECT.name:
            if self.connectionState.name == ConnectionState.CONNECTED.name:
                if self.state.name==FlightState.IDLE.name:
                    self.drone.
                    self.connectionState= ConnectionState.DISCONNECTED
    '''
