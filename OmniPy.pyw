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
		self.width = 800
		self.height = 140
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.actionlabel = QLabel("Action",self)
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
		self.button = QPushButton('Add', self)
		self.button.move(650,80)
		# connect button to function on_click
		self.button.clicked.connect(self.on_click)
		self.show()
		
	@pyqtSlot()
	def on_click(self):
		self.addlabel.text = "Adding..."
		textboxValue = self.actiontextbox.text()
		if textboxValue != "":
			self.send_email(textboxValue)
			self.actiontextbox.setText('')
		self.addlabel.text = ""
 
	def send_email(self,subject):
		import smtplib
		FROM = 'lesfister@gmail.com'
		TO = 'lfister.fcjh9@sync.omnigroup.com'
		SUBJECT = subject
		TEXT = 'Sent via OmniPy'
		# Prepare actual message
		message = """From: %s\nTo: %s\nSubject: %s\n\n%s
		""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.ehlo()
			server.starttls()
			server.login('lesfister@gmail.com', 'ylbhzppwqxhbnhvv')
			server.sendmail(FROM, TO, message)
			server.close()
		except:
			QMessageBox.question(self, 'Error', "Error sending email.", QMessageBox.Ok, QMessageBox.Ok)
 

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
