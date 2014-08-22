#!/usr/bin/python
# -*- coding: utf-8 -*-

import resWnd
from PyQt5 import QtWidgets, QtCore

class ResWindow(QtWidgets.QDialog):
	closeSig = QtCore.pyqtSignal()

	def __init__(self, parent=None):
		super(ResWindow, self).__init__()
		self.ui = resWnd.Ui_ResForm()
		self.ui.setupUi(self)
		self.ui.pbOk.clicked.connect(self.on_close)

	def on_close(self):
		self.hide()
		self.closeSig.emit()

	def closeEvent(self, e):
		self.hide()
		self.closeSig.emit()
		e.ignore()