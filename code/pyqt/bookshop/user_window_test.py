# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_window_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from pymysql import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication,QInputDialog, QLineEdit, QMainWindow, QWidget
import sys
from Insertbook import *
from Insertpurchase import *
from Insertsell import *
from Insertdel import *


class Ui_userWindow(object):
    def __init__(self):
        super().__init__()
        # self.InsertBook = InsertBook


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.book = QtWidgets.QWidget(self.centralwidget)
        self.book.setEnabled(True)
        self.book.setGeometry(QtCore.QRect(190, 40, 701, 411))
        self.book.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.book.setObjectName("book")

        self.label = QtWidgets.QLabel(self.book)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(270, 10, 91, 20))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.book)
        self.layoutWidget.setGeometry(QtCore.QRect(580, 20, 101, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_book = QtWidgets.QPushButton(self.layoutWidget)
        self.add_book.setObjectName("add_book")
        self.verticalLayout_2.addWidget(self.add_book)
        self.del_book = QtWidgets.QPushButton(self.layoutWidget)
        self.del_book.setObjectName("del_book")
        self.verticalLayout_2.addWidget(self.del_book)
        self.purchasebook = QtWidgets.QPushButton(self.layoutWidget)
        self.purchasebook.setObjectName("purchasebook")
        self.verticalLayout_2.addWidget(self.purchasebook)
        self.sellbook = QtWidgets.QPushButton(self.layoutWidget)
        self.sellbook.setObjectName("sellbook")
        self.verticalLayout_2.addWidget(self.sellbook)
        self.search_book = QtWidgets.QPushButton(self.layoutWidget)
        self.search_book.setObjectName("search_book")
        self.verticalLayout_2.addWidget(self.search_book)
        self.table_info = QtWidgets.QTableView(self.book)
        self.table_info.setGeometry(QtCore.QRect(30, 40, 521, 351))
        self.table_info.setObjectName("table_info")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 40, 111, 411))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.see_book_info = QtWidgets.QPushButton(self.layoutWidget1)
        self.see_book_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_book_info.setObjectName("see_book_info")
        self.verticalLayout.addWidget(self.see_book_info)
        self.see_reader_info = QtWidgets.QPushButton(self.layoutWidget1)
        self.see_reader_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_reader_info.setObjectName("see_reader_info")
        self.verticalLayout.addWidget(self.see_reader_info)
        self.see_borrow_info = QtWidgets.QPushButton(self.layoutWidget1)
        self.see_borrow_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.see_borrow_info.setObjectName("see_borrow_info")
        self.verticalLayout.addWidget(self.see_borrow_info)
        self.exit = QtWidgets.QPushButton(self.layoutWidget1)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 登录成功提示


        self.retranslateUi(MainWindow)
        self.exit.clicked.connect(MainWindow.close)
        self.see_book_info.clicked.connect(self.book.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.see_book_info.clicked.connect(lambda: self.get_book_info())



        """下面这段代码是用来弹出各种功能的pushbutton的界面，并绑定到对应的槽上面"""
        childwindow_addbook = child_addbok()
        childwindow_insertpurchase = child_purchase_book()
        childwindow_insertsell = child_sellbook()
        childwindow_insertdel = child_delbook()

        self.add_book.clicked.connect(lambda: childwindow_addbook.show())
        self.purchasebook.clicked.connect(lambda: childwindow_insertpurchase.show())
        self.sellbook.clicked.connect(lambda: childwindow_insertsell.show())
        self.del_book.clicked.connect(lambda: childwindow_insertdel.show())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "书籍信息查看"))
        self.add_book.setText(_translate("MainWindow", "添加书籍"))
        self.del_book.setText(_translate("MainWindow", "删除书籍"))
        self.purchasebook.setText(_translate("MainWindow", "购入书籍"))
        self.sellbook.setText(_translate("MainWindow", "卖出书籍"))
        self.search_book.setText(_translate("MainWindow", "搜索书籍"))
        self.see_book_info.setText(_translate("MainWindow", "查看书籍信息"))
        self.see_reader_info.setText(_translate("MainWindow", "查看读者信息"))
        self.see_borrow_info.setText(_translate("MainWindow", "查看借阅信息"))
        self.exit.setText(_translate("MainWindow", "退出"))
        self.statusbar.showMessage("用户登录成功", 2000)

    def get_book_info(self):
        self.db = connect(host='localhost', port=3306, charset='utf8', database='MySQL', password='zyh20000205',
                          user='root')
        print(123)
        # 创建游标对象
        self.cursor = self.db.cursor()
        sql = "use bookshopmanagement"
        self.cursor.execute(sql)
        self.model = QtSql.QSqlTableModel()
        self.table_info.setModel(self.model)
        sql = "SELECT * FROM book"
        self.cursor.execute(sql)
        # 获取查询到的数据, 是以二维元组的形式存储的, 所以读取需要使用 data[i][j] 下标定位
        data = self.cursor.fetchall()
        print(data)
        sql = " select ISBN,TotalNum from collectionofbook;"
        self.cursor.execute(sql)
        booknum_data = self.cursor.fetchall()
        print(booknum_data)
        print(54)
        # 打印测试
        row = len(data)
        col = len(data[0])
        flag = False
        currentLocation = 0
        MergedList = [[] for x in range(row)]
        for i in range(row):
            for j in range(len(booknum_data)):
                if booknum_data[j][0] == data[i][0]:
                    flag = True
                    currentLocation = j
                    break
            if flag is True:
                for x in range(col):
                    MergedList[i].append(data[i][x])
                MergedList[i].append(booknum_data[currentLocation][1])
            else:
                for x in range(col):
                    MergedList[i].append(data[i][x])
                MergedList[i].append(0)
            flag = False
        print(MergedList)


        model = QtGui.QStandardItemModel(row, len(MergedList[0]))
        # for i in range(row):
        #     for j in range(col+1):
        #         if j is not 3:
        #             model.setItem(i, j, QtGui.QStandardItem(data[i][j]))
        #         else:
        #             model.setItem(i, j, QtGui.QStandardItem(str(data[i][j])))
        #         print(data[i][j])

        for i in range(row):
            for j in range(len(MergedList[0])):
                if j is not 3 and j is not 4:
                    model.setItem(i, j, QtGui.QStandardItem(MergedList[i][j]))
                else:
                    model.setItem(i, j, QtGui.QStandardItem(str(MergedList[i][j])))

        model.setHorizontalHeaderLabels(['ISBN', "书名", "作者", "定价", "存货"])
        self.table_info.setModel(model)
        self.statusbar.showMessage("查询成功！总共查询到"+str(row)+"条数据", 2000)



class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.UI = Ui_userWindow()
        self.UI.setupUi(self)


class child_addbok(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_InputBookinfo()
        self.UI.setupUi(self)

class child_purchase_book(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_insertpurchase()
        self.UI.setupUi(self)


class child_sellbook(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_Insertsell()
        self.UI.setupUi(self)

class child_delbook(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.UI = Ui_delbook()
        self.UI.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = parentWindow()
    childwindow = child_addbok()
    window.UI.add_book.clicked.connect(lambda: childwindow.show())

    window.show()
    sys.exit(app.exec_())