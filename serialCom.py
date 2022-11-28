import serial
import threading

class SerialCom:
    def __init__(self):
        self.ser = serial.Serial('COM17', 256000)
        self.line = ''


    def read_serial(self):
        self.line = self.ser.readline()  # read a '\n' terminated line

        return





    def continous_read(self):
        while True:
            threading.Thread(target=self.read_serial).start()


    def string_to_command(self):
        self.line = self.line.replace(" ", "")
        word_arr = self.line.split(';')

        self.left_right_command = word_arr(0)
        self.forward_backward_command = word_arr(1)
        self.up_down_command = word_arr(2)
        self.yaw_vel_command = word_arr(3)
        self.remote_constrol = word_arr(4)
        self.command = word_arr(5)





