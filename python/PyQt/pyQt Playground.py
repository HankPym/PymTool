from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.label.setText("Entry:")

        self.input = QLineEdit()

        self.button = QPushButton()
        self.button.setText("Say It!")
        self.button.clicked.connect(MainWindow.speak)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def speak():
        print(self.input.text())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
