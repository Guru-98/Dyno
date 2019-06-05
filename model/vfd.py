from serial import Serial, SerialException, PARITY_EVEN
from model.sensors import Sensor
from pymodbus.client.sync import ModbusSerialClient as ModBusClient

class vfd(Sensor):
    def __init__(self, port= None):
        self.serial = ModBusClient(method='rtu', port=port, baudrate=9600, timeout=2, parity=PARITY_EVEN)
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
        self.stop()
        self.serial.close()

    def __del__(self):
        self.close()

if __name__ == "__main__":
    import logging

    logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('pymodbus')
    log.setLevel(logging.ERROR)

    m = vfd('COM6')
    while True:
        data = input('>> ')
        if(data.find('v.run ') != -1):
            dir = int(data[data.find(' ')+1:])
            m.run(dir)
        elif(data == 'v.stop'):
            m.stop()
        elif(data.find('v.torq ') != -1):
            torq = int(data[data.find(' ')+1:])
            m.setTorq(torq)
        elif(data.find('v.freq ') != -1):
            freq = int(data[data.find(' ')+1:])
            m.setSpeed(freq)
        elif(data == 'v.close'):
            m.close()
            break
