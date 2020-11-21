
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from home1 import * 
from PyQt5.QtCore import QObject , pyqtSignal
from cailiao import *
from gonghuodanwei import *
from kucun import *
from ruku import *
from chuku import *
from fuzhang import *
from fuzeren import *
from cailiao_luru import *
from gonghuodanwei_luru import *
from fuzeren_luru import *
from chuku_luru import *
from ruku_luru import *
from fuzhang_luru import *
from querytable_cailiao import *
from querytable_gonghuodanwei import *
from querytable_kucun import *
from querytable_chuku import *
from querytable_ruku import *
from querytable_fuzhang import *
from querytable_fuzeren import *
from querytable_weifu import *
from denglu import *


class MyWindow0(QMainWindow, Ui_MainWindow0):
    def __init__(self, parent=None):
        super(MyWindow0, self).__init__(parent)
        self.setupUi(self)
        

class MyWindow1(QMainWindow, Ui_MainWindow1):
    def __init__(self, parent=None):
        super(MyWindow1, self).__init__(parent)
        self.setupUi(self)


class MyWindow2(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None):
        super(MyWindow2, self).__init__(parent)
        self.setupUi(self)


class MyWindow3(QMainWindow, Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyWindow3, self).__init__(parent)
        self.setupUi(self)


class MyWindow4(QMainWindow, Ui_MainWindow4):
    def __init__(self, parent=None):
        super(MyWindow4, self).__init__(parent)
        self.setupUi(self)


class MyWindow5(QMainWindow, Ui_MainWindow5):
    def __init__(self, parent=None):
        super(MyWindow5, self).__init__(parent)
        self.setupUi(self)


class MyWindow6(QMainWindow, Ui_MainWindow6):
    def __init__(self, parent=None):
        super(MyWindow6, self).__init__(parent)
        self.setupUi(self)


class MyWindow7(QMainWindow, Ui_MainWindow7):
    def __init__(self, parent=None):
        super(MyWindow7, self).__init__(parent)
        self.setupUi(self)


class MyWindow1_2(QMainWindow, Ui_MainWindow1_2):
    def __init__(self, parent=None):
        super(MyWindow1_2, self).__init__(parent)
        self.setupUi(self)


class MyWindow2_2(QMainWindow, Ui_MainWindow2_2):
    def __init__(self, parent=None):
        super(MyWindow2_2, self).__init__(parent)
        self.setupUi(self)


class MyWindow4_2(QMainWindow, Ui_MainWindow4_2):
    def __init__(self, parent=None):
        super(MyWindow4_2, self).__init__(parent)
        self.setupUi(self)


class MyWindow5_2(QMainWindow, Ui_MainWindow5_2):
    def __init__(self, parent=None):
        super(MyWindow5_2, self).__init__(parent)
        self.setupUi(self)


class MyWindow6_2(QMainWindow, Ui_MainWindow6_2):
    def __init__(self, parent=None):
        super(MyWindow6_2, self).__init__(parent)
        self.setupUi(self)


class MyWindow7_2(QMainWindow, Ui_MainWindow7_2):
    def __init__(self, parent=None):
        super(MyWindow7_2, self).__init__(parent)
        self.setupUi(self)


