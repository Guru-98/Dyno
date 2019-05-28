from serial import Serial, SerialException
from model.sensors import Sensor

class dcSource(Sensor):
    def __init__(self, port):
        self.serial = Serial(port, baudrate=9600, timeout=2)
        self.putdata("SYST:ETR")
        self.getdata()
        self.setVoltage(0)
        self.setVoltage(0)
    
    def checkcomm(self,port=None):
        self.putdata("*IDN?")
        data = self.getdata()
        if data.find("APM") is not -1:
            return True
        else:
            return False
    
    def turnON(self):
        self.putdata("OUTP 1")

    def turnOFF(self):
        self.putdata("OUTP 0")

    def setVoltage(self,volt):
        self.putdata("VOLT %s"%(str(volt)))
    
    def setCurrent(self,curr):
        self.putdata("CURR %s"%(str(curr)))

    def measVolt(self):
        return self.getdata("MEAS:VOLT?")

    def measCurr(self):
        return self.getdata("MEAS:CURR?")

    def close(self):
        self.turnOFF()
        self.putdata("SYST:LOC")
        self.serial.close()

if __name__ == "__main__":
    from serial.tools import list_ports

    ports = [port.device for port in list_ports.comports()]
    ports.sort(key=lambda x: int(x.split("COM")[1]))
    for port in ports:
        # print("testing on %s"%(port))
        dc = dcSource(port)
        if dc.checkcomm():
            print(port)
