from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DoubleDateDialog(QDialog):
    def __init__(self,parent=None):
        super(DoubleDateDialog,self).__init__(parent)
        self.setWindowTitle("时间修改")

        layout = QVBoxLayout(self)

        self.LineEdit = QLineEdit(self)
        self.LineEdit.setText("开始日期(包括):")
        self.LineEdit.setReadOnly(True)
        layout.addWidget(self.LineEdit)
        self.datetime_from = QDateTimeEdit(self)
        self.datetime_from.setCalendarPopup(True)
        self.datetime_from.setDisplayFormat("yyyy.MM.dd")
        self.datetime_from.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime_from)
        self.LineEdit2 = QLineEdit(self)
        self.LineEdit2.setText("结束日期(包括):")
        self.LineEdit2.setReadOnly(True)
        layout.addWidget(self.LineEdit2)
        self.datetime_to = QDateTimeEdit(self)
        self.datetime_to.setCalendarPopup(True)
        self.datetime_to.setDisplayFormat("yyyy.MM.dd")
        self.datetime_to.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime_to)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)

    def dateTime_from(self):
        return self.datetime_from.dateTime()
    def dateTime_to(self):
        return self.datetime_to.dateTime()
    @staticmethod
    def getDateTime(parent = None):
        dialog = DoubleDateDialog(parent)
        result = dialog.exec()
        date_from = dialog.dateTime_from()
        date_to = dialog.dateTime_to()
        return (date_from.date(),date_from.time(),result == QDialog.Accepted)

