import sys
from PyQt5 import QtCore, QtWidgets, QtOpenGL, uic
from ui.settings import settingsDialog
from ui.loadcurvelog import dashLoadCurveLog

qtCreatorFile = "ui/landingwindow.ui"
Ui_dynoLandingWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class dynoLanding(QtWidgets.QMainWindow, Ui_dynoLandingWindow):
    def __init__(self,parent=None, winSize=(0,0)):
        super(dynoLanding,self).__init__(parent)
        self.setupUi(self)
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.addWidget(dashLoadCurveLog(self.centralwidget))

        self.actionSettings.triggered.connect(self.showSettingsDialog)
    
    def showSettingsDialog(self):
        dialog = settingsDialog(self)
        res = dialog.exec()
        print(res)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dynoLanding()
    window.showMaximized()
    sys.exit(app.exec_())