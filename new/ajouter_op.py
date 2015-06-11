__author__ = 'imen'
from ui_ajouter_op import Ui_Ajouter_Op
import liste_op
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5 import QtSql
import connexion

class Ajouter_Operation(QWidget, Ui_Ajouter_Op):
    def __init__(self):
        super(Ajouter_Operation, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('operation')
        self.model.select()
        self.annuler_op_aj.clicked.connect(self.toListe)
        self.ajouter_op_aj.clicked.connect(self.add)
        #self.initialiser_op.clicked.connect(self.initialise)

    def initialise(self):
        self.code_op_aj.clear()
        self.nom_op_aj.clear()
        self.minute_op_aj.clear()
        self.machine_op_aj.clear()
        self.Qcritere.clear()
        self.video_path.clear()

    def add(self):
        code_op = self.code_op_aj.text()
        nom_op = self.nom_op_aj.text()
        minutage = self.minute_op_aj.text()
        machine = self.machine_op_aj.text()
        critere = self.Qcritere.text()
        video = self.video_path.text()
        # self.parcourir.clicked.connect(self.import_video)

        nbr = self.model.rowCount()
        print("nombre lignes")
        print(nbr)
        self.model.insertRow(nbr)
        self.model.setData(self.model.index(nbr, 0), code_op)
        self.model.setData(self.model.index(nbr, 1), "admin_02")
        self.model.setData(self.model.index(nbr, 2), nom_op)
        self.model.setData(self.model.index(nbr, 3), minutage)
        self.model.setData(self.model.index(nbr, 4), machine)
        self.model.setData(self.model.index(nbr, 5), critere)
        self.model.setData(self.model.index(nbr, 6), video)
        count = self.model.rowCount()
        print(count)
        if (count == nbr+1):
            self.model.submitAll()
            QMessageBox.information(self, "Success","Add Successful" )
            self.initialise()

        else:
            print(connexion.db.lastError().databaseText())


    def toListe(self):
        self.list = liste_op.Liste_Operation()
        self.list.show()
        self.close()