class MyWindow_denglu(QMainWindow, Ui_MainWindow_denglu):
    def __init__(self, parent=None):
        super(MyWindow_denglu, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    home_page = MyWindow0()
    cailiao_page = MyWindow1()
    cailiao_chaxun_page = TableWidgetContextMenu1_1()
    cailiao_luru_page = MyWindow1_2()
    gonghuodanwei_page = MyWindow2()
    gonghuodanwei_chaxun_page = TableWidgetContextMenu2_1()
    gonghuodanwei_luru_page = MyWindow2_2()
    kucun_page = MyWindow3()
    kuncun_chaxun_page = TableWidgetContextMenu3_1()
    ruku_page = MyWindow4()
    ruku_chaxun_page = TableWidgetContextMenu4_1()
    ruku_luru_page = MyWindow4_2()
    chuku_page = MyWindow5()
    chuku_chaxun_page = TableWidgetContextMenu5_1()
    chuku_luru_page = MyWindow5_2()
    fuzhang_page = MyWindow6()
    fuzhang_chaxun_page = TableWidgetContextMenu6_1()
    fuzhang_luru_page = MyWindow6_2()
    fuzeren_page = MyWindow7()
    fuzeren_chaxun_page = TableWidgetContextMenu7_1()
    fuzeren_luru_page = MyWindow7_2()

    weifuzhang_chaxun_page = TableWidgetContextMenu8_1()

    denglu_page = MyWindow_denglu()

    denglu_page.pushButton.clicked.connect(denglu_page.handle_denglu)
    denglu_page.signal1.connect(home_page.handle_click)

    home_page.pushButton1.clicked.connect(cailiao_page.handle_click)
    home_page.pushButton2.clicked.connect(gonghuodanwei_page.handle_click)
    home_page.pushButton3.clicked.connect(kucun_page.handle_click)
    home_page.pushButton4.clicked.connect(ruku_page.handle_click)
    home_page.pushButton5.clicked.connect(chuku_page.handle_click)
    home_page.pushButton6.clicked.connect(fuzhang_page.handle_click)
    home_page.pushButton7.clicked.connect(fuzeren_page.handle_click)
    home_page.pushButton8.clicked.connect(weifuzhang_chaxun_page.handle_click)

    cailiao_page.pushButton1.clicked.connect(cailiao_chaxun_page.handle_click)
    cailiao_page.pushButton2.clicked.connect(cailiao_luru_page.handle_click)
    cailiao_page.pushButton3.clicked.connect(cailiao_page.handle_back)
    cailiao_luru_page.pushButton.clicked.connect(cailiao_luru_page.handle_luru)
    cailiao_luru_page.pushButton2.clicked.connect(cailiao_luru_page.handle_excel_luru)
    cailiao_luru_page.pushButton2.clicked.connect(cailiao_chaxun_page.handle_click)
    cailiao_luru_page.pushButton2.clicked.connect(cailiao_chaxun_page.handle_flush)
    cailiao_luru_page.pushButton3.clicked.connect(cailiao_luru_page.click_back)

    gonghuodanwei_page.pushButton1.clicked.connect(gonghuodanwei_chaxun_page.handle_click)
    gonghuodanwei_page.pushButton2.clicked.connect(gonghuodanwei_luru_page.handle_click)
    gonghuodanwei_page.pushButton3.clicked.connect(gonghuodanwei_page.handle_back)
    gonghuodanwei_luru_page.pushButton.clicked.connect(gonghuodanwei_luru_page.handle_luru)
    gonghuodanwei_luru_page.pushButton2.clicked.connect(gonghuodanwei_luru_page.click_back)
    gonghuodanwei_luru_page.pushButton3.clicked.connect(gonghuodanwei_luru_page.handle_excel_luru)
    gonghuodanwei_luru_page.pushButton3.clicked.connect(gonghuodanwei_chaxun_page.handle_click)
    gonghuodanwei_luru_page.pushButton3.clicked.connect(gonghuodanwei_chaxun_page.handle_flush)

    kucun_page.pushButton1.clicked.connect(kuncun_chaxun_page.handle_click)
    kucun_page.pushButton3.clicked.connect(kucun_page.handle_back)

    ruku_page.pushButton1.clicked.connect(ruku_chaxun_page.handle_click)
    ruku_page.pushButton2.clicked.connect(ruku_luru_page.handle_click)
    ruku_page.pushButton3.clicked.connect(ruku_page.handle_back)
    ruku_luru_page.pushButton.clicked.connect(ruku_luru_page.handle_luru)
    ruku_luru_page.pushButton2.clicked.connect(ruku_luru_page.click_back)

    chuku_page.pushButton1.clicked.connect(chuku_chaxun_page.handle_click)
    chuku_page.pushButton2.clicked.connect(chuku_luru_page.handle_click)
    chuku_page.pushButton3.clicked.connect(chuku_page.handle_back)
    chuku_luru_page.pushButton.clicked.connect(chuku_luru_page.handle_luru)
    chuku_luru_page.pushButton2.clicked.connect(chuku_luru_page.click_back)

    fuzhang_page.pushButton1.clicked.connect(fuzhang_chaxun_page.handle_click)
    fuzhang_page.pushButton2.clicked.connect(fuzhang_luru_page.handle_click)
    fuzhang_page.pushButton3.clicked.connect(fuzhang_page.handle_back)
    fuzhang_luru_page.pushButton.clicked.connect(fuzhang_luru_page.handle_luru)
    fuzhang_luru_page.pushButton2.clicked.connect(fuzhang_luru_page.click_back)

    fuzeren_page.pushButton1.clicked.connect(fuzeren_chaxun_page.handle_click)
    fuzeren_page.pushButton2.clicked.connect(fuzeren_luru_page.handle_click)
    fuzeren_page.pushButton3.clicked.connect(fuzeren_page.handle_back)
    fuzeren_luru_page.pushButton.clicked.connect(fuzeren_luru_page.handle_luru)
    fuzeren_luru_page.pushButton2.clicked.connect(fuzeren_luru_page.click_back)
    fuzeren_luru_page.pushButton3.clicked.connect(fuzeren_luru_page.handle_excel_luru)
    fuzeren_luru_page.pushButton3.clicked.connect(fuzeren_chaxun_page.handle_click)
    fuzeren_luru_page.pushButton3.clicked.connect(fuzeren_chaxun_page.handle_flush)

    denglu_page.show()
    sys.exit(app.exec_())
