# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_liste_emp.ui'
#
# Created: Tue May 26 23:13:58 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Employee_List(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Liste des Employés")
        MainWindow.resize(750, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(60, 479, 661, 31))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ajouter_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_13)
        self.ajouter_emp.setObjectName("ajouter_emp")
        self.horizontalLayout_10.addWidget(self.ajouter_emp)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.importer_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_13)
        self.importer_emp.setObjectName("importer_emp")
        self.horizontalLayout_10.addWidget(self.importer_emp)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.Modifier_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_13)
        self.Modifier_emp.setObjectName("Modifier_emp")
        self.horizontalLayout_10.addWidget(self.Modifier_emp)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.supprimer_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_13)
        self.supprimer_emp.setObjectName("supprimer_emp")
        self.horizontalLayout_10.addWidget(self.supprimer_emp)
        self.horizontalLayoutWidget_17 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(490, 170, 201, 31))
        self.horizontalLayoutWidget_17.setObjectName("horizontalLayoutWidget_17")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.rechercher_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_17)
        self.rechercher_emp.setObjectName("rechercher_emp")
        self.horizontalLayout_14.addWidget(self.rechercher_emp)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.initialiser_emp = QtWidgets.QPushButton(self.horizontalLayoutWidget_17)
        self.initialiser_emp.setObjectName("initialiser_emp")
        self.horizontalLayout_14.addWidget(self.initialiser_emp)
        self.labelrecherche_emp = QtWidgets.QLabel(self.centralWidget)
        self.labelrecherche_emp.setGeometry(QtCore.QRect(30, 40, 111, 17))
        self.labelrecherche_emp.setObjectName("labelrecherche_emp")
        self.table_emp = QtWidgets.QTableView(self.centralWidget)
        self.table_emp.setGeometry(QtCore.QRect(60, 240, 611, 192))
        self.table_emp.setObjectName("table_emp")
        self.namepage_emp = QtWidgets.QLabel(self.centralWidget)
        self.namepage_emp.setGeometry(QtCore.QRect(275, 10, 450, 30))
        self.namepage_emp.setObjectName("namepage_emp")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 70, 621, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelnaissance_emp = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelnaissance_emp.setObjectName("labelnaissance_emp")
        self.gridLayout_2.addWidget(self.labelnaissance_emp, 0, 4, 1, 1)
        self.labelmatricul_emp = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelmatricul_emp.setObjectName("labelmatricul_emp")
        self.gridLayout_2.addWidget(self.labelmatricul_emp, 0, 2, 1, 1)
        self.labelprenom_emp = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelprenom_emp.setObjectName("labelprenom_emp")
        self.gridLayout_2.addWidget(self.labelprenom_emp, 1, 2, 1, 1)
        self.mat_emp = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.mat_emp.setObjectName("mat_emp")
        self.gridLayout_2.addWidget(self.mat_emp, 0, 3, 1, 1)
        self.labelcin_emp = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelcin_emp.setObjectName("labelcin_emp")
        self.gridLayout_2.addWidget(self.labelcin_emp, 0, 0, 1, 1)
        self.labelembauche_emp = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelembauche_emp.setObjectName("labelembauche_emp")
        self.gridLayout_2.addWidget(self.labelembauche_emp, 1, 4, 1, 1)
        self.cin_emp = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.cin_emp.setObjectName("cin_emp")
        self.gridLayout_2.addWidget(self.cin_emp, 0, 1, 1, 1)
        self.prenom_emp = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.prenom_emp.setObjectName("prenom_emp")
        self.gridLayout_2.addWidget(self.prenom_emp, 1, 3, 1, 1)
        self.labelnom_emp = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelnom_emp.setObjectName("labelnom_emp")
        self.gridLayout_2.addWidget(self.labelnom_emp, 1, 0, 1, 1)
        self.nom_emp = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.nom_emp.setObjectName("nom_emp")
        self.gridLayout_2.addWidget(self.nom_emp, 1, 1, 1, 1)
        #self.date_nass_emp = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        #self.date_nass_emp.setObjectName("date_nass_emp")
        #self.gridLayout_2.addWidget(self.date_nass_emp, 0, 5, 1, 1)
        #self.date_emb_emp = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        #self.date_emb_emp.setObjectName("date_emb_emp")
        #self.gridLayout_2.addWidget(self.date_emb_emp, 1, 5, 1, 1)
        #self.date_emb_emp.setDateTime(QtCore.QDateTime.currentDateTime())
        #self.date_nass_emp.setDateTime(QtCore.QDateTime.currentDateTime())



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Liste Employes", "Liste des Employés"))
        self.ajouter_emp.setText(_translate("MainWindow", "Ajouter"))
        self.importer_emp.setText(_translate("MainWindow", "Importer"))
        self.Modifier_emp.setText(_translate("MainWindow", "Modifier"))
        self.supprimer_emp.setText(_translate("MainWindow", "Supprimer"))
        self.rechercher_emp.setText(_translate("MainWindow", "Rechercher"))
        self.initialiser_emp.setText(_translate("MainWindow", "Initialiser"))
        self.labelrecherche_emp.setText(_translate("MainWindow", "Rechercher par:"))
        self.namepage_emp.setText(_translate("MainWindow", "<html><head/><body><h1><span style=\" color:#55aaff;\">Liste des Employés</span></h1></body></html>"))
        #self.labelnaissance_emp.setText(_translate("MainWindow", "Date Naissance:"))
        self.labelmatricul_emp.setText(_translate("MainWindow", "Matricule:"))
        self.labelprenom_emp.setText(_translate("MainWindow", "Prénom :"))
        self.labelcin_emp.setText(_translate("MainWindow", "CIN :"))
        #self.labelembauche_emp.setText(_translate("MainWindow", "Date Embauche:"))
        self.labelnom_emp.setText(_translate("MainWindow", "Nom :"))

