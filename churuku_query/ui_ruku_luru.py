import xlrd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
import datetime

class Ui_MainWindow4_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        Form.setStyleSheet("QWidget {\n"
"border-image:url(new/table-1.jpg);\n"
"}\n"
"\n"
"#下面的防止背景干扰其他控件\n"
"QTextBrowser {\n"
"border-image:url();\n"
"}\n"
"QLineEdit {\n"
"border-image:url();\n"
"}\n"
"QComboBox {\n"
"border-image:url();\n"
"}\n"
"QLabel {\n"
"border-image:url();\n"
"}\n"
"QPushButton {\n"
"border-image:url();\n"
"}\n"
"QCheckBox {\n"
"border-image:url();\n"
"}\n"
"QDateEdit{\n"
"border-image:url();\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 10, 101, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label.setObjectName("label")
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(281, 30, 481, 41))
        self.lineEdit1.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(161, 70, 101, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(161, 130, 101, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(160, 250, 101, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(160, 300, 101, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(470, 250, 81, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.lineEdit6 = QtWidgets.QLineEdit(Form)
        self.lineEdit6.setGeometry(QtCore.QRect(560, 280, 191, 23))
        self.lineEdit6.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit6.setObjectName("lineEdit6")
        self.comboBox2 = QtWidgets.QComboBox(Form)
        self.comboBox2.setGeometry(QtCore.QRect(580, 180, 171, 22))
        self.comboBox2.setObjectName("comboBox2")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(280, 150, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_17.setObjectName("label_17")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(330, 180, 184, 23))
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(530, 150, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.comboBox3 = QtWidgets.QComboBox(Form)
        self.comboBox3.setGeometry(QtCore.QRect(280, 280, 161, 22))
        self.comboBox3.setObjectName("comboBox3")
        self.lineEdit7 = QtWidgets.QLineEdit(Form)
        self.lineEdit7.setGeometry(QtCore.QRect(580, 380, 171, 23))
        self.lineEdit7.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit7.setObjectName("lineEdit7")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(280, 350, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.comboBox4 = QtWidgets.QComboBox(Form)
        self.comboBox4.setGeometry(QtCore.QRect(330, 380, 171, 21))
        self.comboBox4.setObjectName("comboBox4")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(510, 350, 61, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(280, 100, 111, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(280, 220, 40, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.lineEdit5 = QtWidgets.QLineEdit(Form)
        self.lineEdit5.setGeometry(QtCore.QRect(650, 220, 101, 23))
        self.lineEdit5.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit5.setObjectName("lineEdit5")
        self.lineEdit3 = QtWidgets.QLineEdit(Form)
        self.lineEdit3.setGeometry(QtCore.QRect(330, 220, 101, 23))
        self.lineEdit3.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(Form)
        self.lineEdit4.setGeometry(QtCore.QRect(500, 220, 81, 23))
        self.lineEdit4.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(600, 220, 40, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(450, 220, 40, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(280, 400, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.lineEdit8 = QtWidgets.QLineEdit(Form)
        self.lineEdit8.setGeometry(QtCore.QRect(330, 430, 171, 23))
        self.lineEdit8.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit8.setObjectName("lineEdit8")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(510, 400, 60, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.lineEdit9 = QtWidgets.QLineEdit(Form)
        self.lineEdit9.setGeometry(QtCore.QRect(580, 430, 171, 23))
        self.lineEdit9.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit9.setObjectName("lineEdit9")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(280, 460, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.lineEdit10 = QtWidgets.QLineEdit(Form)
        self.lineEdit10.setGeometry(QtCore.QRect(330, 480, 421, 41))
        self.lineEdit10.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit10.setObjectName("lineEdit10")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(370, 590, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(370, 640, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")



        ##设置文本框只读
        #self.lineEdit1.setReadOnly(True)
        self.lineEdit2.setReadOnly(True)
        #self.lineEdit3.setReadOnly(True)
        #self.lineEdit4.setReadOnly(True)
        self.lineEdit5.setReadOnly(True)
        self.lineEdit6.setReadOnly(True)
        self.lineEdit7.setReadOnly(True)
        self.lineEdit9.setReadOnly(True)
        self.lineEdit9.setReadOnly(True)
        self.lineEdit10.setReadOnly(True)
        ##清除符号
        self.lineEdit1.setClearButtonEnabled(True)

        self.lineEdit3.setClearButtonEnabled(True)
        self.lineEdit4.setClearButtonEnabled(True)

        
        ##设置下拉栏的刷新并且把变动绑定到底下四个文本框中
        firstdata = cailiao_query_allname()
        firstdata_str = []
        for i in firstdata:
            firstdata_str.append(i[0])
        self.comboBox2.addItems(firstdata_str)
        self.comboBox2.activated.connect(self.selectionchange2)

        firstdata2 = fuzeren_query_allname()
        firstdata_str2 = []
        for i in firstdata2:
            firstdata_str2.append(i[0])
        self.comboBox3.addItems(firstdata_str2)
        self.comboBox3.activated.connect(self.selectionchange3)

        firstdata3 = gonghuodanwei_query_allname()
        firstdata_str3 = []
        for i in firstdata3:
            firstdata_str3.append(i[0])
        self.comboBox4.addItems(firstdata_str3)
        self.comboBox4.activated.connect(self.selectionchange4)

        ##把文本框初始化一下
        #self.lineEdit4.setText(self.comboBox4.currentText())
        #self.lineEdit9.setText(self.comboBox9.currentText())
        #self.lineEdit12.setText(self.comboBox12.currentText())

        ###对日期框进行操作
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setCalendarPopup(True)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
        self.dateEdit.setDate(QDate.fromString(nowtime,'yyyy-MM-dd'))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "入库单号"))
        self.label_2.setText(_translate("Form", "日       期"))
        self.label_8.setText(_translate("Form", "材       料"))
        self.label_9.setText(_translate("Form", "负   责  人"))
        self.label_10.setText(_translate("Form", "供   货  商"))
        self.label_11.setText(_translate("Form", "电       话"))
        self.label_15.setText(_translate("Form", "电话"))
        self.label_14.setText(_translate("Form", "联系人"))
        self.label_16.setText(_translate("Form", "地址"))
        self.pushButton1.setText(_translate("Form", "确认"))
        self.pushButton2.setText(_translate("Form", "返回"))
        self.label_17.setText(_translate("Form", "编号"))
        self.label_18.setText(_translate("Form", "名称"))
        self.label_13.setText(_translate("Form", "名称"))
        self.label_12.setText(_translate("Form", "编号"))
        self.label_5.setText(_translate("Form", "数量"))
        self.label_6.setText(_translate("Form", "单位"))
        self.label_7.setText(_translate("Form", "单价"))


    def selectionchange2(self):
        #self.lineEdit4.setText(self.comboBox2.currentText())
        #self.lineEdit4.adjustSize()

        remember_last_top = self.comboBox2.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.comboBox2.currentText()
        res_cailiao_id = cailiao_query_id_by_name(a)
        self.lineEdit2.setText(str(res_cailiao_id[0][0]))
        res_cailiao_danwei = cailiao_query_danwei_by_name(a)
        self.lineEdit5.setText(str(res_cailiao_danwei[0][0]))

        self.comboBox2.clear()
        self.comboBox2.addItem(remember_last_top)
        self.newdata = cailiao_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox2.addItems(self.newdata_str)

    def selectionchange3(self):
        #self.lineEdit9.setText(self.comboBox9.currentText())
        #self.lineEdit9.adjustSize()

        remember_last_top = self.comboBox3.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.comboBox3.currentText()
        res_fuzeren_dianhua = fuzeren_query_dianhua_by_name(a)
        self.lineEdit6.setText(str(res_fuzeren_dianhua[0][0]))

        self.comboBox3.clear()
        self.comboBox3.addItem(remember_last_top)
        self.newdata = fuzeren_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox3.addItems(self.newdata_str)

    def selectionchange4(self):
        #self.lineEdit12.setText(self.comboBox12.currentText())
        #self.lineEdit12.adjustSize()

        remember_last_top = self.comboBox4.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.comboBox4.currentText()
        res_gonghuodanwei_id = gonghuodanwei_query_id_by_name(a)
        res_gonghuodanwei_lianxiren = gonghuodanwei_query_lianxiren_by_name(a)
        res_gonghuodanwei_dianhua = gonghuodanwei_query_dianhua_by_name(a)
        res_gonghuodanwei_dizhi = gonghuodanwei_query_dizhi_by_name(a)
        self.lineEdit7.setText(str(res_gonghuodanwei_id[0][0]))
        self.lineEdit9.setText(str(res_gonghuodanwei_lianxiren[0][0]))
        self.lineEdit8.setText(str(res_gonghuodanwei_dianhua[0][0]))
        self.lineEdit10.setText(str(res_gonghuodanwei_dizhi[0][0]))

        self.comboBox4.clear()
        self.comboBox4.addItem(remember_last_top)
        self.newdata = gonghuodanwei_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox4.addItems(self.newdata_str)


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
                    ruku_add(self.lineEdit1.text(), self.dateEdit.date().toString("yyyy-MM-dd"), \
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

