from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QMenuBar, QStatusBar, QApplication, \
    QMainWindow
import ChrisCalcUI as cc



# setupUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = cc.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())






