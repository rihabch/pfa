__author__ = 'rihab'

import sys

from PyQt5 import QtWidgets


import liste_employe
import connexion

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    connexion.connect()
    MainWindow = liste_employe.Liste_Employe()
    #MainWindow = Ajouter_Employe()
    MainWindow.show()
    sys.exit(app.exec_())