from serial import Serial, SerialException
from model.sensors import Sensor
from PyQt5.QtCore import pyqtSignal, QObject
import logging

logger = logging.getLogger("Dyno."+__name__)

class dcSource(QObject):
    tx = pyqtSignal(str)
    rxbuf = ''
    def __init__(self, port):
        self.port = port
        super(dcSource,self).__init__()
        self.serial = Sensor(port)
        self.tx.connect(self.serial.send)
        self.serial.rx.connect(self.recvdata)
        
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

    def putdata(self,data):
        self.tx.emit(data)

    def recvdata(self,data):
        self.rxbuf = data

    def getdata(self,data=None):
        if data is not None:
            self.putdata(data)
        return self.rxbuf

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
    from PyQt5.QtWidgets import *
    import sys
    import model.devices as devices

    logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('Dyno.model.sensor')
    log.setLevel(logging.DEBUG)

    class MQP(QWidget):
        # tx = pyqtSignal(str)
        def __init__(self,parent=None):
            super(MQP,self).__init__(parent)

            self.dc = [dcSource(port) for port in devices.DCS]
            self.setWindowTitle("TESTING")
            self.setFixedSize(200,100)

            l = QVBoxLayout(self)

            self.txt = QLineEdit(self)
            self.on = QPushButton(self)
            self.off = QPushButton(self)
            l.addWidget(self.txt)
            l.addWidget(self.on)
            l.addWidget(self.off)

            self.on.setText("ON")
            self.off.setText("OFF")
            self.on.clicked.connect(self.onm)
            self.off.clicked.connect(self.offm)

            # [self.tx.connect(dc.send) for dc in self.dcs]
            # [dc.rx.connect(self.recvdata) for dc in self.dcs]
            # self.s.rx.connect(self.recvdata)

        def recvdata(self, data):
            self.lab.setText(data)

        def onm(self):
            [d.turnON() for d in self.dc]

        def offm(self):
            [d.turnOFF() for d in self.dc]


    app = QApplication(sys.argv)
    w = MQP()
    w.show()
    sys.exit(app.exec_())