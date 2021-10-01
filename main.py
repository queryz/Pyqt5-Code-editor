###################
##
##  BY : QUERYZ <queryzram@gmail.com>
##  VERSION : 1.0.0
##  CREATED WITH: PYQT5
##
###################


import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5 import Qt

from ui_main import Ui_MainWindow 
from functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.menu.setFixedWidth(0)        

        self.ui.code.setFont(QtGui.QFont('CeraPro-Bold', 24))

        windowIcon = QtGui.QIcon()
        windowIcon.addPixmap(QtGui.QPixmap("./icons/icon.png"))
        self.ui.btn_settings.setIcon(windowIcon)
        self.setWindowIcon(windowIcon)

        # SCROLL BAR
        self.ui.code.verticalScrollBar().valueChanged.connect(lambda : Functions.scroll_change_value(self))

        # SET BTNS ICONS
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icons/menu.png"))
        self.ui.btn_menu.setIcon(icon)
        self.ui.btn_menu.setIconSize(QtCore.QSize(32, 32))

        icon.addPixmap(QtGui.QPixmap("./icons/home.png"))
        self.ui.btn_home.setIcon(icon)
        self.ui.btn_home.setIconSize(QtCore.QSize(32, 32))

        icon.addPixmap(QtGui.QPixmap("./icons/profile.png"))
        self.ui.btn_profile.setIcon(icon)
        self.ui.btn_profile.setIconSize(QtCore.QSize(32, 32))

        icon.addPixmap(QtGui.QPixmap("./icons/coding.png"))
        self.ui.btn_code.setIcon(icon)
        self.ui.btn_code.setIconSize(QtCore.QSize(32, 32))

        icon.addPixmap(QtGui.QPixmap("./icons/settings.png"))
        self.ui.btn_settings.setIcon(icon)
        self.ui.btn_settings.setIconSize(QtCore.QSize(32, 32))

        # CLOSE/OPEN MENU
        self.ui.btn_menu.clicked.connect(lambda : Functions.click_menu(self, self.ui.menu.width()))
        
        # CODE 
        self.ui.nums.setReadOnly(True)
        self.ui.code.installEventFilter(self)
    
        # CHANGE PAGES
        self.ui.btn_home.clicked.connect(lambda : Functions.change_page(self, 0))
        self.ui.btn_profile.clicked.connect(lambda : Functions.change_page(self, 1))
        self.ui.btn_code.clicked.connect(lambda : Functions.change_page(self, 2))
        self.ui.btn_settings.clicked.connect(lambda : Functions.change_page(self, 3))

        ###############################
        # SHOW MAIN WINDOW
        self.show()

    # NUMBERING
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.ui.code:
            if event.key() == QtCore.Qt.Key_Return and self.ui.code.hasFocus() and event.key() == 16777220:
                self.text = self.ui.nums.toPlainText()
                self.list_nums = self.text.split()
                self.last_num = int(self.list_nums[len(self.list_nums) - 1])
                self.strokes = self.ui.code.toPlainText().split("\n")
                self.num = len(self.strokes) + 1

                if self.last_num <= 9:
                    self.ui.nums.setText(self.text + f"\n{self.num}")
                elif self.last_num >= 10 and self.last_num <= 99:
                    self.ui.nums.setMaximumWidth(30)
                    self.ui.nums.setText(self.text + f"\n{self.num}")     
                elif self.last_num >= 100 and self.last_num <= 999:
                    self.ui.nums.setMaximumWidth(40)
                    self.ui.nums.setText(self.text + f"\n{self.num}")    
                elif self.last_num >= 1000 and self.last_num <= 9999:
                    self.ui.nums.setMaximumWidth(50)
                    self.ui.nums.setText(self.text + f"\n{self.num}")   
                elif self.last_num >= 10000 and self.last_num <= 99999:
                    self.ui.nums.setMaximumWidth(60)
                    self.ui.nums.setText(self.text + f"\n{self.num}")   
                elif self.last_num >= 100000 and self.last_num <= 999999:
                    self.ui.nums.setMaximumWidth(70)
                    self.ui.nums.setText(self.text + f"\n{self.num}")   
                elif self.last_num >= 1000000 and self.last_num <= 9999999:
                    self.ui.nums.setMaximumWidth(80)
                    self.ui.nums.setText(self.text + f"\n{self.num}")   

            if event.key() == 16777219 and self.ui.code.hasFocus():
                self.text = self.ui.nums.toPlainText()
                self.list_nums = self.text.split() 
                self.list_strokes = self.ui.code.toPlainText().split("\n")
                self.last_stroke = self.list_strokes[len(self.list_strokes) - 1]
                self.strokes = len(self.list_strokes)

                if self.list_nums[-1] == "1" or self.list_nums[-1] == 1:
                    return False
                elif self.strokes == int(self.list_nums[-1]) and self.list_nums[-1] != 1 or self.list_nums[-1] != "1" and self.last_stroke == None or self.last_stroke == "":
                    del self.list_nums[-1]
                    self.need_text = " ".join(self.list_nums)
                    self.ui.nums.setText(self.need_text)            
                else:
                    pass

            else:
                pass

        return super().eventFilter(obj, event)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
