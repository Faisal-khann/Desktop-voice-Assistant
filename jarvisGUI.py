import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1445, 917)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Base directory of the script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Background label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setScaledContents(True)

        # Load and store original pixmap
        self.bg_pixmap = QtGui.QPixmap(os.path.join(base_dir, "gif/iron.gif.gif"))
        self.label.setPixmap(self.bg_pixmap)

        # Layout for background stretching
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label)

        # Other UI elements
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 401, 101))
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(base_dir, "gif/initial.gif.gif")))
        self.label_2.setObjectName("label_2")

        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(980, 510, 451, 291))
        # self.label_3.setPixmap(QtGui.QPixmap(os.path.join(base_dir, "gif/iron-man-animated-gif.jpg")))
        # self.label_3.setScaledContents(True)
        # self.label_3.setObjectName("label_3")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1130, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\nborder:none;\ncolor:white;")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1130, 70, 311, 61))
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\nborder:none;\ncolor:white;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 100, 101, 41))
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 100, 101, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 85, 85);")
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "R U N"))
        self.pushButton_2.setText(_translate("MainWindow", "E X I T"))

    def resize_background(self, size):
        if not self.bg_pixmap.isNull():
            scaled = self.bg_pixmap.scaled(size, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
            self.label.setPixmap(scaled)


class CustomMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def resizeEvent(self, event):
        self.ui.resize_background(self.size())
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = CustomMainWindow()
    MainWindow.show()
    sys.exit(app.exec_())