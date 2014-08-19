#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Denisov Sergey 2014'

import sys
from PyQt5 import QtWidgets
from start import StartWindow

def main():
	"""
	Main function for start app
	"""
	app = QtWidgets.QApplication(sys.argv)

	wnd = StartWindow()
	wnd.show()	
	
	app.exec_()

if __name__ == '__main__':
	main()