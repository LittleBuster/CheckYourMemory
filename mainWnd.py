# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWnd.ui'
#
# Created: Mon Aug 18 17:53:54 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(721, 405)
        self.label = QtWidgets.QLabel(MainForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 411))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/reWalls.com-18145.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.edCount = QtWidgets.QLineEdit(MainForm)
        self.edCount.setGeometry(QtCore.QRect(480, 260, 61, 31))
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
        self.label_6 = QtWidgets.QLabel(MainForm)
        self.label_6.setGeometry(QtCore.QRect(130, 250, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pbCheck = QtWidgets.QPushButton(MainForm)
        self.pbCheck.setGeometry(QtCore.QRect(260, 340, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbCheck.setFont(font)
        self.pbCheck.setStyleSheet("QPushButton {\n"
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
        self.pbCheck.setIcon(icon)
        self.pbCheck.setIconSize(QtCore.QSize(24, 24))
        self.pbCheck.setObjectName("pbCheck")
        self.label_7 = QtWidgets.QLabel(MainForm)
        self.label_7.setGeometry(QtCore.QRect(200, 0, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lbDigit = QtWidgets.QLabel(MainForm)
        self.lbDigit.setGeometry(QtCore.QRect(60, 40, 601, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lbDigit.setFont(font)
        self.lbDigit.setAlignment(QtCore.Qt.AlignCenter)
        self.lbDigit.setObjectName("lbDigit")
        self.lbRes = QtWidgets.QLabel(MainForm)
        self.lbRes.setGeometry(QtCore.QRect(60, 150, 601, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lbRes.setFont(font)
        self.lbRes.setAlignment(QtCore.Qt.AlignCenter)
        self.lbRes.setObjectName("lbRes")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.edCount.setText(_translate("MainForm", "1"))
        self.label_6.setText(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Количество повторений:</span></p></body></html>"))
        self.pbCheck.setText(_translate("MainForm", "Ответить"))
        self.label_7.setText(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Число:</span></p></body></html>"))
        self.lbDigit.setText(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:72pt; color:#00ffc8;\">4</span></p></body></html>"))
        self.lbRes.setText(_translate("MainForm", "<html><head/><body><p><span style=\" font-size:36pt; color:#ff0005;\">4</span></p></body></html>"))

