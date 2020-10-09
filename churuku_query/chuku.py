# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuku.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(171, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(20, 10, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 100, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(20, 190, 131, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton3.setFont(font)
        self.pushButton3.setObjectName("pushButton3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 171, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.pushButton3.clicked.connect(self.handle_back)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handle_back(self):
        if self.isVisible():
            self.hide()

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", " "))
        self.pushButton1.setText(_translate("MainWindow", "查询"))
        self.pushButton2.setText(_translate("MainWindow", "录入"))
        self.pushButton3.setText(_translate("MainWindow", "返回"))
        self.menu.setTitle(_translate("MainWindow", "出库记录"))
