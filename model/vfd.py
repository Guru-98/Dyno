from serial import Serial, SerialException, PARITY_EVEN
from sensors import Sensor
from pymodbus.client.sync import ModbusSerialClient as ModBusClient

class vfd(Sensor):
    def __init__(self, port= None):
        self.serial = ModBusClient(method='rtu', port=port, baudrate=9600, timeout=5, parity=PARITY_EVEN)
        self.serial.connect()
    
    def checkcomm(self):
        pass

    def getdata(self):
        pass

    def putdata(self,reg,data):
        self.serial.write_registers(reg,data,unit=1)

    def run(self,dir):
        if(dir == 0):
            self.putdata(0x01,1)
        elif(dir == 1):
            self.putdata(0x01,2)
    
    def stop(self):
        self.putdata(0x01,0)

    def setTorq(self,torq):
        self.putdata(0x0f,4)
        self.putdata(0x04,torq)

    def setSpeed(self,speed):
        self.putdata(0x02,speed)

    def close(self):
        self.serial.close()

if __name__ == "__main__":
    import logging

    logging.basicConfig()
    log = logging.getLogger('pymodbus')
    log.setLevel(logging.DEBUG)

    m = vfd('COM6')
    while True:
        data = input('>> ')
        if(data.find('run ') != -1):
            dir = int(data[data.find(' ')+1:])
            m.run(dir)
        elif(data == 'stop'):
            m.stop()
        elif(data.find('torq ') != -1):
            torq = int(data[data.find(' ')+1:])
            m.setTorq(torq)
        elif(data.find('freq ') != -1):
            freq = int(data[data.find(' ')+1:])
            m.setSpeed(freq)
        elif(data == 'close'):
            m.close()
            break
