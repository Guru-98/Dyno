import sys
from PyQt5 import QtCore, QtWidgets, QtOpenGL, uic
from serial import Serial, SerialException 
from serial.tools import list_ports

qtCreatorFile = "ui/settings.ui"
Ui_SettingsDialog, QtBaseClass = uic.loadUiType(qtCreatorFile)

class settingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
    def __init__(self,parent=None):
        super(settingsDialog,self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setupUi(self)
        ports = [(port.device,port) for port in list_ports.comports()]
        ports.sort(key=lambda x: int(x[0].split("COM")[1]))
        [opt.addItem(port[0],port[1]) for port in ports for opt in self.findChildren(QtWidgets.QComboBox)]

    def accept(self):
        print("OK")
        for row in range(0,self.settingsList.rowCount()):
            l = self.settingsList.itemAt(row,QtWidgets.QFormLayout.LabelRole).widget()
            d = self.settingsList.itemAt(row,QtWidgets.QFormLayout.FieldRole).widget()
            print(l.text(),d.currentData()) # d.currentData()

        # set serial ports to sensors
        # check sensors comm
        
        self.done(1)

    def reject(self):
        print("NOK")
        self.done(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = settingsDialog()
    dialog.show()
    sys.exit(app.exec_())