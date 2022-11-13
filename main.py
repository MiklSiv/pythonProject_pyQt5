import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def add():
    print("12345")

def app():
    app = QApplication(sys.argv)
    window1 = QMainWindow()
    window2 = QMainWindow()

    window1.setWindowTitle("Простая программа")
    #window2.setWindowTitle("Простая программа 2")
    window1.setGeometry(300, 200, 300, 200)
    #window2.setGeometry(300, 600, 400, 200)

    text = QtWidgets.QLabel(window1)
    text.setText('Просто текст')
    text.move(100, 50)
    text.adjustSize()

    btn = QtWidgets.QPushButton(window1)
    btn.setText('Нажми на меня')
    btn.move(50, 100)
    btn.setFixedWidth(200)
    btn.clicked.connect(add)


    #window2.show()
    window1.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    app()