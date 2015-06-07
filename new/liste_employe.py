from ui_liste_emp import Ui_Employee_List
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtCore

class Liste_Employe(QWidget, Ui_Employee_List):
    def __init__(self):
        super(Liste_Employe, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "CIN")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Matricule")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Code Utilisateur")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Nom")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Prenom")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Date Embauche")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Image")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Presence")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Date Naissance")
        print (self.model.rowCount())
        self.table_emp.setModel(self.model)

