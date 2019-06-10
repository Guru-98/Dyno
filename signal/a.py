from PyQt5.QtCore import *
from serial import Serial, serial_for_url

class A(QObject):
    def __init__(self,p):
        self.serial = serial_for_url(p)

    def tx(self,d):
        self.serial.write(d.encode('utf-8'))

    def rx(self):
        return self.serial.read_all()