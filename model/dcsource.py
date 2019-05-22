from serial import Serial, SerialException
from sensors import Sensor

class dcSource(Sensor):
    def __init__(self, port= None):
        self.serial = Serial(port, baudrate=9600, timeout=2)
    
    def checkcomm(self):
        self.putdata("*IDN?")
        data = self.getdata()
        print(data)
        if data.find("APM") is not -1:
            return True
        else:
            return False
    
    def setVoltage(self,volt):
        self.putdata("VOLT %s"%(str(volt)))
    
    def setCurrent(self,curr):
        self.putdata("CURR %s"%(str(curr)))

    def measVolt(self):
        return self.getdata("MEAS:VOLT?")

    def measCurr(self):
        return self.getdata("MEAS:CURR?")


if __name__ == "__main__":
    from serial.tools import list_ports

    ports = [(port.device,port) for port in list_ports.comports()]
    ports.sort(key=lambda x: int(x[0].split("COM")[1]))
    for port in ports:
        # print("testing on %s"%(port[0]))
        dc = dcSource(port[0])
        if dc.checkcomm():
            print(port[0])