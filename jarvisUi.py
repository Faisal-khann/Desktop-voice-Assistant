
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(1450, 917)
        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-70, -20, 1521, 941))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imgg/iron.gif.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imgg/initial.gif.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(990, 790, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1090, 790, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "background-color: rgb(255, 170, 127);\n"
            "background-color: rgb(255, 255, 127);"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1130, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(
            "border-radius:none;\n" "background:transparent;\n" "color:white;"
        )
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1130, 70, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet(
            "border-radius:none;\n" "background:transparent;\n" "color:white"
        )
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(990, 500, 461, 291))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../imgg/iron-man-animated-gif.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        jarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
        self.pushButton.setText(_translate("jarvisUi", "R U N"))
        self.pushButton_2.setText(_translate("jarvisUi", "E X I T"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
