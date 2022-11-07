import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		self.title = 'Add to Omnifocus Inbox'
		self.left = 100
		self.top = 100
		self.width = 1100
		self.height = 800
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.actionlabel = QLabel("Text",self)
		self.actionlabel.move(20, 25)
		self.actionlabel.resize(100,25)
		self.actionlabel.setAlignment(Qt.AlignRight)

		self.addlabel = QLabel(" ",self)
		self.addlabel.move(40, 80)
		self.addlabel.resize(100,25)

		# Create textboxes
		self.actiontextbox = QLineEdit(self)
		self.actiontextbox.move(130, 20)
		self.actiontextbox.resize(600,40)

		# Create a button in the window
		self.button = QPushButton('Clear', self)
		self.button.move(650,80)
		# connect button to function on_click
		self.button.clicked.connect(self.on_click)
		self.show()
		
	@pyqtSlot()
	def on_click(self):
		self.actiontextbox.setText('')
 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
