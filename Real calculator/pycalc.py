import sys

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QPlainTextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('calc.ui', self)
        self.screen = ''
        self.data = ''
        for i in self.buttonGroup_digits.buttons():
            i.clicked.connect(self.run)
        self.btn_clear.clicked.connect(self.clear)
        for i in self.buttonGroup_binary.buttons():
            i.clicked.connect(self.operation)
        self.btn_eq.clicked.connect(self.result)
         
         
    def clear(self):
        self.screen = ''
        self.data = ''
        self.table.display(0)
         
    def run(self):
        # print(self.sender().text())
        if self.data and self.data[-1].isdigit():
            self.screen += self.sender().text()
                ##   print("kk", self.screen)
        else:
            self.screen = self.sender().text()
            self.data += self.sender().text()
            print(self.data)
            self.table.display(int(self.screen))
         
    def operation(self):
        # print(self.sender().text())
        if self.data and self.data[-1].isdigit():
            self.data += self.sender().text()
        elif self.data[-1] in '+-*/':
            self.data = self.data[:-1] + self.sender().text()
        print(self.data)
         
    def result(self):
        # print(eval(self.data))
        self.screen = str(eval(self.data))
        self.data = str(self.screen)
        #  print('result', self.screen, self.data)
        self.table.display(float(self.screen))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_()) 