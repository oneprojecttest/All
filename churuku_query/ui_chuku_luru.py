from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
import datetime

class Ui_MainWindow5_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(850, 680)
        Form.setFixedSize(850, 680)
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
        self.label.setGeometry(QtCore.QRect(150, 30, 101, 78))
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
        self.lineEdit1.setGeometry(QtCore.QRect(290, 50, 421, 41))
        self.lineEdit1.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 100, 101, 78))
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
        self.label_8.setGeometry(QtCore.QRect(150, 160, 101, 78))
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
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(490, 210, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(240, 210, 40, 78))
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
        self.lineEdit2.setGeometry(QtCore.QRect(290, 240, 181, 23))
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.comboBox2 = QtWidgets.QComboBox(Form)
        self.comboBox2.setGeometry(QtCore.QRect(540, 240, 171, 22))
        self.comboBox2.setObjectName("comboBox2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(490, 280, 40, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.lineEdit3 = QtWidgets.QLineEdit(Form)
        self.lineEdit3.setGeometry(QtCore.QRect(290, 280, 181, 23))
        self.lineEdit3.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(Form)
        self.lineEdit4.setGeometry(QtCore.QRect(540, 280, 171, 23))
        self.lineEdit4.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 280, 40, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(490, 320, 81, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(140, 320, 101, 78))
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
        self.lineEdit5 = QtWidgets.QLineEdit(Form)
        self.lineEdit5.setGeometry(QtCore.QRect(540, 350, 171, 23))
        self.lineEdit5.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit5.setObjectName("lineEdit5")
        self.comboBox3 = QtWidgets.QComboBox(Form)
        self.comboBox3.setGeometry(QtCore.QRect(290, 350, 181, 22))
        self.comboBox3.setObjectName("comboBox3")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(140, 380, 101, 78))
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
        self.lineEdit6 = QtWidgets.QLineEdit(Form)
        self.lineEdit6.setGeometry(QtCore.QRect(290, 400, 421, 41))
        self.lineEdit6.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit6.setObjectName("lineEdit6")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(350, 500, 299, 36))
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
        self.pushButton2.setGeometry(QtCore.QRect(350, 550, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(290, 130, 161, 22))
        self.dateEdit.setObjectName("dateEdit")


        ##设置文本框只读
        self.lineEdit2.setReadOnly(True)
        self.lineEdit4.setReadOnly(True)
        self.lineEdit5.setReadOnly(True)
        ##
        self.lineEdit1.setClearButtonEnabled(True)
        self.lineEdit3.setClearButtonEnabled(True)
        self.lineEdit6.setClearButtonEnabled(True)                

        ##设置下拉栏的刷新并且把变动绑定到底下四个文本框中
        firstdata1 = cailiao_query_allname()
        firstdata_str1 = []
        for i in firstdata1:
            firstdata_str1.append(i[0])
        self.comboBox2.addItems(firstdata_str1)
        self.comboBox2.activated.connect(self.selectionchange2)

        firstdata2 = fuzeren_query_allname()

        firstdata_str2 = []
        for i in firstdata2:
            firstdata_str2.append(i[0])
        #     print("hello")
        self.comboBox3.addItems(firstdata_str2)
        self.comboBox3.activated.connect(self.selectionchange3)

        ##把文本框初始化一下
        #self.lineEdit4.setText(self.comboBox4.currentText())
        #self.lineEdit6.setText(self.comboBox6.currentText())

        ###对日期框进行操作
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setCalendarPopup(True)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
        self.dateEdit.setDate(QDate.fromString(nowtime,'yyyy-MM-dd'))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "出库录入"))
        self.label.setText(_translate("Form", "入库单号"))
        self.label_2.setText(_translate("Form", "日       期"))
        self.label_8.setText(_translate("Form", "材       料"))
        self.label_18.setText(_translate("Form", "名称"))
        self.label_17.setText(_translate("Form", "编号"))
        self.label_6.setText(_translate("Form", "单位"))
        self.label_5.setText(_translate("Form", "数量"))
        self.label_11.setText(_translate("Form", "电话"))
        self.label_9.setText(_translate("Form", "负   责  人"))
        self.label_10.setText(_translate("Form", "用        途"))
        self.pushButton1.setText(_translate("Form", "确认"))
        self.pushButton2.setText(_translate("Form", "返回"))



    def selectionchange2(self):
        #self.lineEdit4.setText(self.comboBox4.currentText())
        #self.lineEdit4.adjustSize()

        remember_last_top = self.comboBox2.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.comboBox2.currentText()
        res_cailiao_id = cailiao_query_id_by_name(a)
        self.lineEdit2.setText(str(res_cailiao_id[0][0]))
        res_cailiao_danwei = cailiao_query_danwei_by_name(a)
        self.lineEdit4.setText(str(res_cailiao_danwei[0][0]))

        self.comboBox2.clear()
        self.comboBox2.addItem(remember_last_top)
        self.newdata = cailiao_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox2.addItems(self.newdata_str)

    def selectionchange3(self):
        #self.lineEdit6.setText(self.comboBox6.currentText())
        #self.lineEdit6.adjustSize()

        remember_last_top = self.comboBox3.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.comboBox3.currentText()
        res_fuzeren_dianhua = fuzeren_query_dianhua_by_name(a)
        self.lineEdit5.setText(str(res_fuzeren_dianhua[0][0]))

        self.comboBox3.clear()
        self.comboBox3.addItem(remember_last_top)
        self.newdata = fuzeren_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox3.addItems(self.newdata_str)

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
                self.lineEdit2.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit4.text() == '' or \
                self.lineEdit5.text() == '' or \
                self.lineEdit6.text() == '' ):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        ##检测有没有与主键冲突
        elif (self.lineEdit1.text() in allid):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
        else:
            ##检测一下数字栏是不是数字
            if (is_number(self.lineEdit5.text()) != True):
                reply = PQW.QMessageBox.warning(self, '警告', "请输入正确的数量", PQW.QMessageBox.Yes)
            else:
                chuku_add(self.lineEdit1.text(), self.dateEdit.date().toString("yyyy-MM-dd"), self.lineEdit2.text(), \
                          float(self.lineEdit3.text()), self.comboBox3.currentText(),self.lineEdit6.text())
                reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    ##本页的返回键事件
    def click_back(self):
        if self.isVisible():
            self.hide()

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()