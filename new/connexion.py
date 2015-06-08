__author__ = 'rihab'

from PyQt5 import QtSql

def connect():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName("localhost")
    db.setDatabaseName("pfa")
    db.setUserName("imen")
    db.setPassword("imen")
    ok = db.open()

    if ok:
        print("connected")
    else:
        print(db.lastError().text())