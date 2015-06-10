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

        self.mat_cmp_anj.editingChanged.connect(self.add_info(matricule))
        #nom_employe = self.nom_cmp_aj.text()
        #prenom_employe = self.prenom_cmp_aj.text()
        #operation = self.op_cmp_aj.text()
        allure = self.allure_cmp_aj.text()
        retouche = self.retouche_cmp_aj.text()
        competence = retouche*allure

        validator_int = QtGui.QIntValidator(matricule)
        matricule.setValidator(validator_int)
        validator_float = QtGui.QDoubleValidator(retouche,allure)
        retouche.setValidator(validator_float)
        allure.setValidator(validator_float)
        matricule.textChanged.connect(self.check_state)
        matricule.textChanged.emit(matricule.text())
        retouche.textChanged.connect(self.check_state)
        retouche.textChanged.emit(retouche.text())
        allure.textChanged.connect(self.check_state)
        allure.textChanged.emit(allure.text())


        nbr = self.model.rowCount()
        self.model.insertRow(nbr)
        self.model.setData(self.model.index(nbr - 1, 0), matricule)
        self.model.setData(self.model.index(nbr - 1, 1), '1')
        self.model.setData(self.model.index(nbr - 1, 2), '1')
        self.model.setData(self.model.index(nbr - 1, 3), allure)
        self.model.setData(self.model.index(nbr - 1, 4), retouche)
        self.model.setData(self.model.index(nbr - 1, 5), competence)
        self.model.setData(self.model.index(nbr - 1, 6), QtCore.QDateTime.currentDateTime())
        if self.model.submitAll():
           QMessageBox.information(self, "Success","Add Successful" )

        else:
            self.db = QtSql.QSqlDatabase.database()
            print(self.db.lastError().databaseText())

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
            index = self.model2.fieldIndex("nom")
            index2 = self.model2.fieldIndex("prenom")
            nom_employe = self.model2.data(index2)
            prenom_employe = self.prenom_cmp_aj.text()
            self.nom_cmp_aj.insert(nom_employe)
            self.prenom_cmp_aj.insert(prenom_employe)
