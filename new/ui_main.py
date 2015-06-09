# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created: Tue Jun  9 18:14:38 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 582)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 25))
        self.menubar.setObjectName("menubar")
        self.menuGestion_Employes = QtWidgets.QMenu(self.menubar)
        self.menuGestion_Employes.setObjectName("menuGestion_Employes")
        self.menuGestion_Operations = QtWidgets.QMenu(self.menubar)
        self.menuGestion_Operations.setObjectName("menuGestion_Operations")
        self.menu_quilibrage = QtWidgets.QMenu(self.menubar)
        self.menu_quilibrage.setObjectName("menu_quilibrage")
        self.menuStatistiqus = QtWidgets.QMenu(self.menubar)
        self.menuStatistiqus.setObjectName("menuStatistiqus")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Liste_Employes = QtWidgets.QAction(MainWindow)
        self.Liste_Employes.setIconVisibleInMenu(False)
        self.Liste_Employes.setObjectName("Liste_Employes")
        self.Competences = QtWidgets.QAction(MainWindow)
        self.Competences.setObjectName("Competences")
        self.Details_Gamme = QtWidgets.QAction(MainWindow)
        self.Details_Gamme.setObjectName("Details_Gamme")
        self.Details_Operation = QtWidgets.QAction(MainWindow)
        self.Details_Operation.setObjectName("Details_Operation")
        self.Creer_equilibrage = QtWidgets.QAction(MainWindow)
        self.Creer_equilibrage.setObjectName("Creer_equilibrage")
        self.Liste_equilibrage = QtWidgets.QAction(MainWindow)
        self.Liste_equilibrage.setObjectName("Liste_equilibrage")
        self.menuGestion_Employes.addAction(self.Liste_Employes)
        self.menuGestion_Employes.addAction(self.Competences)
        self.menuGestion_Operations.addAction(self.Details_Gamme)
        self.menuGestion_Operations.addAction(self.Details_Operation)
        self.menu_quilibrage.addAction(self.Creer_equilibrage)
        self.menu_quilibrage.addAction(self.Liste_equilibrage)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuGestion_Employes.menuAction())
        self.menubar.addAction(self.menuGestion_Operations.menuAction())
        self.menubar.addAction(self.menu_quilibrage.menuAction())
        self.menubar.addAction(self.menuStatistiqus.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuGestion_Employes.setTitle(_translate("MainWindow", "Gestion Employés"))
        self.menuGestion_Operations.setTitle(_translate("MainWindow", "Gestion Opérations"))
        self.menu_quilibrage.setTitle(_translate("MainWindow", "Équilibrage"))
        self.menuStatistiqus.setTitle(_translate("MainWindow", "Consulter Statistiques"))
        self.menuHome.setTitle(_translate("MainWindow", "Accueil"))
        self.Liste_Employes.setText(_translate("MainWindow", "Liste Employés"))
        self.Competences.setText(_translate("MainWindow", "Compétences"))
        self.Details_Gamme.setText(_translate("MainWindow", "Détails Gamme"))
        self.Details_Operation.setText(_translate("MainWindow", "Détails Opération"))
        self.Creer_equilibrage.setText(_translate("MainWindow", "Créer Équilibrage"))
        self.Liste_equilibrage.setText(_translate("MainWindow", "Liste Équilibrage"))

