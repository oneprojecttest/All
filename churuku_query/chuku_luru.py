# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuku_luru.ui'
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

class Ui_MainWindow5_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 260, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(378, 101, 171, 24))
        self.lineEdit3.setObjectName("lineEdit3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(380, 169, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 190, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(200, 169, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(22, 101, 171, 24))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 169, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(20, 210, 171, 24))
        self.lineEdit5.setObjectName("lineEdit5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit7.setGeometry(QtCore.QRect(380, 210, 171, 24))
        self.lineEdit7.setObjectName("lineEdit7")
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(570, 130, 171, 21))
        self.comboBox4.setObjectName("comboBox4")
        self.comboBox6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox6.setGeometry(QtCore.QRect(200, 240, 171, 21))
        self.comboBox6.setObjectName("comboBox6")
        self.dateEdit2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit2.setGeometry(QtCore.QRect(200, 100, 171, 21))
        self.dateEdit2.setObjectName("dateEdit2")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(570, 100, 171, 24))
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(200, 210, 171, 24))
        self.lineEdit6.setObjectName("lineEdit6")
        self.lineEdit8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit8.setGeometry(QtCore.QRect(760, 100, 171, 24))
        self.lineEdit8.setObjectName("lineEdit8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(760, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit9.setGeometry(QtCore.QRect(570, 210, 171, 24))
        self.lineEdit9.setObjectName("lineEdit9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 170, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 26))
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
        self.lineEdit6.setReadOnly(True)
        self.lineEdit7.setReadOnly(True)
        self.lineEdit8.setReadOnly(True)

        ##设置下拉栏的刷新并且把变动绑定到底下四个文本框中
        firstdata1 = cailiao_query_allname()
        firstdata_str1 = []
        for i in firstdata1:
            firstdata_str1.append(i[0])
        self.comboBox4.addItems(firstdata_str1)
        self.comboBox4.activated.connect(self.selectionchange1)

        firstdata2 = fuzeren_query_allname()
        firstdata_str2 = []
        for i in firstdata2:
            firstdata_str2.append(i[0])
        self.comboBox6.addItems(firstdata_str2)
        self.comboBox6.activated.connect(self.selectionchange2)

        ##把文本框初始化一下
        self.lineEdit4.setText(self.comboBox4.currentText())
        self.lineEdit6.setText(self.comboBox6.currentText())

        ###对日期框进行操作
        self.dateEdit2.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit2.setCalendarPopup(True)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
        self.dateEdit2.setDate(QDate.fromString(nowtime,'yyyy-MM-dd'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectionchange1(self):
        self.lineEdit4.setText(self.comboBox4.currentText())
        self.lineEdit4.adjustSize()

        remember_last_top = self.comboBox4.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.lineEdit4.text()
        res_cailiao_id = cailiao_query_id_by_name(a)
        self.lineEdit3.setText(str(res_cailiao_id[0][0]))
        res_cailiao_danwei = cailiao_query_danwei_by_name(a)
        self.lineEdit8.setText(str(res_cailiao_danwei[0][0]))

        self.comboBox4.clear()
        self.comboBox4.addItem(remember_last_top)
        self.newdata = cailiao_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox4.addItems(self.newdata_str)

    def selectionchange2(self):
        self.lineEdit6.setText(self.comboBox6.currentText())
        self.lineEdit6.adjustSize()

        remember_last_top = self.comboBox6.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.lineEdit6.text()
        res_fuzeren_dianhua = fuzeren_query_dianhua_by_name(a)
        self.lineEdit7.setText(str(res_fuzeren_dianhua[0][0]))

        self.comboBox6.clear()
        self.comboBox6.addItem(remember_last_top)
        self.newdata = fuzeren_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox6.addItems(self.newdata_str)

    '''def autoshow_combo4(self):
        a = self.comboBox4.currentText()
        res = cailiao_query_id_by_name(a)
        self.lineEdit3.setText(str(res[0][0]))

    def autoshow_combo6(self):
        a = self.comboBox6.currentText()
        res = fuzeren_query_dianhua_by_name(a)
        self.lineEdit7.setText(res[0][0])'''

    def handle_luru(self):
        a = chuku_query_allid()
        allid = []  ##这是之前的所有出库编号
        for i in a:
            allid.append(i[0])

        ##检测有没有空值
        if (self.lineEdit1.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit5.text() == '' or \
                self.lineEdit7.text() == '' or \
                self.lineEdit8.text() == '' or \
                self.lineEdit9.text() == '' ):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        ##检测有没有与主键冲突
        elif (self.lineEdit1.text() in allid):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
        else:
            ##检测一下数字栏是不是数字
            if (is_number(self.lineEdit5.text()) != True):
                reply = PQW.QMessageBox.warning(self, '警告', "请输入正确的数量", PQW.QMessageBox.Yes)
            else:
                chuku_add(self.lineEdit1.text(), self.dateEdit2.date().toString("yyyy-MM-dd"), self.lineEdit3.text(), \
                          float(self.lineEdit5.text()), self.comboBox6.currentText(),self.lineEdit9.text())
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
        self.label_4.setText(_translate("MainWindow", "材料名称"))
        self.pushButton2.setText(_translate("MainWindow", "返回"))
        self.label_5.setText(_translate("MainWindow", "出库单信息录入"))
        self.label_8.setText(_translate("MainWindow", "负责人电话"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_7.setText(_translate("MainWindow", "负责人"))
        self.label_2.setText(_translate("MainWindow", "日期"))
        self.label.setText(_translate("MainWindow", "出库单号"))
        self.label_6.setText(_translate("MainWindow", "数量"))
        self.label_3.setText(_translate("MainWindow", "材料编号"))
        self.label_9.setText(_translate("MainWindow", "单位"))
        self.label_10.setText(_translate("MainWindow", "用途"))
        self.menu.setTitle(_translate("MainWindow", "录入"))

