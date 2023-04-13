import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Mywidget(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main1.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Рисование')
        self.side = self.lineEdit.text()
        self.coeff = self.lineEdit_2.text()
        self.n = self.lineEdit_3.text()
        self.label.setText(self.side)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 0, 0))
        # Рисуем прямоугольник заданной кистью
        qp.drawRect(30, 30, 120, 30)
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(30, 60, 120, 30)
        qp.setBrush(QColor(0, 0, 255))
        qp.drawRect(30, 90, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mywidget()
    ex.show()
    sys.exit(app.exec())
