from PyQt5.QtWidgets import *
from ui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle('Apple Calculator')
        self.ui.zero.clicked.connect(lambda: self.set_text('0'))
        self.ui.one.clicked.connect(lambda: self.set_text('1'))
        self.ui.two.clicked.connect(lambda: self.set_text('2'))
        self.ui.three.clicked.connect(lambda: self.set_text('3'))
        self.ui.four.clicked.connect(lambda: self.set_text('4'))
        self.ui.five.clicked.connect(lambda: self.set_text('5'))
        self.ui.six.clicked.connect(lambda: self.set_text('6'))
        self.ui.seven.clicked.connect(lambda: self.set_text('7'))
        self.ui.eight.clicked.connect(lambda: self.set_text('8'))
        self.ui.nine.clicked.connect(lambda: self.set_text('9'))
        self.ui.divide.clicked.connect(lambda: self.set_text('/'))
        self.ui.multiply.clicked.connect(lambda: self.set_text('*'))
        self.ui.dot.clicked.connect(lambda: self.set_text('.'))
        self.ui.square.clicked.connect(lambda: self.set_text('²'))
        self.ui.cube.clicked.connect(lambda: self.set_text('³'))
        self.ui.plus.clicked.connect(lambda: self.set_text('+'))
        self.ui.minus.clicked.connect(lambda: self.set_text('-'))
        self.ui.equal.clicked.connect(lambda: self.calculate())
        self.ui.AC.clicked.connect(lambda: self.clear())
    def set_text(self, sign):
        text = self.ui.label.text()
        text = text+sign
        self.ui.label.setText(text)
    def calculate(self):
        text = self.ui.label.text()
        if '³' in text:
            text = text.replace('³', '**3')
        if '²' in text:
            text = text.replace('²', '**2')
        text = str(eval(text))
        self.ui.label.setText(text)
    def clear(self):
        self.ui.label.setText('')

app = QApplication([])
application = calc()
application.show()
app.exec()