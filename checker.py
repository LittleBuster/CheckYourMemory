import random
from PyQt5 import QtWidgets
from result import ResWindow

class Checker():
	diff = 0
	count = 0
	digit_list = []
	isFirst = True
	isError = False
	errors = 0
	right = 0

	def __init__(self):
		super(Checker, self).__init__()
		self.resWnd = ResWindow()
		self.resWnd.closeSig.connect(self.on_close_result)

	def set_params(self, diff, count):
		self.diff = diff
		self.count = count

	def set_main_wnd(self, wnd):
		self.mainWnd = wnd

	def set_start_wnd(self, wnd):
		self.startWnd = wnd

	def on_close_result(self):
		for i in range(0, len(self.digit_list)-1):
			del self.digit_list[i]

		print(self.digit_list)
		self.startWnd.show()
		self.gen_new_digit()

	def gen_new_digit(self):
		self.mainWnd.ui.lbRes.setText( "" )
		if len(self.digit_list) < self.count:
			digit = random.randrange(1, self.diff + 1)

			self.digit_list.append(digit)
			#Show digit
			self.mainWnd.ui.lbDigit.setText("<html><head/><body><p><span style='font-size:72pt; color:#00ffc8;'>" + str(digit) + "</span></p></body></html>")
		else:
			if not self.isFirst:
				self.mainWnd.hide()
				self.resWnd.ui.lbRight.setText("<html><head/><body><p><span style='font-size:36pt; color:#00ff2a;'>" + str(self.right) + "</span></p></body></html>")
				self.resWnd.ui.lbError.setText("<html><head/><body><p><span style='font-size:36pt; color:#ff0005;'>" + str(self.errors) + "</span></p></body></html>")
				self.resWnd.show()
				self.right = 0
				self.errors = 0

	def add_digit(self, count_digit):
		if count_digit < 0:
			QtWidgets.QMessageBox.warning(self.mainWnd, 'Error', 'Количество повторений не может быть отрицательно!', QtWidgets.QMessageBox.Yes)
			return

		cnt = -1
		for d in self.digit_list:
			if d == self.digit_list[ len(self.digit_list) -1 ]:
				cnt += 1

		if count_digit == cnt:
			self.right += 1
			self.mainWnd.ui.lbRes.setText( "<html><head/><body><p><span style='font-size:36pt; color:#00ff1e;'>Ответ верный!</span></p></body></html>")
		else:
			self.errors += 1
			self.isError = True
			self.mainWnd.ui.lbRes.setText( "<html><head/><body><p><span style='font-size:36pt; color:#ff0005;'>Ответ неверный!</span></p></body></html>")