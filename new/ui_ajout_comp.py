# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ajout_comp.ui'
#
# Created: Wed Jun 10 08:09:21 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ajout_Competence(object):
    def setupUi(self, Form):
        Form.setObjectName("Ajouter Competence")
        Form.resize(781, 480)
        self.formLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(200, 160, 351, 217))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.labelmat_cmp_aj = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelmat_cmp_aj.setObjectName("labelmat_cmp_aj")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelmat_cmp_aj)
        self.mat_cmp_aj = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.mat_cmp_aj.setObjectName("mat_cmp_aj")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mat_cmp_aj)
        """self.labelnom_cmp_aj = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelnom_cmp_aj.setObjectName("labelnom_cmp_aj")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelnom_cmp_aj)
        self.nom_cmp_aj = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.nom_cmp_aj.setObjectName("nom_cmp_aj")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nom_cmp_aj)
        self.labelprenom_cmp_aj = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelprenom_cmp_aj.setObjectName("labelprenom_cmp_aj")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelprenom_cmp_aj)
        self.prenom_cmp_aj = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.prenom_cmp_aj.setObjectName("prenom_cmp_aj")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.prenom_cmp_aj)"""
        self.op_cmp_aj = QtWidgets.QComboBox(self.formLayoutWidget_4)
        self.op_cmp_aj.setObjectName("op_cmp_aj")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.op_cmp_aj)
        self.labelallure_cmp_aj = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelallure_cmp_aj.setObjectName("labelallure_cmp_aj")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelallure_cmp_aj)
        self.allure_cmp_aj = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.allure_cmp_aj.setObjectName("allure_cmp_aj")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.allure_cmp_aj)
        self.labelretouche_cmp_aj = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelretouche_cmp_aj.setObjectName("labelretouche_cmp_aj")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelretouche_cmp_aj)
        self.retouche_cmp_aj = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.retouche_cmp_aj.setObjectName("retouche_cmp_aj")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.retouche_cmp_aj)
        self.labelcode_cmp_aj = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.labelcode_cmp_aj.setObjectName("labelcode_cmp_aj")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelcode_cmp_aj)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(200, 400, 351, 41))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.enregistrer_cmp = QtWidgets.QPushButton(self.horizontalLayoutWidget_12)
        self.enregistrer_cmp.setObjectName("enregistrer_cmp")
        self.horizontalLayout_9.addWidget(self.enregistrer_cmp)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        #self.initialiser_aj_cmp = QtWidgets.QPushButton(self.horizontalLayoutWidget_12)
        #self.initialiser_aj_cmp.setObjectName("initialiser_aj_cmp")
        #self.horizontalLayout_9.addWidget(self.initialiser_aj_cmp)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.annuler_cmp = QtWidgets.QPushButton(self.horizontalLayoutWidget_12)
        self.annuler_cmp.setObjectName("annuler_cmp")
        self.horizontalLayout_9.addWidget(self.annuler_cmp)
        self.name_page_comp_aj = QtWidgets.QLabel(Form)
        self.name_page_comp_aj.setGeometry(QtCore.QRect(230, 50, 350, 30))
        self.name_page_comp_aj.setObjectName("name_page_comp_aj")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Ajouter Competence", "Ajouter des Compétences"))
        self.labelmat_cmp_aj.setText(_translate("Form", "Matricule:"))
        #self.labelnom_cmp_aj.setText(_translate("Form", "Nom :"))
        #elf.labelprenom_cmp_aj.setText(_translate("Form", "Prénom : "))
        self.labelallure_cmp_aj.setText(_translate("Form", "Allure :"))
        self.labelretouche_cmp_aj.setText(_translate("Form", "Taux de Retouche :"))
        self.labelcode_cmp_aj.setText(_translate("Form", "Code Opération :"))
        self.enregistrer_cmp.setText(_translate("Form", "Enregistrer"))
        #self.initialiser_aj_cmp.setText(_translate("Form", "Initialiser"))
        self.annuler_cmp.setText(_translate("Form", "Annuler"))
        self.name_page_comp_aj.setText(_translate("Form", "<html><head/><body><h1><span style=\" color:#55aaff;\">Ajouter des Compétences</span></h1></body></html>"))

