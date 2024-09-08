import sys
import PyQt5
from PyQt5.QtWidgets import *
from UiPy import Ui_MainWindow


app = QApplication(sys.argv)
Main = QMainWindow()
ex = Ui_MainWindow()
ex.setupUi(Main)
Main.show()


# Build common functions
def run():
    if ex.radioButton.isChecked():
        ex.graphicsView.clear()
        ex.graphicsView.plot([i  for i in range(10)], [i ** 0.5 for i in range(10)], pen='r')
    elif ex.radioButton_2.isChecked():
        ex.graphicsView.clear()
        ex.graphicsView.plot([i for i in range(10)], [i for i in range(10)], pen='g')
    elif ex.radioButton_3.isChecked():
        ex.graphicsView.clear()
        ex.graphicsView.plot([i for i in range(10)], [i ** 2 for i in range(10)], pen='b')
    elif ex.radioButton_4.isChecked():
        ex.graphicsView.clear()
        ex.graphicsView.plot([i for i in range(10)], [i ** 3 for i in range(10)], pen='w')


# Build of the "super" functions
def build_q_func():
    a = float(ex.lineEdit.text())
    b = float(ex.lineEdit_2.text())
    c = float(ex.lineEdit_3.text())
    ex.graphicsView.clear()
    ex.graphicsView.plot([i for i in range(10)], [i ** 2 * a + b * i + c for i in range(10)], pen='r')


def build_l_func():
    k = float(ex.lineEdit_6.text())
    b = float(ex.lineEdit_4.text())
    ex.graphicsView.clear()
    ex.graphicsView.plot([i for i in range(10)], [k * i + b for i in range(10)], pen='r')

        
def build_r_func():
    m = float(ex.lineEdit_7.text())
    n = float(ex.lineEdit_5.text())
    ex.graphicsView.clear()
    ex.graphicsView.plot([i for i in range(10)], [(i + m) ** 0.5 + n for i in range(10)], pen='r')


# buttons of building of the simple functions
ex.radioButton.clicked.connect(run)
ex.radioButton_2.clicked.connect(run)
ex.radioButton_3.clicked.connect(run)
ex.radioButton_4.clicked.connect(run)

# buttons of building of the "super" functions
ex.pushButton.clicked.connect(build_q_func)
ex.pushButton_2.clicked.connect(build_l_func)
ex.pushButton_3.clicked.connect(build_r_func)

sys.exit(app.exec_())
