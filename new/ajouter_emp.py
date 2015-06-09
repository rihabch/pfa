
__author__ = 'imen'
from ui_ajouter_emp import Ui_Add_Employee
from liste_employe import Liste_Employe
from PyQt5.QtWidgets import QWidget, QMessageBox
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
        self.initialiser_emp.clicked.connect(self.initialise)



    def add(self):
        matricule_employe = self.mat_aj_emp.text()
        cin_employe = self.cin_aj_emp.text()
        nom_employe = self.nom_aj_emp.text()
        prenom_employe = self.prenom_aj_emp.text()
        date_naissance = self.naiss_aj_emp.text()
        date_embauche = self.emb_aj_emp.text()
        #photo = self.photo_aj_emp.text()
        self.parcourir.clicked.connect(self.import_picture)
        nbr = self.model.rowCount()
        self.model.insertRow(nbr)
        self.model.setData(self.model.index(nbr - 1, 0), cin_employe)
        self.model.setData(self.model.index(nbr - 1, 1), matricule_employe)
        self.model.setData(self.model.index(nbr - 1, 2), 1)
        self.model.setData(self.model.index(nbr - 1, 3), nom_employe)
        self.model.setData(self.model.index(nbr - 1, 4), prenom_employe)
        self.model.setData(self.model.index(nbr - 1, 5), date_embauche)
        # self.model.setData(self.model.index(nbr - 1, 6),str(dir + "" + photo))
        self.model.setData(self.model.index(nbr - 1, 8), date_naissance)
        if self.model.submitAll():
           QMessageBox.information(self, "Success","Add Successful" )

        else:
            self.db = QtSql.QSqlDatabase.database()
            print(self.db.lastError().databaseText())


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

        # fileName = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title', '/home/imen', selectedFilter='*.*')
        # if fileName:
         #   print (fileName)

        filename, filter = QtGui.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir=os.getenv("HOME"))
        print( 'filename:', filename)
        print ('filter:', filter)