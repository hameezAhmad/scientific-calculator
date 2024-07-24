import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import math

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 400, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
             
        # self.title_label = QLabel("Calculator by Hameez")
        # self.title_label.setFont(QFont('Arial', 20))
        # self.title_label.setAlignment(Qt.AlignCenter)
        # self.layout.addWidget(self.title_label)

        self.display = QLineEdit()
        self.display.setFont(QFont('Arial', 24))
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.display)

        self.buttons_layout = QGridLayout()
        self.layout.addLayout(self.buttons_layout)

        self.expression = ""

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3), ('C', 0, 4),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3), ('(', 1, 4),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), (')', 2, 4),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3), ('%', 3, 4),
            ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('log', 4, 3), ('ln', 4, 4),
            ('π', 5, 0), ('e', 5, 1), ('sqrt', 5, 2), ('x^2', 5, 3), ('x^y', 5, 4),
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text)
            button.setFont(QFont('Arial', 18))
            button.setStyleSheet("background-color: lightgrey; color: black; border: none; padding: 10px;")
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            self.buttons_layout.addWidget(button, row, col)

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.expression = ""
            self.display.setText("")
        elif char in ["sin", "cos", "tan", "log", "ln", "sqrt", "x^2", "x^y", "π", "e"]:
            self.handle_advanced_functions(char)
        else:
            self.expression += str(char)
            self.display.setText(self.expression)

    def handle_advanced_functions(self, func):
        try:
            if func == "sin":
                self.expression = str(math.sin(math.radians(float(self.expression))))
            elif func == "cos":
                self.expression = str(math.cos(math.radians(float(self.expression))))
            elif func == "tan":
                self.expression = str(math.tan(math.radians(float(self.expression))))
            elif func == "log":
                self.expression = str(math.log10(float(self.expression)))
            elif func == "ln":
                self.expression = str(math.log(float(self.expression)))
            elif func == "sqrt":
                self.expression = str(math.sqrt(float(self.expression)))
            elif func == "x^2":
                self.expression = str(float(self.expression) ** 2)
            elif func == "x^y":
                self.expression += "**"
            elif func == "π":
                self.expression = str(math.pi)
            elif func == "e":
                self.expression = str(math.e)
            self.display.setText(self.expression)
        except:
            self.expression = "Error"
            self.display.setText(self.expression)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
            self.display.setText(self.expression)
        except:
            self.expression = "Error"
            self.display.setText(self.expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScientificCalculator()
    window.show()
    sys.exit(app.exec_())
