



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow0(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(1000, 400)
        Form.setFixedSize(1000,400)
        Form.setStyleSheet("QWidget {\n"
"border-image:url(new/1-2.jpg);\n"
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
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(270, 60, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 60, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 60, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 60, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 210, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 210, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 210, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QtCore.QRect(650, 210, 151, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{background-color:rgba(255, 245, 221,160);\n"
"color:#ffffff;\n"
"}\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(890, 20, 40, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"border-radius:20px;/*圆角弧度(为正方形边长一半时就是圆形)*/\n"
"background-color:rgba(255, 245, 221,160);/*背景色*/\n"
"color:#ffffff;\n"
"}\n"
"\n"
"QPushButton:hover{/*鼠标悬停*/background-color:rgba(255,255,255,100);}QPushButton:pressed{/*鼠标按下*/background-color:rgba(255,255,255,200);}")
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def handle_click(self):
        if not self.isVisible():
                self.show()
                       
    def click_back(self):
        if self.isVisible():
            self.hide()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理界面"))
        self.pushButton.setText(_translate("Form", "材料"))
        self.pushButton_2.setText(_translate("Form", "供货单位"))
        self.pushButton_3.setText(_translate("Form", "库存"))
        self.pushButton_4.setText(_translate("Form", "入库"))
        self.pushButton_5.setText(_translate("Form", "出库"))
        self.pushButton_6.setText(_translate("Form", "付账"))
        self.pushButton_7.setText(_translate("Form", "未付"))
        self.pushButton_8.setText(_translate("Form", "负责人"))
        self.pushButton_9.setText(_translate("Form", "注销"))