__author__ = 'root'

from PyQt5.QtWidgets import QWidget
from ui_grille_comp import Ui_Grille
from PyQt5 import QtSql


class Grille (QWidget, Ui_Grille):
    def __init__(self):
        super(Grille, self).__init__()
        self.setupUi(self)
        self.model1 = QtSql.QSqlRelationalTableModel()
        self.model1.setTable('operations')
        self.model2 = QtSql.QSqlRelationalTableModel()
        self.model2.setTable('employes')
        self.grille.setRowCount(self.model2.rowCount())
        self.grille.setColumnCount(self.model1.rowCount())
