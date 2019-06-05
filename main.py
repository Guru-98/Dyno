import sys
from PyQt5 import QtWidgets
from ui.landingwindow import dynoLanding
import logging


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = dynoLanding()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    logging.basicConfig(format= '%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%d-%b-%y %H:%M:%S')
    log = logging.getLogger('Dyno.model.dcsource')
    log.setLevel(logging.INFO)
    log.disabled = True

    main()