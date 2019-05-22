from serial import Serial, SerialException, PARITY_EVEN
from sensors import Sensor
from pymodbus.client.sync import ModbusSerialClient as ModBusClient

class vfd(Sensor):
    def __init__(self, port= None):
        pass
    
    def checkcomm(self):
        pass

    def getdata(self):
        pass

    def putdata(self):
        pass

if __name__ == "__main__":
    import logging
    import struct
    from serial import PARITY_EVEN

    logging.basicConfig()
    log = logging.getLogger('pymodbus')
    log.setLevel(logging.DEBUG)

    modbus = ModBusClient(method='rtu', port='COM6', baudrate=9600, timeout=5, parity=PARITY_EVEN)
    modbus.connect()

    r = modbus.read_holding_registers(0x05, 1, unit=1)
    print(r.registers)
    modbus.close()