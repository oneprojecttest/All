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
from PyQt5 import QtCore, QtGui, QtWidgets

class TableWidgetContextMenu2_1(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu2_1,self).__init__()
        self.setupUi()

    def setupUi(self):
       
        self.setObjectName("Form")
        self.setFixedSize(877, 437)
        self.setStyleSheet("")

        self.labels=['供货单位编号', '名称', '联系人','联系人电话','地址','质量认证编号','是否合格供应商','操作']


        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(50, 80, 741, 151))
        self.tableWidget.setStyleSheet("background-color:rgba(206,206,206,100);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(4)
        

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setItem(1,5,item)
        '''
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        item.setFont(font)
        
        self.tableWidget.setItem(0, 0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        item.setFont(font)
        self.tableWidget.setItem(0, 1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        item.setFont(font)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        item.setFont(font)
        self.tableWidget.setItem(0, 3, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        '''
        #self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStyleSheet("color:rgba(255,255,235,100);")
        self.tableWidget.horizontalHeader().setStyleSheet("background-color:rgba(206,206,206,100);")

        self.tableWidget.setHorizontalHeaderLabels(self.labels)

        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setGeometry(QtCore.QRect(0, -10, 881, 461))
        self.tableView.setStyleSheet("QTableView {\n"
            "border-image:url(new/table.jpg);\n"
            "}")
        self.tableView.horizontalHeader().setStyleSheet("QHeaderView::section {"
                                                       "color: black;padding-left: 4px;border: 1px solid #6c6c6c;}")

        self.tableView.setObjectName("tableView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(300, 270, 241, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
            "background-color:rgba(206,206,206,200);\n"
            "color:#ffffff;\n"
            "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
            "background-color:rgba(206,206,206,200);\n"
            "color:#ffffff;\n"
            "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tableView.raise_()
        self.tableWidget.raise_()

        self.verticalLayoutWidget.raise_()

        self.show_table()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "供货单位查询"))
        
        '''
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "新建行"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "新建行"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "新建行"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "新建行"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "新建列"))
        '''
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        '''
        self.tableWidget.item(0, 0).setText(_translate("Form", "材料编号"))
        self.tableWidget.item(0, 1).setText(_translate("Form", "名称"))
        self.tableWidget.item(0, 2).setText(_translate("Form", "规格"))
        self.tableWidget.item(0, 3).setText(_translate("Form", "单位"))
        '''
        '''
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "规格"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "单位"))
        '''

        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_5.setText(_translate("Form", "插入"))
        self.pushButton.setText(_translate("Form", "刷新"))



       
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
                self.tableWidget.setCellWidget(i, len(item), self.buttonForRow(item[0]) )
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




    def buttonForRow(self,id):
        widget=QWidget()
        # 修改
        
        #updateBtn = QPushButton('修改')
        #updateBtn.setStyleSheet(''' text-align : center;
        #                                    background-color : NavajoWhite;
        #                                    height : 30px;
        #                                    border-style: outset;
        #                                   font : 13px  ''')
 

        #updateBtn.clicked.connect()
         # 查看
        #viewBtn = QPushButton('查看')
        #viewBtn.setStyleSheet(''' text-align : center;
        #                          background-color : DarkSeaGreen;
        #                           height : 30px;
        #                           border-style: outset;
        #                           font : 13px; ''')


 
         # 删除
        deleteBtn = QPushButton('删除')
        deleteBtn.setStyleSheet(''' text-align : center;
                                     background-color : LightCoral;
                                     height : 30px;
                                     border-style: outset;
                                     font : 13px; ''')
        #deleteBtn.clicked.connect(self.handle_delete(id))
 
        hLayout = QHBoxLayout()
        #hLayout.addWidget(updateBtn)
        #hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)
        return widget