from serial import Serial, SerialException, PARITY_ODD
from serial.tools import list_ports
from sensors import Sensor

class dcSource(Sensor):
    def __init__(self, port= None):
        self.serial = Serial(port, baudrate=9600, timeout=2)
    
    def checkcomm(self):
        self.serial.write("SYST:ETR\n".encode('utf-8'))
        self.serial.write("SYST:LOC\n".encode('utf-8'))
        data = self.serial.read_until()
        # print(data)
        if data != b'':
            return True
        else:
            return False
    
    def getdata(self):
        pass

    def putdata(self):

        pass

if __name__ == "__main__":
    ports = [(port.device,port) for port in list_ports.comports()]
    ports.sort(key=lambda x: int(x[0].split("COM")[1]))
    for port in ports:
        # print("testing on %s"%(port[0]))
        dc = dcSource(port[0])
        if dc.checkcomm():
            print(port[0])