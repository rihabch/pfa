__author__ = 'imen'

from ui_ajout_comp import Ui_Ajout_Competence
import liste_comp
from PyQt5.QtWidgets import QWidget , QMessageBox
from PyQt5 import QtSql, QtCore, QtGui

class Ajout_Competence(QWidget, Ui_Ajout_Competence):
    def __init__(self):
        super(Ajout_Competence, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('competence')
        self.model.select()
        self.annuler_cmp.clicked.connect(self.toListe)
        self.initialiser_aj_cmp.clicked.connect(self.initialise)
        self.enregistrer_cmp.clicked.connect(self.add)

    def add(self):
        matricule= self.mat_cmp_aj.text()
        #nom_employe = self.nom_cmp_aj.text()
        #prenom_employe = self.prenom_cmp_aj.text()
        operation = self.op_cmp_aj.text()
        allure = self.allure_cmp_aj.text()
        retouche = self.retouche_cmp_aj.text()
        validator_int = QtGui.QIntValidator(0,100,self)
        int_expreg = QtCore.QRegExp('[0-9]+')
        int_validator = QtGui.QRegExpValidator(int_expreg,self.mat_cmp_aj)
        self.mat_cmp_aj.setValidator(int_validator)
        self.retouche_cmp_aj.setValidator(validator_int)
        self.allure_cmp_aj.setValidator(validator_int)
        if not (self.allure_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Allure non valide")
        if not (self.mat_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Matricule non valide")
        if not (self.retouche_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Retouche non valide")
        if (self.allure_cmp_aj.hasAcceptableInput()) and (self.mat_cmp_aj.hasAcceptableInput()) and (self.retouche_cmp_aj.hasAcceptableInput()):
            print("verifié")
            if int(retouche) > 8:
                pour_comp = int(allure) - int(retouche)
            else:
                pour_comp = int(allure)
            competence = self.set_comp(pour_comp)
            print("competence")
            print(competence)
            nbr = self.model.rowCount()
            self.model.insertRow(nbr)
            self.model.setData(self.model.index(nbr - 1, 0), int(matricule))
            self.model.setData(self.model.index(nbr - 1, 1), 'admin_01')
            self.model.setData(self.model.index(nbr - 1, 2), operation)
            self.model.setData(self.model.index(nbr - 1, 3), int(allure))
            self.model.setData(self.model.index(nbr - 1, 4), int(retouche))
            self.model.setData(self.model.index(nbr - 1, 5), competence)
            self.model.setData(self.model.index(nbr - 1, 6), QtCore.QDateTime.currentDateTime())

            if self.model.submitAll():
                QMessageBox.information(self, "Succes","Ajout avec Succes" )

            else:
                self.db = QtSql.QSqlDatabase.database()
                QMessageBox.information(self, "Echec","Echec Ajout" )
                print (self.db.lastError().text())

    def initialise(self):
        self.mat_cmp_aj.clear()
        self.nom_cmp_aj.clear()
        self.prenom_cmp_aj.clear()
        self.op_cmp_aj.clear()
        self.allure_cmp_aj.clear()
        self.retouche_cmp_aj.clear()

    def toListe(self):

        self.list = liste_comp.Liste_Competence()
        self.list.show()
        self.close()

    def add_info(self,matricule, prenom_employe):
        self.model2 = QtSql.QSqlRelationalTableModel()
        self.model2.setTable('employe')
        critere ="matricule = %s" %(matricule)
        print(critere)
        self.model2.setFilter(critere)
        self.model2.select()
        if (self.model2.rowCount() == 1):
            print('ok add_info')
            record = self.model.record(0)
            self.prenom_cmp_aj.insert(prenom_employe)
            self.prenom_cmp_aj.insert(prenom_employe)
            nom_employe = record.value("nom")
            prenom_employe = record.value("prenom")
            #index = self.model2.fieldIndex("nom")
            #index2 = self.model2.fieldIndex("prenom")
            #nom_employe = self.model2.data(index2)
            #prenom_employe = self.prenom_cmp_aj.text()
            print("nom employe")
            print(nom_employe)
            print("prenom employe")
            print(prenom_employe)
            self.nom_cmp_aj.insert(nom_employe)
            self.prenom_cmp_aj.insert(prenom_employe)

    def set_comp(self,com):
        if com < 20:
            return 1
        elif com< 40:
            return 2
        elif com < 60:
            return 3
        elif com < 80:
            return 4
        else:
            return 5

