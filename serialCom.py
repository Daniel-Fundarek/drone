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







