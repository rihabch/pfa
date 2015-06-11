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
from ui_main import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)


    #MainWindow = MyApp()
    connexion.connect()
    #MainWindow = Liste_Operation()
    #MainWindow = Liste_Employe()
    #MainWindow = Ajouter_Employe()
    #MainWindow = Liste_Competence()
    #MainWindow = Login()
    MainWindow = Ajout_Competence()
    MainWindow.show()
    #connexion.connect()
    sys.exit(app.exec_())
