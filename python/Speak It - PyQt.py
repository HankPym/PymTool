import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtGui import QIcon
import sayit

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Speak It - PyQt6 Version")
        self.setWindowIcon(QIcon('images/f.ico'))
        self.setFixedWidth(400)

        widget = QLineEdit()
        widget.setMaxLength(80)
        widget.setPlaceholderText("Type what you want me to say here...")
        widget.returnPressed.connect(self.speak)

        self.setCentralWidget(widget)
        self.prevmsg = "You haven't typed anything."

    def speak(self):
        msg = self.centralWidget().text()
        if (msg == "quit" or msg == "exit"):
            self.prevmsg = ""
            app.quit()
        elif (msg == "" or msg == "repeat"):
            msg = self.prevmsg
        else:
            self.prevmsg = msg
        self.centralWidget().clear()
        sayit.sayit(msg)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
