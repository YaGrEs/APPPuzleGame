import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox, QDialog, QGraphicsScene, QGraphicsView, QHBoxLayout, \
    QDialogButtonBox
import random
from PyQt6 import uic, QtCore
from PyQt6.QtGui import QCloseEvent

from main_dialog import Ui_Dialog
from first_task import Ui_Form
from second_task import Ui_Form2
from third_task import Ui_Form3


class Third(QWidget):
    def __init__(self):
        super().__init__()
        self.f3 = Ui_Form3()
        self.f3.setupUi(self)
        self.f3.ans.clicked.connect(self.answerbutton)
        self.show()

    def answerbutton(self, event: QCloseEvent):
        if str(self.f3.textEdit.toPlainText()) == self.f3.answer3.text():
            dlg = QMessageBox(self)
            dlg.setWindowTitle("CONGRATULATIONS!")
            dlg.setText("YOU ARE WINNER")
            dlg.exec()
            event.accept()


        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("SORRY!")
            dlg.setText("THIS IS NOT CORRECT")
            dlg.exec()
            event.accept()




class Second(QWidget):
    def __init__(self):
        super().__init__()
        self.f2 = Ui_Form2()
        self.f2.setupUi(self)
        self.f2.Right.clicked.connect(self.Rbutton)
        self.f2.Left.clicked.connect(self.Lbutton)
        self.show()

    def Rbutton(self, event: QCloseEvent):
        check2 = self.f2.answer2.text()
        if check2 == 'R':
            self.tt = Third()
            self.setVisible(False)
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("SORRY!")
            dlg.setText("THIS IS NOT CORRECT")
            dlg.exec()
            event.accept()

    def Lbutton(self, event: QCloseEvent):
        check2 = self.f2.answer2.text()
        if check2 == 'L':
            self.tt = Third()
            self.setVisible(False)
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("SORRY!")
            dlg.setText("THIS IS NOT CORRECT")
            dlg.exec()
            event.accept()


class First(QWidget):
    def __init__(self):
        super().__init__()
        self.f = Ui_Form()
        self.f.setupUi(self)
        self.f.Yes.clicked.connect(self.YesButton)
        self.f.No.clicked.connect(self.NoButton)
        self.show()
    def YesButton(self, event: QCloseEvent):
        check = self.f.answer.text()
        if check == '1':
            self.st = Second()
            self.setVisible(False)
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("SORRY!")
            dlg.setText("THIS IS NOT CORRECT")
            dlg.exec()
            event.accept()
    def NoButton(self, event: QCloseEvent):
        check = self.f.answer.text()
        if check == '1':
            dlg = QMessageBox(self)
            dlg.setWindowTitle("PERFECT!")
            dlg.setText("THIS IS NOT CORRECT")
            dlg.exec()
            event.accept()
        else:
            self.st = Second()
            self.setVisible(False)

class start(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.result)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(27000)
        self.show()
    def result(self):
        self.timer.start()
        self.timer.timeout.connect(self.on_timeout)
        self.ff = First()
        self.setVisible(False)

    def on_timeout(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("SORRY!")
        dlg.setText("Time is over!")
        dlg.exec()
        a = QCloseEvent
        self.cls(a)
    def cls(self, event):
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = start()
    sys.exit(app.exec())