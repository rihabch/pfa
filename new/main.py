__author__ = 'rihab'

import sys

from PyQt5 import QtWidgets
from ajouter_emp import Ajouter_Employe
from liste_employe import Liste_Employe
from liste_op import Liste_Operation
from ajouter_op import Ajouter_Operation
from login import Login
import connexion


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    connexion.connect()
    MainWindow = Liste_Operation()
    #MainWindow = Ajouter_Operation()
    #MainWindow = Liste_Employe()
    #MainWindow = Ajouter_Employe()
    #MainWindow = Login()
    MainWindow.show()
    sys.exit(app.exec_())