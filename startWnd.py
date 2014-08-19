# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWnd.ui'
#
# Created: Mon Aug 18 15:59:10 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartForm(object):
    def setupUi(self, StartForm):
        StartForm.setObjectName("StartForm")
        StartForm.resize(604, 402)
        self.label = QtWidgets.QLabel(StartForm)
        self.label.setGeometry(QtCore.QRect(-30, -90, 641, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/desktopwallpapers.org.ua-2725.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StartForm)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 601, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(StartForm)
        self.label_3.setGeometry(QtCore.QRect(0, 40, 601, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(StartForm)
        self.label_5.setGeometry(QtCore.QRect(110, 170, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.edDiff = QtWidgets.QLineEdit(StartForm)
        self.edDiff.setGeometry(QtCore.QRect(410, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edDiff.setFont(font)
        self.edDiff.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}")
        self.edDiff.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edDiff.setObjectName("edDiff")
        self.edCount = QtWidgets.QLineEdit(StartForm)
        self.edCount.setGeometry(QtCore.QRect(410, 250, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.edCount.setFont(font)
        self.edCount.setStyleSheet("QLineEdit {\n"
"    background-color: rgba(23, 115, 255, 137);\n"
"    border-width: 1px;\n"
"color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 255, 255);\n"
"     border-style: solid;\n"
"     border-radius: 5px;\n"
"}")
        self.edCount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edCount.setObjectName("edCount")
        self.label_6 = QtWidgets.QLabel(StartForm)
        self.label_6.setGeometry(QtCore.QRect(110, 240, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pbStart = QtWidgets.QPushButton(StartForm)
        self.pbStart.setGeometry(QtCore.QRect(310, 330, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbStart.setFont(font)
        self.pbStart.setStyleSheet("QPushButton {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(82, 100, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.596154 rgba(85, 250, 255, 255), stop:1 rgba(190, 255, 255, 255));\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/apply_5183.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbStart.setIcon(icon)
        self.pbStart.setIconSize(QtCore.QSize(24, 24))
        self.pbStart.setObjectName("pbStart")
        self.pbExit = QtWidgets.QPushButton(StartForm)
        self.pbExit.setGeometry(QtCore.QRect(90, 330, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbExit.setFont(font)
        self.pbExit.setStyleSheet("QPushButton {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(0, 29, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"    color:rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"     border-style: solid;\n"
"     border-radius: 10px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.655502 rgba(82, 100, 203, 255), stop:1 rgba(190, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:qlineargradient(spread:reflect, x1:0.515, y1:1, x2:0.528, y2:0, stop:0 rgba(0, 143, 250, 255), stop:0.596154 rgba(85, 250, 255, 255), stop:1 rgba(190, 255, 255, 255));\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbExit.setIcon(icon1)
        self.pbExit.setIconSize(QtCore.QSize(24, 24))
        self.pbExit.setObjectName("pbExit")

        self.retranslateUi(StartForm)
        QtCore.QMetaObject.connectSlotsByName(StartForm)

    def retranslateUi(self, StartForm):
        _translate = QtCore.QCoreApplication.translate
        StartForm.setWindowTitle(_translate("StartForm", "Form"))
        self.label_2.setText(_translate("StartForm", "<html><head/><body><p><span style=\" font-size:48pt; color:#00ffc8;\">Check</span></p></body></html>"))
        self.label_3.setText(_translate("StartForm", "<html><head/><body><p><span style=\" font-size:48pt; color:#00ffc8;\">Your Memory</span></p></body></html>"))
        self.label_5.setText(_translate("StartForm", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Уровень сложности:</span></p></body></html>"))
        self.edDiff.setText(_translate("StartForm", "1"))
        self.edCount.setText(_translate("StartForm", "1"))
        self.label_6.setText(_translate("StartForm", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Количество ходов:</span></p></body></html>"))
        self.pbStart.setText(_translate("StartForm", "Поехали!"))
        self.pbExit.setText(_translate("StartForm", "Выход"))

