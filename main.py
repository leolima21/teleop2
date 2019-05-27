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

		# Titulo da janela
		self.setWindowTitle("Hanz1 - Painel de controle")

		# Botoes 
		self.but_frente = QPushButton('Forward')
		self.but_tras = QPushButton('Back')
		self.but_esq = QPushButton('Turn Left')
		self.but_dir = QPushButton('Turn Right')

		# Atribuicao das funcoes
		self.but_frente.clicked.connect(publicar('w'))
		self.but_tras.clicked.connect(publicar('s'))
		self.but_esq.clicked.connect(publicar('a'))
		self.but_dir.clicked.connect(publicar('d'))

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


def ros_node():
	# Objeto que ira publicar no topico teleop_topic
	pub = rospy.Publisher('teleop_topic', String, queue_size=10)

	# Inicio do node teleop_pub
	rospy.init_node('teleop_pub', anonymous=True)


def publicar(comando):
	# Publicacao da info no topico
	rospy.loginfo(comando)
	pub.publish(comando)

	# Esperar 2s ate o proximo comando
	time.sleep(2)


if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = MainWindow()

	ros_node()

	window.show()

	app.exec_()
