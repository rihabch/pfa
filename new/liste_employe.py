from ui_liste_emp import Ui_Employee_List
import ajouter_emp
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql, QtCore, QtGui, QtWidgets
from session import Session

class Liste_Employe(QWidget, Ui_Employee_List):
    def __init__(self):
        super(Liste_Employe, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.table_emp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_emp.setModel(self.model)
        self.model.select()
        self.fill(self.model)
        self.initialiser_emp.clicked.connect(self.initialise)
        self.rechercher_emp.clicked.connect(self.search)
        self.ajouter_emp.clicked.connect(self.toAdd)
        self.Modifier_emp.clicked.connect(self.edit)
        self.supprimer_emp.clicked.connect(self.delete_row)
        session = Session()
        print("login admin: ")
        print(session.passe)


    def fill(self,model):
        model.setHeaderData(0, QtCore.Qt.Horizontal, "CIN")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Matricule")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Code Utilisateur")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Nom")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Prenom")
        model.setHeaderData(5, QtCore.Qt.Horizontal, "Date Embauche")
        model.setHeaderData(6, QtCore.Qt.Horizontal, "Image")
        model.setHeaderData(7, QtCore.Qt.Horizontal, "Presence")
        model.setHeaderData(8, QtCore.Qt.Horizontal, "Date Naissance")
        self.table_emp.setModel(model)

    def initialise(self):
        self.cin_emp.clear()
        self.mat_emp.clear()
        self.nom_emp.clear()
        self.prenom_emp.clear()
        self.model2 = QtSql.QSqlRelationalTableModel()
        self.model2.setTable('employe')
        self.table_emp.setModel(self.model2)
        self.model2.select()
        self.fill(self.model2)
        #self.date_emb_emp.setDateTime(QtCore.QDateTime.currentDateTime())
        #self.date_nass_emp.setDateTime(QtCore.QDateTime.currentDateTime())

    def search(self):
        cin_employe = self.cin_emp.text()
        matricule_employe = self.mat_emp.text()
        nom_employe = self.nom_emp.text()
        prenom_employe = self.prenom_emp.text()
        #date_embauche = self.date_emb_emp.date().toString("yyyy-MM-dd")
        #date_naissance = self.date_nass_emp.date().toString("yyyy-MM-dd")
        critere =""
        if not len(cin_employe) == 0:
            critere += " cin_emp = %s" %(cin_employe)
        if not len(matricule_employe) == 0:
            critere += " matricule = %s" %(matricule_employe)
        if not len(nom_employe) == 0:
            critere += " nom = '%s'" %(nom_employe)
        if not len(prenom_employe) == 0:
            critere += " prenom = '%s'" %(prenom_employe)
        #if not len(date_embauche) == 0:
        #    critere += " AND date_embauche = %s" %(date_embauche)
        #if not len(date_naissance) == 0:
        #    critere += " AND date_naissance = %s" %(date_naissance)
        print(critere)
        self.model.setFilter(critere)
        self.model.select()
        print(self.model.rowCount())
        if (self.model.rowCount()>= 1):
            print('ok search')
            self.fill(self.model)


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

    def toAdd(self):
        self.ajout = ajouter_emp.Ajouter_Employe()
        self.ajout.show()
        self.close()


    def delete_row(self):

            reply = QtWidgets.QMessageBox.question(self, "Demande de suppression","Êtes-vous sûr de vouloir supprimer l'employé ?",
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)

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


