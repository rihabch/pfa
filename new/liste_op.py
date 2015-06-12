__author__ = 'imen'

from ui_liste_op import Ui_Liste_Op
from ajouter_op import Ajouter_Operation
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql, QtCore, QtWidgets


class Liste_Operation(QWidget, Ui_Liste_Op):
    def __init__(self):
        super(Liste_Operation, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('operation')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView.setModel(self.model)
        self.model.select()
        self.fill(self.model)
        self.initialiser_op.clicked.connect(self.initialise)
        self.recherche_op.clicked.connect(self.search)
        self.ajouter_op.clicked.connect(self.toAdd)
        self.modifier_op.clicked.connect(self.edit)
        self.supprimer_op.clicked.connect(self.delete_row)

    def fill(self,model):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Code Operation")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Code Utilisateur")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Nom Operation")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Minutage")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Nom Machine")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Critere de Qualite")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Video")
        self.tableView.setModel(model)

    def initialise(self):
        self.code_op.clear()
        self.nom_op.clear()
        self.machine_op.clear()
        self.model2 = QtSql.QSqlRelationalTableModel()
        self.model2.setTable('operation')
        self.tableView.setModel(self.model2)
        self.model2.select()
        self.fill(self.model2)


    def search(self):
        code = self.code_op.text()
        nom = self.nom_op.text()
        machine = self.machine_op.text()
        critere =""
        if not len(code) == 0:
            critere += " code_op = %s" %(code)
        if not len(nom) == 0:
            critere += " nom_op = %s" %(nom)
        if not len(machine) == 0:
            critere += " machine = '%s'" %(machine)

        print(critere)
        self.model.setFilter(critere)
        self.model.select()
        print(self.model.rowCount())
        if (self.model.rowCount()>= 1):
            print('ok search')
            self.fill(self.model)

    def toAdd(self):
        self.ajout = Ajouter_Operation()
        self.ajout.show()
        self.close()


    def edit(self):
        reply = QtWidgets.QMessageBox.question(self, "Demande de modification","Êtes-vous sûr de vouloir modifier l'opération ?",
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

            reply = QtWidgets.QMessageBox.question(self, "Demande de suppression","Êtes-vous sûr de vouloir supprimer l'opération ?",
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                l = self.tableView.currentIndex().row()
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
