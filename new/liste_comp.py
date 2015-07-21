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
        self.model.setTable('competences')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.competence.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.model.select()
        self.fill(self.model)
        self.initialiser_cmp.clicked.connect(self.initialise)
        self.rechercher_cmp.clicked.connect(self.search)
        self.affecter_cmp.clicked.connect(self.toAdd)
        self.modifier_cmp.clicked.connect(self.edit)
        self.supprimer_cmp.clicked.connect(self.delete_row)


    def fill(self,model):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Matricule")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Code Operation")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Code Utilisateur")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Allure")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Taux de retouche")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Competence")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Date Affectation")
        self.competence.setModel(model)

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


    def toAdd(self):
        self.ajout = ajout_comp.Ajout_Competence()
        self.ajout.show()
        self.close()


    def initialise(self):
        self.line_ouvr_cmp.clear()
        self.op_cmp.clear()
        self.comp_cmp.clear()
        self.model2 = QtSql.QSqlRelationalTableModel()
        self.model2.setTable('competence')
        self.competence.setModel(self.model2)
        self.model2.select()
        self.fill(self.model2)


    def search(self):
        ouvr = self.line_ouvr_cmp.text()
        oper = self.op_cmp.text()
        comp = self.comp_cmp.text()
        critere =""
        if not len(ouvr) == 0:
            critere += " matricule = %s" %(ouvr)
        if not len(oper) == 0:
            critere += " code_op = %s" %(oper)
        if not len(comp) == 0:
            critere += " competence = '%s'" %(comp)
        print(critere)
        self.model.setFilter(critere)
        self.model.select()
        print(self.model.rowCount())
        if (self.model.rowCount()>= 1):
            print('ok search')
            self.fill(self.model)


    def delete_row(self):

            reply = QtWidgets.QMessageBox.question(self, "Demande de suppression","Êtes-vous sûr de vouloir supprimer la compétence ?",
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                l = self.competence.currentIndex().row()
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


