#!/usr/bin/python
# -*- coding: utf-8 -*-

import startWnd
from main import MainWindow
from PyQt5 import QtWidgets

class StartWindow(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super(StartWindow, self).__init__()
		self.ui = startWnd.Ui_StartForm()
		self.ui.setupUi(self)

		self.mw = MainWindow()
		self.mw.set_start_wnd(self)
		self.ui.pbStart.clicked.connect(self.on_start)
		self.ui.pbExit.clicked.connect(self.on_close_clicked)

	def on_close_clicked(self):
		QtWidgets.QApplication.quit()

	def on_start(self):
		diff = int
		count = int

		try:
			diff = int( self.ui.edDiff.text() )
		except:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Неверные символы в поле сложность! Необходимо число!', QtWidgets.QMessageBox.Yes)
			self.ui.edDiff.setText("1")
			return

		try:
			count = int( self.ui.edCount.text() )
		except:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Неверные символы в поле ходов! Необходимо число!', QtWidgets.QMessageBox.Yes)
			self.ui.edCount.setText("1")
			return

		if diff < 1:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Сложность должны быть больше единицы', QtWidgets.QMessageBox.Yes)
			return

		if count < 1:
			QtWidgets.QMessageBox.warning(self, 'Error', 'Количество ходов должно быть больше единицы', QtWidgets.QMessageBox.Yes)
			return

		self.mw.checker.set_params(diff, count)
		self.mw.start_test()

		self.hide()
		self.mw.show()