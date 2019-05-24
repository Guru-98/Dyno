from serial import Serial, SerialException


class Sensor():
    def __init__(self, port= None):
        self.serial = port

    def checkcomm(self):
        pass

    def getdata(self,txdata:str=None)->str:
        if(type(self.serial) is Serial):
            if(txdata is not None):
                self.putdata(txdata)
            data = self.serial.read_until('\n')
            return data.decode('utf-8').strip()

    def putdata(self,data:str):
        if(type(self.serial) is Serial):
            self.serial.write((data+'\n').encode('utf-8'))
