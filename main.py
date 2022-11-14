import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
n = 10
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простая программа")
        self.setGeometry(300, 200, 300, 200)

        self.add_text = QtWidgets.QLabel(self)

        self.text = QtWidgets.QLabel(self)
        self.text.setText('Просто текст')
        self.text.move(100, 50)
        self.text.adjustSize()
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText('Нажми на меня')
        self.btn.move(50, 100)
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add)

    def add(self):
        global n
        n += 10
        self.add_text.setText('Просто текст 67')
        self.add_text.move(100, n)
        self.add_text.adjustSize()






def app():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()