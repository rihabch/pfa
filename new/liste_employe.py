from ui_liste_emp import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql

class Liste_Employe(QWidget, Ui_Form):
    def __init__(self):
        super(Liste_Employe, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.model.select()
        print (self.model.rowCount())
        self.table_emp.setModel(self.model)