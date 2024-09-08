import sys
import difflib

# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('antiplag.ui', self)
        self.res_button.clicked.connect(self.compare)
        
    def compare(self):
        
        if float(self.spincount.text().replace(',', '.')) <= round(difflib.SequenceMatcher(None, self.text_1.toPlainText().lower(), self.text_2.toPlainText().lower()).ratio() * 100, 2):
            self.resultat.setStyleSheet("background-color: rgb(255, 0, 0)")
            self.resultat.setText('Код похож на {} %'.format((str(round(difflib.SequenceMatcher(None, self.text_1.toPlainText().lower(), self.text_2.toPlainText().lower()).ratio() * 100, 2)))))
        else:
            self.resultat.setStyleSheet("background-color: rgb(0, 128, 0)")
            self.resultat.setText('Код похож на {} %'.format((str(round(difflib.SequenceMatcher(None, self.text_1.toPlainText().lower(), self.text_2.toPlainText().lower()).ratio() * 100, 2)))))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=MainWindow()
    ex.show()
    sys.exit(app.exec_())
