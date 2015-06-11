__author__ = 'rihab'

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from ajouter_emp import Ajouter_Employe
from liste_comp import Liste_Competence
from liste_employe import Liste_Employe
from liste_op import Liste_Operation
from login import Login
from ajout_comp import Ajout_Competence
import connexion

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    #MainWindow = MyApp()

    connexion.connect()
    #MainWindow = Liste_Operation()
    #MainWindow = Liste_Employe()
    #MainWindow = Ajouter_Employe()
    #MainWindow = Liste_Competence()
    MainWindow = Login()

    MainWindow.show()
    sys.exit(app.exec_())
