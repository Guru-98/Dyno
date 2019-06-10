from serial import Serial, SerialException
from PyQt5.QtCore import pyqtSlot, QObject
from time import sleep
import logging

logger = logging.getLogger('Dyno.'+__name__)

class Sensor(QObject):
    def __init__(self, port= None):
        self.serial = Serial(baudrate=9600, timeout=2)
        try:
            self.serial.port = port
        except:
            self.serial = None

    def checkcomm(self):
        pass

    @pyqtSlot(str)
    def getdata(self,txdata:str=None)->str:
        if(type(self.serial) is Serial and self.serial.isOpen()):
            if(txdata is not None):
                self.putdata(txdata)
            data = self.serial.read_until('\n')
            logger.debug("Got data(raw) -::>  %s"%(data))
            logger.debug("Got data(utf) -::>  %s"%(data.decode('utf-8').strip()))
            return data.decode('utf-8').strip()
        else:
            logger.error("Not a serial port")
            pass

    @pyqtSlot(str)
    def putdata(self,data:str):
        if(type(self.serial) is Serial and self.serial.isOpen()):
            logger.debug("Put data(raw) -::>  %s"%((data+'\n').encode('utf-8')))
            logger.debug("Put data(utf) -::>  %s"%(data))
            self.serial.write((data+'\n').encode('utf-8'))
        else:
            logger.error("Not a serial port")
            pass


if __name__ == '__main__':
    from PyQt5.QtCore import QThread
    s = Sensor('COM6')

    s.putdata("*IDN?")
    print(s.getdata())