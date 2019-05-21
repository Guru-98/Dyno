import sys
from PyQt5 import QtCore, QtWidgets, QtOpenGL, uic

qtCreatorFile = "ui/settings.ui"
Ui_SettingsDialog, QtBaseClass = uic.loadUiType(qtCreatorFile)

class settingsDialog(QtWidgets.QDialog, Ui_SettingsDialog):
    def __init__(self,parent=None):
        super(settingsDialog,self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setupUi(self)

    def accept(self):
        print("OK")
        self.done(1)

    def reject(self):
        print("NOK")
        self.done(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = settingsDialog()
    dialog.show()
    sys.exit(app.exec_())