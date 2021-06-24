import sys
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect
from PyQt5.QtWidgets import QWidget, QLabel, QApplication,QLineEdit,QGridLayout,QPushButton,QMenuBar,QStatusBar,QMainWindow
from PyQt5.uic.properties import QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(241, 238)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 110, 221, 31))

        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)

        self.btn_4 = QPushButton(self.layoutWidget)
        self.btn_4.setObjectName(u"btn_4")
        self.gridLayout_3.addWidget(self.btn_4, 0, 0, 1, 1)

        self.btn_5 = QPushButton(self.layoutWidget)
        self.btn_5.setObjectName(u"btn_5")
        self.gridLayout_3.addWidget(self.btn_5, 0, 1, 1, 1)

        self.btn_6 = QPushButton(self.layoutWidget)
        self.btn_6.setObjectName(u"btn_6")
        self.gridLayout_3.addWidget(self.btn_6, 0, 2, 1, 1)

        self.sub_btn = QPushButton(self.layoutWidget)
        self.sub_btn.setObjectName(u"sub_btn")
        self.gridLayout_3.addWidget(self.sub_btn, 0, 3, 1, 1)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 140, 221, 31))
        self.gridLayout_4 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)

        self.btn_1 = QPushButton(self.layoutWidget_2)
        self.btn_1.setObjectName(u"btn_1")
        self.gridLayout_4.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_2 = QPushButton(self.layoutWidget_2)
        self.btn_2.setObjectName(u"btn_2")
        self.gridLayout_4.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QPushButton(self.layoutWidget_2)
        self.btn_3.setObjectName(u"btn_3")
        self.gridLayout_4.addWidget(self.btn_3, 0, 2, 1, 1)

        self.mult_btn = QPushButton(self.layoutWidget_2)
        self.mult_btn.setObjectName(u"mult_btn")
        self.gridLayout_4.addWidget(self.mult_btn, 0, 3, 1, 1)

        self.layoutWidget_3 = QWidget(self.centralwidget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 170, 221, 31))

        self.gridLayout_5 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)

        self.dec_btn = QPushButton(self.layoutWidget_3)
        self.dec_btn.setObjectName(u"dec_btn")
        self.gridLayout_5.addWidget(self.dec_btn, 0, 1, 1, 1)

        self.divd_btn = QPushButton(self.layoutWidget_3)
        self.divd_btn.setObjectName(u"divd_btn")
        self.gridLayout_5.addWidget(self.divd_btn, 0, 2, 1, 1)

        self.btn_0 = QPushButton(self.layoutWidget_3)
        self.btn_0.setObjectName(u"btn_0")
        self.gridLayout_5.addWidget(self.btn_0, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 221, 51))

        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 2)

        self.clear_btn = QPushButton(self.widget)
        self.clear_btn.setObjectName(u"clear_btn")
        self.gridLayout.addWidget(self.clear_btn, 1, 0, 1, 1)

        self.enter_btn = QPushButton(self.widget)
        self.enter_btn.setObjectName(u"enter_btn")
        self.gridLayout.addWidget(self.enter_btn, 1, 1, 1, 1)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 80, 221, 31))

        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.btn_7 = QPushButton(self.widget1)
        self.btn_7.setObjectName(u"btn_7")
        self.gridLayout_2.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_8 = QPushButton(self.widget1)
        self.btn_8.setObjectName(u"btn_8")
        self.gridLayout_2.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_9 = QPushButton(self.widget1)
        self.btn_9.setObjectName(u"btn_9")
        self.gridLayout_2.addWidget(self.btn_9, 0, 2, 1, 1)

        self.plus_btn = QPushButton(self.widget1)
        self.plus_btn.setObjectName(u"plus_btn")
        self.gridLayout_2.addWidget(self.plus_btn, 0, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 241, 21))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.clear_btn.clicked.connect(self.lineEdit.clear)
        self.btn_0.clicked.connect(self.clicked_on_0)
        self.btn_1.clicked.connect(self.clicked_on_1)
        self.btn_2.clicked.connect(self.clicked_on_2)
        self.btn_3.clicked.connect(self.clicked_on_3)
        self.btn_4.clicked.connect(self.clicked_on_4)
        self.btn_5.clicked.connect(self.clicked_on_5)
        self.btn_6.clicked.connect(self.clicked_on_6)
        self.btn_7.clicked.connect(self.clicked_on_7)
        self.btn_8.clicked.connect(self.clicked_on_8)
        self.btn_9.clicked.connect(self.clicked_on_9)

        self.dec_btn.clicked.connect(self.clicked_on_dec)

        self.plus_btn.clicked.connect(self.clicked_on_plus)
        self.sub_btn.clicked.connect(self.clicked_on_sub)
        self.mult_btn.clicked.connect(self.clicked_on_mult)
        self.divd_btn.clicked.connect(self.clicked_on_divd)
        self.enter_btn.clicked.connect(self.clicked_on_Enter)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chris' Calc", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.sub_btn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.mult_btn.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.dec_btn.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.divd_btn.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.enter_btn.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.plus_btn.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi
        QMetaObject.connectSlotsByName(MainWindow)


    def clicked_on_0(self):
        current_text = self.lineEdit.text()
        text = current_text + "0"
        self.lineEdit.setText(text)
    def clicked_on_1(self):
        current_text = self.lineEdit.text()
        text = current_text + "1"
        self.lineEdit.setText(text)
    def clicked_on_2(self):
        current_text = self.lineEdit.text()
        text = current_text + "2"
        self.lineEdit.setText(text)
    def clicked_on_3(self):
        current_text = self.lineEdit.text()
        text = current_text + "3"
        self.lineEdit.setText(text)
    def clicked_on_4(self):
        current_text = self.lineEdit.text()
        text = current_text + "4"
        self.lineEdit.setText(text)
    def clicked_on_5(self):
        current_text = self.lineEdit.text()
        text = current_text + "5"
        self.lineEdit.setText(text)
    def clicked_on_6(self):
        current_text = self.lineEdit.text()
        text = current_text + "6"
        self.lineEdit.setText(text)
    def clicked_on_7(self):
        current_text = self.lineEdit.text()
        text = current_text + "7"
        self.lineEdit.setText(text)
    def clicked_on_8(self):
        current_text = self.lineEdit.text()
        text = current_text + "8"
        self.lineEdit.setText(text)
    def clicked_on_9(self):
        current_text = self.lineEdit.text()
        text = current_text + "9"
        self.lineEdit.setText(text)

    def clicked_on_dec(self):
        current_text = self.lineEdit.text()
        text = current_text + "."
        self.lineEdit.setText(text)

    def clicked_on_plus(self):
        current_text = self.lineEdit.text()
        text = current_text + "+"
        self.lineEdit.setText(text)
    def clicked_on_sub(self):
        current_text = self.lineEdit.text()
        text = current_text + "-"
        self.lineEdit.setText(text)
    def clicked_on_divd(self):
        current_text = self.lineEdit.text()
        text = current_text + "/"
        self.lineEdit.setText(text)
    def clicked_on_mult(self):
        current_text = self.lineEdit.text()
        text = current_text + "*"
        self.lineEdit.setText(text)
    def clicked_on_Enter(self):

        try:
            full_line = self.lineEdit.text()
            total_string = len(full_line)

            for i in range(len(full_line)):
                if full_line[i] == "+" or full_line[i] == "-" or full_line[i] == "*" or full_line[i] == "/":
                    operator_pos = i
            var1 = float(full_line[0:operator_pos])
            var2 = float(full_line[operator_pos + 1:total_string])
            if full_line[operator_pos] == "+":
                var3 = var1 + var2
            elif full_line[operator_pos] == "-":
                var3 = var1 - var2
            elif full_line[operator_pos] == "*":
                var3 = var1 * var2
            elif full_line[operator_pos] == "/":
                var3 = var1 / var2
            round(var3, 2)
            self.lineEdit.setText(str(var3))
        except:
            self.lineEdit.setText("Error")





