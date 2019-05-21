import sys
from PyQt5 import QtWidgets
from ui.landingwindow import dynoLanding

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dynoLanding()
    window.showMaximized()
    sys.exit(app.exec_())