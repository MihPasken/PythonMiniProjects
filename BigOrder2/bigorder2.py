import sys

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QPlainTextEdit

main_arr = ['Чизбургер', 'Гамбургер', 'Кока - кола', 'Нагетсы']
price_arr = [100, 150, 50, 125]
summ_arr = list()
count_arr = list()

hamburgers = 0
cheeseburgers = 0
cocacola = 0
negets = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('bigord2.ui', self)
        self.pushButton.clicked.connect(lambda: self.btn_clk(self.checkBox.isChecked(), self.checkBox_2.isChecked(), self.checkBox_3.isChecked(), self.checkBox_4.isChecked()))

        self.checkBox.clicked.connect(self.upload)
        self.checkBox_2.clicked.connect(self.upload_2)
        self.checkBox_3.clicked.connect(self.upload_3)
        self.checkBox_4.clicked.connect(self.upload_4)

    def btn_clk(self, *status):
        print(status)
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText('Ваш заказ: ')
        self.plainTextEdit.appendPlainText('')
        
        count_arr.append(int(self.lineEdit.text()))
        count_arr.append(int(self.lineEdit_2.text()))
        count_arr.append(int(self.lineEdit_3.text()))
        count_arr.append(int(self.lineEdit_4.text()))
        
        print(count_arr)
        for i in range(4):
            if status[i] == True:
                string = str(main_arr[i]) + '-----' + str(count_arr[i]) + '-----' + str(price_arr[i] * count_arr[i])
                self.plainTextEdit.appendPlainText(string)
                summ_arr.append(price_arr[i] * count_arr[i])
            else:
                pass

        self.plainTextEdit.appendPlainText('')
        self.plainTextEdit.appendPlainText('Итого: {}'.format(sum(summ_arr)))
        count_arr.clear()
        summ_arr.clear()
    
    def upload(self):
        if self.checkBox.isChecked():
            cheeseburgers = 1
            self.lineEdit.setEnabled(True)
            self.lineEdit.setText(str(cheeseburgers))
        else:
            self.lineEdit.setEnabled(False)
            self.lineEdit.setText('0')
            
    def upload_2(self):
        if self.checkBox_2.isChecked():
            hamburgers = 1
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_2.setText(str(hamburgers))
        else:
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_2.setText('0')
            
    def upload_3(self):
        if self.checkBox_3.isChecked():
            cocacola = 1
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_3.setText(str(cocacola))
        else:
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_3.setText('0')
            
    def upload_4(self):
        if self.checkBox_4.isChecked():
            negets = 1
            self.lineEdit_4.setEnabled(True)
            self.lineEdit_4.setText(str(1))
        else:
            self.lineEdit_4.setEnabled(False)
            self.lineEdit_4.setText('0')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_()) 