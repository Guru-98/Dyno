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

        self.readSettings()

    def readSettings(self):
        import configparser

        config = configparser.ConfigParser()
        config.read('settings.ini')

        DC1 = config.get('devices','DC1',fallback="COM1")
        DC2 = config.get('devices','DC2',fallback="COM1")
        DC3 = config.get('devices','DC3',fallback="COM1")
        DC4 = config.get('devices','DC4',fallback="COM1")
        DC5 = config.get('devices','DC5',fallback="COM1")        
        VFD = config.get("devices","VFD",fallback="COM1")
        OSC = config.get("devices","OSC",fallback="COM1")

        self.dC1ComboBox.setCurrentText(DC1)
        self.dC2ComboBox.setCurrentText(DC2)
        self.dC3ComboBox.setCurrentText(DC3)
        self.dC4ComboBox.setCurrentText(DC4)
        self.dC5ComboBox.setCurrentText(DC5)

        self.VFDComboBox.setCurrentText(VFD)
        self.OSCComboBox.setCurrentText(OSC)

    def writesettings(self):
        import configparser

        config = configparser.ConfigParser()
        config['devices'] = {}

        config['devices']['DC1'] = self.dC1ComboBox.currentText()
        config['devices']['DC2'] = self.dC2ComboBox.currentText()
        config['devices']['DC3'] = self.dC3ComboBox.currentText()
        config['devices']['DC4'] = self.dC4ComboBox.currentText()
        config['devices']['DC5'] = self.dC5ComboBox.currentText()

        config['devices']['VFD'] = self.VFDComboBox.currentText()
        config['devices']['OSC'] = self.OSCComboBox.currentText()

        with open('settings.ini','w') as configFile:
            config.write(configFile)

    def accept(self):
        self.writesettings()
        self.done(1)

    def reject(self):
        print("NOK")
        self.done(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = settingsDialog()
    dialog.show()
    sys.exit(app.exec_())