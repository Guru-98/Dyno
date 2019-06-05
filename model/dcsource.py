from serial import Serial, SerialException
from model.sensors import Sensor
import logging

logger = logging.getLogger("Dyno."+__name__)

class dcSource(Sensor):
    port = ''
    def __init__(self, port):
        self.port = port
        super(dcSource,self).__init__(port)
        logger.info("DC init in %s",self.port)
        self.putdata("SYST:ETR")
        logger.debug("%s :: %s",self.port,self.getdata())
    
    def checkcomm(self,port=None):
        self.putdata("*IDN?")
        data = self.getdata()
        if data.find("APM") is not -1:
            return True
        else:
            return False
    
    def turnON(self):
        logger.info("%s :: TurnON",self.port)
        self.putdata("OUTP 1")
        logger.debug("%s :: %s",self.port,self.getdata())

    def turnOFF(self):
        logger.info("%s :: TurnOFF",self.port)
        self.putdata("OUTP 0")
        logger.debug("%s :: %s",self.port,self.getdata())

    def setVoltage(self,volt):
        logger.info("%s :: Set voltage to %d",self.port,volt)
        self.putdata("VOLT %s"%(str(volt)))
        logger.debug("%s :: %s",self.port,self.getdata())
    
    def setCurrent(self,curr):
        logger.info("%s :: Set current to %d",self.port,curr)
        self.putdata("CURR %s"%(str(curr)))
        logger.debug("%s :: %s",self.port,self.getdata())

    def measVolt(self):
        logger.info("%s :: Measure Voltage", self.port)
        return self.getdata("MEAS:VOLT?")

    def measCurr(self):
        logger.info("%s :: Measure Current",self.port)
        return self.getdata("MEAS:CURR?")

    def close(self):
        logger.info("%s :: Closing",self.port)
        self.turnOFF()
        self.putdata("SYST:LOC")
        self.serial.close()

    def __del__(self):
        self.close()

if __name__ == "__main__":
    import model.devices as devices

    logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('Dyno.model.sensor')
    log.setLevel(logging.DEBUG)

    dc = [dcSource(port) for port in devices.DCS]

    while True:
        data = input('>> ')
        if(data.find('d.volt ') != -1):
            volt = int(data[data.find(' ')+1:])
            [d.setVoltage(volt) for d in dc]
        elif (data.find('d.curr ') != -1):
            curr = int(data[data.find(' ')+1:])
            [d.setCurrent(curr) for d in dc]
        elif (data.find('d.on') != -1):
            [d.turnON() for d in dc]
        elif (data.find('d.off') != -1):
            [d.turnOFF() for d in dc]
        elif (data.find('d.mvolt') != -1):
            print([d.measVolt() for d in dc])
        elif (data.find('d.mcurr') != -1):
            print([d.measCurr() for d in dc])
        elif(data == 'close'):
            [d.close() for d in dc]
            break