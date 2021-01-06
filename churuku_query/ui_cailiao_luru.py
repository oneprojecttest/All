import xlrd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
from sql import *

def open_excel():
       
        try:
            book = xlrd.open_workbook(r'C:\Users\CZQ\Desktop\czq_dev\All\churuku_query\cailiao_luru.xlsx')  #文件名，把文件与py文件放在同一目录下
            print("open excel file!")
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name('Sheet1')   #execl里面的worksheet1
            return sheet
        except:
            print("locate worksheet in excel failed!")

class Ui_MainWindow1_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(600, 480)
        Form.setFixedSize(600,480)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        Form.setFont(font)
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
            "}")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 300, 231, 124))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
            "background-color:rgba(206,206,206,200);\n"
            "color:#000000;\n"
            "}")
        self.pushButton2.setObjectName("pushButton2")
        self.verticalLayout.addWidget(self.pushButton2)

        self.pushButton3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("QPushButton{\n"
            "background-color:rgba(206,206,206,200);\n"
            "color:#000000;\n"
            "}")
        self.pushButton3.setObjectName("pushButton3")
        self.verticalLayout.addWidget(self.pushButton3)
        
        self.pushButton1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("QPushButton{\n"
            "background-color:rgba(206,206,206,200);\n"
            "color:#000000;\n"
            "}")
        self.pushButton1.setObjectName("pushButton1")
        self.verticalLayout.addWidget(self.pushButton1)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 190, 40, 69))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel{\n"
            "\n"
            "color:#ffffff;\n"
            "}")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
            "\n"
            "color:#ffffff;\n"
            "}")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 90, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
            "\n"
            "color:#ffffff;\n"
            "}")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 40, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
            "\n"
            "color:#ffffff;\n"
            "}")
        self.label.setObjectName("label")
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(170, 60, 309, 31))
        self.lineEdit1.setStyleSheet("QLineEdit{\n"
            "background-color:rgba(255,255,255,120);\n"
            "color:#000000;\n"
            "\n"
            "}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(170, 120, 309, 31))
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
            "background-color:rgba(255,255,255,120);\n"
            "color:#000000;\n"
            "\n"
            "}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(Form)
        self.lineEdit3.setGeometry(QtCore.QRect(170, 170, 309, 31))
        self.lineEdit3.setStyleSheet("QLineEdit{\n"
            "background-color:rgba(255,255,255,120);\n"
            "color:#000000;\n"
            "\n"
            "}")
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(Form)
        self.lineEdit4.setGeometry(QtCore.QRect(170, 220, 309, 31))
        self.lineEdit4.setStyleSheet("QLineEdit{\n"
            "background-color:rgba(255,255,255,120);\n"
            "color:#000000;\n"
            "\n"
            "}")
        self.lineEdit4.setObjectName("lineEdit4")

        self.lineEdit1.setClearButtonEnabled(True)
        self.lineEdit1.setClearButtonEnabled(True)
        self.lineEdit1.setClearButtonEnabled(True)
        self.lineEdit1.setClearButtonEnabled(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "材料录入"))
        self.pushButton2.setText(_translate("Form", "确认"))
        self.pushButton3.setText(_translate("Form", "从Excel导入"))
        self.pushButton1.setText(_translate("Form", "返回"))
        self.label_4.setText(_translate("Form", "单位"))
        self.label_3.setText(_translate("Form", "规格"))
        self.label_2.setText(_translate("Form", "名称"))
        self.label.setText(_translate("Form", "编号"))



    def handle_luru(self):
        if( self.lineEdit1.text() == '' or \
                self.lineEdit2.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit4.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        else:
            a = cailiao_query_allid()
            allid = []
            for i in a:
                allid.append(i[0])
            if (self.lineEdit1.text() in allid):
                reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
            ###上面已经排除了不正确的输入，现在真正开始录入
            else:
                cailiao_add(self.lineEdit1.text(),self.lineEdit2.text(),self.lineEdit3.text(),self.lineEdit4.text())
                reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)
                self.lineEdit1.clear()
                self.lineEdit2.clear()
                self.lineEdit3.clear()
                self.lineEdit4.clear()

    

    def handle_excel_luru(self):
        sheet = open_excel()
        ####
        for i in range(1, sheet.nrows): #第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
 
            data0 = sheet.cell(i,0).value #取第i行第0列
            data1 = sheet.cell(i,1).value#取第i行第1列，下面依次类推
            data2 = sheet.cell(i,2).value
            data3 = sheet.cell(i,3).value

            cailiao_add(data0,data1,data2,data3)
        reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

        
    ##本页的返回键事假
    def click_back(self):
        if self.isVisible():
            self.hide()

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()
