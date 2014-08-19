# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resWnd.ui'
#
# Created: Mon Aug 18 21:43:16 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResForm(object):
    def setupUi(self, ResForm):
        ResForm.setObjectName("ResForm")
        ResForm.resize(626, 328)
        self.label = QtWidgets.QLabel(ResForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 631, 331))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/PanoramaBackground.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(ResForm)
        self.label_6.setGeometry(QtCore.QRect(140, 100, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pbOk = QtWidgets.QPushButton(ResForm)
        self.pbOk.setGeometry(QtCore.QRect(220, 270, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pbOk.setFont(font)
        self.pbOk.setStyleSheet("QPushButton {\n"
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
        self.pbOk.setIcon(icon)
        self.pbOk.setIconSize(QtCore.QSize(24, 24))
        self.pbOk.setObjectName("pbOk")
        self.lbRight = QtWidgets.QLabel(ResForm)
        self.lbRight.setGeometry(QtCore.QRect(440, 90, 31, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lbRight.setFont(font)
        self.lbRight.setAlignment(QtCore.Qt.AlignCenter)
        self.lbRight.setObjectName("lbRight")
        self.lbError = QtWidgets.QLabel(ResForm)
        self.lbError.setGeometry(QtCore.QRect(440, 160, 31, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lbError.setFont(font)
        self.lbError.setAlignment(QtCore.Qt.AlignCenter)
        self.lbError.setObjectName("lbError")
        self.label_7 = QtWidgets.QLabel(ResForm)
        self.label_7.setGeometry(QtCore.QRect(140, 170, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lbDigit = QtWidgets.QLabel(ResForm)
        self.lbDigit.setGeometry(QtCore.QRect(100, -30, 601, 111))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.lbDigit.setFont(font)
        self.lbDigit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbDigit.setObjectName("lbDigit")

        self.retranslateUi(ResForm)
        QtCore.QMetaObject.connectSlotsByName(ResForm)

    def retranslateUi(self, ResForm):
        _translate = QtCore.QCoreApplication.translate
        ResForm.setWindowTitle(_translate("ResForm", "Form"))
        self.label_6.setText(_translate("ResForm", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Правильных ответов:</span></p></body></html>"))
        self.pbOk.setText(_translate("ResForm", "Ok"))
        self.lbRight.setText(_translate("ResForm", "<html><head/><body><p><span style=\" font-size:36pt; color:#00ff2a;\">4</span></p></body></html>"))
        self.lbError.setText(_translate("ResForm", "<html><head/><body><p><span style=\" font-size:36pt; color:#ff0005;\">4</span></p></body></html>"))
        self.label_7.setText(_translate("ResForm", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Ошибок:</span></p></body></html>"))
        self.lbDigit.setText(_translate("ResForm", "<html><head/><body><p><span style=\" font-size:48pt; color:#00ffc8;\">Результаты:</span></p></body></html>"))

