from model.vfd import vfd
from model.dcsource import dcSource
import model.devices as devices
from serial.tools import list_ports

if __name__ == "__main__":
    print(devices.DCS)
    dc = [dcSource(port) for port in devices.DCS]
    m = vfd(devices.VFD)
    input(">> ")
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
        elif(data.find('d.volt ') != -1):
            volt = int(data[data.find(' ')+1:])
            [d.setVoltage(volt) for d in dc]
        elif (data.find('d.curr ') != -1):
            curr = int(data[data.find(' ')+1:])
            [d.setCurrent(curr) for d in dc]
        elif (data.find('d.on') != -1):
            [d.turnON() for d in dc]
        elif (data.find('d.off') != -1):
            [d.turnOFF() for d in dc]
        elif(data == 'close'):
            m.close()
            [d.close() for d in dc]
            break