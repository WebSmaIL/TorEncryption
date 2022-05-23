from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import resourse


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 400)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo100x100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.977273, stop:0 rgba(114, 0, 156, 255), stop:1 rgba(195, 0, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.keyInput = QtWidgets.QLineEdit(self.centralwidget)
        self.keyInput.setGeometry(QtCore.QRect(90, 350, 170, 30))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setItalic(True)
        self.keyInput.setFont(font)
        self.keyInput.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 234, 0);")
        self.keyInput.setObjectName("keyInput")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(360, 15, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 100, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(580, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_10.setObjectName("label_10")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(420, 160, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convert.setFont(font)
        self.convert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert.setStyleSheet("color: rgb(255, 255, 255);")
        self.convert.setObjectName("convert")
        self.convert_2 = QtWidgets.QPushButton(self.centralwidget)
        self.convert_2.setGeometry(QtCore.QRect(420, 260, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convert_2.setFont(font)
        self.convert_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.convert_2.setObjectName("convert_2")
        self.enter_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.enter_text.setGeometry(QtCore.QRect(30, 140, 390, 200))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.enter_text.setFont(font)
        self.enter_text.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 234, 0);")
        self.enter_text.setObjectName("enter_text")
        self.result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(580, 140, 390, 200))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 234, 0);")
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 350, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 350, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_12.setObjectName("label_12")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 350, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 35, 35))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/img/img/logo_mini.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vigener encryption"))
        self.keyInput.setPlaceholderText(_translate("MainWindow", "Введите ключ"))
        self.label_8.setText(_translate("MainWindow", "Шифр Виженера"))
        self.label_9.setText(_translate("MainWindow", "Входные данные"))
        self.label_10.setText(_translate("MainWindow", "Результат"))
        self.convert.setText(_translate("MainWindow", "Зашифровать"))
        self.convert_2.setText(_translate("MainWindow", "Дешифровать"))
        self.enter_text.setPlaceholderText(_translate("MainWindow", "Введите сообщение..."))
        self.label_11.setText(_translate("MainWindow", "Ключ"))
        self.label_12.setText(_translate("MainWindow", "Язык"))
        self.comboBox.setItemText(0, _translate("MainWindow", "En"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ru"))

        self.alphabets = ['0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ','0123456789АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя ']
        
        self.convert.clicked.connect(lambda: self.vigenere_encrypt(
            self.enter_text.toPlainText(),
            self.keyInput.text(),
            self.alphabets
            ))
        
        self.convert_2.clicked.connect(lambda: self.vigenere_decrypt(
            self.enter_text.toPlainText(),
            self.keyInput.text(),
            self.alphabets
        ))
        

    def vigenere( self,
        text: str,
        key: str,
        alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ',
        encrypt=True):

        result = ''

        for i in range(len(text)):
            letter_n = alphabet.index(text[i])
            key_n = alphabet.index(key[i % len(key)])

            if encrypt:
                value = (letter_n + key_n) % len(alphabet)
            else:
                value = (letter_n - key_n) % len(alphabet)

            result += alphabet[value]

        return result


    def vigenere_encrypt(self, text, key, alphabet):
        if self.comboBox.currentText() == "En":
            alpn = alphabet[0]
        else:
            alpn = alphabet[1]
        
        self.result.setPlainText(self.vigenere(text=text, key=key, alphabet=alpn, encrypt=True))


    def vigenere_decrypt(self, text, key, alphabet):
        if self.comboBox.currentText() == "En":
            alpn = alphabet[0]
        else:
            alpn = alphabet[1]

        self.result.setPlainText(self.vigenere(text=text, key=key, alphabet=alpn, encrypt=False))

        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
