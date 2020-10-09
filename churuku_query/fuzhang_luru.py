# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuzhang_luru.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
import datetime

class Ui_MainWindow6_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 325)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(22, 91, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(200, 201, 171, 24))
        self.lineEdit5.setObjectName("lineEdit5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dateEdit2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit2.setGeometry(QtCore.QRect(200, 90, 171, 21))
        self.dateEdit2.setObjectName("dateEdit2")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 240, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, -10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 180, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(390, 200, 171, 24))
        self.lineEdit6.setText("")
        self.lineEdit6.setObjectName("lineEdit6")
        self.comboBox3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox3.setGeometry(QtCore.QRect(380, 120, 171, 21))
        self.comboBox3.setObjectName("comboBox3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(20, 201, 171, 24))
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEdit7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit7.setGeometry(QtCore.QRect(570, 90, 171, 24))
        self.lineEdit7.setText("")
        self.lineEdit7.setObjectName("lineEdit7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(570, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(380, 90, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit3.setFont(font)
        self.lineEdit3.setObjectName("lineEdit3")
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        self.label9.setGeometry(QtCore.QRect(760, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.comboBox8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox8.setGeometry(QtCore.QRect(760, 90, 171, 21))
        self.comboBox8.setObjectName("comboBox8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        ##设置文本框只读
        self.lineEdit3.setReadOnly(True)
        self.lineEdit4.setReadOnly(True)
        self.lineEdit5.setReadOnly(True)
        self.lineEdit6.setReadOnly(True)

        ##设置下拉栏的刷新并且把变动绑定到底下四个文本框中
        firstdata = gonghuodanwei_query_allname()
        firstdata_str = []
        for i in firstdata:
            firstdata_str.append(i[0])
        self.comboBox3.addItems(firstdata_str)
        self.comboBox3.activated.connect(self.selectionchange)

        ##把文本框初始化一下
        self.lineEdit3.setText(self.comboBox3.currentText())

        ##把付账方式的combox初始化
        init_str1 = '转账'
        init_str2 = '现金'
        self.comboBox8.addItem(str(init_str1))
        self.comboBox8.addItem(str(init_str2))

        ###对日期框进行操作
        self.dateEdit2.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit2.setCalendarPopup(True)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
        self.dateEdit2.setDate(QDate.fromString(nowtime,'yyyy-MM-dd'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectionchange(self):
        self.lineEdit3.setText(self.comboBox3.currentText())
        self.lineEdit3.adjustSize()

        remember_last_top = self.comboBox3.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.lineEdit3.text()
        res_id = gonghuodanwei_query_id_by_name(a)
        res_lianxiren = gonghuodanwei_query_lianxiren_by_name(a)
        res_dianhua = gonghuodanwei_query_dianhua_by_name(a)

        print(res_id)
        print(res_id[0])
        print(res_id[0][0])
        self.lineEdit4.setText(str(res_id[0][0]))
        self.lineEdit5.setText(str(res_lianxiren[0][0]))
        self.lineEdit6.setText(str(res_dianhua[0][0]))

        self.comboBox3.clear()
        self.comboBox3.addItem(remember_last_top)
        self.newdata = gonghuodanwei_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox3.addItems(self.newdata_str)

    def handle_luru(self):
        a = fuzhang_query_allid()
        allid = []  ##这是之前的所有出库编号
        for i in a:
            allid.append(i[0])
        #print(allid)

        ##检测有没有空值
        if (self.lineEdit1.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit4.text() == '' or \
                self.lineEdit5.text() == '' or \
                self.lineEdit6.text() == '' or \
                self.lineEdit7.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        ##检测有没有与主键冲突
        elif (self.lineEdit1.text() in allid):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
        else:
            ##检测一下数字栏是不是数字
            if (is_number(self.lineEdit7.text()) != True):
                reply = PQW.QMessageBox.warning(self, '警告', "请输入正确的付账金额", PQW.QMessageBox.Yes)
            else:
                m = self.comboBox8.currentText()
                fuzhang_add(self.lineEdit1.text(), self.dateEdit2.date().toString("yyyy-MM-dd"), \
                            self.lineEdit4.text(), float(self.lineEdit7.text()),
                            str(m))
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
        self.label_3.setText(_translate("MainWindow", "供货单位名称"))
        self.pushButton2.setText(_translate("MainWindow", "返回"))
        self.label_5.setText(_translate("MainWindow", "付账信息录入"))
        self.label_9.setText(_translate("MainWindow", "联系人"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_11.setText(_translate("MainWindow", "联系人电话"))
        self.label_2.setText(_translate("MainWindow", "日期"))
        self.label.setText(_translate("MainWindow", "付账单号"))
        self.label_10.setText(_translate("MainWindow", "供货单位编号"))
        self.label_12.setText(_translate("MainWindow", "付账金额"))
        self.label9.setText(_translate("MainWindow", "付账方式"))
        self.menu.setTitle(_translate("MainWindow", "录入"))

