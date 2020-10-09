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

class TableWidgetContextMenu4_1(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu4_1,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("入库记录查询")
        self.labels=['入库单号', '日期', '材料编号','材料名称','数量','单价','总金额','负责人','负责人电话','供货单位编号','供货单位名称','联系人','联系人电话','地址']
        self.resize(1200, 750)
        layout = QVBoxLayout()
        layout_H = QHBoxLayout()
        self.btn0 = QPushButton('刷新',self)
        layout_H.addWidget(self.btn0)
        self.btn1 = QPushButton('按日期查询',self)
        layout_H.addWidget(self.btn1)
        self.btn2 = QPushButton('按材料编号查询',self)
        layout_H.addWidget(self.btn2)
        self.btn3 = QPushButton('按负责人查询',self)
        layout_H.addWidget(self.btn3)
        self.btn4 = QPushButton('按供货单位查询',self)
        layout_H.addWidget(self.btn4)
        self.btn5 = QPushButton('导出至excel',self)
        layout_H.addWidget(self.btn5)
        layout.addLayout(layout_H)
        self.tableWidget = QTableWidget()
        self.btn0.clicked.connect(self.show_table)
        self.btn1.clicked.connect(self.handle1)
        self.btn2.clicked.connect(self.handle2)
        self.btn3.clicked.connect(self.handle3)
        self.btn4.clicked.connect(self.handle4)
        self.btn5.clicked.connect(self.handle5)
        self.tableWidget.horizontalHeader().sectionDoubleClicked.connect(self.HorSectionClicked)#表头双击信号
        self.tableWidget.doubleClicked.connect(self.table_double_clicked)#表内双击信号
        layout.addWidget(self.tableWidget)
        ##设置目录
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setHorizontalHeaderLabels(self.labels)
        self.show_table()

        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(4,60)
        self.tableWidget.setColumnWidth(5,80)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setColumnWidth(9,150)
        self.tableWidget.setColumnWidth(10,200)
        self.tableWidget.setColumnWidth(13,300)

        ##禁止修改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setLayout(layout)

    def show_table(self):
        data = ruku_query()
        self.show_query(data)

     
    def show_query(self,data):
        ##生成表格
        self.tableWidget.clearContents()
        
        if data:
            self.tableWidget.setRowCount(len(data))
            for i in range(0,len(data)):
                item = data[i]
                data2 = cailiao_query_byid(item[2])
                data3 = fuzeren_query_byname(item[6])
                data4 = gonghuodanwei_query_byid(item[7])
                newItem = QTableWidgetItem(str(item[0]))
                self.tableWidget.setItem(i, 0, newItem)
                time0 = item[1].strftime("%Y-%m-%d")
                newItem = QTableWidgetItem(str(time0))
                self.tableWidget.setItem(i, 1, newItem)
                newItem = QTableWidgetItem(str(item[2]))
                self.tableWidget.setItem(i, 2, newItem)
                newItem = QTableWidgetItem(str(data2[1]))
                self.tableWidget.setItem(i, 3, newItem)
                for j in range(4,8):
                    newItem = QTableWidgetItem(str(item[j-1]))
                    self.tableWidget.setItem(i, j, newItem)
                newItem = QTableWidgetItem(str(data3[1]))
                self.tableWidget.setItem(i, 8, newItem)
                newItem = QTableWidgetItem(str(item[7]))
                self.tableWidget.setItem(i, 9, newItem)
                for j in range(10,14):
                    newItem = QTableWidgetItem(str(data4[j-9]))
                    self.tableWidget.setItem(i, j, newItem)
        else:
            self.tableWidget.setRowCount(1)
            newItem = QTableWidgetItem("未找到")
            self.tableWidget.setItem(0, 0, newItem)

    ##双击排序     
    def HorSectionClicked(self,index):
        self.tableWidget.clearContents()
        if index == 0:
            data = ruku_query_orderbyid()
            self.show_query(data)
        elif index == 1:
            data = ruku_query_orderbytime()
            self.show_query(data)
        elif index == 2 or index == 3:
            data = ruku_query_orderbycailiao_id()
            self.show_query(data)
        elif index == 4:
            data = ruku_query_orderbyshuliang()
            self.show_query(data)
        elif index == 5:
            data = ruku_query_orderbydanjia()
            self.show_query(data)
        elif index == 6:
            data = ruku_query_orderbyjine()
            self.show_query(data)
        elif index == 7 or index == 8:
            data = ruku_query_orderbyfuzeren_name()
            self.show_query(data)
        else:
            data = ruku_query_orderbygonghuodanwei_id()
            self.show_query(data)

    ##双击单元格修改
    def table_double_clicked(self,index):
        if index.column() == 0:
            QMessageBox.about(self,'警告','入库编号不可修改！')
        elif index.column() == 1:
            dialog = DateDialog(self)
            result = dialog.exec()
            date = dialog.dateTime()
            dialog.destroy()
            if result:
                ruku_modify(str(self.tableWidget.item(index.row(),0).text()),\
                             str(date.toString(Qt.ISODate).split('T')[0]),\
                             str(self.tableWidget.item(index.row(),2).text()),\
                             float(self.tableWidget.item(index.row(),4).text()),\
                             str(self.tableWidget.item(index.row(),5).text()),\
                             str(self.tableWidget.item(index.row(),7).text()),\
                             str(self.tableWidget.item(index.row(),9).text())\
                             )
                newItem = QTableWidgetItem(str(date.toString(Qt.ISODate).split('T')[0]))
                self.tableWidget.setItem(index.row(),1, newItem)
                QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 2:
            num, ok = QInputDialog.getText(self,'信息修改','将入库单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                data = cailiao_query_byid(num)
                if data:

                     ruku_modify(str(self.tableWidget.item(index.row(),0).text()),\
                                 str(self.tableWidget.item(index.row(),1).text()),\
                                 str(num),\
                                 float(self.tableWidget.item(index.row(),4).text()),\
                                 str(self.tableWidget.item(index.row(),5).text()),\
                                 str(self.tableWidget.item(index.row(),7).text()),\
                                 str(self.tableWidget.item(index.row(),9).text())\
                                 )
                     newItem = QTableWidgetItem(str(num))
                     self.tableWidget.setItem(index.row(),index.column(), newItem)
                     newItem = QTableWidgetItem(str(data[1]))
                     self.tableWidget.setItem(index.row(),index.column()+1, newItem)
                     QMessageBox.about(self,'成功','修改成功！')
                else:
                    QMessageBox.about(self,'格式错误','请输入正确的材料编号！')
        
        elif index.column() == 3:
            QMessageBox.about(self,'警告','此表中材料名称不可修改！\n若修改材料请直接修改材料编号！')
            
        elif index.column() == 4:
            num, ok = QInputDialog.getText(self,'信息修改','将入库单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                 try:
                    test = float(num)
                 except:
                    QMessageBox.about(self,'格式错误','格式错误，请输入数字！')
                    return
                 ruku_modify(str(self.tableWidget.item(index.row(),0).text()),\
                             str(self.tableWidget.item(index.row(),1).text()),\
                             str(self.tableWidget.item(index.row(),2).text()),\
                             float(num),\
                             float(self.tableWidget.item(index.row(),5).text()),\
                             str(self.tableWidget.item(index.row(),7).text()),\
                             str(self.tableWidget.item(index.row(),9).text())\
                             )
                 newItem = QTableWidgetItem(str(num))
                 self.tableWidget.setItem(index.row(),4, newItem)
                 newItem = QTableWidgetItem(str(float(num)*float(self.tableWidget.item(index.row(),5).text())))
                 self.tableWidget.setItem(index.row(), 6, newItem)
                 QMessageBox.about(self,'成功','修改成功！')
        elif index.column() == 5:
            num, ok = QInputDialog.getText(self,'信息修改','将入库单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                 try:
                    test = float(num)
                 except:
                    QMessageBox.about(self,'格式错误','格式错误，请输入数字！')
                    return
                 ruku_modify(str(self.tableWidget.item(index.row(),0).text()),\
                             str(self.tableWidget.item(index.row(),1).text()),\
                             str(self.tableWidget.item(index.row(),2).text()),\
                             float(self.tableWidget.item(index.row(),4).text()),\
                             float(num),\
                             str(self.tableWidget.item(index.row(),7).text()),\
                             str(self.tableWidget.item(index.row(),9).text())\
                             )
                 newItem = QTableWidgetItem(str(num))
                 self.tableWidget.setItem(index.row(),5, newItem)
                 newItem = QTableWidgetItem(str(float(num)*float(self.tableWidget.item(index.row(),4).text())))
                 self.tableWidget.setItem(index.row(),6, newItem)
                 QMessageBox.about(self,'成功','修改成功！')
        
        elif index.column() == 6:
            QMessageBox.about(self,'警告','此表中金额不可修改！\n若修改金额请修改单价！')
        elif index.column() == 7:
            name, ok = QInputDialog.getText(self,'信息修改','将入库单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                       +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                       +')\n修改为:')
            if ok:
                data = fuzeren_query_byname(name)
                if data:
                
                     ruku_modify(str(self.tableWidget.item(index.row(),0).text()),\
                                 str(self.tableWidget.item(index.row(),1).text()),\
                                 str(self.tableWidget.item(index.row(),2).text()),\
                                 float(self.tableWidget.item(index.row(),4).text()),\
                                 str(self.tableWidget.item(index.row(),5).text()),\
                                 str(name),\
                                 str(self.tableWidget.item(index.row(),9).text())\
                                 )
                     
                     newItem = QTableWidgetItem(str(name))
                     self.tableWidget.setItem(index.row(),index.column(), newItem)
                     newItem = QTableWidgetItem(str(data[1]))
                     self.tableWidget.setItem(index.row(),index.column()+1, newItem)
                     QMessageBox.about(self,'成功','修改成功！')
                else:
                    QMessageBox.about(self,'格式错误','请输入正确的负责人姓名！')
        elif index.column() == 8:
            QMessageBox.about(self,'警告','此表中负责人电话不可修改！\n若修改负责人电话请到负责人信息查询页面！')
        elif index.column() == 9:
            num, ok = QInputDialog.getText(self,'信息修改','将入库单号为'+str(self.tableWidget.item(index.row(),0).text())\
                                        +'\n的'+str(self.labels[index.column()])+'('+str(self.tableWidget.item(index.row(),index.column()).text())\
                                        +')\n修改为:')
            if ok:
                data = gonghuodanwei_query_byid(num)
                if data:
                    ruku_modify(str(self.tableWidget.item(index.row(),0).text()),\
                                str(self.tableWidget.item(index.row(),1).text()),\
                                str(self.tableWidget.item(index.row(),2).text()),\
                                float(self.tableWidget.item(index.row(),4).text()),\
                                str(self.tableWidget.item(index.row(),5).text()),\
                                str(self.tableWidget.item(index.row(),7).text()),\
                                str(num)\
                                )
                    newItem = QTableWidgetItem(str(num))
                    self.tableWidget.setItem(index.row(),index.column(), newItem)
                    for i in range(1,5):
                        newItem = QTableWidgetItem(str(data[i]))
                        self.tableWidget.setItem(index.row(),index.column()+i, newItem)
                    QMessageBox.about(self,'成功','修改成功！')
            else:
                QMessageBox.about(self,'格式错误','请输入正确的材料编号！')
        else:
            QMessageBox.about(self,'警告','此表中'+str(self.labels[index.column()])+'不可修改！\n若修改'+str(self.labels[index.column()])+'请到供货单位信息查询页面！')
            
    
        
    
        
    def handle1(self):
        dialog = DoubleDateDialog(self)
        result = dialog.exec()
        date_from = dialog.dateTime_from()
        date_to = dialog.dateTime_to()
        dialog.destroy()
        if result:
            data = ruku_query_bytime(date_from.toString(Qt.ISODate).split('T')[0],date_to.toString(Qt.ISODate).split('T')[0])
            self.show_query(data)
    def handle2(self):
        cailiao_id, ok = QInputDialog.getText(self,'信息查询','想要查询的材料编号为：')
        if ok:
            data = ruku_query_bycailiao_id(cailiao_id)
            self.show_query(data)
    def handle3(self):
        fuzeren_name, ok = QInputDialog.getText(self,'信息查询','想要查询的负责人姓名为：')
        if ok:
            data = ruku_query_byfuzeren(fuzeren_name)
            self.show_query(data)
    def handle4(self):
        gonghuodanwei_id, ok = QInputDialog.getText(self,'信息查询','想要查询的供货单位编号为：')
        if ok:
            data = ruku_query_bygonghuodanwei(gonghuodanwei_id)
            self.show_query(data)
    def handle5(self):
        ##设置保存目录
        aim = "C:\\报表\\入库记录\\"
        self.mkdir(aim)
        nowTime=time.strftime("%Y%m%d%H%M%S", time.localtime())
        nowDate=time.strftime("%Y%m%d", time.localtime())
        filename = str(nowTime)+'.xls'
        wbk = xlwt.Workbook(encoding = 'utf-8')
        self.sheet = wbk.add_sheet("入库记录报表"+nowDate, cell_overwrite_ok=True)
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

    ##本页的返回键事件
    def click_back(self):
        if self.isVisible():
            self.hide()

    ##上一页调用本页
    def handle_click(self):
        if not self.isVisible():
            self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetContextMenu4_1()
    example.show()
    sys.exit(app.exec_())


