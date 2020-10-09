import pymysql
from datetime import datetime
import time
import sys
import xlutils,xlwt
from PyQt5.QtWidgets import (QMenu, QPushButton, QWidget, QTableWidget, QVBoxLayout, QHBoxLayout, QApplication, QTableWidgetItem,
                             QAbstractItemView, QHeaderView, QMainWindow, QInputDialog, QMessageBox, QFileDialog)
from PyQt5.QtCore import QObject, Qt, QDir
from PyQt5.QtGui import *
from sql import *
from DateDialog import DateDialog
from DoubleDateDialog import DoubleDateDialog
import os

class TableWidgetContextMenu7_1(QWidget):

    def __init__(self):
        super(TableWidgetContextMenu7_1,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("负责人查询")
        self.labels=['负责人名称', '电话']
        self.resize(300, 750);
        layout = QVBoxLayout()
        layout_H = QHBoxLayout()
        self.btn0 = QPushButton('刷新',self)
        layout_H.addWidget(self.btn0)
        self.btn1 = QPushButton('导出至excel',self)
        layout_H.addWidget(self.btn1)
        layout.addLayout(layout_H)
        self.tableWidget = QTableWidget()
        self.btn0.clicked.connect(self.show_table)
        self.btn1.clicked.connect(self.handle1)
        self.tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.HorSectionClicked)#表头双击信号
        self.tableWidget.doubleClicked.connect(self.table_double_clicked)#表内双击信号
        layout.addWidget(self.tableWidget)
        ##设置目录
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.show_table()
        ##禁止修改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setLayout(layout)
        
    def show_table(self):
        data = fuzeren_query()
        self.show_query(data)

    def show_query(self,data):
        ##生成表格
        self.tableWidget.clearContents()
        if data:
            self.tableWidget.setRowCount(len(data))
            for i in range(0,len(data)):
                item = data[i]
                for j in range(0,len(item)):
                    newItem = QTableWidgetItem(str(item[j]))
                    self.tableWidget.setItem(i, j, newItem)
        else:
            self.tableWidget.setRowCount(1)
            newItem = QTableWidgetItem("未找到")
            self.tableWidget.setItem(0, 0, newItem)

    ##双击排序     
    def HorSectionClicked(self,index):
        self.tableWidget.clearContents()
        if index == 0:
            data = fuzeren_query_orderbyname()
            self.show_query(data)
        else:
            data = fuzeren_query_orderbydianhua()
            self.show_query(data)
            
    ##双击单元格修改
    def table_double_clicked(self,index):
        if index.column() == 0:
            QMessageBox.about(self,'警告','负责人姓名不可修改！')
        else:
            text, ok = QInputDialog.getText(self,'信息修改','将负责人'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                fuzeren_modify(str(self.tableWidget.item(index.row(),0).text()),\
                               str(text)\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
       
            
    def handle1(self):
        ##设置保存目录
        aim = "C:\\报表\\负责人信息\\"
        self.mkdir(aim)
        nowTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
        nowDate=time.strftime("%Y%m%d", time.localtime())
        filename = str(nowTime)+'.xls'
        wbk = xlwt.Workbook(encoding = 'utf-8')
        self.sheet = wbk.add_sheet("负责人信息"+nowDate, cell_overwrite_ok=True)
        row = 0
        col = 0
        for i in range(self.tableWidget.columnCount()):
            self.sheet.write(0, i, str(self.labels[i]))
        for i in range(self.tableWidget.columnCount()):
            for x in range(self.tableWidget.rowCount()):
                try:
                    text = str(self.tableWidget.item(row, col).text())
                    self.sheet.write(row+1, col, text)
                    row += 1
                except AttributeError:
                    row += 1
            row = 0
            col += 1
        path = aim + filename
        wbk.save(path)
        QMessageBox.about(self,'成功',path+'\n导出成功！')

    def mkdir(self,path):
        path=path.strip()
        path=path.rstrip("\\")
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path) 
            return True
        else:
            return False

    def handle_click(self):
        if not self.isVisible():
            self.show()


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetContextMenu()
    example.show()
    sys.exit(app.exec_())'''


