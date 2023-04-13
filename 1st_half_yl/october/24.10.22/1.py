import sys

from random import choice
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Супрематизм')

        self.type = 0

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.type = 1
            self.x = event.x()
            self.y = event.y()
        elif event.button() == Qt.RightButton:
            self.type = 2
            self.x = event.x()
            self.y = event.y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.type = 3
            self.x = event.x()
            self.y = event.y()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.drawEllipse(40, 40, 400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())