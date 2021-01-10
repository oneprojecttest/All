# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from home1 import *
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
from PyQt5.QtCore import QObject , pyqtSignal
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout

class Ui_MainWindow_denglu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 275)
        MainWindow.setStyleSheet("QWidget {
            "border-image:url(C:/Users/CZQ/Desktop/czq_dev/All/churuku_query/new/登录背景.jpg);\n"
            "}\n"
            "#下面的防止背景干扰其他控件\n"

            "QLineEdit {\n"
                "border-image:url();\n"
            "}\n"
            "QLabel {\n"
                "border-image:url();\n"
            "}\n"
            "QMessageBox {\n"
                "border-image:url();\n"
            "}\n"            
            "QPushButton {\n"
                "border-image:url();\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(150, 100, 191, 41))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(150, 170, 191, 41))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 160, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.lineEdit2.setEchoMode(QLineEdit.Password)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    signal1 = pyqtSignal()#####################定义一个信号，信号绑定写在 show1.py中
    signal2 = pyqtSignal()
    def handle_back(self):
        if self.isVisible():
            self.hide()

    def handle_denglu(self):
        a = self.lineEdit1.text()
        b = self.lineEdit2.text()
        time_now = QDateTime.currentDateTime()
        time_now = time_now.toString('yyyy-MM-dd-HH-mm-ss')
        allyonghuming = []
        allroot = []
        tmp = denglu_query_allyonghuming()
        tmp_root = root_denglu_query_allyonghuming()
        for i in tmp:
            allyonghuming.append(str(i[0]))
        for i in tmp_root:
            allroot.append(str(i[0]))
        if a == '' or b == '':
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        else:
            ###不存在此用户
            if a in allroot:
                res_root = root_denglu_query_mima_by_yonghuming(a)[0][0]
                if b == res_root:
                    ##密码匹配，则直接登录Home1页面，并且使得当前页隐身，同时添加登录成功信息
                    denglu_record_add(str(time_now), str(a), '成功')##添加登录成功信息
                    self.hide()###登录页隐身
                    self.signal2.emit()###发射信号，让home1不在隐身，信号绑定写在show1.py中                
                else:
                    print(get_md5(b))
                    ##密码不匹配 弹出警告框，并且录入失败信息
                    reply = PQW.QMessageBox.warning(self, '警告', "密码不正确", PQW.QMessageBox.Yes)
                    denglu_record_add(str(time_now),str(a),'失败')

            elif a in allyonghuming:
                res = denglu_query_mima_by_yonghuming(a)[0][0]
                if get_md5(b) == res:
                 ##密码匹配，则直接登录Home1页面，并且使得当前页隐身，同时添加登录成功信息
                    denglu_record_add(str(time_now), str(a), '成功')##添加登录成功信息
                    self.hide()###登录页隐身
                    self.signal1.emit()###发射信号，让home1不在隐身，信号绑定写在show1.py中
                else:
                    print(get_md5(b))
                    ##密码不匹配 弹出警告框，并且录入失败信息
                    reply = PQW.QMessageBox.warning(self, '警告', "密码不正确", PQW.QMessageBox.Yes)
                    denglu_record_add(str(time_now),str(a),'失败')
            elif a not in allyonghuming:
                reply = PQW.QMessageBox.warning(self, '警告', "不存在此用户", PQW.QMessageBox.Yes)

            


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "出入库系统—登录界面"))
        self.label_2.setText(_translate("MainWindow", "用户名："))
        self.label_3.setText(_translate("MainWindow", "密码："))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.menu.setTitle(_translate("MainWindow", "登录界面"))
