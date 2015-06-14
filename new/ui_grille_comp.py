# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_grille_comp.ui'
#
# Created: Fri Jun 12 07:55:12 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Grille(object):
    def setupUi(self, Form):
        Form.setObjectName("Grille de Compétences")
        Form.resize(799, 594)
        self.grille = QtWidgets.QTableWidget(Form)
        self.grille.setGeometry(QtCore.QRect(30, 30, 741, 531))
        self.grille.setObjectName("grille")
        self.grille.setColumnCount(0)
        self.grille.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Grille de Compétences", "Grille de Compétences"))

