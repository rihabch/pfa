__author__ = 'imen'

from ui_ajouter_emp import Ui_Add_Employee
import liste_employe
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql, QtCore, QtGui
from datetime import date, datetime
from session import Session


class Ajouter_Employe(QWidget, Ui_Add_Employee):
    def __init__(self):
        super(Ajouter_Employe, self).__init__()
        self.setupUi(self)
        # session = Session()
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.model.select()
        self.annuler_emp.clicked.connect(self.toListe)
        #self.initialiser_emp.clicked.connect(self.initialise)
        self.enregistrer_emp.clicked.connect(self.add)

    def add(self):
        matricule_employe = self.mat_aj_emp.text()

        int_expreg = QtCore.QRegExp('[0-9]+')
        int_validator = QtGui.QRegExpValidator(int_expreg, self.mat_aj_emp)
        self.mat_aj_emp.setValidator(int_validator)

        cin_employe = self.cin_aj_emp.text()
        cin_expreg = QtCore.QRegExp('[0-9]{8}')
        cin_validator = QtGui.QRegExpValidator(cin_expreg, self.cin_aj_emp)
        self.cin_aj_emp.setValidator(cin_validator)
        nom_employe = self.nom_aj_emp.text()
        prenom_employe = self.prenom_aj_emp.text()
        date_naissance = self.naiss_aj_emp.text()
        date_embauche = self.emb_aj_emp.text()
        if (date_naissance > date_embauche):
            ok = False
            QMessageBox.information(self, "Erreur", "Dates non valides")
        else:
            ok = True
        if not (self.mat_aj_emp.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur", "Matricule non valide")
        if not (self.cin_aj_emp.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur", "CIN non valide")
        if (self.cin_aj_emp.hasAcceptableInput()) and (self.mat_aj_emp.hasAcceptableInput()) and ok:
            nbr = self.model.rowCount()
            print("nombre lignes")
            print(nbr)
            self.model.insertRow(nbr)
            self.model.setData(self.model.index(nbr, 1), matricule_employe)
            self.model.setData(self.model.index(nbr, 0), cin_employe)
            self.model.setData(self.model.index(nbr, 4), prenom_employe)
            self.model.setData(self.model.index(nbr, 3), nom_employe)
            self.model.setData(self.model.index(nbr, 7), "P")
            self.model.setData(self.model.index(nbr, 5), date_embauche)
            self.model.setData(self.model.index(nbr, 8), date_naissance)
            # self.model.setData(self.model.index(nbr - 1, 6),str(dir + "" + photo))
            self.model.setData(self.model.index(nbr, 2), 'admin_02')






            count = self.model.rowCount()
            print(count)
            if (count == nbr + 1):
                self.model.submitAll()
                QMessageBox.information(self, "Succes", "Ajout avec Succes")
                self.initialise()

    def initialise(self):
        self.mat_aj_emp.clear()
        self.cin_aj_emp.clear()
        self.nom_aj_emp.clear()
        self.prenom_aj_emp.clear()
        #self.naiss_aj_emp.setDate(datetime.datetime.strptime('01/01/2000',"%d/%m/%Y").date())
        #self.emb_aj_emp.setDate(datetime.datetime.strptime('01/01/2000',"%d/%m/%Y").date())
        #self.photo_aj_emp.clear()

    def import_picture(self):

        fileName = QWidget.QFileDialog.getSaveFileName(self, 'Dialog Title', '/home/imen', selectedFilter='*.*')
        if fileName:
            print(fileName)
            QMessageBox.information(self, "Fichier", self.trUtf8("Vous avez sélectionné :\n") + fileName)

    def toListe(self):
        self.list = liste_employe.Liste_Employe()
        self.list.show()
        self.close()
