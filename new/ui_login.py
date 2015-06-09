# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_login.ui'
#
# Created: Tue Jun  9 01:12:17 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Login")
        Form.resize(400, 300)
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(190, 70, 113, 27))
        self.user.setObjectName("user")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(190, 110, 113, 27))
        self.password.setObjectName("password")
       # self.password.setEchoMode(Password)
        self.codelabel = QtWidgets.QLabel(Form)
        self.codelabel.setGeometry(QtCore.QRect(60, 70, 66, 17))
        self.codelabel.setObjectName("codelabel")
        self.passwordlabel = QtWidgets.QLabel(Form)
        self.passwordlabel.setGeometry(QtCore.QRect(55, 110, 101, 20))
        self.passwordlabel.setObjectName("passwordlabel")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 141, 17))
        self.label_3.setObjectName("label_3")
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(140, 180, 98, 27))
        self.login.setObjectName("login")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Login", "Login"))
        self.codelabel.setText(_translate("Form", "Code"))
        self.passwordlabel.setText(_translate("Form", "Mot de Passe"))
        self.label_3.setText(_translate("Form", "Page Connexion"))
        self.login.setText(_translate("Form", "Login"))

