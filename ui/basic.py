from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL
import sys

class Ui_MainWidget(object):
    def setupUi(self,MainWidget,winSize):
        MainWidget.setObjectName("Dyno")
        self.centralwidget = QtWidgets.QWidget(MainWidget)
        self.centralwidget.setMaximumSize(winSize)
    
        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.setVerticalSpacing(10)
        
        self.motorID_container = QtWidgets.QVBoxLayout()
        self.motorID_lab = QtWidgets.QLabel(self.centralwidget)
        self.motorID_lab.setText("Motor &ID")
        self.motorID_container.addWidget(self.motorID_lab,alignment=QtCore.Qt.AlignHCenter)

        self.motorID = QtWidgets.QLineEdit(self.centralwidget)
        self.motorID_container.addWidget(self.motorID,alignment=QtCore.Qt.AlignHCenter)
        self.motorID_lab.setBuddy(self.motorID)
        self.layout.addLayout(self.motorID_container,0,0,1,11,alignment=QtCore.Qt.AlignHCenter)

        spacer = QtOpenGL.QGLWidget(self.centralwidget)
        self.layout.addWidget(spacer,1,0,1,11,alignment=QtCore.Qt.AlignHCenter)

        load_l = QtWidgets.QLabel(self.centralwidget)
        load_l.setText("Load %")
        self.layout.addWidget(load_l,2,0,2,1,alignment=QtCore.Qt.AlignCenter)

        con_ip_l = QtWidgets.QLabel(self.centralwidget)
        con_ip_l.setText("Controller i/p")
        self.layout.addWidget(con_ip_l,2,1,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_op_l = QtWidgets.QLabel(self.centralwidget)
        cont_op_l.setText("Controller o/p")
        self.layout.addWidget(cont_op_l,2,4,1,3,alignment=QtCore.Qt.AlignHCenter)

        motor_op_l = QtWidgets.QLabel(self.centralwidget)
        motor_op_l.setText("Motor o/p")
        self.layout.addWidget(motor_op_l,2,7,1,3,alignment=QtCore.Qt.AlignHCenter)

        cont_v_ip_l = QtWidgets.QLabel(self.centralwidget)
        cont_v_ip_l.setText("Voltage i/p")
        self.layout.addWidget(cont_v_ip_l,3,1,alignment=QtCore.Qt.AlignHCenter)

        cont_i_ip_l = QtWidgets.QLabel(self.centralwidget)
        cont_i_ip_l.setText("Current i/p")
        self.layout.addWidget(cont_i_ip_l,3,2,alignment=QtCore.Qt.AlignHCenter)

        cont_p_ip_l = QtWidgets.QLabel(self.centralwidget)
        cont_p_ip_l.setText("Power i/p")
        self.layout.addWidget(cont_p_ip_l,3,3,alignment=QtCore.Qt.AlignHCenter)

        cont_v_op_l = QtWidgets.QLabel(self.centralwidget)
        cont_v_op_l.setText("Voltage o/p")
        self.layout.addWidget(cont_v_op_l,3,4,alignment=QtCore.Qt.AlignHCenter)

        cont_i_op_l = QtWidgets.QLabel(self.centralwidget)
        cont_i_op_l.setText("Current o/p")
        self.layout.addWidget(cont_i_op_l,3,5,alignment=QtCore.Qt.AlignHCenter)

        cont_p_op_l = QtWidgets.QLabel(self.centralwidget)
        cont_p_op_l.setText("Power o/p")
        self.layout.addWidget(cont_p_op_l,3,6,alignment=QtCore.Qt.AlignHCenter)

        motor_rpm_l = QtWidgets.QLabel(self.centralwidget)
        motor_rpm_l.setText("Motor RPM")
        self.layout.addWidget(motor_rpm_l,3,7,alignment=QtCore.Qt.AlignHCenter)

        motor_tor_l = QtWidgets.QLabel(self.centralwidget)
        motor_tor_l.setText("Motor Torque")
        self.layout.addWidget(motor_tor_l,3,8,alignment=QtCore.Qt.AlignHCenter)

        motor_pow_l = QtWidgets.QLabel(self.centralwidget)
        motor_pow_l.setText("Motor Power")
        self.layout.addWidget(motor_pow_l,3,9,alignment=QtCore.Qt.AlignHCenter)

        k = 4
        for i in range(125,0,-25):
            load = QtWidgets.QLineEdit(self.centralwidget)
            load.setAlignment(QtCore.Qt.AlignHCenter)
            load.setText(str(i))
            cont_v_ip = QtWidgets.QLineEdit(self.centralwidget)
            cont_v_ip.setAlignment(QtCore.Qt.AlignHCenter)
            cont_i_ip = QtWidgets.QLineEdit(self.centralwidget)
            cont_i_ip.setAlignment(QtCore.Qt.AlignHCenter)
            cont_p_ip = QtWidgets.QLineEdit(self.centralwidget)
            cont_p_ip.setAlignment(QtCore.Qt.AlignHCenter)
            cont_v_op = QtWidgets.QLineEdit(self.centralwidget)
            cont_v_op.setAlignment(QtCore.Qt.AlignHCenter)
            cont_i_op = QtWidgets.QLineEdit(self.centralwidget)
            cont_i_op.setAlignment(QtCore.Qt.AlignHCenter)
            cont_p_op = QtWidgets.QLineEdit(self.centralwidget)
            cont_p_op.setAlignment(QtCore.Qt.AlignHCenter)
            motor_rpm = QtWidgets.QLineEdit(self.centralwidget)
            motor_rpm.setAlignment(QtCore.Qt.AlignHCenter)
            motor_tor = QtWidgets.QLineEdit(self.centralwidget)
            motor_tor.setAlignment(QtCore.Qt.AlignHCenter)
            motor_pow = QtWidgets.QLineEdit(self.centralwidget)
            motor_pow.setAlignment(QtCore.Qt.AlignHCenter)
            run_buton = QtWidgets.QPushButton(self.centralwidget)
            run_buton.setText(">")

            self.layout.addWidget(load,k,0,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(cont_v_ip,k,1,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(cont_i_ip,k,2,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(cont_p_ip,k,3,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(cont_v_op,k,4,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(cont_i_op,k,5,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(cont_p_op,k,6,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(motor_rpm,k,7,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(motor_tor,k,8,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(motor_pow,k,9,alignment=QtCore.Qt.AlignHCenter)
            self.layout.addWidget(run_buton,k,10,alignment=QtCore.Qt.AlignHCenter)

            k+=1

        run_all_button = QtWidgets.QPushButton(self.centralwidget)
        run_all_button.setText(">>")
        self.layout.addWidget(run_all_button,k,0,1,10,alignment=QtCore.Qt.AlignHCenter)

        #self.centralwidget.adjustSize()

app = QtWidgets.QApplication(sys.argv)
MainWidget = QtWidgets.QWidget()
winSize = QtCore.QSize(app.primaryScreen().geometry().width(),app.primaryScreen().geometry().height())
ui = Ui_MainWidget()
ui.setupUi(MainWidget,winSize)
MainWidget.showMaximized()
sys.exit(app.exec_())