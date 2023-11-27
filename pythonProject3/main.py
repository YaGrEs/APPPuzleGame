import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QDialog, QGraphicsScene, QGraphicsView, QHBoxLayout
import random
from PyQt6 import uic

from main_dialog import Ui_Dialog
from first_task import Ui_Form

class First(QWidget):
    def __init__(self):
        super().__init__()
        self.f = Ui_Form()
        self.f.setupUi(self)
        self.show()
class start(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.result)
        self.show()
    def result(self):
        self.ff = First()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = start()
    sys.exit(app.exec())