import sys

from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QPushButton, QApplication, QVBoxLayout
from PyQt5 import sip


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.glbl_var = {}  # общие параметры игры (уровень, результаты)
        self.numbers_var = {'count': 0}  # параметры для блока Числа
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('Квадрат памяти')
        self.setStyleSheet("background-color: #cff4fc;")

        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)
        frame.setGeometry(40, 40, 300, 300)

        label = QLabel('вот такой вот тут текст\nлфг полный', frame)
        label.setGeometry(40, 40, 100, 30)

        btn = QPushButton('press', frame)
        btn.clicked.connect(lambda _: self.btn_press(frame))
        btn.setGeometry(0, 20, 20, 10)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())