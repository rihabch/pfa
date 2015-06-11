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
        #    self.cin_cmp_aj.editingFinished.connect(lambda: self.add_info(123))
        self.annuler_cmp.clicked.connect(self.toListe)
        self.initialiser_aj_cmp.clicked.connect(self.initialise)
        self.enregistrer_cmp.clicked.connect(self.add)

    def add(self):
        matricule= self.cin_cmp_aj.text()
        #nom_employe = self.nom_cmp_aj.text()
        #prenom_employe = self.prenom_cmp_aj.text()
        operation = self.op_cmp_aj.text()
        allure = self.allure_cmp_aj.text()
        retouche = self.retouche_cmp_aj.text()

        op_expreg = QtCore.QRegExp('[A-Za-z]{3}[0-9]*')
        op_validator = QtGui.QRegExpValidator(op_expreg,self.op_cmp_aj)
        self.op_cmp_aj.setValidator(op_validator)

        int_expreg = QtCore.QRegExp('[0-9]+')
        int_validator = QtGui.QRegExpValidator(int_expreg,self.cin_cmp_aj)
        self.cin_cmp_aj.setValidator(int_validator)

        validator_int = QtGui.QIntValidator(0,100,self)
        self.retouche_cmp_aj.setValidator(validator_int)
        self.allure_cmp_aj.setValidator(validator_int)

        if not (self.cin_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Matricule non valide")

        if not (self.op_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Operation non valide")

        if not (self.allure_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Allure non valide")

        if not (self.retouche_cmp_aj.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","Retouche non valide")

        if (self.allure_cmp_aj.hasAcceptableInput()) and (self.cin_cmp_aj.hasAcceptableInput()) \
                and (self.retouche_cmp_aj.hasAcceptableInput()) and (self.op_cmp_aj.hasAcceptableInput()):
            allureint = int(self.allure_cmp_aj.text())
            retoucheint = int(self.retouche_cmp_aj.text())
            competence = retoucheint*allureint
            print(competence)
            nbr = self.model.rowCount()
            print("nombre lignes")
            print(nbr)
            self.model.insertRow(nbr)
            self.model.setData(self.model.index(nbr-1, 0), matricule)
            self.model.setData(self.model.index(nbr-1, 1), operation)
            self.model.setData(self.model.index(nbr-1, 2), 'admin_02')
            self.model.setData(self.model.index(nbr-1, 3), allure)
            self.model.setData(self.model.index(nbr-1, 4), retouche)
            self.model.setData(self.model.index(nbr-1, 5), competence)
            self.model.setData(self.model.index(nbr-1, 6), QtCore.QDateTime.currentDateTime)
            count = self.model.rowCount()
            print(count)
            self.model.submitAll()
            if (count == nbr+1):
                self.model.submitAll()
                QMessageBox.information(self, "Success","Add Successful" )
                self.initialise()

    def initialise(self):
        self.cin_cmp_aj.clear()
        #self.nom_cmp_aj.clear()
        #self.prenom_cmp_aj.clear()
        self.op_cmp_aj.clear()
        self.allure_cmp_aj.clear()
        self.retouche_cmp_aj.clear()

    def toListe(self):
        self.list = liste_comp.Liste_Competence()
        self.list.show()
        self.close()

    def check_state(self, *args, **kwargs):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#c4df9b' # green
        else:
            color = '#f6989d' # red
            sender.setStyleSheet('QLineEdit { background-color: %s }' % color)


    def add_info(self,matricule):
        self.model2 = QtSql.QSqlRelationalTableModel()
        self.model2.setTable('employe')
        critere ="matricule = %s" %(matricule)
        print(critere)
        self.model2.setFilter(critere)
        self.model2.select()
        if (self.model2.rowCount() == 1):
            print('ok add_info')
            record = self.model.record(0)
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