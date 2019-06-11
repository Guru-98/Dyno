from serial import Serial, SerialException
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QIODevice, QObject, QByteArray
from PyQt5.QtSerialPort import QSerialPort
import threading
from time import sleep
import logging

logger = logging.getLogger('Dyno.'+__name__)

class Sensor(QObject):
    rx = pyqtSignal(str)
    def __init__(self, port= None):
        super(Sensor,self).__init__()
        try:
            # self.serial = Serial(port,baudrate=9600, timeout=2)
            self.serial = QSerialPort(port)
            self.serial.open(QIODevice.ReadWrite)
            self.serial.setBaudRate(115200)
            self.serial.setReadBufferSize(1024)
        except:
            self.serial = None

        self.serial.readyRead.connect(self.recv)

    @pyqtSlot(str)
    def send(self,data):
        logging.debug(data)
        self.serial.write(data.encode('utf-8'))

    @pyqtSlot()
    def recv(self):
        data = self.serial.readLine()
        data = bytes(data).decode('utf-8').strip()
        logging.debug(data)
        self.rx.emit(data)

    def close(self):
        self.serial.close()

if __name__ == '__main__':
    from PyQt5.QtWidgets import *
    import sys
    from model import devices
    import logging

    logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    logging.root.setLevel(logging.DEBUG)

    class MQP(QWidget):
        tx = pyqtSignal(str)
        def __init__(self,parent=None):
            super(MQP,self).__init__(parent)

            self.dcs = [Sensor(dc) for dc in devices.DCS]
            self.setWindowTitle("TESTING")
            self.setFixedSize(200,100)

            l = QVBoxLayout(self)

            self.txt = QLineEdit(self)
            self.btn = QPushButton(self)
            self.lab = QLabel(self)
            l.addWidget(self.txt)
            l.addWidget(self.btn)
            l.addWidget(self.lab)

            self.btn.setText("Check")
            self.btn.clicked.connect(self.senddata)

            [self.tx.connect(dc.send) for dc in self.dcs]
            [dc.rx.connect(self.recvdata) for dc in self.dcs]
            # self.s.rx.connect(self.recvdata)

        def recvdata(self, data):
            self.lab.setText(data)

        def senddata(self):
            self.tx.emit(self.txt.text())

    app = QApplication(sys.argv)
    w = MQP()
    w.show()
    sys.exit(app.exec_())
