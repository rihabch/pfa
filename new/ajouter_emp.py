__author__ = 'rihab'
from ui_ajouter_emp import Ui_Add_Employee
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql

class Ajouter_Employe(QWidget, Ui_Add_Employee):
    def __init__(self):
        super(Ajouter_Employe, self).__init__()
        self.setupUi(self)
        self.enregistrer_emp.clicked.connect(self.add)

    def add(self):
        print("ok")

