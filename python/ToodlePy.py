import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
class App(QMainWindow):
 
	def __init__(self):
		super().__init__()
		self.title = 'Add ToodleDo Action'
		self.left = 100
		self.top = 100
		self.width = 800
		self.height = 260
		self.initUI()
 
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		
		self.actionlabel = QLabel("Action",self)
		self.actionlabel.move(20, 25)
		self.actionlabel.resize(100,25)
		self.actionlabel.setAlignment(Qt.AlignRight)

		# Create textboxes
		self.actiontextbox = QLineEdit(self)
		self.actiontextbox.move(130, 20)
		self.actiontextbox.resize(600,40)

		self.startlabel = QLabel("Start Date",self)
		self.startlabel.move(20, 85)
		self.startlabel.resize(100,25)
		self.startlabel.setAlignment(Qt.AlignRight)

		self.startdatebox = QLineEdit(self)
		self.startdatebox.move(130, 80)
		self.startdatebox.resize(600,40)

		self.duelabel = QLabel("Due Date",self)
		self.duelabel.move(20, 145)
		self.duelabel.resize(100,25)
		self.duelabel.setAlignment(Qt.AlignRight)

		self.duedatebox = QLineEdit(self)
		self.duedatebox.move(130, 140)
		self.duedatebox.resize(600,40)

		# Create a button in the window
		self.button = QPushButton('Add', self)
		self.button.move(650,210)
		# connect button to function on_click
		self.button.clicked.connect(self.on_click)
		self.show()
		
	@pyqtSlot()
	def on_click(self):
		textboxValue = self.actiontextbox.text()
		startdateValue = self.startdatebox.text()
		if startdateValue != '':
			textboxValue = textboxValue + ' >' + startdateValue
		duedateValue = self.duedatebox.text()
		if duedateValue != '':
			textboxValue = textboxValue + ' #' + duedateValue
		self.send_email(textboxValue)
		self.actiontextbox.setText('')
		self.startdatebox.setText('')
		self.duedatebox.setText('')
 
	def send_email(self,subject):
		import smtplib
		FROM = 'lesfister@gmail.com'
		TO = 'MailMe.59588@toodledo.com'
		SUBJECT = subject
		TEXT = 'Sent via ToodleDo Python'
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
