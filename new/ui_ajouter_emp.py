# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ajouter_emp.ui'
#
# Created: Wed May 27 09:04:03 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_Employee(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ajouter Employe")
        MainWindow.resize(736, 525)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 60, 401, 252))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_mat_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_mat_aj_emp.setObjectName("label_mat_aj_emp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_mat_aj_emp)
        self.mat_aj_emp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mat_aj_emp.setObjectName("mat_aj_emp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mat_aj_emp)
        self.label_cin_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_cin_aj_emp.setObjectName("label_cin_aj_emp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_cin_aj_emp)
        self.cin_aj_emp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cin_aj_emp.setObjectName("cin_aj_emp")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cin_aj_emp)
        self.label_nom_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_nom_aj_emp.setObjectName("label_nom_aj_emp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_nom_aj_emp)
        self.nom_aj_emp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nom_aj_emp.setObjectName("nom_aj_emp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nom_aj_emp)
        self.label_prenom_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_prenom_aj_emp.setObjectName("label_prenom_aj_emp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_prenom_aj_emp)
        self.prenom_aj_emp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.prenom_aj_emp.setObjectName("prenom_aj_emp")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prenom_aj_emp)
        self.naiss_aj_emp = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.naiss_aj_emp.setObjectName("naiss_aj_emp")
        self.naiss_aj_emp.setCalendarPopup(True)

        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.naiss_aj_emp)
        self.label_emb_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_emb_aj_emp.setObjectName("label_emb_aj_emp")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_emb_aj_emp)
        self.emb_aj_emp = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.emb_aj_emp.setObjectName("emb_aj_emp")
        self.emb_aj_emp.setCalendarPopup(True)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.emb_aj_emp)
        #self.label_photo_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        #self.label_photo_aj_emp.setObjectName("label_photo_aj_emp")
        #self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_photo_aj_emp)
        #self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        #self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #self.photo_aj_emp = QtWidgets.QLineEdit(self.formLayoutWidget)
        #self.photo_aj_emp.setObjectName("photo_aj_emp")
        #self.horizontalLayout_2.addWidget(self.photo_aj_emp)
        #self.parcourir = QtWidgets.QToolButton(self.formLayoutWidget)
        #self.parcourir.setObjectName("parcourir")
        #self.horizontalLayout_2.addWidget(self.parcourir)
        #self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_naiss_aj_emp = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_naiss_aj_emp.setObjectName("label_naiss_aj_emp")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_naiss_aj_emp)
        self.namepage_aj_emp = QtWidgets.QLabel(self.centralWidget)
        self.namepage_aj_emp.setGeometry(QtCore.QRect(200, 10, 300, 30))
        self.namepage_aj_emp.setObjectName("namepage_aj_emp")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(80, 400, 401, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.enregistrer_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.enregistrer_emp.setObjectName("enregistrer_emp")
        self.horizontalLayout_6.addWidget(self.enregistrer_emp)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)

        self.annuler_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.annuler_emp.setObjectName("annuler_emp")
        self.horizontalLayout_6.addWidget(self.annuler_emp)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)

        self.initialiser_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.initialiser_emp.setObjectName("initialiser_emp")
        self.horizontalLayout_6.addWidget(self.initialiser_emp)

        today = QtCore.QDate.currentDate()
        self.naiss_aj_emp.setDate(today)
        self.emb_aj_emp.setDate(today)

        locale = QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France)
        self.naiss_aj_emp.calendarWidget().setLocale(locale)
        self.emb_aj_emp.calendarWidget().setLocale(locale)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ajouter Employe", "Ajouter des Employés"))
        self.label_mat_aj_emp.setText(_translate("MainWindow", "Matricule :"))
        self.label_cin_aj_emp.setText(_translate("MainWindow", "CIN :"))
        self.label_nom_aj_emp.setText(_translate("MainWindow", "Nom :"))
        self.label_prenom_aj_emp.setText(_translate("MainWindow", "Prénom :"))
        self.label_emb_aj_emp.setText(_translate("MainWindow", "Date Embauche :"))
        #self.label_photo_aj_emp.setText(_translate("MainWindow", "Photo :"))
        #self.parcourir.setText(_translate("MainWindow", "..."))
        self.label_naiss_aj_emp.setText(_translate("MainWindow", "Date Naissance :"))
        self.namepage_aj_emp.setText(_translate("MainWindow", "<html><head/><body><h1><span style=\" color:#55aaff;\">Ajouter des Employés</span></h1></body></html>"))
        self.enregistrer_emp.setText(_translate("MainWindow", "Enregistrer"))
        self.annuler_emp.setText(_translate("MainWindow", "Annuler"))
        self.initialiser_emp.setText(_translate("MainWindow", "Initialiser"))


