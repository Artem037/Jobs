import sys

from PyQt5.QtWidgets import QApplication, QFrame, QGridLayout, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, \
    QVBoxLayout, QMainWindow
from PyQt5.QtCore import QEvent


class Widget(QMainWindow):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.layoutUI()

    def layoutUI(self):
        self.setGeometry(100, 100, 700, 500)
        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)

        btns = {(0, 0): "Button1", (1, 0): "Button7", (2, 0): "Button13", (3, 0): "Button19", (4, 0): "Button25",
                (5, 0): "Button31",
                (0, 1): "Button2", (1, 1): "Button8", (2, 1): "Button14", (3, 1): "Button20", (4, 1): "Button26",
                (5, 1): "Button32",
                (0, 2): "Button3", (1, 2): "Button9", (2, 2): "Button15", (3, 2): "Button21", (4, 2): "Button27",
                (5, 2): "Button33",
                (0, 3): "Button4", (1, 3): "Button10", (2, 3): "Button16", (3, 3): "Button22", (4, 3): "Button28",
                (5, 3): "Button34",
                (0, 4): "Button5", (1, 4): "Button11", (2, 4): "Button17", (3, 4): "Button23", (4, 4): "Button29",
                (5, 4): "Button35",
                (0, 5): "Button6", (1, 5): "Button12", (2, 5): "Button18", (3, 5): "Button24", (4, 5): "Button30",
                (5, 5): "Button36"}

        for pos, name in btns.items():
            x, y = pos
            btn = QPushButton(self.frame)
            btn.setText(name)
            btn.setFixedSize(100, 65)
            self.gridLayout.addWidget(btn, x, y)
        self.frame.resize(600, 390)
        self.frame.move(45, 45)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
