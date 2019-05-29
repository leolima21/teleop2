#!/usr/bin/env python

# Bibliotecas necessarias
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import sys

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import time


class MainWindow(QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		# Objeto que ira publicar no topico teleop_topic
		self.pub = rospy.Publisher('teleop_topic', String, queue_size=10)

		# Inicio do node teleop_pub
		rospy.init_node('teleop_pub', anonymous=True)

		# Titulo da janela
		self.setWindowTitle("Hanz1 - Painel de controle")

		# Botoes 
		self.but_frente = QPushButton('Forward')
		self.but_tras = QPushButton('Back')
		self.but_esq = QPushButton('Turn Left')
		self.but_dir = QPushButton('Turn Right')

		# Atribuicao das funcoes
		self.but_frente.clicked.connect(self.publicar_w)
		self.but_tras.clicked.connect(self.publicar_s)
		self.but_esq.clicked.connect(self.publicar_a)
		self.but_dir.clicked.connect(self.publicar_d)

		# Grid layout 
		layout = QGridLayout()

		layout.addWidget(self.but_frente, 1, 1)
		layout.addWidget(self.but_esq, 2, 0)
		layout.addWidget(self.but_dir, 2, 2)
		layout.addWidget(self.but_tras, 3, 1)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget) 


	# Funcoes de publicacao
	def publicar_w (self):
		rospy.loginfo('w')
		self.pub.publish('w')

	def publicar_s (self):
		rospy.loginfo('s')
		self.pub.publish('s')
	
	def publicar_a (self):
		rospy.loginfo('a')
		self.pub.publish('a')

	def publicar_d (self):
		rospy.loginfo('d')
		self.pub.publish('d')	


if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()

	window.show()

	app.exec_()
