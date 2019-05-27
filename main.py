#!/usr/bin/env python

from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		# Titulo da janela
		self.setWindowTitle("Hanz1 - Painel de controle")

		# Botoes 
		self.but_frente = QPushButton('Forward')
		self.but_tras = QPushButton('Back')
		self.but_esq = QPushButton('Turn Left')
		self.but_dir = QPushButton('Turn Right')

		# Atribuicao das funcoes
		#self.but_frente.clicked.connect(self.move(str('w'))
		#self.but_tras.clicked.connect(self.move(str('s'))
		#self.but_esq.clicked.connect(self.move(str('a'))
		#self.but_dir.clicked.connect(self.move(str('d'))

		# Grid layout 
		layout = QGridLayout()

		layout.addWidget(self.but_frente, 1, 1)
		layout.addWidget(self.but_esq, 2, 0)
		layout.addWidget(self.but_dir, 2, 2)
		layout.addWidget(self.but_tras, 3, 1)

		# Widget principal
		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget) 

	def move (self, direction):
		if (direction == 'w'):
			print('ERRO')
		elif (direction == 's'):
			print('ERRO')
		elif (direction == 'a'):
			print('ERRO')
		elif (direction == 'd'):
			print('ERRO')
		else:
			print('ERRO')
	

if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()

	window.show()

	app.exec_()






