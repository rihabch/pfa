__author__ = 'rihab'

import sys

from PyQt5 import QtWidgets
from login import Login
import connexion


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    connexion.connect()

    MainWindow = Login()
    MainWindow.show()
    sys.exit(app.exec_())