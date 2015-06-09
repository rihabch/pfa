__author__ = 'imen'

from ui_liste_op import Ui_Liste_Op
import ajouter_op
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtCore


class Liste_Operation(QWidget, Ui_Liste_Op):
    def __init__(self):
        super(Liste_Operation, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('operation')
        self.model.select()
        self.fill()
        self.initialiser_op.clicked.connect(self.initialise)
        #self.recherche_op.clicked.connect(self.search)
        self.ajouter_op.clicked.connect(self.toAdd)

    def fill(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Code Operation")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Code Utilisateur")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Nom Operation")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Minutage")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Nom Machine")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Critere de Qualite")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Video")
        print(self.model.rowCount())
        self.tableView.setModel(self.model)

    def initialise(self):
        self.code_op_aj.clear()
        self.nom_op_aj.clear()
        self.minute_op_aj.clear()
        self.machine_op_aj.clear()
        self.Qcritere.clear()
        self.video_path.clear()

    def toAdd(self):
        self.ajout = ajouter_op.Ajouter_Operation()
        self.ajout.show()
        self.close()


    def edit(self):
        self.table_emp.setModel(self.model)
        row = self.model.rowCount()
        self.model.insertRow(row)
        if self.model.submitAll():
            print("ok edit")
            QMessageBox.information(self, "Success","Edit Successful" )