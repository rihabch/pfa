__author__ = 'rihab'

from PyQt5 import QtCore, QtGui, QtWidgets
from liste_employe import Liste_Employe
from PyQt5 import QtSql
import sys

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Liste_Employe()


    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName("localhost")
    db.setDatabaseName("pfaDB")
    db.setUserName("postgres")
    db.setPassword("root")
    ok = db.open()

    if ok:
        print("connecte")
    else:
        print(db.lastError().text())

    MainWindow = Liste_Employe()
    MainWindow.show()

    sys.exit(app.exec_())


def connect():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName("localhost")
    db.setPort(5433)
    db.setDatabaseName("pfaDB")
    db.setUserName("postgres")
    db.setPassword("root")
    ok = db.open()

    print(db.lastError().text())
    return db
