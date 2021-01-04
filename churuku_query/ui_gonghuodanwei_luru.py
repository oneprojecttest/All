import xlrd
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
from sql import *
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC

def open_excel():
       
        try:
            book = xlrd.open_workbook(r'C:\Users\CZQ\Desktop\czq_dev\All\churuku_query\gonghuodanwei_luru.xlsx')  #文件名，把文件与py文件放在同一目录下
            print("open excel file!")
        except:
            print("open excel file failed!")
        try:
            sheet = book.sheet_by_name('Sheet1')   #execl里面的worksheet1
            return sheet
        except:
            print("locate worksheet in excel failed!")

class Ui_MainWindow2_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 647)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("QWidget {\n"
"border-image:url(C:/Users/CZQ/Desktop/czq_dev/All/churuku_query/new/table-1.jpg);\n"
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
"}")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(410, 150, 40, 69))
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
        self.label_3.setGeometry(QtCore.QRect(209, 140, 61, 78))
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
        self.label_2.setGeometry(QtCore.QRect(220, 90, 40, 78))
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
        self.label.setGeometry(QtCore.QRect(220, 40, 40, 78))
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
        self.lineEdit1.setGeometry(QtCore.QRect(290, 60, 309, 31))
        self.lineEdit1.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(290, 120, 309, 31))
        self.lineEdit2.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(Form)
        self.lineEdit3.setGeometry(QtCore.QRect(290, 170, 111, 31))
        self.lineEdit3.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(Form)
        self.lineEdit4.setGeometry(QtCore.QRect(460, 170, 141, 31))
        self.lineEdit4.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 210, 61, 78))
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
        self.lineEdit5.setGeometry(QtCore.QRect(290, 220, 309, 61))
        self.lineEdit5.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit5.setObjectName("lineEdit5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(150, 290, 131, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.lineEdit6 = QtWidgets.QLineEdit(Form)
        self.lineEdit6.setGeometry(QtCore.QRect(290, 320, 309, 31))
        self.lineEdit6.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.lineEdit6.setObjectName("lineEdit6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(230, 360, 40, 78))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel{\n"
"\n"
"color:#ffffff;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(290, 390, 87, 22))
        self.comboBox.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255,255,255,120);\n"
"color:#000000;\n"
"\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(290, 440, 299, 36))
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
        self.pushButton2.setGeometry(QtCore.QRect(290, 540, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton2.setFont(font)
        self.pushButton2.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 490, 299, 36))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(206,206,206,200);\n"
"color:#000000;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.comboBox.setObjectName("comboBox")
        ##初始化下拉栏
        self.comboBox.addItem('是')
        self.comboBox.addItem('否')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "确认"))
        self.pushButton2.setText(_translate("Form", "从Excel导入"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.label_4.setText(_translate("Form", "电话"))
        self.label_3.setText(_translate("Form", "联系人"))
        self.label_2.setText(_translate("Form", "名称"))
        self.label.setText(_translate("Form", "编号"))
        self.label_5.setText(_translate("Form", "地址"))
        self.label_6.setText(_translate("Form", "质量认证编号"))
        self.label_7.setText(_translate("Form", "合格"))


    def handle_luru(self):
        if( self.lineEdit1.text() == '' or \
                self.lineEdit2.text() == '' or \
                self.lineEdit3.text() == '' or \
                self.lineEdit4.text() == '' or \
                self.lineEdit5.text() == '' or \
                self.lineEdit6.text() == ''):
            reply = PQW.QMessageBox.warning(self, '警告', "请不要有空输入", PQW.QMessageBox.Yes)
        else:
            a = gonghuodanwei_query_allid()
            allid = []
            for i in a:
                allid.append(i[0])
            if (self.lineEdit1.text() in allid):
                reply = PQW.QMessageBox.warning(self, '警告', "请不要录入重复编号", PQW.QMessageBox.Yes)
            ###上面已经排除了不正确的输入，现在真正开始录入
            else:
                gonghuodanwei_add(self.lineEdit1.text(),self.lineEdit2.text(),self.lineEdit3.text(), \
                            self.lineEdit4.text(),self.lineEdit5.text(),self.lineEdit6.text(), \
                            self.comboBox.currentText())
                reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)

    def handle_excel_luru(self):
        sheet = open_excel()
        ####
        for i in range(1, sheet.nrows): #第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
 
            data0 = sheet.cell(i,0).value #取第i行第0列
            data1 = sheet.cell(i,1).value#取第i行第1列，下面依次类推
            data2 = sheet.cell(i,2).value
            data3 = sheet.cell(i,3).value
            data4 = sheet.cell(i,4).value 
            data5 = sheet.cell(i,5).value
            data6 = sheet.cell(i,6).value
            
            gonghuodanwei_add(data0,data1,data2,data3,data4,data5,data6)
        reply = PQW.QMessageBox.warning(self, '提示', "录入成功", PQW.QMessageBox.Yes)    

    ##本页的返回键事件
    def click_back(self):
        if self.isVisible():
            self.hide()

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()