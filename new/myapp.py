__author__ = 'root'


from ajouter_emp import Ajouter_Employe
from liste_comp import Liste_Competence
from liste_employe import Liste_Employe
from liste_op import Liste_Operation
from ajout_comp import Ajout_Competence
import connexion
from ui_main import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Configure l'interface utilisateur.
        self.setupUi(self)
        self.Liste_Employes.triggered.connect(self.toListe_emp)
        self.Competences.triggered.connect(self.toComp)
        self.Details_Operation.triggered.connect(self.toOp)

    def toListe_emp(self):
        self.list = Liste_Employe()
        self.list.show()
    def toComp (self):
        self.comp = Liste_Competence()
        self.comp.show()
    def toOp(self):
        self.op = Liste_Operation()
        self.op.show()