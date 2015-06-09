from ui_liste_emp import Ui_Employee_List
import ajouter_emp
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql, QtCore
from session import Session

class Liste_Employe(QWidget, Ui_Employee_List):
    def __init__(self):
        super(Liste_Employe, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.model.select()
        self.fill()
        self.initialiser_emp.clicked.connect(self.initialise)
        self.rechercher_emp.clicked.connect(self.search)
        self.ajouter_emp.clicked.connect(self.add_interface)
        session = Session()
        print("login admin: ")
        print(session.passe)


    def fill(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "CIN")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Matricule")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Code Utilisateur")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Nom")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Prenom")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Date Embauche")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Image")
        self.model.setHeaderData(7, QtCore.Qt.Horizontal, "Presence")
        self.model.setHeaderData(8, QtCore.Qt.Horizontal, "Date Naissance")
        print (self.model.rowCount())
        self.table_emp.setModel(self.model)

    def initialise(self):
        self.cin_emp.clear()
        self.mat_emp.clear()
        self.nom_emp.clear()
        self.prenom_emp.clear()
        #self.date_emb_emp.setDateTime(QtCore.QDateTime.currentDateTime())
        #self.date_nass_emp.setDateTime(QtCore.QDateTime.currentDateTime())

    def search(self):
        cin_employe = self.cin_emp.text()
        matricule_employe = self.mat_emp.text()
        nom_employe = self.nom_emp.text()
        prenom_employe = self.prenom_emp.text()
        #date_embauche = self.date_emb_emp.date().toString("yyyy-MM-dd")
        #date_naissance = self.date_nass_emp.date().toString("yyyy-MM-dd")
        print(cin_employe)
        print(matricule_employe)
        print(nom_employe)
        print(prenom_employe)
        #print(date_embauche)
        #print(date_naissance)
        critere =""
        if not len(cin_employe) == 0:
            critere += " cin_emp = %s" %(cin_employe)
        if not len(matricule_employe) == 0:
            critere += " and matricule = %s" %(matricule_employe)
        if not len(nom_employe) == 0:
            critere += " and nom = '%s'" %(nom_employe)
        if not len(prenom_employe) == 0:
            critere += " and prenom = '%s'" %(prenom_employe)
        #if not len(date_embauche) == 0:
        #    critere += " AND date_embauche = %s" %(date_embauche)
        #if not len(date_naissance) == 0:
        #    critere += " AND date_naissance = %s" %(date_naissance)
        print(critere)
        self.model.setFilter(critere)
        self.model.select()
        print(self.model.rowCount())
        if (self.model.rowCount()== 1):
            print('ok')
            self.fill()


    def edit(self):
        row = self.table_emp.currentRow()
        column = self.table_emp.currentColumn()
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.table_emp.itemAt(row, column)
        ID = item.text()
        print(ID)

    def add_interface(self):
        self.ajout = ajouter_emp.Ajouter_Employe()
        self.ajout.show()

    def delete_row(self):

        self.model.setEditStrategy(self.model.OnManualSubmit)
        self.model.select()
        #self.model
        #tv = QTableView(mw)
        #tv.setModel(model)
