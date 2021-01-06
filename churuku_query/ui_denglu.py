# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CZQ\Desktop\czq_dev\All\churuku_query\登录界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from ui_home import *
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
from PyQt5.QtCore import QObject , pyqtSignal
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout

class Ui_MainWindow_denglu(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(819, 483)
        Dialog.setStyleSheet("QWidget {\n"
                "border-image:url(churuku_query/new/1-2.jpg);\n"
            "}\n"

            "#下面的防止背景干扰其他控件\n"
            "QTextBrowser {\n"
                "border-image:url();\n"
            "}\n"
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(270, 327, 301, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
            "background-color:rgba(255, 245, 221,200);\n"
            "color:#ffffff;\n"
        "}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 240, 301, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
            "background-color:rgba(255,255,255,120);\n"
            "color:#000000;\n"
        "}")
        self.lineEdit_2.setText("")
        
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 170, 301, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
            "background-color:rgba(255,255,255,120);\n"
            "color:#000000;\n"
            "\n"
        "}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 140, 72, 15))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
            "color:#ffffff;\n"
        "}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 215, 72, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
            "color:#ffffff;\n"
        "}")
        self.label_2.setObjectName("label_2")

        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.returnPressed.connect(self.handle_denglu)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "被装管理登录界面"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.label.setText(_translate("Dialog", "用户"))
        self.label_2.setText(_translate("Dialog", "密码"))

    signal1 = pyqtSignal()#####################定义一个信号，信号绑定写在 show1.py中
    signal2 = pyqtSignal()
    def handle_back(self):
        if self.isVisible():
            self.hide()

    def handle_denglu(self):
        a = self.lineEdit_3.text()
        b = self.lineEdit_2.text()
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
