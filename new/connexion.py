__author__ = 'rihab'

from PyQt5 import QtSql

def connect():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName("localhost")
    db.setDatabaseName("pfaDB")
    db.setUserName("postgres")
    db.setPassword("root")
    ok = db.open()

    if ok:
        print("connected")
    else:
        print(db.lastError().text())