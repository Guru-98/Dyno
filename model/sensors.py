from serial import Serial, SerialException

class Sensor():
    def __init__(self, port= None):
        self.serial = port

    def checkcomm(self):
        pass

    def getdata(self):
        pass

    def putdata(self):
        pass