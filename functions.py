###################
##
##  BY : QUERYZ <queryzram@gmail.com>
##  VERSION : 1.0.0
##  CREATED BY : PYQT5
##
###################


from PyQt5.QtCore import QPropertyAnimation
from main import MainWindow


class Functions(MainWindow):
    # TOGLE/OPEN MENU
    def click_menu(self, width):
        if width == 0:
            end_width = 46

            # ANIMATION 
            self.animation = QPropertyAnimation(self.ui.menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(end_width)
            self.animation.start()
        elif width == 46:
            end_width = 0

            # ANIMATION 
            self.animation = QPropertyAnimation(self.ui.menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(end_width)
            self.animation.start()            
    
    # CHANGE PAGES 
    def change_page(self, index):
        self.ui.stackedWidget.setCurrentIndex(int(index))

    # SCROLL'S VALUE CHANGED
    def scroll_change_value(self):        
        self.ui.nums.verticalScrollBar().setValue(self.ui.code.verticalScrollBar().value())