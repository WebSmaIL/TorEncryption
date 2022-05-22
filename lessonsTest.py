from PyQt5 import QtCore, QtGui, QtWidgets
import resourse
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 220)
        MainWindow.setMinimumSize(QtCore.QSize(320, 220))
        MainWindow.setMaximumSize(QtCore.QSize(320, 220))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo100x100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.977273, stop:0 rgba(114, 0, 156, 255), stop:1 rgba(195, 0, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 175, 35, 35))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/img/logo_mini.png"))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        
        # Массив с файлами
        self.filesArr = []   
             
        for file in os.listdir("./lessons"):
            # Перебор всех файлов в директории с лекциями
            if file.endswith(".pdf"):
                # Добавление селект итемов в соответствии с количеством pdf файлов
                self.comboBox.addItem("")
                # Добавление названий всех pdf файлов в массив
                self.filesArr.append(os.path.join(file))
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lecture"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))
        self.label_6.setText(_translate("MainWindow", "Выберите лекцию"))

        # Заполнение селектов в comboBox из названий файлов
        for item in range (self.comboBox.count()):
            self.comboBox.setItemText(item, self.filesArr[item].split('.')[0])    

        # Открытие лекции
        self.pushButton.clicked.connect(lambda: self.openLesson())
        
    def openLesson(self):
        # Функция открытия pdf файла
        str = self.comboBox.currentText() + ".pdf"
        if os.getcwd().split('\\')[-1] != "lessons":
            os.chdir("./lessons/")
        os.startfile(str)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
