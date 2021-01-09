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


class TableWidgetContextMenu2_1(QWidget):

    def __init__(self):
        super(TableWidgetContextMenu2_1,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("供货单位查询")
        self.labels=['供货单位编号', '名称', '联系人','联系人电话','地址','质量认证编号','是否合格供应商']
        self.resize(1200, 750)
        
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
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.show_table()
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(4,300)
        self.tableWidget.setColumnWidth(5,150)
        ##禁止修改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setLayout(layout)
        
    def show_table(self):
        data = gonghuodanwei_query()
        self.show_query(data)

    def handle_flush(self):
        data = gonghuodanwei_query()
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
            data = gonghuodanwei_query_orderbyid()
            self.show_query(data)
        elif index == 1:
            data = gonghuodanwei_query_orderbyname()
            self.show_query(data)
        elif index == 2:
            data = gonghuodanwei_query_orderbylianxiren()
            self.show_query(data)
        elif index == 3:
            data = gonghuodanwei_query_orderbydianhua()
            self.show_query(data)
        elif index == 4:
            data = gonghuodanwei_query_orderbydizhi()
            self.show_query(data)
        elif index == 5:
            data = gonghuodanwei_query_orderbyisoid()
            self.show_query(data)
        else:
            data = gonghuodanwei_query_orderbyhege()
            self.show_query(data)
            
    ##双击单元格修改
    def table_double_clicked(self,index):
        if index.column() == 0:
            QMessageBox.about(self,'警告','供货单位编号不可修改！')
        elif index.column() == 1:
            text, ok = QInputDialog.getText(self,'信息修改','将供货单位编号为'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                gonghuodanwei_modify(str(self.tableWidget.item(index.row(),0).text()),\
                            str(text),\
                            str(self.tableWidget.item(index.row(),2).text()),\
                            str(self.tableWidget.item(index.row(),3).text()),\
                            str(self.tableWidget.item(index.row(),4).text()),\
                            str(self.tableWidget.item(index.row(),5).text()),\
                            str(self.tableWidget.item(index.row(),6).text())\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 2:
            text, ok = QInputDialog.getText(self,'信息修改','将供货单位编号为'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                gonghuodanwei_modify(str(self.tableWidget.item(index.row(),0).text()),\
                            str(self.tableWidget.item(index.row(),1).text()),\
                            str(text),\
                            str(self.tableWidget.item(index.row(),3).text()),\
                            str(self.tableWidget.item(index.row(),4).text()),\
                            str(self.tableWidget.item(index.row(),5).text()),\
                            str(self.tableWidget.item(index.row(),6).text())\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 3:
            text, ok = QInputDialog.getText(self,'信息修改','将供货单位编号为'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                gonghuodanwei_modify(str(self.tableWidget.item(index.row(),0).text()),\
                            str(self.tableWidget.item(index.row(),1).text()),\
                            str(self.tableWidget.item(index.row(),2).text()),\
                            str(text),\
                            str(self.tableWidget.item(index.row(),4).text()),\
                            str(self.tableWidget.item(index.row(),5).text()),\
                            str(self.tableWidget.item(index.row(),6).text())\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 4:
            text, ok = QInputDialog.getText(self,'信息修改','将供货单位编号为'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                gonghuodanwei_modify(str(self.tableWidget.item(index.row(),0).text()),\
                            str(self.tableWidget.item(index.row(),1).text()),\
                            str(self.tableWidget.item(index.row(),2).text()),\
                            str(self.tableWidget.item(index.row(),3).text()),\
                            str(text),\
                            str(self.tableWidget.item(index.row(),5).text()),\
                            str(self.tableWidget.item(index.row(),6).text())\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 5:
            text, ok = QInputDialog.getText(self,'信息修改','将供货单位编号为'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                gonghuodanwei_modify(str(self.tableWidget.item(index.row(),0).text()),\
                            str(self.tableWidget.item(index.row(),1).text()),\
                            str(self.tableWidget.item(index.row(),2).text()),\
                            str(self.tableWidget.item(index.row(),3).text()),\
                            str(self.tableWidget.item(index.row(),4).text()),\
                            str(text),\
                            str(self.tableWidget.item(index.row(),6).text())\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
        else:
            text, ok = QInputDialog.getText(self,'信息修改','将供货单位编号为'+str(self.tableWidget.item(index.row(),0).text())\
                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                        +')\n修改为:')
            if ok:
                gonghuodanwei_modify(str(self.tableWidget.item(index.row(),0).text()),\
                            str(self.tableWidget.item(index.row(),1).text()),\
                            str(self.tableWidget.item(index.row(),2).text()),\
                            str(self.tableWidget.item(index.row(),3).text()),\
                            str(self.tableWidget.item(index.row(),4).text()),\
                            str(self.tableWidget.item(index.row(),5).text()),\
                            str(text)\
                            )
                newItem = QTableWidgetItem(str(text))
                self.tableWidget.setItem(index.row(),index.column(), newItem)
                QMessageBox.about(self,'成功','修改成功！')
            
    def handle1(self):
        ##设置保存目录
        aim = "C:\\报表\\供货单位\\"
        self.mkdir(aim)
        nowTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
        nowDate=time.strftime("%Y%m%d", time.localtime())
        filename = str(nowTime)+'.xls'
        wbk = xlwt.Workbook(encoding = 'utf-8')
        self.sheet = wbk.add_sheet("供货单位"+nowDate, cell_overwrite_ok=True)
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

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()



'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetContextMenu()
    example.show()
    sys.exit(app.exec_())'''


