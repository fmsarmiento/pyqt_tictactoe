# Import widgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # UI to be loaded
        uic.loadUi("tictactoe.ui", self)
        # Define widgets here
        self.button1 = self.findChild(QPushButton, "pushButton1")
        self.button2 = self.findChild(QPushButton, "pushButton2")
        self.button3 = self.findChild(QPushButton, "pushButton3")
        self.button4 = self.findChild(QPushButton, "pushButton4")
        self.button5 = self.findChild(QPushButton, "pushButton5")
        self.button6 = self.findChild(QPushButton, "pushButton6")
        self.button7 = self.findChild(QPushButton, "pushButton7")
        self.button8 = self.findChild(QPushButton, "pushButton8")
        self.button9 = self.findChild(QPushButton, "pushButton9")
        self.resetButton = self.findChild(QPushButton, "newGame")
        self.label = self.findChild(QLabel, "label")

        # Set tic tac toe counter
        self.counter = 0

        # Define events here
        self.button1.clicked.connect(lambda: self.clicker(self.button1)) # When button 1 is clicked, we pass in the button itself on the function
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.resetButton.clicked.connect(lambda: self.clicker(self.resetButton))
        # Note that lambda is used when we have a function that needs another input other than self
        self.actionRed.triggered.connect(lambda: self.change("red"))
        self.actionGreen.triggered.connect(lambda: self.change("green"))
        self.actionBlue.triggered.connect(lambda: self.change("blue"))
        self.actionGray.triggered.connect(lambda: self.change("gray"))
        # Show the app
        self.show()

    def checkWin(self):
        for win in ["X","O"]:
            if ((self.button1.text() == win) and (self.button2.text() == win) and (self.button3.text() == win)) or ((self.button4.text() == win) and (self.button5.text() == win) and (self.button6.text() == win)) or ((self.button7.text() == win) and (self.button8.text() == win) and (self.button9.text() == win))or ((self.button1.text() == win) and (self.button4.text() == win) and (self.button7.text() == win)) or ((self.button2.text() == win) and (self.button5.text() == win) and (self.button8.text() == win)) or ((self.button3.text() == win) and (self.button6.text() == win) and (self.button9.text() == win)) or ((self.button1.text() == win) and (self.button5.text() == win) and (self.button9.text() == win)) or ((self.button3.text() == win) and (self.button5.text() == win) and (self.button7.text() == win)):
                button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, 
                                self.button6, self.button7, self.button8, self.button9]
                for items in button_list:
                    items.setEnabled(False)
                if self.counter % 2 == 0:
                    self.label.setText("O wins!")
                else:
                    self.label.setText("X wins!")
                self.counter = 0

    def clicker(self, b): # b is the button pressed
        if b == self.resetButton:
            button_list = [self.button1, self.button2, self.button3, self.button4, self.button5, 
                            self.button6, self.button7, self.button8, self.button9]
            for items in button_list:
                items.setText("?")
                items.setEnabled(True)
            self.counter = 0
            self.label.setText("X Goes First!")
        else:
            if (self.counter%2 == 0):
                b.setText("X")
                self.label.setText("O's turn!")
            else: 
                b.setText("O")
                self.label.setText("X's turn!")
            self.counter += 1
            b.setEnabled(False)
            self.checkWin()

    def change(self, color):
        self.setStyleSheet("background-color: {}".format(color))

# Initialisation
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()