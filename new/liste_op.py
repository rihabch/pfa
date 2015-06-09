__author__ = 'imen'
from ui_liste_op import Ui_Liste_Op


from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtCore

class Liste_Op(QWidget, Ui_Liste_Op()):
    def __init__(self):
        super(Liste_Op, self).__init__()
        self.setupUi(self)