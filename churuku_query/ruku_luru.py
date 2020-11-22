# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ruku_luru.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import xlrd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
import datetime

def open_excel():
       
        try:
            book = xlrd.open_workbook(r'ruku_luru.xlsx')  #文件名，把文件与py文件放在同一目录下
            print("open excel file!")
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name('Sheet1')   #execl里面的worksheet1
            return sheet
        except:
            print("locate worksheet in excel failed!")

class Ui_MainWindow4_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(570, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit1.setGeometry(QtCore.QRect(22, 91, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 390, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 209, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, -10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(200, 209, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit10.setGeometry(QtCore.QRect(200, 250, 171, 24))
        self.lineEdit10.setObjectName("lineEdit10")
        self.dateEdit2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit2.setGeometry(QtCore.QRect(200, 90, 171, 21))
        self.dateEdit2.setObjectName("dateEdit2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 129, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 340, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit5.setGeometry(QtCore.QRect(20, 170, 171, 24))
        self.lineEdit5.setObjectName("lineEdit5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 50, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox4.setGeometry(QtCore.QRect(570, 120, 161, 21))
        self.comboBox4.setObjectName("comboBox4")
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setGeometry(QtCore.QRect(378, 91, 171, 24))
        self.lineEdit3.setObjectName("lineEdit3")
        self.comboBox9 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox9.setGeometry(QtCore.QRect(20, 280, 171, 21))
        self.comboBox9.setObjectName("comboBox9")
        self.lineEdit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit6.setGeometry(QtCore.QRect(200, 171, 171, 24))
        self.lineEdit6.setObjectName("lineEdit6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(200, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit11.setGeometry(QtCore.QRect(380, 251, 171, 24))
        self.lineEdit11.setObjectName("lineEdit11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(380, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(570, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.comboBox12 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox12.setGeometry(QtCore.QRect(570, 280, 161, 21))
        self.comboBox12.setObjectName("comboBox12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 309, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.lineEdit13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit13.setGeometry(QtCore.QRect(20, 350, 171, 24))
        self.lineEdit13.setText("")
        self.lineEdit13.setObjectName("lineEdit13")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(200, 309, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lineEdit14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit14.setGeometry(QtCore.QRect(200, 350, 171, 24))
        self.lineEdit14.setText("")
        self.lineEdit14.setObjectName("lineEdit14")
        self.lineEdit15 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit15.setGeometry(QtCore.QRect(380, 351, 171, 24))
        self.lineEdit15.setText("")
        self.lineEdit15.setObjectName("lineEdit15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(380, 310, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.lineEdit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit4.setGeometry(QtCore.QRect(570, 90, 161, 24))
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit12.setGeometry(QtCore.QRect(570, 250, 161, 24))
        self.lineEdit12.setObjectName("lineEdit12")
        self.lineEdit9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit9.setGeometry(QtCore.QRect(20, 250, 171, 24))
        self.lineEdit9.setObjectName("lineEdit9")
        self.label16 = QtWidgets.QLabel(self.centralwidget)
        self.label16.setGeometry(QtCore.QRect(382, 129, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label16.setFont(font)
        self.label16.setObjectName("label16")
        self.lineEdit16 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit16.setGeometry(QtCore.QRect(380, 170, 171, 24))
        self.lineEdit16.setObjectName("lineEdit16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 26))
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
        self.lineEdit9.setReadOnly(True)
        self.lineEdit10.setReadOnly(True)
        self.lineEdit11.setReadOnly(True)
        self.lineEdit12.setReadOnly(True)
        self.lineEdit13.setReadOnly(True)
        self.lineEdit14.setReadOnly(True)
        self.lineEdit15.setReadOnly(True)
        self.lineEdit16.setReadOnly(True)

        ##设置下拉栏的刷新并且把变动绑定到底下四个文本框中
        firstdata = cailiao_query_allname()
        firstdata_str = []
        for i in firstdata:
            firstdata_str.append(i[0])
        self.comboBox4.addItems(firstdata_str)
        self.comboBox4.activated.connect(self.selectionchange4)

        firstdata2 = fuzeren_query_allname()
        firstdata_str2 = []
        for i in firstdata2:
            firstdata_str2.append(i[0])
        self.comboBox9.addItems(firstdata_str2)
        self.comboBox9.activated.connect(self.selectionchange9)

        firstdata3 = gonghuodanwei_query_allname()
        firstdata_str3 = []
        for i in firstdata3:
            firstdata_str3.append(i[0])
        self.comboBox12.addItems(firstdata_str3)
        self.comboBox12.activated.connect(self.selectionchange12)

        ##把文本框初始化一下
        self.lineEdit4.setText(self.comboBox4.currentText())
        self.lineEdit9.setText(self.comboBox9.currentText())
        self.lineEdit12.setText(self.comboBox12.currentText())

        ###对日期框进行操作
        self.dateEdit2.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit2.setCalendarPopup(True)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
        self.dateEdit2.setDate(QDate.fromString(nowtime,'yyyy-MM-dd'))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectionchange4(self):
        self.lineEdit4.setText(self.comboBox4.currentText())
        self.lineEdit4.adjustSize()

        remember_last_top = self.comboBox4.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.lineEdit4.text()
        res_cailiao_id = cailiao_query_id_by_name(a)
        self.lineEdit3.setText(str(res_cailiao_id[0][0]))
        res_cailiao_danwei = cailiao_query_danwei_by_name(a)
        self.lineEdit16.setText(str(res_cailiao_danwei[0][0]))

        self.comboBox4.clear()
        self.comboBox4.addItem(remember_last_top)
        self.newdata = cailiao_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox4.addItems(self.newdata_str)

    def selectionchange9(self):
        self.lineEdit9.setText(self.comboBox9.currentText())
        self.lineEdit9.adjustSize()

        remember_last_top = self.comboBox9.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.lineEdit9.text()
        res_fuzeren_dianhua = fuzeren_query_dianhua_by_name(a)
        self.lineEdit10.setText(str(res_fuzeren_dianhua[0][0]))

        self.comboBox9.clear()
        self.comboBox9.addItem(remember_last_top)
        self.newdata = fuzeren_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox9.addItems(self.newdata_str)

    def selectionchange12(self):
        self.lineEdit12.setText(self.comboBox12.currentText())
        self.lineEdit12.adjustSize()

        remember_last_top = self.comboBox12.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.lineEdit12.text()
        res_gonghuodanwei_id = gonghuodanwei_query_id_by_name(a)
        res_gonghuodanwei_lianxiren = gonghuodanwei_query_lianxiren_by_name(a)
        res_gonghuodanwei_dianhua = gonghuodanwei_query_dianhua_by_name(a)
        res_gonghuodanwei_dizhi = gonghuodanwei_query_dizhi_by_name(a)
        self.lineEdit11.setText(str(res_gonghuodanwei_id[0][0]))
        self.lineEdit13.setText(str(res_gonghuodanwei_lianxiren[0][0]))
        self.lineEdit14.setText(str(res_gonghuodanwei_dianhua[0][0]))
        self.lineEdit15.setText(str(res_gonghuodanwei_dizhi[0][0]))

        self.comboBox12.clear()
        self.comboBox12.addItem(remember_last_top)
        self.newdata = gonghuodanwei_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox12.addItems(self.newdata_str)

    '''def autoshow_combo4(self):
        a = self.comboBox4.currentText()
        res = cailiao_query_id_by_name(a)
        self.lineEdit3.setText(str(res[0][0]))

    def autoshow_combo9(self):
        a = self.comboBox9.currentText()
        res = fuzeren_query_dianhua_by_name(a)
        self.lineEdit10.setText(str(res[0][0]))

    def autoshow_combo12(self):
        a = self.comboBox12.currentText()
        res_id = gonghuodanwei_query_id_by_name(a)
        res_lianxiren = gonghuodanwei_query_lianxiren_by_name(a)
        res_dianhua = gonghuodanwei_query_dianhua_by_name(a)
        res_dizhi = gonghuodanwei_query_dianhua_by_name(a)
        self.lineEdit11.setText(str(res_id[0][0]))
        self.lineEdit13.setText(str(res_lianxiren[0][0]))
        self.lineEdit14.setText(str(res_dianhua[0][0]))
        self.lineEdit15.setText(str(res_dizhi[0][0]))'''

    def handle_luru(self):
        a = ruku_query_allid()
        allid = []  ##这是之前的所有出库编号
        for i in a:
            allid.append(i[0])
        ##print(allid)

        ##检测有没有空值
        if (self.lineEdit1.text() == '' or \
                self.lineEdit5.text() == '' or \
                self.lineEdit6.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        ##检测有没有与主键冲突
        elif (self.lineEdit1.text() in allid):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
        else:
            ##检测一下数字栏是不是数字
            if (is_number(self.lineEdit5.text()) == False)  \
                    or (is_number(self.lineEdit6.text()) == False):
                reply = PQW.QMessageBox.warning(self, '警告', "请输入正确的数量", PQW.QMessageBox.Yes)
            else:
                if float(self.lineEdit6.text()) < 0:
                    reply = PQW.QMessageBox.warning(self, '警告', "请输入正确的数量", PQW.QMessageBox.Yes)
                else:
                    ruku_add(self.lineEdit1.text(), self.dateEdit2.date().toString("yyyy-MM-dd"), \
                             self.lineEdit3.text(), self.lineEdit5.text(), \
                             float(self.lineEdit6.text()), self.comboBox9.currentText(), self.lineEdit11.text())
                    reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    ###手写一个函数判断一个数是不是数（包括整数和小数） 返回true表示是数

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
        self.label_2.setText(_translate("MainWindow", "日期"))
        self.pushButton2.setText(_translate("MainWindow", "返回"))
        self.label_7.setText(_translate("MainWindow", "负责人"))
        self.label_5.setText(_translate("MainWindow", "入库单信息录入"))
        self.label_8.setText(_translate("MainWindow", "负责人电话"))
        self.label.setText(_translate("MainWindow", "入库单号"))
        self.label_6.setText(_translate("MainWindow", "数量"))
        self.pushButton.setText(_translate("MainWindow", "确认"))
        self.label_3.setText(_translate("MainWindow", "材料编号"))
        self.label_9.setText(_translate("MainWindow", "单价"))
        self.label_12.setText(_translate("MainWindow", "供货单位编号"))
        self.label_13.setText(_translate("MainWindow", "供货单位名称"))
        self.label_14.setText(_translate("MainWindow", "联系人"))
        self.label_15.setText(_translate("MainWindow", "联系人电话"))
        self.label_16.setText(_translate("MainWindow", "地址"))
        self.label16.setText(_translate("MainWindow", "单位"))
        self.menu.setTitle(_translate("MainWindow", "录入"))

