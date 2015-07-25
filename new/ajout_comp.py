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
        self.model.setTable('competences')

        self.model.setRelation(1,QtSql.QSqlRelation("operations", "code_op", "code_op"))
        self.model.setRelation(0,QtSql.QSqlRelation("employes", "matricule", "matricule"))
        #self.model.setRelation(0,QtSql.QSqlRelation("employe", "matricule", "nom"))
        #self.model.setRelation(0,QtSql.QSqlRelation("employe", "matricule", "prenom"))

        self.model.select()

        self.relationModel = self.model.relationModel(1)
        self.op_cmp_aj.setModel(self.relationModel)
        self.op_cmp_aj.setModelColumn(self.relationModel.fieldIndex("code_op"))

        self.relationModel2 = self.model.relationModel(0)
        self.mat_cmp_aj.setModel(self.relationModel2)
        self.mat_cmp_aj.setModelColumn(self.relationModel2.fieldIndex("matricule"))


        #self.mat_cmp_aj.currentIndexChanged.connect(self.add_info)

        self.annuler_cmp.clicked.connect(self.toListe)
        #self.initialiser_aj_cmp.clicked.connect(self.initialise)
        self.enregistrer_cmp.clicked.connect(self.add)

    def add(self):
        matricule= str(self.mat_cmp_aj.currentText())

        #nom_employe = self.nom_cmp_aj.text()
        #prenom_employe = self.prenom_cmp_aj.text()
        operation = str(self.op_cmp_aj.currentText())
        allure = self.allure_cmp_aj.text()
        total = self.retouche_cmp_aj.text()
        p_ret = self.retouche_comp.text()
        #self.parcourir.clicked.connect(self.import_picture)



        validator_int = QtGui.QIntValidator(0,100,self)
        int_validator = QtGui.QIntValidator(self)
        self.allure_cmp_aj.setValidator(validator_int)
        self.retouche_cmp_aj.setValidator(int_validator)
        self.retouche_comp.setValidator(int_validator)

        if not (self.allure_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Allure non valide")

        if not (self.retouche_cmp_aj.hasAcceptableInput() or self.retouche_comp.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Retouche non valide")

        if (self.retouche_comp.hasAcceptableInput()) and (self.retouche_cmp_aj.hasAcceptableInput()):
            if int(total) < int(p_ret):
               QMessageBox.information(self, "Erreur","Le nombre de pièces retouchées est supérieur au nombre total de pièces")
            else:
                retouche = (int(p_ret)*100)/ int(total)

        if (self.allure_cmp_aj.hasAcceptableInput()) and (self.retouche_comp.hasAcceptableInput()) and (self.retouche_cmp_aj.hasAcceptableInput()):
            print("verifié")
            if int(retouche) > 8:
                pour_comp = int(allure) - int(retouche)
            else:
                pour_comp = int(allure)
            competence = self.set_comp(pour_comp)
            print("competence")
            print(competence)

            nbr = self.model.rowCount()
            print("nombre lignes")
            print(nbr)
            self.model.insertRow(nbr)
            self.model.setData(self.model.index(nbr, 0), matricule)
            self.model.setData(self.model.index(nbr, 1), operation)
            self.model.setData(self.model.index(nbr, 6), 'admin_02')
            self.model.setData(self.model.index(nbr, 3), allure)
            self.model.setData(self.model.index(nbr, 4), retouche)
            self.model.setData(self.model.index(nbr, 2), competence)
            self.model.setData(self.model.index(nbr, 5), QtCore.QDateTime.currentDateTime())
            count = self.model.rowCount()
            print(count)
            if (count == nbr+1):
                self.model.submitAll()
                QMessageBox.information(self, "Succes","Ajout avec Succes" )
                self.initialise()



    def initialise(self):
        self.mat_cmp_aj.clear()
        #self.nom_cmp_aj.clear()
        #self.prenom_cmp_aj.clear()
        self.op_cmp_aj.clear()
        self.allure_cmp_aj.clear()
        self.retouche_cmp_aj.clear()
        self.retouche_comp.clear()

    def toListe(self):
        self.list = liste_comp.Liste_Competence()
        self.list.show()
        self.close()

    """def add_info(self):
        matricule= str(self.mat_cmp_aj.currentText())
        print(matricule)
        self.model.relationModel(0).setFilter("matricule = '%s'" %matricule)
        self.nom_cmp_aj.setModel(self.relationModel2)
        self.nom_cmp_aj.setModelColumn(self.relationModel2.fieldIndex("nom"))
        self.model.select()
        nom= str(self.nom_cmp_aj.currentText())
        print("nom")
        print(nom)
        self.prenom_cmp_aj.setModel(self.relationModel2)
        self.prenom_cmp_aj.setModelColumn(self.relationModel2.fieldIndex("prenom"))
        prenom= str(self.prenom_cmp_aj.currentText())

        print("prenom")
        print(prenom)
"""
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

