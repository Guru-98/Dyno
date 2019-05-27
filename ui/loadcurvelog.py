import sys
from PyQt5 import QtCore, QtWidgets, QtOpenGL, uic
# from model.dcsource import dcSource
# from model.vfd import vfd
# from model.oscilloscope import oscilloscope
# from model import devices

class dashLoadCurveLog(QtWidgets.QWidget):
    def __init__(self,parent=None):
        self.dataRowsNo = 0
        super(dashLoadCurveLog,self).__init__(parent)

        self.container = QtWidgets.QVBoxLayout(self)

        self.motorID_container = QtWidgets.QHBoxLayout()
        self.motorID_lab = QtWidgets.QLabel(self)
        self.motorID_lab.setText("Motor &ID")
        self.motorID = QtWidgets.QLineEdit(self)
        self.motorID_lab.setBuddy(self.motorID)
        self.motorID_container.addWidget(self.motorID_lab,alignment=QtCore.Qt.AlignRight)
        self.motorID_container.addWidget(self.motorID    ,alignment=QtCore.Qt.AlignLeft)
        self.motorID_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        # self.motorID_container.setAlignment(self.motorID,QtCore.Qt.AlignHCenter)
        # self.motorID_container.setAlignment(self.motorID_l,QtCore.Qt.AlignHCenter)
        self.container.addLayout(self.motorID_container,0)

        # spacer = QtOpenGL.QGLWidget(self)
        # self.container.addWidget(spacer,alignment=QtCore.Qt.AlignHCenter)

        self.layout = QtWidgets.QGridLayout()
        self.container.addLayout(self.layout,0)

        self.loadHeader()
        self.dataTable = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.dataTable,2,0,1,11,alignment=QtCore.Qt.AlignHCenter)

        actions = QtWidgets.QHBoxLayout()
        self.addRowbtn = QtWidgets.QPushButton(self)
        self.addRowbtn.setText("+")
        self.addRowbtn.clicked.connect(self.addLoadRow)
        actions.addWidget(self.addRowbtn,alignment=QtCore.Qt.AlignHCenter)

        self.runAllbtn = QtWidgets.QPushButton(self)
        self.runAllbtn.setText(">>")
        self.runAllbtn.clicked.connect(self.runAll)
        actions.addWidget(self.runAllbtn,alignment=QtCore.Qt.AlignHCenter)

        self.container.addLayout(actions,0)

        [self.addRowbtn.click() for _ in range(4)]
        
        # self.dcS = [(port) for port in devices.dcS]
        # self.vfd = vfd(devices.vfd)
        # self.osc = oscilloscope(devices.osc)

    def loadHeader(self):
        load_l = QtWidgets.QLabel(self)
        load_l.setText("Load %")
        self.layout.addWidget(load_l,0,0,2,1,alignment=QtCore.Qt.AlignCenter)

        con_ip_l = QtWidgets.QLabel(self)
        con_ip_l.setText("Controller i/p")
        self.layout.addWidget(con_ip_l,0,1,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_op_l = QtWidgets.QLabel(self)
        cont_op_l.setText("Controller o/p")
        self.layout.addWidget(cont_op_l,0,4,1,3,alignment=QtCore.Qt.AlignHCenter)

        motor_op_l = QtWidgets.QLabel(self)
        motor_op_l.setText("Motor o/p")
        self.layout.addWidget(motor_op_l,0,7,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_v_ip_l = QtWidgets.QLabel(self)
        cont_v_ip_l.setText("Voltage i/p")
        self.layout.addWidget(cont_v_ip_l,1,1,alignment=QtCore.Qt.AlignHCenter)

        cont_i_ip_l = QtWidgets.QLabel(self)
        cont_i_ip_l.setText("Current i/p")
        self.layout.addWidget(cont_i_ip_l,1,2,alignment=QtCore.Qt.AlignHCenter)

        cont_p_ip_l = QtWidgets.QLabel(self)
        cont_p_ip_l.setText("Power i/p")
        self.layout.addWidget(cont_p_ip_l,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_v_op_l = QtWidgets.QLabel(self)
        cont_v_op_l.setText("Voltage o/p")
        self.layout.addWidget(cont_v_op_l,1,4,alignment=QtCore.Qt.AlignHCenter)

        cont_i_op_l = QtWidgets.QLabel(self)
        cont_i_op_l.setText("Current o/p")
        self.layout.addWidget(cont_i_op_l,1,5,alignment=QtCore.Qt.AlignHCenter)

        cont_p_op_l = QtWidgets.QLabel(self)
        cont_p_op_l.setText("Power o/p")
        self.layout.addWidget(cont_p_op_l,1,6,alignment=QtCore.Qt.AlignHCenter)

        motor_rpm_l = QtWidgets.QLabel(self)
        motor_rpm_l.setText("Motor RPM")
        self.layout.addWidget(motor_rpm_l,1,7,alignment=QtCore.Qt.AlignHCenter)

        motor_tor_l = QtWidgets.QLabel(self)
        motor_tor_l.setText("Motor Torque")
        self.layout.addWidget(motor_tor_l,1,8,alignment=QtCore.Qt.AlignHCenter)

        motor_pow_l = QtWidgets.QLabel(self)
        motor_pow_l.setText("Motor Power")
        self.layout.addWidget(motor_pow_l,1,9,alignment=QtCore.Qt.AlignHCenter)

    def addLoadRow(self):
        if self.dataRowsNo <= 8:
            row = loadRow(self)
            container = QtWidgets.QVBoxLayout(self)
            container.addWidget(row)
            self.dataTable.addLayout(container)
            if self.dataRowsNo == 8:
                self.addRowbtn.setDisabled(True)
        self.dataRowsNo += 1

    def runAll(self):
        [self.dataTable.itemAt(i).widget().runbtn.click() for i in range(self.dataRowsNo)]

class loadRow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(loadRow,self).__init__(parent)
        self.parent = parent
        self.layout = QtWidgets.QHBoxLayout(self)

        self.load = QtWidgets.QLineEdit(self)
        self.load.setAlignment(QtCore.Qt.AlignHCenter)
        self.cont_v_ip = QtWidgets.QLineEdit(self)
        self.cont_v_ip.setAlignment(QtCore.Qt.AlignHCenter)
        self.cont_i_ip = QtWidgets.QLineEdit(self)
        self.cont_i_ip.setAlignment(QtCore.Qt.AlignHCenter)
        self.cont_p_ip = QtWidgets.QLineEdit(self)
        self.cont_p_ip.setAlignment(QtCore.Qt.AlignHCenter)
        self.cont_v_op = QtWidgets.QLineEdit(self)
        self.cont_v_op.setAlignment(QtCore.Qt.AlignHCenter)
        self.cont_i_op = QtWidgets.QLineEdit(self)
        self.cont_i_op.setAlignment(QtCore.Qt.AlignHCenter)
        self.cont_p_op = QtWidgets.QLineEdit(self)
        self.cont_p_op.setAlignment(QtCore.Qt.AlignHCenter)
        self.motor_rpm = QtWidgets.QLineEdit(self)
        self.motor_rpm.setAlignment(QtCore.Qt.AlignHCenter)
        self.motor_tor = QtWidgets.QLineEdit(self)
        self.motor_tor.setAlignment(QtCore.Qt.AlignHCenter)
        self.motor_pow = QtWidgets.QLineEdit(self)
        self.motor_pow.setAlignment(QtCore.Qt.AlignHCenter)
        
        self.runbtn = QtWidgets.QPushButton(self)
        self.runbtn.setText(">")
        self.runbtn.clicked.connect(self.runRow)

        self.layout.addWidget(self.load     ,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.cont_v_ip,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.cont_i_ip,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.cont_p_ip,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.cont_v_op,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.cont_i_op,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.cont_p_op,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.motor_rpm,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.motor_tor,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.motor_pow,alignment=QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.runbtn,alignment=QtCore.Qt.AlignHCenter)

    def runRow(self):
        self.runbtn.setStyleSheet("background: green")
        # dcS:list(dcSource) = self.parent.dcS
        # vfd:vfd = self.parent.vfd
        # osc:oscilloscope = self.parent.osc

        load = int(self.load.text())
        
        volt = int(self.cont_v_ip.text())
        curr = int(self.cont_i_ip.text())
        
        # for dc in dcS:
        #     dc.setVoltage(volt)
        #     dc.setCurrent(curr/5)
        #     dc.turnON()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dashLoadCurveLog()
    window.showMaximized()
    sys.exit(app.exec_())