# сделать единую frame и очищать ее при надобности
# функция на очищение фрейма

import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QMenu, QAction, QLabel, QPushButton, QGridLayout, \
    QWidget
from PyQt5.QtGui import QFont

from random import shuffle

class Button(QPushButton):
    def __init__(self, value, parent):
        self.setObjectName(value)
        self.setParent(parent)
        return self


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.glbl_var = {}  # общие параметры игры (уровень, результаты)
        self.numbers_var = {'count': 0}  # параметры для блока Числа

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setGeometry(0, 0, 700, 500)

        self.initUI()
        self._createMenuBar()
        self._connectActions()

    def initUI(self):
        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('Квадрат памяти')
        self.setStyleSheet("background-color: #cff4fc;")



    def _createMenuBar(self):
        menuBar = self.menuBar()
        self.playMenu = QMenu("Играть", self)

        self.lvl1Action = QAction("1 уровень", self)
        self.lvl2Action = QAction("2 уровень", self)
        self.lvl3Action = QAction("3 уровень", self)

        self.playMenu.addAction(self.lvl1Action)
        self.playMenu.addAction(self.lvl2Action)
        self.playMenu.addAction(self.lvl3Action)

        menuBar.addMenu(self.playMenu)

        self.resultAction = QAction('Результаты', self)
        self.exitAction = QAction('Выход', self)

        menuBar.addAction(self.resultAction)
        menuBar.addAction(self.exitAction)

    def _connectActions(self):
        self.lvl1Action.triggered.connect(lambda: self.numbers_menu_click(1))
        self.lvl2Action.triggered.connect(lambda: self.numbers_menu_click(2))
        self.lvl3Action.triggered.connect(lambda: self.numbers_menu_click(3))
        self.resultAction.triggered.connect(self.result_func)
        self.exitAction.triggered.connect(self.exit_func)

    def numbers_menu_click(self, level):
        # Запуск игры Числа
        self.clear()

        self.glbl_var['lvl'] = level

        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(12)

        self.label_instr = QLabel(self.frame)
        self.label_instr.setGeometry(150, 125, 400, 100)
        self.label_instr.setText("Будут показаны числа\n"
                                 "Ваша задача запомнить их расположение в порядке возрастания,\n"
                                 "и нажать на них в этом порядке.")
        self.label_instr.setStyleSheet("background-color: #cff4fc")
        self.label_instr.setFont(font)
        self.label_instr.setAlignment(Qt.AlignCenter)

        font.setPointSize(16)

        self.btn_instr = QPushButton(self.frame)
        self.btn_instr.setGeometry(285, 225, 130, 40)
        self.btn_instr.setText("Начать")
        self.btn_instr.setStyleSheet("background-color: #f8d7da")
        self.btn_instr.setFont(font)

        self.btn_instr.clicked.connect(lambda _: self.numbers_run())

        self.show_widgets()


    def numbers_run(self):
        # Установка лимита на кол-во слов
        if self.glbl_var['lvl'] == 1:
            loop = 6
        elif self.glbl_var['lvl'] == 2:
            loop = 9
        else:
            loop = 12
        self.numbers_var["loop"] = loop
        self.numbers_var["sub_lvl"] = self.glbl_var["lvl"]  # стартовый уровень игры

        self.numbers_field()

    def numbers_field(self):
        # Создание поля

        self.clear()

        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QRect(45, 50, 600, 390))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)

        a = [f'{j}-{i}' for j in range(6) for i in range(6)]
        shuffle(a)
        a = a[:self.numbers_var["sub_lvl"] + 3]
        print(a)

        for x in range(6):
            for y in range(6):
                if f'{x}-{y}' in a:
                    b = a.index(f'{x}-{y}') + 1
                    btn = Button(f'{x}{y}', self.frame)
                    btn.setObjectName(f'{x}{y}')
                    btn.setText(str(a.index(f'{x}-{y}') + 1))
                    btn.setStyleSheet("background-color: violet")
                    btn.setFont(QFont("Calibri", 16))
                    btn.setFixedSize(100, 65)
                    btn.clicked.connect(lambda _: self.numbers_btn_click((btn, b)))
                    self.gridLayout.addWidget(btn, x, y)
                else:
                    b = 'no'
                    btn = Button(f'{x}{y}', self.frame)
                    btn.setObjectName(f'{x}{y}')
                    btn.setStyleSheet("background-color: lavender")
                    btn.setFont(QFont("Calibri", 16))
                    btn.setFixedSize(100, 65)
                    btn.clicked.connect(lambda _: self.numbers_btn_click((btn, b)))
                    self.gridLayout.addWidget(btn, x, y)

        self.show_widgets()

    def numbers_btn_click(self, params):
        # Обработка нажатия кнопок поля
        print(self.sender())
        button, b = params
        self.numbers_var['count'] += 1

        font = QFont()
        font.setFamily("Calibri")
        print(b, button.objectName())

        if b == self.numbers_var['count']:
            button.setStyleSheet("background-color: lavender")
            if self.numbers_var['count'] == self.numbers_var["loop"]:

                self.clear()

                self.numbers_var['count'] = 0
                self.res_update(self.glbl_var['lvl'] * 3)

                font.setPointSize(14)

                self.lbl_cong = QLabel('Поздравляем, Вы выиграли!', self.frame)
                self.lbl_cong.setAlignment(Qt.AlignCenter)
                self.lbl_cong.setFont(font)
                self.lbl_cong.setProperty("color", "#dc3545")
                self.lbl_cong.setProperty("backcolor", "#cff4fc")
                self.lbl_cong.setGeometry(20, 10, 280, 60)

                font.setPointSize(15)

                self.restart_btn = QPushButton('Играть снова', self.frame)
                self.restart_btn.setFont(font)
                self.restart_btn.setStyleSheet("background color: #f8d7da")
                self.restart_btn.clicked.connect(lambda _: self.numbers_run())
                self.restart_btn.setGeometry(40, 90, 240, 40)

                self.show_widgets()

            if self.numbers_var['count'] == self.numbers_var["sub_lvl"] + 3:
                self.numbers_var['count'] = 0
                self.numbers_var["sub_lvl"] += 1
                self.numbers_field()
            if self.numbers_var['count'] == 1:
                for widget in self.gridLayout.children():
                    widget.setText('')
        else:
            self.clear() # очистка

            self.numbers_var['count'] = 0

            font.setPointSize(14)
            font.setBold(True)

            self.lbl_lose = QLabel("Вы проиграли", self.frame)
            self.lbl_lose.setAlignment(Qt.AlignCenter)
            self.lbl_lose.setFont(font)
            self.lbl_lose.setStyleSheet("background color: #cff4fc")
            self.lbl_lose.setGeometry(20, 10, 280, 60)

            font.setPointSize(15)
            font.setBold(False)

            self.btn_lose = QPushButton('Играть снова', self.frame)
            self.btn_lose.setFont(font)
            self.btn_lose.setStyleSheet("background color: #f8d7da")
            self.btn_lose.clicked.connect(lambda _: self.numbers_run())
            self.btn_lose.setGeometry(40, 90, 240, 40)

            self.show_widgets()

    def result_func(self):
        pass

    def exit_func(self):
        self.close()

    def clear(self):
        for widget in self.frame.children():
            widget.setParent(None)

    def show_widgets(self):
        for widget in self.frame.children():
            widget.show()

    def res_update(self, res):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
