from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(370, 616)
        MainWindow.setStyleSheet(u"background-color: black;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 330, 61))
        font = QFont()
        font.setFamily(u"Arial Unicode MS")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setStyleSheet(u"color: white")
        self.AC = QPushButton(self.centralwidget)
        self.AC.setObjectName(u"AC")
        self.AC.setGeometry(QRect(20, 220, 60, 60))
        font1 = QFont()
        font1.setPointSize(30)
        self.AC.setFont(font1)
        self.AC.setStyleSheet(u"background-color: #D4D4D2;\n"
"border-radius: 30px;\n"
"color: #1C1C1C")
        self.cube = QPushButton(self.centralwidget)
        self.cube.setObjectName(u"cube")
        self.cube.setGeometry(QRect(200, 220, 60, 60))
        self.cube.setFont(font1)
        self.cube.setStyleSheet(u"background-color: #D4D4D2;\n"
"border-radius: 30px;\n"
"color: #1C1C1C")
        self.square = QPushButton(self.centralwidget)
        self.square.setObjectName(u"square")
        self.square.setGeometry(QRect(110, 220, 60, 60))
        self.square.setFont(font1)
        self.square.setStyleSheet(u"background-color: #D4D4D2;\n"
"border-radius: 30px;\n"
"color: #1C1C1C")
        self.divide = QPushButton(self.centralwidget)
        self.divide.setObjectName(u"divide")
        self.divide.setGeometry(QRect(290, 220, 60, 60))
        font2 = QFont()
        font2.setPointSize(36)
        self.divide.setFont(font2)
        self.divide.setStyleSheet(u"background-color: #FF9500;\n"
"border-radius: 30px;\n"
"color: white;")
        self.minus = QPushButton(self.centralwidget)
        self.minus.setObjectName(u"minus")
        self.minus.setGeometry(QRect(290, 380, 60, 60))
        self.minus.setFont(font2)
        self.minus.setStyleSheet(u"background-color: #FF9500;\n"
"border-radius: 30px;\n"
"color: white;")
        self.multiply = QPushButton(self.centralwidget)
        self.multiply.setObjectName(u"multiply")
        self.multiply.setGeometry(QRect(290, 300, 60, 60))
        self.multiply.setFont(font2)
        self.multiply.setStyleSheet(u"background-color: #FF9500;\n"
"border-radius: 30px;\n"
"color: white;")
        self.plus = QPushButton(self.centralwidget)
        self.plus.setObjectName(u"plus")
        self.plus.setGeometry(QRect(290, 460, 60, 60))
        self.plus.setFont(font2)
        self.plus.setStyleSheet(u"background-color: #FF9500;\n"
"border-radius: 30px;\n"
"color: white;")
        self.equal = QPushButton(self.centralwidget)
        self.equal.setObjectName(u"equal")
        self.equal.setGeometry(QRect(290, 540, 60, 60))
        self.equal.setFont(font2)
        self.equal.setStyleSheet(u"background-color: #FF9500;\n"
"border-radius: 30px;\n"
"color: white;")
        self.seven = QPushButton(self.centralwidget)
        self.seven.setObjectName(u"seven")
        self.seven.setGeometry(QRect(20, 300, 60, 60))
        self.seven.setFont(font1)
        self.seven.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.eight = QPushButton(self.centralwidget)
        self.eight.setObjectName(u"eight")
        self.eight.setGeometry(QRect(110, 300, 60, 60))
        self.eight.setFont(font1)
        self.eight.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.nine = QPushButton(self.centralwidget)
        self.nine.setObjectName(u"nine")
        self.nine.setGeometry(QRect(200, 300, 60, 60))
        self.nine.setFont(font1)
        self.nine.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.four = QPushButton(self.centralwidget)
        self.four.setObjectName(u"four")
        self.four.setGeometry(QRect(20, 380, 60, 60))
        self.four.setFont(font1)
        self.four.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.five = QPushButton(self.centralwidget)
        self.five.setObjectName(u"five")
        self.five.setGeometry(QRect(110, 380, 60, 60))
        self.five.setFont(font1)
        self.five.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.six = QPushButton(self.centralwidget)
        self.six.setObjectName(u"six")
        self.six.setGeometry(QRect(200, 380, 60, 60))
        self.six.setFont(font1)
        self.six.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.one = QPushButton(self.centralwidget)
        self.one.setObjectName(u"one")
        self.one.setGeometry(QRect(20, 460, 60, 60))
        self.one.setFont(font1)
        self.one.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.two = QPushButton(self.centralwidget)
        self.two.setObjectName(u"two")
        self.two.setGeometry(QRect(110, 460, 60, 60))
        self.two.setFont(font1)
        self.two.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.three = QPushButton(self.centralwidget)
        self.three.setObjectName(u"three")
        self.three.setGeometry(QRect(200, 460, 60, 60))
        self.three.setFont(font1)
        self.three.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.dot = QPushButton(self.centralwidget)
        self.dot.setObjectName(u"dot")
        self.dot.setGeometry(QRect(200, 540, 60, 60))
        self.dot.setFont(font1)
        self.dot.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        self.zero = QPushButton(self.centralwidget)
        self.zero.setObjectName(u"zero")
        self.zero.setGeometry(QRect(20, 540, 150, 60))
        self.zero.setFont(font1)
        self.zero.setStyleSheet(u"background-color: #1C1C1C;\n"
"border-radius: 30px;\n"
"color: white;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.cube.setText(QCoreApplication.translate("MainWindow", u"x³", None))
        self.square.setText(QCoreApplication.translate("MainWindow", u"x²", None))
        self.divide.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.multiply.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi


