__author__ = 'imen'

from ui_liste_comp import Ui_Liste_Competence
import ajout_comp
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql, QtCore, QtWidgets

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
        self.supprimer_cmp.clicked.connect(self.delete_row)


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
        reply = QtWidgets.QMessageBox.question(self, "Demande de modification","Êtes-vous sûr de vouloir modifier la compétence ?",
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


    def toAdd(self):
        self.ajout = ajout_comp.Ajout_Competence()
        self.ajout.show()
        self.close()


    def delete_row(self):

        reply = QtWidgets.QMessageBox.question(self, "Demande de suppression","Êtes-vous sûr de vouloir supprimer cette compétence ?",QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)

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