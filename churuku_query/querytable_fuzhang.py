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


class TableWidgetContextMenu6_1(QWidget):

    def __init__(self):
        super(TableWidgetContextMenu6_1,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("付账记录查询")
        self.labels=['付账单号', '日期', '供货单位编号','供货单位名称','联系人','联系人电话','已付金额','付款方式']
        self.resize(1100, 750);
        layout = QVBoxLayout()
        layout_H = QHBoxLayout()
        self.btn0 = QPushButton('刷新',self)
        layout_H.addWidget(self.btn0)
        self.btn1 = QPushButton('按日期查询',self)
        layout_H.addWidget(self.btn1)
        self.btn4 = QPushButton('按供货单位查询',self)
        layout_H.addWidget(self.btn4)
        self.btn5 = QPushButton('导出至excel',self)
        layout_H.addWidget(self.btn5)
        layout.addLayout(layout_H)
        self.tableWidget = QTableWidget()
        self.btn0.clicked.connect(self.show_table)
        self.btn1.clicked.connect(self.handle1)
        self.btn4.clicked.connect(self.handle4)
        self.btn5.clicked.connect(self.handle5)
        self.tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.HorSectionClicked)#表头双击信号
        self.tableWidget.doubleClicked.connect(self.table_double_clicked)#表内双击信号
        layout.addWidget(self.tableWidget)
        ##设置目录
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.show_table()
        
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,200)
        ##禁止修改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setLayout(layout)
        

    def show_table(self):
        data = fuzhang_query()
        self.show_query(data)

     
    def show_query(self,data):
        ##生成表格
        self.tableWidget.clearContents()
        if data:
            self.tableWidget.setRowCount(len(data))
            for i in range(0,len(data)):
                item = data[i]
                data3 = gonghuodanwei_query_byid(item[2])
                newItem = QTableWidgetItem(str(item[0]))
                self.tableWidget.setItem(i, 0, newItem)
                time0 = item[1].strftime("%Y-%m-%d")
                newItem = QTableWidgetItem(str(time0))
                self.tableWidget.setItem(i, 1, newItem)
                newItem = QTableWidgetItem(str(item[2]))
                self.tableWidget.setItem(i, 2, newItem)
                for j in range(3,6):
                    newItem = QTableWidgetItem(str(data3[j-2]))
                    self.tableWidget.setItem(i, j, newItem)
                newItem = QTableWidgetItem(str(item[3]))
                self.tableWidget.setItem(i, 6, newItem)
                newItem = QTableWidgetItem(str(item[4]))
                self.tableWidget.setItem(i, 7, newItem)
        else:
            self.tableWidget.setRowCount(1)
            newItem = QTableWidgetItem("未找到")
            self.tableWidget.setItem(0, 0, newItem)
            
    ##双击排序
    def HorSectionClicked(self,index):
        self.tableWidget.clearContents()
        if index == 0:
            data = fuzhang_query_orderbyid()
            self.show_query(data)
        elif index == 1:
            data = fuzhang_query_orderbytime()
            self.show_query(data)
        elif index == 2 or index == 3 or index == 4 or index == 5:
            data = fuzhang_query_orderbygonghuodanwei_id()
            self.show_query(data)
        elif index == 6:
            data = fuzhang_query_orderbyfuzhang()
            self.show_query(data)
        else:
            data = fuzhang_query_orderbyfangshi()
            self.show_query(data)

    ##双击单元格修改
    def table_double_clicked(self,index):
        if index.column() == 0:
            QMessageBox.about(self,'警告','付账单号不可修改！')
        elif index.column() == 1:
            dialog = DateDialog(self)
            result = dialog.exec()
            date = dialog.dateTime()
            dialog.destroy()
            if result:
                fuzhang_modify(str(self.tableWidget.item(index.row(),0).text()),\
                             str(date.toString(Qt.ISODate).split('T')[0]),\
                             str(self.tableWidget.item(index.row(),2).text()),\
                             float(self.tableWidget.item(index.row(),6).text()),\
                             str(self.tableWidget.item(index.row(),7).text())\
                             )
                newItem = QTableWidgetItem(str(date.toString(Qt.ISODate).split('T')[0]))
                self.tableWidget.setItem(index.row(),1, newItem)
                QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 2:
            num, ok = QInputDialog.getText(self,'信息修改','将付账单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                data = gonghuodanwei_query_byid(num)
                if data:
                     data2 = gonghuodanwei_query_byid(num)
                     fuzhang_modify(str(self.tableWidget.item(index.row(),0).text()),\
                             str(self.tableWidget.item(index.row(),1).text()),\
                             str(num),\
                             float(self.tableWidget.item(index.row(),6).text()),\
                             str(self.tableWidget.item(index.row(),7).text())\
                             )
                     newItem = QTableWidgetItem(str(num))
                     self.tableWidget.setItem(index.row(),index.column(), newItem)
                     for i in range(1,4):
                         newItem = QTableWidgetItem(str(data2[i]))
                         self.tableWidget.setItem(index.row(),index.column()+i, newItem)
                     QMessageBox.about(self,'成功','修改成功！')
                else:
                    QMessageBox.about(self,'格式错误','请输入正确的入账单号！')
        elif index.column() == 6:
            num, ok = QInputDialog.getText(self,'信息修改','将付账单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                 try:
                    test = float(num)
                 except:
                    QMessageBox.about(self,'格式错误','格式错误，请输入数字！')
                    return
                 fuzhang_modify(str(self.tableWidget.item(index.row(),0).text()),\
                             str(self.tableWidget.item(index.row(),1).text()),\
                             str(self.tableWidget.item(index.row(),2).text()),\
                             float(num),\
                             str(self.tableWidget.item(index.row(),7).text())\
                             )
                 newItem = QTableWidgetItem(str(num))
                 self.tableWidget.setItem(index.row(),index.column(), newItem)
                 QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 7:
            num, ok = QInputDialog.getText(self,'信息修改','将付账单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                if num == '转账' or num == '现金':
                    fuzhang_modify(str(self.tableWidget.item(index.row(),0).text()),\
                                 str(self.tableWidget.item(index.row(),1).text()),\
                                 str(self.tableWidget.item(index.row(),2).text()),\
                                 float(self.tableWidget.item(index.row(),6).text()),\
                                 str(num)\
                                 )
                    newItem = QTableWidgetItem(str(num))
                    self.tableWidget.setItem(index.row(),index.column(), newItem)
                    QMessageBox.about(self,'成功','修改成功！')
                else:
                    QMessageBox.about(self,'格式错误','请输入转账或现金！')
        
        else:
            QMessageBox.about(self,'警告','此表中'+str(self.labels[index.column()])+'不可修改！\n若修改'+str(self.labels[index.column()])+'请到入库记录查询页面！')
            
        
    def handle1(self):
        dialog = DoubleDateDialog(self)
        result = dialog.exec()
        date_from = dialog.dateTime_from()
        date_to = dialog.dateTime_to()
        dialog.destroy()
        if result:
            data = fuzhang_query_bytime(date_from.toString(Qt.ISODate).split('T')[0],date_to.toString(Qt.ISODate).split('T')[0])
            self.show_query(data)
    def handle4(self):
        gonghuodanwei_id, ok = QInputDialog.getText(self,'信息查询','想要查询的供货单位编号为：')
        if ok:
            data = fuzhang_query_bygonghuodanwei(gonghuodanwei_id)
            self.show_query(data)
    def handle5(self):
        ##设置保存目录
        aim = "C:\\报表\\付账记录\\"
        self.mkdir(aim)
        nowTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
        nowDate=time.strftime("%Y%m%d", time.localtime())
        filename = str(nowTime)+'.xls'
        wbk = xlwt.Workbook(encoding = 'utf-8')
        self.sheet = wbk.add_sheet("付账记录报表"+nowDate, cell_overwrite_ok=True)
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
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetContextMenu6_1()
    example.show()
    sys.exit(app.exec_())


