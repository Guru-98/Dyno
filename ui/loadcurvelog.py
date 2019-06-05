import sys
from PyQt5 import QtCore, QtWidgets, QtOpenGL, uic
from model.dcsource import dcSource
from model.vfd import vfd
from model.oscilloscope import oscilloscope
import model.devices as devices

class dashLoadCurveLog(QtWidgets.QWidget):
    def __init__(self,parent=None):
        self.dataRowsNo = 1
        super(dashLoadCurveLog,self).__init__(parent)

        self.container = QtWidgets.QVBoxLayout(self)

        self.motor_data = QtWidgets.QGroupBox(self)
        self.motor_data.setTitle("Motor Parameters")
        self.motor_data_layout = QtWidgets.QHBoxLayout()
        self.motor_data_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.motor_data_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.motor_data_layout.setSpacing(50)
        self.motor_data.setLayout(self.motor_data_layout)
        
        self.motorID_container = QtWidgets.QHBoxLayout()
        self.motorID_lab = QtWidgets.QLabel(self)
        self.motorID_lab.setText("Motor &ID")
        self.motorID = QtWidgets.QLineEdit(self)
        self.motorID_lab.setBuddy(self.motorID)
        self.motorID_container.addWidget(self.motorID_lab,alignment=QtCore.Qt.AlignRight)
        self.motorID_container.addWidget(self.motorID    ,alignment=QtCore.Qt.AlignLeft)
        self.motorID_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.motor_data_layout.addLayout(self.motorID_container)

        self.motorT_container = QtWidgets.QHBoxLayout()
        self.motorT_lab = QtWidgets.QLabel(self)
        self.motorT_lab.setText("Rated &Torque")
        self.motorT = QtWidgets.QLineEdit(self)
        self.motorT_lab.setBuddy(self.motorT)
        self.motorT_container.addWidget(self.motorT_lab,alignment=QtCore.Qt.AlignRight)
        self.motorT_container.addWidget(self.motorT    ,alignment=QtCore.Qt.AlignLeft)
        self.motorT_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.motor_data_layout.addLayout(self.motorT_container)

        self.motorN_container = QtWidgets.QHBoxLayout()
        self.motorN_lab = QtWidgets.QLabel(self)
        self.motorN_lab.setText("Rated S&peed")
        self.motorN = QtWidgets.QLineEdit(self)
        self.motorN_lab.setBuddy(self.motorN)
        self.motorN_container.addWidget(self.motorN_lab,alignment=QtCore.Qt.AlignRight)
        self.motorN_container.addWidget(self.motorN    ,alignment=QtCore.Qt.AlignLeft)
        self.motorN_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.motor_data_layout.addLayout(self.motorN_container)

        self.motorV_container = QtWidgets.QHBoxLayout()
        self.motorV_lab = QtWidgets.QLabel(self)
        self.motorV_lab.setText("Rated &Voltage")
        self.motorV = QtWidgets.QLineEdit(self)
        self.motorV_lab.setBuddy(self.motorV)
        self.motorV_container.addWidget(self.motorV_lab,alignment=QtCore.Qt.AlignRight)
        self.motorV_container.addWidget(self.motorV    ,alignment=QtCore.Qt.AlignLeft)
        self.motorV_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.motor_data_layout.addLayout(self.motorV_container)

        self.motorI_container = QtWidgets.QHBoxLayout()
        self.motorI_lab = QtWidgets.QLabel(self)
        self.motorI_lab.setText("Max &Current")
        self.motorI = QtWidgets.QLineEdit(self)
        self.motorI_lab.setBuddy(self.motorI)
        self.motorI_container.addWidget(self.motorI_lab,alignment=QtCore.Qt.AlignRight)
        self.motorI_container.addWidget(self.motorI    ,alignment=QtCore.Qt.AlignLeft)
        self.motorI_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.motor_data_layout.addLayout(self.motorI_container)

        self.control_container = QtWidgets.QGroupBox()
        self.control_lab = QtWidgets.QLabel(self)
        self.control_lab.setText("Mode")
        self.controlT = QtWidgets.QRadioButton(self)
        self.controlT.setText("Torque")
        self.controlN = QtWidgets.QRadioButton(self)
        self.controlN.setText("Speed")
        self.control_container.addWidget(self.control_lab,alignment=QtCore.Qt.AlignRight)
        self.control_container.addWidget(self.controlT    ,alignment=QtCore.Qt.AlignLeft)
        self.control_container.addWidget(self.controlN    ,alignment=QtCore.Qt.AlignLeft)
        self.controlT_container.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.motor_data_layout.addLayout(self.control_container)

        self.container.addWidget(self.motor_data,0)
        
        #===========================================================#

        spacer = QtOpenGL.QGLWidget(self)
        self.container.addWidget(spacer,alignment=QtCore.Qt.AlignHCenter)
        self.container.addSpacerItem(QtWidgets.QSpacerItem(1,30,QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.Maximum))

        self.layout = QtWidgets.QGridLayout()
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.container.addLayout(self.layout,0)

        self.loadHeader()
        self.dataTable = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.dataTable,2,0,1,12,alignment=QtCore.Qt.AlignHCenter)

        actions = QtWidgets.QHBoxLayout()
        self.addRowbtn = QtWidgets.QPushButton(self)
        self.addRowbtn.setText("+")
        self.addRowbtn.clicked.connect(self.addLoadRow)
        actions.addWidget(self.addRowbtn,alignment=QtCore.Qt.AlignHCenter)

        self.runAllbtn = QtWidgets.QPushButton(self)
        self.runAllbtn.setText(">>")
        self.runAllbtn.clicked.connect(self.runAll)
        actions.addWidget(self.runAllbtn,alignment=QtCore.Qt.AlignHCenter)

        self.container.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.MinimumExpanding,QtWidgets.QSizePolicy.MinimumExpanding))
        self.container.addLayout(actions,0)

        [self.addRowbtn.click() for _ in range(4)]

        self.dcS = [dcSource(port) for port in devices.DCS]
        self.vfd = vfd(devices.VFD)
        self.osc = oscilloscope(devices.OSC)

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
        self.layout.addWidget(cont_v_ip_l,1,1)

        cont_i_ip_l = QtWidgets.QLabel(self)
        cont_i_ip_l.setText("Current i/p")
        self.layout.addWidget(cont_i_ip_l,1,2)

        cont_p_ip_l = QtWidgets.QLabel(self)
        cont_p_ip_l.setText("Power i/p")
        self.layout.addWidget(cont_p_ip_l,1,3)

        cont_v_op_l = QtWidgets.QLabel(self)
        cont_v_op_l.setText("Voltage o/p")
        self.layout.addWidget(cont_v_op_l,1,4)

        cont_i_op_l = QtWidgets.QLabel(self)
        cont_i_op_l.setText("Current o/p")
        self.layout.addWidget(cont_i_op_l,1,5)

        cont_p_op_l = QtWidgets.QLabel(self)
        cont_p_op_l.setText("Power o/p")
        self.layout.addWidget(cont_p_op_l,1,6)

        motor_rpm_l = QtWidgets.QLabel(self)
        motor_rpm_l.setText("Motor RPM")
        self.layout.addWidget(motor_rpm_l,1,7)

        motor_tor_l = QtWidgets.QLabel(self)
        motor_tor_l.setText("Motor Torque")
        self.layout.addWidget(motor_tor_l,1,8)

        motor_pow_l = QtWidgets.QLabel(self)
        motor_pow_l.setText("Motor Power")
        self.layout.addWidget(motor_pow_l,1,9)

        run_l = QtWidgets.QLabel(self)
        run_l.setText("Run")
        self.layout.addWidget(run_l,1,10)

        del_l = QtWidgets.QLabel(self)
        del_l.setText("Del")
        self.layout.addWidget(del_l,1,11)

    def addLoadRow(self):
        if self.dataRowsNo <= 8:
            row = loadRow(self)
            self.dataTable.addWidget(row)
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
        self.layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.load      = QtWidgets.QLineEdit(self)
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

        self.delbtn = QtWidgets.QPushButton(self)
        self.delbtn.setText("-")
        self.delbtn.clicked.connect(self.delRow)

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
        self.layout.addWidget(self.delbtn,alignment=QtCore.Qt.AlignHCenter)

        self.running = False

    def runRow(self):
        if self.running == False:
            self.running = True
            self.runbtn.setStyleSheet("background: green")
        
            s2i = lambda x: int(x) if x else 0
            s2f = lambda x: float(x) if x else 0

            f2s = lambda x: int(('%0.2f'%(x)).replace('.',''))
            f2t = lambda x: int(('%0.1f'%(x)).replace('.',''))
            
            maxT = s2i(self.parent.motorT.text())
            maxT = f2t(maxT)
            load = s2i(self.parent.motorN.text()) / 30 * s2f(self.load.text()) / 100
            load = f2s(load)

            volt = s2i(self.parent.motorV.text())
            curr = s2i(self.parent.motorI.text())
            
            for dc in self.parent.dcS:
                dc.setVoltage(volt)
                dc.setCurrent(curr//5)
                dc.turnON()
            
            self.parent.vfd.setTorq(maxT)
            self.parent.vfd.setSpeed(load)
            self.parent.vfd.run(1)
        else:
            self.running = False
            self.runbtn.setStyleSheet("background: none")
            for dc in self.parent.dcS:
                dc.turnOFF()
            
            self.parent.vfd.stop()
    def delRow(self):
        self.parent.dataRowsNo -= 1
        self.parent.addRowbtn.setEnabled(True)
        self.deleteLater()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dashLoadCurveLog()
    window.showMaximized()
    sys.exit(app.exec_())