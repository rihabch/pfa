__author__ = 'imen'


from ui_ajouter_emp import Ui_Add_Employee
import liste_employe
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QValidator
from PyQt5 import QtSql, QtCore, QtGui
from session import Session


class Ajouter_Employe(QWidget, Ui_Add_Employee):
    def __init__(self):
        super(Ajouter_Employe, self).__init__()
        self.setupUi(self)
        #session = Session()
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.model.select()
        self.annuler_emp.clicked.connect(self.toListe)
        self.initialiser_emp.clicked.connect(self.initialise)
        self.enregistrer_emp.clicked.connect(self.add)





    def add(self):
        matricule_employe = self.mat_aj_emp.text()
        int_expreg = QtCore.QRegExp('[0-9]+')
        int_validator = QtGui.QRegExpValidator(int_expreg,self.mat_aj_emp)
        self.mat_aj_emp.setValidator(int_validator)
        cin_employe = self.cin_aj_emp.text()
        cin_expreg = QtCore.QRegExp('[0-9]{8}')
        cin_validator = QtGui.QRegExpValidator(cin_expreg,self.cin_aj_emp)
        self.cin_aj_emp.setValidator(cin_validator)
        nom_employe = self.nom_aj_emp.text()
        prenom_employe = self.prenom_aj_emp.text()
        date_naissance = self.naiss_aj_emp.text()
        date_embauche = self.emb_aj_emp.text()
        if not (self.cin_aj_emp.hasAcceptableInput()):
            QMessageBox.information(self, "Erreur","CIN non valide")
        if not (self.mat_aj_emp.hasAcceptableInput):
            QMessageBox.information(self, "Erreur","Matricule non valide")
        # photo = self.photo_aj_emp.text()
        self.parcourir.clicked.connect(self.import_picture)
        if self.cin_aj_emp.hasAcceptableInput() and self.mat_aj_emp.hasAcceptableInput():
            nbr = self.model.rowCount()
            self.model.insertRow(nbr)
            self.model.setData(self.model.index(nbr - 1, 0), cin_employe)
            self.model.setData(self.model.index(nbr - 1, 1), matricule_employe)
            self.model.setData(self.model.index(nbr - 1, 2), 'admin_01')
            self.model.setData(self.model.index(nbr - 1, 3), nom_employe)
            self.model.setData(self.model.index(nbr - 1, 4), prenom_employe)
            self.model.setData(self.model.index(nbr - 1, 5), date_embauche)
            #self.model.setData(self.model.index(nbr - 1, 6),photo)
            self.model.setData(self.model.index(nbr - 1 , 7), 'P')
            self.model.setData(self.model.index(nbr - 1, 8), date_naissance)

            if self.model.submitAll():
                QMessageBox.information(self, "Succès", "Ajout avec Succès")
                print("ajout avec succes")
            else:
                QMessageBox.information(self, "Echec","Echec de l'ajout")


    def initialise(self):
        self.mat_aj_emp.clear()
        self.cin_aj_emp.clear()
        self.nom_aj_emp.clear()
        self.prenom_aj_emp.clear()
        self.naiss_aj_emp.setDateTime(QtCore.QDateTime.currentDateTime())
        self.emb_aj_emp.setDateTime(QtCore.QDateTime.currentDateTime())
        self.photo_aj_emp.clear()

    def import_picture(self):

        #QtGui.QFileDialog.getOpenFileName(None, "Boite d'ouverture de fichier")

        # QFileDialog.getOpenFileName(self, 'Open File')

         #fileName = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title', '/home/imen', selectedFilter='*.*')
         #if fileName:
          #  print (fileName)
        print("wselna lel import")
        fichier = QtGui.QfileDialog.getOpenFileName(self, "Ouvrir un fichier","/home","Images (*.png *.gif *.jpg *.jpeg)")
        print("en train d'ouvrir un fichier")
        if fichier:
            QmessageBox.information(self,"Fichier",self.trUtf8("Vous avez sélectionné :\n") + fichier)


    def toListe(self):
        self.list = liste_employe.Liste_Employe()
        self.list.show()
        self.close()