# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ajouter_op.ui'
#
# Created: Tue Jun  9 17:34:13 2015
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ajouter_Op(object):
    def setupUi(self, Form):
        Form.setObjectName("Ajouter des Opérations")
        Form.resize(785, 515)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(210, 340, 311, 31))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ajouter_op_aj = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.ajouter_op_aj.setObjectName("ajouter_op_aj")
        self.horizontalLayout_8.addWidget(self.ajouter_op_aj)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.annuler_op_aj = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.annuler_op_aj.setObjectName("annuler_op_aj")
        self.horizontalLayout_8.addWidget(self.annuler_op_aj)
        self.namepage_ajout_op = QtWidgets.QLabel(Form)
        self.namepage_ajout_op.setGeometry(QtCore.QRect(275, 30, 450, 40))
        self.namepage_ajout_op.setObjectName("namepage_ajout_op")
        self.formLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(190, 90, 371, 211))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelcode_op_aj = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelcode_op_aj.setObjectName("labelcode_op_aj")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelcode_op_aj)
        self.code_op_aj = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.code_op_aj.setObjectName("code_op_aj")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.code_op_aj)
        self.labelnom_op_aj = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelnom_op_aj.setObjectName("labelnom_op_aj")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelnom_op_aj)
        self.nom_op_aj = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.nom_op_aj.setObjectName("nom_op_aj")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nom_op_aj)
        self.labelminutage_op_aj = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelminutage_op_aj.setObjectName("labelminutage_op_aj")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelminutage_op_aj)
        self.minute_op_aj = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.minute_op_aj.setObjectName("minute_op_aj")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.minute_op_aj)
        self.labelmachine_op_aj = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.labelmachine_op_aj.setObjectName("labelmachine_op_aj")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelmachine_op_aj)
        self.machine_op_aj = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.machine_op_aj.setObjectName("machine_op_aj")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.machine_op_aj)
        #self.critere_op_aj = QtWidgets.QLabel(self.formLayoutWidget_2)
        #self.critere_op_aj.setObjectName("critere_op_aj")
        #self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.critere_op_aj)
        #self.Qcritere = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        #self.Qcritere.setObjectName("Qcritere")
        #self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Qcritere)
        #self.video_op_aj = QtWidgets.QLabel(self.formLayoutWidget_2)
        #self.video_op_aj.setObjectName("video_op_aj")
        #self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.video_op_aj)
        #self.horizontalLayout = QtWidgets.QHBoxLayout()
        #self.horizontalLayout.setObjectName("horizontalLayout")
        #self.video_path = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        #self.video_path.setObjectName("video_path")
        #self.horizontalLayout.addWidget(self.video_path)
        #self.toolButton = QtWidgets.QToolButton(self.formLayoutWidget_2)
        #self.toolButton.setObjectName("toolButton")
        #self.horizontalLayout.addWidget(self.toolButton)
        #self.formLayout_2.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        #self.initialiser_op = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        #self.initialiser_op.setObjectName("initialiser_op")
        #self.horizontalLayout_8.addWidget(self.initialiser_op)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Ajouter des Operations", "Ajouter des Opérations"))
        self.ajouter_op_aj.setText(_translate("Form", "Enregistrer"))
        self.annuler_op_aj.setText(_translate("Form", "Annuler"))
        #self.initialiser_op.setText(_translate("Form", "Initialiser"))
        self.namepage_ajout_op.setText(_translate("Form", "<html><head/><body><h1><span style=\" color:#55aaff;\">Ajouter des Opérations</span></h1></body></html>"))
        self.labelcode_op_aj.setText(_translate("Form", "Code Opération:"))
        self.labelnom_op_aj.setText(_translate("Form", "Nom Opération:"))
        self.labelminutage_op_aj.setText(_translate("Form", "Minutage:"))
        self.labelmachine_op_aj.setText(_translate("Form", "Machine:"))
        #self.critere_op_aj.setText(_translate("Form", "Critère de Qualité:"))
        #self.video_op_aj.setText(_translate("Form", "Vidéo:"))
        #self.toolButton.setText(_translate("Form", "..."))

