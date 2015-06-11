__author__ = 'imen'

from ui_liste_op import Ui_Liste_Op
import ajouter_op
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtCore, QtWidgets


class Liste_Operation(QWidget, Ui_Liste_Op):
    def __init__(self):
        super(Liste_Operation, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('operation')
        self.model.select()
        self.fill()
        self.initialiser_op.clicked.connect(self.initialise)
        self.recherche_op.clicked.connect(self.search)
        self.ajouter_op.clicked.connect(self.toAdd)
        self.supprimer_op.clicked.connect(self.delete_row)

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
        self.code_op.clear()
        self.nom_op.clear()
        self.machine_op.clear()


    def search(self):
        print("trying to do some research")

    def toAdd(self):
        self.ajout = ajouter_op.Ajouter_Operation()
        self.ajout.show()
        self.close()


    def edit(self):
        reply = QtWidgets.QMessageBox.question(self, "Demande de modification","Êtes-vous sûr de vouloir modifier l'employé ?",
        QtWidgets.QMessageBox.Yes,
        QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            row = self.model.rowCount()
            selection = QtCore.QItemSelectionModel(self.model)
            index = selection.currentIndex()

            if  self.model.insertRow(row,index):
                self.model.submitAll()
                print("ok edit")
                QMessageBox.information(self, "Succès","Modification avec succès")
                self.initialise()
            else:
                QMessageBox.information(self, "Erreur","Erreur modification attribut")
        else:
                reply.close(self)


    def delete_row(self):

        reply = QtWidgets.QMessageBox.question(self, "Demande de suppression","Êtes-vous sûr de vouloir supprimer cette opération ?",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            l = self.table_emp.currentIndex().row()
            print("ligne")
            print(l)
            selection = QtCore.QItemSelectionModel(self.model)
            index = selection.currentIndex()
            if self.model.removeRows(l, 1, index):
                self.model.submitAll()
                print("ok suppression")
                QMessageBox.information(self, "Succès","Suppression avec succès")
                self.initialise()

            else:
                QMessageBox.information(self, "Erreur","Erreur suppression attribut")

        else:
            reply.close(self)