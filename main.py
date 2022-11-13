import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def app():
    app = QApplication(sys.argv)
    window1 = QMainWindow()
    window2 = QMainWindow()

    window1.setWindowTitle("Простая программа 1")
    window2.setWindowTitle("Простая программа 2")
    window1.setGeometry(300, 200, 300, 200)
    window2.setGeometry(300, 600, 400, 200)

    window2.show()
    window1.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    app()