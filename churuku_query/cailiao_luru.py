# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cailiao_luru.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from sql import *

class Ui_MainWindow1_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 227)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(540, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 90, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 140, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(11, 100, 707, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout.addWidget(self.lineEdit1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout.addWidget(self.lineEdit2)
        self.lineEdit3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.horizontalLayout.addWidget(self.lineEdit3)
        self.lineEdit4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit4.setObjectName("lineEdit4")
        self.horizontalLayout.addWidget(self.lineEdit4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 26))
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
                self.lineEdit2.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit4.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        else:
            a = cailiao_query_allid()
            allid = []
            for i in a:
                allid.append(i[0])
            if (self.lineEdit1.text() in allid):
                reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
            ###上面已经排除了不正确的输入，现在真正开始录入
            else:
                cailiao_add(self.lineEdit1.text(),self.lineEdit2.text(),self.lineEdit3.text(),self.lineEdit4.text())
                reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)


    ##本页的返回键事假
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
        self.label.setText(_translate("MainWindow", "编号"))
        self.label_2.setText(_translate("MainWindow", "名称"))
        self.label_3.setText(_translate("MainWindow", "规格"))
        self.label_4.setText(_translate("MainWindow", "单位"))
        self.label_5.setText(_translate("MainWindow", "材料信息录入"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.pushButton2.setText(_translate("MainWindow", "返回"))
        self.menu.setTitle(_translate("MainWindow", "录入"))
