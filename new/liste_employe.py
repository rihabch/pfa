from ui_liste_emp import Ui_Employee_List
from ajouter_emp import Ajouter_Employe
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtCore

class Liste_Employe(QWidget, Ui_Employee_List):
    def __init__(self):
        super(Liste_Employe, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('employe')
        self.fill()
        self.initialiser_emp.clicked.connect(self.initialise)
        self.rechercher_emp.clicked.connect(self.search)
        self.ajouter_emp.clicked.connect(self.add_interface)
        #self.table_emp.itemChanged.connect(self.edit)

    def fill(self):
        self.model.select()
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
        self.date_emb_emp.setDateTime(QtCore.QDateTime.currentDateTime())
        self.date_nass_emp.setDateTime(QtCore.QDateTime.currentDateTime())

    def search(self):
        cin_employe = self.cin_emp.text()
        matricule_employe = self.mat_emp.text()
        nom_employe = self.nom_emp.text()
        prenom_employe = self.prenom_emp.text()
        date_embauche = self.date_emb_emp.date().toString("yyyy-MM-dd")
        date_naissance = self.date_nass_emp.date().toString("yyyy-MM-dd")
        print(cin_employe)
        print(matricule_employe)
        print(nom_employe)
        print(prenom_employe)
        print(date_embauche)
        print(date_naissance)
        query = QtSql.QSqlQuery()
        query.exec("select * from employe where matricule = "+matricule_employe)
        while query.next():
            print("query value", query.value(0))


    def edit(self):
        row = self.table_emp.currentRow()
        column = self.table_emp.currentColumn()
        print("Row %d and Column %d was clicked" % (row, column))
        item = self.table_emp.itemAt(row, column)
        ID = item.text()
        print(ID)

    def add_interface(self):
        self.ajout = Ajouter_Employe()
        self.ajout.show()
