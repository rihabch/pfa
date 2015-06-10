__author__ = 'imen'

from ui_liste_comp import Ui_Liste_Competence
import ajout_comp
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql, QtCore

class Liste_Competence(QWidget, Ui_Liste_Competence):
    def __init__(self):
        super(Liste_Competence, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('competence')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.fill()
        self.initialiser_cmp.clicked.connect(self.initialise)
        #self.rechercher_cmp.clicked.connect(self.search)
        self.affecter_cmp.clicked.connect(self.toAdd)
        self.modifier_cmp.clicked.connect(self.edit)


    def fill(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Matricule")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Nom")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Prenom")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Code Operation")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Nom Operation")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Competence")
        print (self.model.rowCount())
        self.competence.setModel(self.model)

    def initialise(self):
        self.line_ouvr_cmp.clear()
        self.op_cmp.clear()
        self.comp_cmp.clear()


    def edit(self):
        self.table_emp.setModel(self.model)
        row = self.model.rowCount()
        self.model.insertRow(row)
        if self.model.submitAll():
            print("ok edit")
            QMessageBox.information(self, "Success","Edit Successful" )


    def toAdd(self):
        self.ajout = ajout_comp.Ajout_Competence()
        self.ajout.show()
        self.close()