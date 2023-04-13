import sys

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QMenu, QAction, QLabel, QPushButton, QGridLayout, \
    QWidget
from PyQt5.QtGui import QFont

from random import shuffle


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.glbl_var = {}  # общие параметры игры (уровень, результаты)
        self.numbers_var = {'count': 0}  # параметры для блока Числа
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

        self.glbl_var['lvl'] = level

        self.centralwidget = QWidget()

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setGeometry(QRect(50, 120, 600, 151))
        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(12)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.label_instr = QLabel(self.frame_2)
        self.label_instr.setGeometry(QRect(0, 0, 600, 111))
        self.label_instr.setLayoutDirection(Qt.RightToLeft)
        self.label_instr.setText("Будут показаны числа\n"
                                 "Ваша задача запомнить их расположение в порядке возрастания,\n"
                                 "и нажать на них в этом порядке.")
        self.label_instr.setStyleSheet("background-color: #cff4fc")
        self.label_instr.setFont(font)
        self.label_instr.setAlignment(Qt.AlignCenter)

        font.setPointSize(15)

        self.btn_instr = QPushButton(self.frame_2)
        self.btn_instr.setGeometry(QRect(235, 110, 131, 41))
        self.btn_instr.setText("Начать")
        self.btn_instr.setStyleSheet("background-color: #f8d7da")
        self.btn_instr.setFont(font)

        self.btn_instr.clicked.connect(lambda _: self.numbers_run())

        self.setCentralWidget(self.centralwidget)

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

        self.frame_2.hide()

        self.frame = QFrame(self)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout = QGridLayout(self.frame)

        a = [f'{j}-{i}' for j in range(6) for i in range(6)]
        shuffle(a)
        a = a[:self.numbers_var["sub_lvl"] + 3]

        for x in range(6):
            for y in range(6):
                if f'{x}-{y}' in a:
                    b = a.index(f'{x}-{y}') + 1
                    btn = QPushButton(self.frame)
                    btn.setText(str(a.index(f'{x}-{y}') + 1))
                    btn.setStyleSheet("background-color: violet")
                    btn.setFont(QFont("Calibri", 16))
                    btn.setFixedSize(100, 65)
                    btn.clicked.connect(lambda _: self.numbers_btn_click((btn, b)))
                    self.gridLayout.addWidget(btn, x, y)
                else:
                    b = 'no'
                    btn = QPushButton(self.frame)
                    btn.setStyleSheet("background-color: lavender")
                    btn.setFont(QFont("Calibri", 16))
                    btn.setFixedSize(100, 65)
                    btn.clicked.connect(lambda _: self.numbers_btn_click((btn, b)))
                    self.gridLayout.addWidget(btn, x, y)
        self.frame.setGeometry(45, 50, 600, 390)
        self.frame.show()

    def numbers_btn_click(self, params):
        pass
        # Обработка нажатия кнопок поля

        # button, b = params
        # self.numbers_var['count'] += 1
        #
        # self.frame_cong = QFrame(self)
        # self.frame_cong.setFrameShape(QFrame.StyledPanel)
        # self.frame_cong.setFrameShadow(QFrame.Raised)
        # self.frame_cong.setGeometry(170, 110, 320, 140)
        #
        # font = QFont()
        # font.setFamily("Calibri")
        #
        # if b == self.numbers_var['count']:
        #     button.setStyleSheet("background-color: lavender")
        #     if self.numbers_var['count'] == self.numbers_var["loop"]:
        #         self.frame.hide()
        #         self.numbers_var['count'] = 0
        #         self.res_update(self.glbl_var['lvl'] * 3)
        #
        #         font.setPointSize(14)
        #
        #         self.lbl_cong = QLabel('Поздравляем, Вы выиграли!', self.frame_cong)
        #         self.lbl_cong.setAlignment(Qt.AlignCenter)
        #         self.lbl_cong.setFont(font)
        #         self.lbl_cong.setProperty("color", "#dc3545")
        #         self.lbl_cong.setProperty("backcolor", "#cff4fc")
        #         self.lbl_cong.setGeometry(20, 10, 280, 60)
        #
        #         font.setPointSize(15)
        #
        #         self.restart_btn = QPushButton('Играть снова', self.frame_cong)
        #         self.restart_btn.setFont(font)
        #         self.restart_btn.setStyleSheet("background color: #f8d7da")
        #         self.restart_btn.clicked.connect(lambda _: self.numbers_run)
        #         self.restart_btn.setGeometry(40, 90, 240, 40)
        #
        #     if self.numbers_var['count'] == self.numbers_var["sub_lvl"] + 3:
        #         self.numbers_var['count'] = 0
        #         self.numbers_var["sub_lvl"] += 1
        #         self.numbers_field()
        #     if self.numbers_var['count'] == 1:
        #         for widget in self.frame.children():
        #             widget.setText('')
        # else:
        #     self.frame.hide()  # очистка
        #     self.numbers_var['count'] = 0
        #
        #     font.setPointSize(14)
        #     font.setBold(True)
        #
        #     self.lbl_lose = QLabel("Вы проиграли", self.frame_cong)
        #     self.lbl_lose.setAlignment(Qt.AlignCenter)
        #     self.lbl_lose.setFont(font)
        #     self.lbl_lose.setStyleSheet("background color: #cff4fc")
        #     self.lbl_lose.setGeometry(20, 10, 280, 60)
        #
        #     font.setPointSize(15)
        #     font.setBold(False)
        #
        #     self.btn_lose = QPushButton('Играть снова', self.frame_cong)
        #     self.btn_lose.setFont(font)
        #     self.btn_lose.setStyleSheet("background color: #f8d7da")
        #     self.btn_lose.clicked.connect(lambda _: self.numbers_run)
        #     self.btn_lose.setGeometry(40, 90, 240, 40)
        #
        #     self.frame_cong.show()

    def result_func(self):
        pass

    def exit_func(self):
        self.close()

    def clear(self):
        widgets = self.frame.layout().count()
        if widgets > 1:
            for i in range(widgets-1):
                widget = self.frame.layout().itemAt(0).widget()
                self.frame.layout().removeWidget(widget)
                widget.hide()

    def res_update(self, res):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


# и numbers_btn_click
