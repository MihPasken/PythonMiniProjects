# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'antiplag.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_1.setGeometry(QtCore.QRect(38, 130, 431, 401))
        self.text_1.setObjectName("text_1")
        self.text_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(488, 130, 431, 401))
        self.text_2.setObjectName("text_2")
        self.about_text1 = QtWidgets.QLabel(self.centralwidget)
        self.about_text1.setGeometry(QtCore.QRect(38, 100, 55, 16))
        self.about_text1.setObjectName("about_text1")
        self.about_text2 = QtWidgets.QLabel(self.centralwidget)
        self.about_text2.setGeometry(QtCore.QRect(488, 100, 55, 16))
        self.about_text2.setObjectName("about_text2")
        self.checkproc = QtWidgets.QLabel(self.centralwidget)
        self.checkproc.setGeometry(QtCore.QRect(38, 50, 161, 20))
        self.checkproc.setObjectName("checkproc")
        self.spincount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spincount.setGeometry(QtCore.QRect(198, 50, 721, 22))
        self.spincount.setObjectName("spincount")
        self.res_button = QtWidgets.QPushButton(self.centralwidget)
        self.res_button.setGeometry(QtCore.QRect(40, 550, 881, 28))
        self.res_button.setObjectName("res_button")
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(40, 580, 881, 20))
        self.resultat.setObjectName("resultat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.about_text1.setText(_translate("MainWindow", "Текст 1"))
        self.about_text2.setText(_translate("MainWindow", "Текст 2"))
        self.checkproc.setText(_translate("MainWindow", "Порог срабатывания (%)"))
        self.res_button.setText(_translate("MainWindow", "Сравнить"))
        self.resultat.setText(_translate("MainWindow", "TextLabel"))
