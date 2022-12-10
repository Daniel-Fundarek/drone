import serial
import threading


class SerialCom:
    def __init__(self, tello,run_cycle):
        self.drone = tello
        self.run_cycle=run_cycle
        self.ser = serial.Serial('COM3', 256000)
        self.line = ''
        self.left_right_command = 0
        self.forward_backward_command = 0
        self.up_down_command = 0

        self.yaw_vel_command = 0
        self.remote_control = 0
        self.command = ''
        self.counter = -3
        self.prevCounter = -5
        self.drone.connect()
        #self.run_cycle.powerDrone(self)

        # self.continous_read()

    def read_serial(self):
        self.line = self.ser.readline()  # read a '\n' terminated line

        return

    def continous_read(self):
        self.read_serial()
        while self.command != 'stop_serial':
            #if self.command == 'rc_command':
            try:
                self.read_serial()
                self.string_to_command()

            except:
                print("Reading Failed")
            self.run_cycle.emergencyLanding(self.prevCounter, self.counter)
            self.print_cmd()
            self.run_cycle.controlDrone(self.left_right_command,self.forward_backward_command,self.up_down_command,self.yaw_vel_command,self.command)
            self.prevCounter = self.counter
                #Tu implementovat funkcie
                #self.drone.send_rc_control(self.left_right_command, self.forward_backward_command, self.up_down_command,self.yaw_vel_command)


            # here will go implementation of flight control

    def print_cmd(self):
        print(
            f'right/letf: {self.left_right_command}, fowr/back: {self.forward_backward_command} up/down: {self.up_down_command}, yaw: {self.yaw_vel_command}, command: {self.command}, prevCounter: {self.prevCounter}, counter: {self.counter}')

    def string_to_command(self):
        self.line = self.line.decode("utf-8")

        self.line = self.line.replace("\\", "")
        self.line = self.line.replace("\n", "")
        self.line = self.line.replace(" ", "")
        word_arr = self.line.split(',')

        self.left_right_command = int(word_arr[0])
        self.forward_backward_command = int(word_arr[1])
        self.up_down_command = int(word_arr[2])

        self.yaw_vel_command = int(word_arr[3])
       # self.remote_control = int(word_arr[4])
        self.command = word_arr[4]
        self.counter = word_arr[5]


    def set_command(self, command):
        self.command = command


