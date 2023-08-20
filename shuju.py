import deeplab
from web import *
from Table import *
import cv2
import numpy as np
import pyqtgraph as pg
import paragraph
import deeplab
import predict
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import glo
import sqlite3
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery

database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
database.setDatabaseName('mysql.db')
database.open()

query = QSqlQuery()  #######
query.prepare('create table shuju (xiangsu varchar(30),zhanbi varchar(30))')
if not query.exec_():
    query.lastError()
else:
    print('create a table')
A=[1,2,3,3,45,5,6,7]
B=[3,8,45,5,67,8,7,4]
for i in range(len(A)):
            insert_sql = 'insert into shuju values (?,?)'
            query.prepare(insert_sql)
            query.addBindValue(A[i])
            query.addBindValue(B[i])
            query.execBatch()
            if not query.exec_():
                print(query.lastError())
            else:
                print('inserted')