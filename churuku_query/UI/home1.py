# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject , pyqtSignal

class Ui_MainWindow0(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 61))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(110, 140, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(110, 240, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(110, 340, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(460, 140, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton4.setFont(font)
        self.pushButton4.setObjectName("pushButton4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 90, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(QtCore.QRect(460, 240, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton5.setFont(font)
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(QtCore.QRect(460, 340, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton6.setFont(font)
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(QtCore.QRect(110, 440, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton7.setFont(font)
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(QtCore.QRect(460, 440, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton8.setFont(font)
        self.pushButton8.setObjectName("pushButton8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def handle_click(self):
        if not self.isVisible():
            self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "欢迎来到出入库系统"))
        self.pushButton1.setText(_translate("MainWindow", "材料信息"))
        self.pushButton2.setText(_translate("MainWindow", "供货商信息"))
        self.pushButton3.setText(_translate("MainWindow", "库房信息"))
        self.pushButton4.setText(_translate("MainWindow", "入库信息"))
        self.label_2.setText(_translate("MainWindow", "基本信息"))
        self.label_3.setText(_translate("MainWindow", "流水信息"))
        self.pushButton5.setText(_translate("MainWindow", "出库信息"))
        self.pushButton6.setText(_translate("MainWindow", "付账信息"))
        self.pushButton7.setText(_translate("MainWindow", "负责人信息"))
        self.pushButton8.setText(_translate("MainWindow", "未付账信息"))