__author__ = 'rihab'
from ui_login import Ui_Login
from liste_employe import Liste_Employe
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql, QtGui
from session import Session

class Login(QWidget, Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.model = QtSql.QSqlRelationalTableModel()
        self.model.setTable('utilisateur')
        self.login.clicked.connect(self.submit)
        #self.msgBox= QtGui.QMessageBox.warning(self, 'Error Connection', 'Bad user or password')
    def submit(self):
        user_code = self.user.text()
        passwd = self.password.text()
        critere =""
        if not len(user_code) == 0:
            critere += " code_util = %s" %(user_code)
        if not len(passwd) == 0:
            critere += " AND mot_de_passe = '%s'" %(passwd)
        print(critere)
        self.model.setFilter(critere)
        self.model.select()

        if (self.model.rowCount()== 1):
            print('ok')
            self.Main = Liste_Employe()
            self.Main.show()
            self.close()
            session = Session(user_code,passwd)
            print("login: ")
            print(session.passe)

        else:
            print("not ok")
            self.user.clear()
            self.password.clear()
            #msgBox = QtGui.QMessageBox()
            #print("connexion échouée")

            #ret = self.msgBox.exec_()