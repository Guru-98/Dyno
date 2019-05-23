from vfd import vfd
from dcsource import dcSource
import logging

if __name__ == "__main__":
    d = dcSource('COM7')
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
        elif(data.find('d.volt ') != -1):
            volt = int(data[data.find(' ')+1:])
            d.setVoltage(48)
        elif (data.find('d.curr ') != -1):
            curr = int(data[data.find(' ')+1:])
            d.setCurrent(curr)
        elif (data.find('d.on') != -1):
            d.turnON()
        elif (data.find('d.off') != -1):
            d.turnOFF()
        elif(data == 'close'):
            m.close()
            d.close()
            break