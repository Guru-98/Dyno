import sys
from PyQt5 import QtCore, QtWidgets, QtOpenGL, uic

class dashLoadCurveLog(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(dashLoadCurveLog,self).__init__(parent)

        self.layout = QtWidgets.QGridLayout(self)

        self.motorID_container = QtWidgets.QVBoxLayout()
        self.motorID_lab = QtWidgets.QLabel(self)
        self.motorID_lab.setText("Motor &ID")
        self.motorID_container.addWidget(self.motorID_lab,alignment=QtCore.Qt.AlignHCenter)

        self.motorID = QtWidgets.QLineEdit(self)
        self.motorID_container.addWidget(self.motorID,alignment=QtCore.Qt.AlignHCenter)
        self.motorID_lab.setBuddy(self.motorID)
        self.layout.addLayout(self.motorID_container,0,0,1,11,alignment=QtCore.Qt.AlignHCenter)

        spacer = QtOpenGL.QGLWidget(self)
        self.layout.addWidget(spacer,1,0,1,11,alignment=QtCore.Qt.AlignHCenter)

        self.loadHeader()
        dataTable = []

        k = 4
        for i in range(125,0,-25):
            dataRow = loadRow(self)
            dataRow.load.setText(str(i))
            dataTable.append((str(i),dataRow))
            self.layout.addWidget(dataRow,k,0,1,11,alignment=QtCore.Qt.AlignHCenter)
            k+=1

        run_all_button = QtWidgets.QPushButton(self)
        run_all_button.setText(">>")
        self.layout.addWidget(run_all_button,k,0,1,11,alignment=QtCore.Qt.AlignHCenter)

    def loadHeader(self):
        load_l = QtWidgets.QLabel(self)
        load_l.setText("Load %")
        self.layout.addWidget(load_l,2,0,2,1,alignment=QtCore.Qt.AlignCenter)

        con_ip_l = QtWidgets.QLabel(self)
        con_ip_l.setText("Controller i/p")
        self.layout.addWidget(con_ip_l,2,1,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_op_l = QtWidgets.QLabel(self)
        cont_op_l.setText("Controller o/p")
        self.layout.addWidget(cont_op_l,2,4,1,3,alignment=QtCore.Qt.AlignHCenter)

        motor_op_l = QtWidgets.QLabel(self)
        motor_op_l.setText("Motor o/p")
        self.layout.addWidget(motor_op_l,2,7,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_v_ip_l = QtWidgets.QLabel(self)
        cont_v_ip_l.setText("Voltage i/p")
        self.layout.addWidget(cont_v_ip_l,3,1,alignment=QtCore.Qt.AlignHCenter)

        cont_i_ip_l = QtWidgets.QLabel(self)
        cont_i_ip_l.setText("Current i/p")
        self.layout.addWidget(cont_i_ip_l,3,2,alignment=QtCore.Qt.AlignHCenter)

        cont_p_ip_l = QtWidgets.QLabel(self)
        cont_p_ip_l.setText("Power i/p")
        self.layout.addWidget(cont_p_ip_l,3,3,alignment=QtCore.Qt.AlignHCenter)

        cont_v_op_l = QtWidgets.QLabel(self)
        cont_v_op_l.setText("Voltage o/p")
        self.layout.addWidget(cont_v_op_l,3,4,alignment=QtCore.Qt.AlignHCenter)

        cont_i_op_l = QtWidgets.QLabel(self)
        cont_i_op_l.setText("Current o/p")
        self.layout.addWidget(cont_i_op_l,3,5,alignment=QtCore.Qt.AlignHCenter)

        cont_p_op_l = QtWidgets.QLabel(self)
        cont_p_op_l.setText("Power o/p")
        self.layout.addWidget(cont_p_op_l,3,6,alignment=QtCore.Qt.AlignHCenter)

        motor_rpm_l = QtWidgets.QLabel(self)
        motor_rpm_l.setText("Motor RPM")
        self.layout.addWidget(motor_rpm_l,3,7,alignment=QtCore.Qt.AlignHCenter)

        motor_tor_l = QtWidgets.QLabel(self)
        motor_tor_l.setText("Motor Torque")
        self.layout.addWidget(motor_tor_l,3,8,alignment=QtCore.Qt.AlignHCenter)

        motor_pow_l = QtWidgets.QLabel(self)
        motor_pow_l.setText("Motor Power")
        self.layout.addWidget(motor_pow_l,3,9,alignment=QtCore.Qt.AlignHCenter)

class loadRow(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(loadRow,self).__init__(parent)

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
        self.run_buton = QtWidgets.QPushButton(self)
        self.run_buton.setText(">")

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
        self.layout.addWidget(self.run_buton,alignment=QtCore.Qt.AlignHCenter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dashLoadCurveLog()
    window.showMaximized()
    sys.exit(app.exec_())