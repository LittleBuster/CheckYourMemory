#!/usr/bin/python
# -*- coding: utf-8 -*-

import mainWnd
from checker import Checker
from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__()
		self.ui = mainWnd.Ui_MainForm()
		self.ui.setupUi(self)

		width = self.frameGeometry().width()
		height = self.frameGeometry().height()

		wid = QtWidgets.QDesktopWidget()
		screenWidth = wid.screen().width()
		screenHeight = wid.screen().height()
		self.setGeometry((screenWidth/2)-(width/2),(screenHeight/2)-(height/2),width,height)

		self.checker = Checker()
		self.checker.set_main_wnd(self)		
		
		self.ui.pbCheck.clicked.connect(self.on_check_clicked)

	def set_start_wnd(self, wnd):
		self.startWnd = wnd
		self.checker.set_start_wnd(wnd)

	def closeEvent(self, e):
		result = QtWidgets.QMessageBox.question(self, 'Закрытие', 'Вы действительно хотите завершить тест?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if result == QtWidgets.QMessageBox.Yes:
			self.hide()
			self.startWnd.show()
		else:
			e.ignore()

	def start_test(self):
		self.checker.gen_new_digit()
		self.checker.isFirst = False

	def on_check_clicked(self):
		digit = 0

		if self.ui.pbCheck.text() == "Ответить":
			try:
				count = int( self.ui.edCount.text() )
			except:
				QtWidgets.QMessageBox.warning(self, 'Error', 'Неверные символы в поле повторений! Необходимо число!', QtWidgets.QMessageBox.Yes)
				self.ui.edDiff.setText("0")
				return

			self.checker.add_digit( count )
			self.ui.pbCheck.setText("Далее")
			self.ui.pbCheck.setIcon(QtGui.QIcon("images/next_8028.ico"))			
			return
		else:
			if not self.checker.isError:
				self.checker.gen_new_digit()
			else:
				self.ui.lbRes.setText("")
				self.checker.isError = False
			self.ui.pbCheck.setIcon(QtGui.QIcon("images/apply_5183.ico"))
			self.ui.pbCheck.setText("Ответить")