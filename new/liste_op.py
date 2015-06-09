__author__ = 'imen'
from ui_liste_op import Ui_Liste_Op

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtCore


class Liste_Operation(QWidget, Ui_Liste_Op):
    def __init__(self):
        super(Liste_Operation, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('operation')
        self.model.select()
        self.fill()
        self.initialiser_op.clicked.connect(self.initialise)
        self.recherche_op.clicked.connect(self.search)
        #self.ajouter_op.clicked.connect(self.add_interface)

    def fill(self):
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Code Operation")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Code Utilisateur")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Nom Operation")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Minutage")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Nom Machine")
        self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Critere de Qualite")
        self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Video")
        print(self.model.rowCount())
        self.tableView.setModel(self.model)

    def initialise(self):
        self.code_op_aj.clear()
        self.nom_op_aj.clear()
        self.minute_op_aj.clear()
        self.machine_op_aj.clear()
        self.Qcritere.clear()
        self.video_path.clear()

    def search(self):
        print("trying to do some research")
