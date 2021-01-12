# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuzeren_luru.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import xlrd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC

def open_excel():
       
        try:
            book = xlrd.open_workbook(r'fuzeren_luru.xlsx')  #文件名，把文件与py文件放在同一目录下
            print("open excel file!")
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name('Sheet1')   #execl里面的worksheet1
            return sheet
        except:
            print("locate worksheet in excel failed!")

class Ui_MainWindow7_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 59, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(24, 59, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(26, 100, 171, 24))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(14, -1, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")\

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(300, 140, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(24, 140, 200, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")

        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(216, 100, 171, 24))
        self.lineEdit2.setObjectName("lineEdit2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handle_luru(self):
        if( self.lineEdit1.text() == '' or \
                self.lineEdit2.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        else:
            a = fuzeren_query_allname()
            allid = []
            for i in a:
                allid.append(i[0])
            if (self.lineEdit1.text() in allid):
                reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
            ###上面已经排除了不正确的输入，现在真正开始录入
            else:
                fuzeren_add(self.lineEdit1.text(),self.lineEdit2.text())
                reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    def handle_excel_luru(self):
        sheet = open_excel()
        ####
        for i in range(1, sheet.nrows): #第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
 
            data0 = sheet.cell(i,0).value #取第i行第0列
            data1 = sheet.cell(i,1).value#取第i行第1列，下面依次类推
          

            fuzeren_add(data0,data1)
        reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    ##本页的返回键事件
    def click_back(self):
        if self.isVisible():
            self.hide()

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "联系电话"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label.setText(_translate("MainWindow", "姓名"))
        self.label_5.setText(_translate("MainWindow", "负责人信息录入"))
        self.pushButton2.setText(_translate("MainWindow", "返回"))
        self.pushButton3.setText(_translate("MainWindow", "从excel导入"))

        self.menu.setTitle(_translate("MainWindow", "录入"))
