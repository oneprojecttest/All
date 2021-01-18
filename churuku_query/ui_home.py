# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject , pyqtSignal

class Ui_MainWindow(object):
        # print("12")
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(930, 703)
                MainWindow.setStyleSheet("QWidget {\n"
                        "border-image:url(new/登录背景.jpg);\n"
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
                self.pushButton_7 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_7.setGeometry(QtCore.QRect(140, 210, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_7.setFont(font)
                self.pushButton_7.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_7.setObjectName("pushButton_7")
                self.pushButton_8 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_8.setGeometry(QtCore.QRect(140, 70, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_8.setFont(font)
                self.pushButton_8.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_8.setObjectName("pushButton_8")
                self.pushButton_9 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_9.setGeometry(QtCore.QRect(140, 360, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_9.setFont(font)
                self.pushButton_9.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_9.setObjectName("pushButton_9")
                self.pushButton_10 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_10.setGeometry(QtCore.QRect(140, 500, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_10.setFont(font)
                self.pushButton_10.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_10.setObjectName("pushButton_10")
                self.pushButton_11 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_11.setGeometry(QtCore.QRect(460, 220, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_11.setFont(font)
                self.pushButton_11.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_11.setObjectName("pushButton_11")
                self.pushButton_12 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_12.setGeometry(QtCore.QRect(460, 70, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_12.setFont(font)
                self.pushButton_12.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_12.setObjectName("pushButton_12")
                self.pushButton_13 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_13.setGeometry(QtCore.QRect(460, 360, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_13.setFont(font)
                self.pushButton_13.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_13.setObjectName("pushButton_13")
                self.pushButton_14 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_14.setGeometry(QtCore.QRect(460, 500, 158, 101))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(14)
                font.setBold(True)
                font.setItalic(False)
                font.setWeight(75)
                self.pushButton_14.setFont(font)
                self.pushButton_14.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_14.setObjectName("pushButton_14")
                self.pushButton_17 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_17.setGeometry(QtCore.QRect(311, 127, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_17.setFont(font)
                self.pushButton_17.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_17.setObjectName("pushButton_17")
                self.pushButton_18 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_18.setGeometry(QtCore.QRect(311, 72, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_18.setFont(font)
                self.pushButton_18.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_18.setObjectName("pushButton_18")
                self.pushButton_20 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_20.setGeometry(QtCore.QRect(311, 267, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_20.setFont(font)
                self.pushButton_20.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_20.setObjectName("pushButton_20")
                self.pushButton_19 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_19.setGeometry(QtCore.QRect(311, 212, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_19.setFont(font)
                self.pushButton_19.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_19.setObjectName("pushButton_19")
                self.pushButton_22 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_22.setGeometry(QtCore.QRect(311, 390, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_22.setFont(font)
                self.pushButton_22.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_22.setObjectName("pushButton_22")
                self.pushButton_25 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_25.setGeometry(QtCore.QRect(311, 557, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_25.setFont(font)
                self.pushButton_25.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_25.setObjectName("pushButton_25")
                self.pushButton_24 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_24.setGeometry(QtCore.QRect(311, 502, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_24.setFont(font)
                self.pushButton_24.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_24.setObjectName("pushButton_24")
                self.pushButton_30 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_30.setGeometry(QtCore.QRect(631, 362, 99, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_30.setFont(font)
                self.pushButton_30.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_30.setObjectName("pushButton_30")
                self.pushButton_31 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_31.setGeometry(QtCore.QRect(631, 417, 99, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_31.setFont(font)
                self.pushButton_31.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_31.setObjectName("pushButton_31")
                self.pushButton_29 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_29.setGeometry(QtCore.QRect(631, 277, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_29.setFont(font)
                self.pushButton_29.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_29.setObjectName("pushButton_29")
                self.pushButton_28 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_28.setGeometry(QtCore.QRect(631, 222, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_28.setFont(font)
                self.pushButton_28.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_28.setObjectName("pushButton_28")
                self.pushButton_26 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_26.setGeometry(QtCore.QRect(631, 72, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_26.setFont(font)
                self.pushButton_26.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_26.setObjectName("pushButton_26")
                self.pushButton_27 = QtWidgets.QPushButton(MainWindow)
                self.pushButton_27.setGeometry(QtCore.QRect(631, 127, 82, 37))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(50)
                self.pushButton_27.setFont(font)
                self.pushButton_27.setStyleSheet("background-color:rgba(135,206,235,200);\n"
                        "color:#ffffff;\n"
                        "border-radius: 50px;  border: 2px groove gray;\n"
                        "\n"
                        "\n"
                        "border-style: outset;\n"
                        "\n"
                        "padding:5px;\n"
                        "min-height:20px;\n"
                        "border-radius:15px;")
                self.pushButton_27.setObjectName("pushButton_27")
                
 
        
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        def handle_click(self):
                if not self.isVisible():
                        self.show()
                        self.pushButton_17.hide()
                        self.pushButton_18.hide()
                        self.pushButton_19.hide()
                        self.pushButton_20.hide()
                        self.pushButton_22.hide()
                        self.pushButton_24.hide()
                        self.pushButton_25.hide()
                        self.pushButton_26.hide()
                        self.pushButton_27.hide()
                        self.pushButton_28.hide()
                        self.pushButton_29.hide()
                        self.pushButton_30.hide()
                        self.pushButton_31.hide()

        def handle_cailiao_click(self):
                if not self.pushButton_17.isVisible():
                        self.pushButton_17.show()
                      
                else:
                        self.pushButton_17.hide()
                if not self.pushButton_18.isVisible():
                        self.pushButton_18.show()   
                else:
                        self.pushButton_18.hide()
        def handle_gonghuodanwei_click(self):
                if not self.pushButton_19.isVisible():
                        self.pushButton_19.show()
                else:
                        self.pushButton_19.hide()
                if not self.pushButton_20.isVisible():
                        self.pushButton_20.show()  
                else:
                        self.pushButton_20.hide()
        def handle_kucun_click(self):
                if not self.pushButton_22.isVisible():
                        self.pushButton_22.show()
                else:
                        self.pushButton_22.hide()
                
        def handle_ruku_click(self):
                if not self.pushButton_24.isVisible():
                        self.pushButton_24.show()
                else:
                        self.pushButton_24.hide()
                if not self.pushButton_25.isVisible():
                        self.pushButton_25.show() 
                else:
                        self.pushButton_25.hide()         
        def handle_chuku_click(self):
                if not self.pushButton_26.isVisible():
                        self.pushButton_26.show()
                else:
                        self.pushButton_26.hide()
                if not self.pushButton_27.isVisible():
                        self.pushButton_27.show()   
                else:
                        self.pushButton_27.hide()
        def handle_fuzhang_click(self):
                if not self.pushButton_28.isVisible():
                        self.pushButton_28.show()
                else:
                        self.pushButton_28.hide()
                if not self.pushButton_29.isVisible():
                        self.pushButton_29.show()  
                else:
                        self.pushButton_29.hide()
        def handle_fuzeren_click(self):
                if not self.pushButton_30.isVisible():
                        self.pushButton_30.show()
                else:
                        self.pushButton_30.hide()
                if not self.pushButton_31.isVisible():
                        self.pushButton_31.show()  
                else:
                        self.pushButton_31.hide()
                             
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.pushButton_7.setText(_translate("MainWindow", "供货单位"))
                self.pushButton_8.setText(_translate("MainWindow", "材料"))
                self.pushButton_9.setText(_translate("MainWindow", "库存"))
                self.pushButton_10.setText(_translate("MainWindow", "入库"))
                self.pushButton_11.setText(_translate("MainWindow", "付账"))
                self.pushButton_12.setText(_translate("MainWindow", "出库"))
                self.pushButton_13.setText(_translate("MainWindow", "负责人"))
                self.pushButton_14.setText(_translate("MainWindow", "未付账"))
                self.pushButton_17.setText(_translate("MainWindow", "材料录入"))
                self.pushButton_18.setText(_translate("MainWindow", "材料查询"))
                self.pushButton_20.setText(_translate("MainWindow", "供货录入"))
                self.pushButton_19.setText(_translate("MainWindow", "供货查询"))
                self.pushButton_22.setText(_translate("MainWindow", "库存查询"))
                self.pushButton_25.setText(_translate("MainWindow", "入库录入"))
                self.pushButton_24.setText(_translate("MainWindow", "入库查询"))
                self.pushButton_30.setText(_translate("MainWindow", "负责人查询"))
                self.pushButton_31.setText(_translate("MainWindow", "负责人录入"))
                self.pushButton_29.setText(_translate("MainWindow", "付账录入"))
                self.pushButton_28.setText(_translate("MainWindow", "付账查询"))
                self.pushButton_26.setText(_translate("MainWindow", "出库查询"))
                self.pushButton_27.setText(_translate("MainWindow", "出库录入"))
