import xlrd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC

def open_excel():
       
        try:
            book = xlrd.open_workbook(r'fuzeren_luru.xlsx')  #文件名，把文件与py文件放在同一目录下
            print("open excel file!")
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name('Sheet1')   #execl里面的worksheet1
            return sheet
        except:
            print("locate worksheet in excel failed!")

class Ui_MainWindow7_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 520)
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
"}\n"
"\n"
"QPlainTextEdit{\n"
"border-image:url();\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 111, 78))
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
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(260, 60, 241, 41))
        self.lineEdit1.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 110, 111, 78))
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
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(260, 130, 241, 41))
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 200, 111, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(260, 200, 241, 101))
        self.plainTextEdit.setStyleSheet("QPlainTextEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(230, 350, 231, 36))
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
        self.pushButton2.setGeometry(QtCore.QRect(230, 400, 231, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(Form)
        self.pushButton3.setGeometry(QtCore.QRect(230, 450, 231, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton3.setObjectName("pushButton3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "姓       名"))
        self.label_3.setText(_translate("Form", "电       话"))
        self.label_4.setText(_translate("Form", "备       注"))
        self.pushButton1.setText(_translate("Form", "确认"))
        self.pushButton2.setText(_translate("Form", "返回"))
        self.pushButton3.setText(_translate("Form", "从Excel导入"))



    def handle_luru(self):
        if( self.lineEdit1.text() == '' or \
                self.lineEdit2.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        else:
            a = fuzeren_query_allname()
            allid = []
            for i in a:
                allid.append(i[0])
            if (self.lineEdit1.text() in allid):
                reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
            ###上面已经排除了不正确的输入，现在真正开始录入
            else:
                fuzeren_add(self.lineEdit1.text(),self.lineEdit2.text())
                reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    def handle_excel_luru(self):
        sheet = open_excel()
        ####
        for i in range(1, sheet.nrows): #第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
 
            data0 = sheet.cell(i,0).value #取第i行第0列
            data1 = sheet.cell(i,1).value#取第i行第1列，下面依次类推
          

            fuzeren_add(data0,data1)
        reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    ##本页的返回键事件
    def click_back(self):
        if self.isVisible():
            self.hide()

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()
