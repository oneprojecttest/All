from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from PyQt5.QtCore import QDate,QDateTime,QTime
import datetime

class Ui_MainWindow6_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 640)
        Form.setStyleSheet("QWidget {\n"
"border-image:url(churuku_query/new/table-1.jpg);\n"
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
        self.label.setGeometry(QtCore.QRect(70, 70, 111, 78))
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
        self.lineEdit1.setGeometry(QtCore.QRect(190, 90, 481, 41))
        self.lineEdit1.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 111, 78))
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
        self.label_8.setGeometry(QtCore.QRect(70, 190, 111, 78))
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
        self.comboBox2 = QtWidgets.QComboBox(Form)
        self.comboBox2.setGeometry(QtCore.QRect(190, 220, 191, 22))
        self.comboBox2.setObjectName("comboBox2")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(410, 190, 40, 78))
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
        self.lineEdit2.setGeometry(QtCore.QRect(480, 220, 191, 23))
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(70, 250, 111, 78))
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
        self.lineEdit3 = QtWidgets.QLineEdit(Form)
        self.lineEdit3.setGeometry(QtCore.QRect(190, 280, 191, 23))
        self.lineEdit3.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit3.setObjectName("lineEdit3")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(410, 250, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.lineEdit4 = QtWidgets.QLineEdit(Form)
        self.lineEdit4.setGeometry(QtCore.QRect(480, 280, 191, 23))
        self.lineEdit4.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 310, 111, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.lineEdit5 = QtWidgets.QLineEdit(Form)
        self.lineEdit5.setGeometry(QtCore.QRect(190, 340, 191, 23))
        self.lineEdit5.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit5.setObjectName("lineEdit5")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(410, 310, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_19.setObjectName("label_19")
        self.comboBox3 = QtWidgets.QComboBox(Form)
        self.comboBox3.setGeometry(QtCore.QRect(480, 340, 191, 22))
        self.comboBox3.setObjectName("comboBox3")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(290, 470, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(290, 420, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton1.setObjectName("pushButton1")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(190, 160, 191, 22))
        self.dateEdit.setObjectName("dateEdit")


        ##设置文本框只读
        self.lineEdit3.setReadOnly(True)
        self.lineEdit4.setReadOnly(True)
        self.lineEdit2.setReadOnly(True)
        #self.lineEdit6.setReadOnly(True)

        ##设置下拉栏的刷新并且把变动绑定到底下四个文本框中
        firstdata = gonghuodanwei_query_allname()
        firstdata_str = []
        for i in firstdata:
            firstdata_str.append(i[0])
        self.comboBox2.addItems(firstdata_str)
        self.comboBox2.activated.connect(self.selectionchange)

        ##把文本框初始化一下
        self.lineEdit3.setText(self.comboBox3.currentText())

        ##把付账方式的combox初始化
        init_str1 = '转账'
        init_str2 = '现金'
        self.comboBox3.addItem(str(init_str1))
        self.comboBox3.addItem(str(init_str2))

        ###对日期框进行操作
        self.dateEdit.setDisplayFormat('yyyy-MM-dd')
        self.dateEdit.setCalendarPopup(True)
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d")
        self.dateEdit.setDate(QDate.fromString(nowtime,'yyyy-MM-dd'))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "付账录入"))
        self.label.setText(_translate("Form", "付账单号"))
        self.label_2.setText(_translate("Form", "日       期"))
        self.label_8.setText(_translate("Form", "供货单位"))
        self.label_17.setText(_translate("Form", "编号"))
        self.label_9.setText(_translate("Form", "负   责  人"))
        self.label_18.setText(_translate("Form", "电话"))
        self.label_3.setText(_translate("Form", "金        额"))
        self.label_19.setText(_translate("Form", "方式"))
        self.pushButton2.setText(_translate("Form", "返回"))
        self.pushButton1.setText(_translate("Form", "确认"))


    def selectionchange(self):
        #self.lineEdit3.setText(self.comboBox3.currentText())
        #self.lineEdit3.adjustSize()

        remember_last_top = self.comboBox2.currentText()  ##记住最上面的一项，每次查找都使得这一项变成最上面的一项

        a = self.comboBox2.currentText()
        res_id = gonghuodanwei_query_id_by_name(a)
        res_lianxiren = gonghuodanwei_query_lianxiren_by_name(a)
        res_dianhua = gonghuodanwei_query_dianhua_by_name(a)

        print(res_id)
        print(res_id[0])
        print(res_id[0][0])
        self.lineEdit2.setText(str(res_id[0][0]))
        self.lineEdit3.setText(str(res_lianxiren[0][0]))
        self.lineEdit4.setText(str(res_dianhua[0][0]))

        self.comboBox2.clear()
        self.comboBox2.addItem(remember_last_top)
        self.newdata = gonghuodanwei_query_allname()
        self.newdata_str = []
        for i in self.newdata:
            if i[0] != remember_last_top:
                self.newdata_str.append(i[0])
        self.comboBox2.addItems(self.newdata_str)

    def handle_luru(self):
        a = fuzhang_query_allid()
        allid = []  ##这是之前的所有出库编号
        for i in a:
            allid.append(i[0])
        #print(allid)

        ##检测有没有空值
        if (self.lineEdit1.text() == '' or \
                self.lineEdit2.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit4.text() == '' or \
                self.lineEdit5.text() == '' or \
                self.comboBox2.currentText() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        ##检测有没有与主键冲突
        elif (self.lineEdit1.text() in allid):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
        else:
            ##检测一下数字栏是不是数字
            if (is_number(self.lineEdit5.text()) != True):
                reply = PQW.QMessageBox.warning(self, '警告', "请输入正确的付账金额", PQW.QMessageBox.Yes)
            else:
                m = self.comboBox3.currentText()
                fuzhang_add(self.lineEdit1.text(), self.dateEdit.date().toString("yyyy-MM-dd"), \
                            self.lineEdit2.text(), float(self.lineEdit5.text()),
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