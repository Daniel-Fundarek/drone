import serial
import threading


class SerialCom:
    def __init__(self, tello):
        self.drone = tello
        self.ser = serial.Serial('COM17', 256000)
        self.line = ''
        self.left_right_command = 0
        self.forward_backward_command = 0
        self.up_down_command = 0

        self.yaw_vel_command = 0
        self.remote_control = 0
        self.command = ''
        #self.continous_read()

    def read_serial(self):
        self.line = self.ser.readline()  # read a '\n' terminated line

        return

    def continous_read(self):
        while self.command != 'stop_serial':
            self.read_serial()
            self.string_to_command()
            self.print_cmd()

            # here will go implementation of flight control

    def print_cmd(self):
        print(
            f'a: {self.left_right_command}, b: {self.up_down_command}, c: {self.yaw_vel_command}, d {self.remote_control}, e: {self.command}, f: {self.forward_backward_command}')

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
        self.remote_control = int(word_arr[4])
        #self.command = word_arr[5]

    def set_command(self, command):
        self.command = command
