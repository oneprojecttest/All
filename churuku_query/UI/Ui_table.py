# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\CZQ\Desktop\czq_dev\All\churuku_query\UI\table.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(679, 530)
        Form.setStyleSheet("QWidget {\n"
"border-image:url(C:/Users/CZQ/Desktop/czq_dev/All/churuku_query/new/登录背景.jpg);\n"
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
"QTableWidget{\n"
"border-image:url();\n"
"}\n"
"\n"
"QHorizontalHeaderLabels{\n"
"border-image:url();\n"
"}\n"
"\n"
"QVertitalHeaderLabels{\n"
"border-image:url();\n"
"}\n"
"QScrollArea{\n"
"border-image:url();\n"
"}\n"
"QStringList{\n"
"background-color:rgba(135,206,235,200);\n"
"color:#000000;\n"
"}\n"
"\n"
"QHorizontalHeader{\n"
"border-image:url();\n"
"}")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(40, 60, 611, 321))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 0, 0, 160))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(29)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 420, 92, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(135,206,235,200);\n"
"color:#000000;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 430, 92, 28))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgba(135,206,235,200);\n"
"color:#000000;\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "A"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "B"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "C"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "D"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "E"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "F"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "G"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "H"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "I"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "J"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
