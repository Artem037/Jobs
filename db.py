import sys

import string

import sqlite3

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QFrame, QMenu, QAction, QLabel, QPushButton, QGridLayout, \
    QWidget, QLineEdit, QDialog
from PyQt5.QtGui import QFont

from random import shuffle


class MemoSquare(QMainWindow):
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
        self.label_instr.setGeometry(50, 120, 600, 100)
        self.label_instr.setText("Будут показаны числа\n"
                                 "Ваша задача запомнить их расположение в порядке возрастания,\n"
                                 "и нажать на них в этом порядке.")
        self.label_instr.setStyleSheet("background-color: #cff4fc")
        self.label_instr.setFont(font)
        self.label_instr.setAlignment(Qt.AlignCenter)

        font.setPointSize(16)

        self.btn_instr = QPushButton(self.frame)
        self.btn_instr.setGeometry(285, 270, 130, 40)
        self.btn_instr.setText("Начать")
        self.btn_instr.setStyleSheet("background-color: #f8d7da")
        self.btn_instr.setFont(font)

        self.btn_instr.clicked.connect(self.numbers_run)

        font.setPointSize(12)

        self.label = QLabel(self.frame)
        self.label.setGeometry(80, 230, 210, 30)
        self.label.setText("Введите ваш никнейм:")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: #cff4fc")
        self.label.setFont(font)

        self.line_edit = QLineEdit(self.frame)
        self.line_edit.setGeometry(300, 230, 270, 30)
        self.line_edit.setFont(font)
        self.line_edit.setStyleSheet("background-color: white")

        self.show_widgets()

    def numbers_run(self):
        # Проверка на корректность никнейма

        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setPointSize(12)

        dlg = QDialog(self)
        dlg.setStyleSheet("background-color: #cff4fc;")
        dlg.setGeometry(150, 200, 410, 70)
        dlg.setWindowTitle('ERROR')

        allowed_symbols = ''.join(
            [chr(i) for i in range(
                ord('а'), ord('а') + 32)]) + ''.join([chr(i) for i in range(
                    ord('А'), ord('А') + 32)]) + string.ascii_lowercase + string.ascii_uppercase + string.digits + '-_'

        if self.line_edit.text():
            if len(self.line_edit.text()) > 25:
                error_lbl = QLabel(dlg)
                error_lbl.setFont(font)
                error_lbl.setGeometry(20, 10, 370, 50)
                error_lbl.setText("Вы ввели слишком длинный никнейм\nпопробуйте заново!")
                error_lbl.setAlignment(Qt.AlignCenter)
                dlg.exec()
                self.numbers_menu_click(self.glbl_var['lvl'])
            else:
                for symb in self.line_edit.text():
                    if symb not in allowed_symbols:
                        error1_lbl = QLabel(dlg)
                        error1_lbl.setFont(font)
                        error1_lbl.setGeometry(20, 10, 360, 50)
                        error1_lbl.setText("Вы ввели никнейм с недопущенными символами\nпопробуйте заново!")
                        error1_lbl.setAlignment(Qt.AlignCenter)
                        dlg.exec()
                        self.numbers_menu_click(self.glbl_var['lvl'])
                        break
                else:
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
        else:
            error2_label = QLabel(dlg)
            error2_label.setFont(font)
            error2_label.setGeometry(20, 10, 370, 50)
            error2_label.setText("Перед началом игры пожалуйста введите никнейм")
            error2_label.setAlignment(Qt.AlignCenter)
            dlg.exec()
            self.numbers_menu_click(self.glbl_var['lvl'])

    def numbers_field(self):
        # Создание поля

        self.clear()

        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QRect(45, 50, 600, 390))

        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(0)

        a = [f'{i}-{j}' for j in range(6) for i in range(6)]
        shuffle(a)
        a = a[:self.numbers_var["sub_lvl"] + 3]

        self.btns = []

        for x in range(6):
            for y in range(6):
                if f'{x}-{y}' in a:
                    b = a.index(f'{x}-{y}') + 1
                    btn = QPushButton(self.frame)
                    self.btns.append(btn)
                    btn.setObjectName(str(b))
                    btn.setText(str(a.index(f'{x}-{y}') + 1))
                    btn.setStyleSheet("background-color: violet")
                    btn.setFont(QFont("Calibri", 16))
                    btn.setFixedSize(100, 65)
                    btn.clicked.connect(self.numbers_btn_click)
                    self.gridLayout.addWidget(btn, x, y)
                else:
                    b = 'no'
                    btn = QPushButton(self.frame)
                    btn.setObjectName(b)
                    btn.setStyleSheet("background-color: lavender")
                    btn.setFont(QFont("Calibri", 16))
                    btn.setFixedSize(100, 65)
                    btn.clicked.connect(self.numbers_btn_click)
                    self.gridLayout.addWidget(btn, x, y)

        self.show_widgets()

    def numbers_btn_click(self):
        # Обработка нажатия кнопок поля
        if self.sender().objectName() == 'no':
            b = 'no'
        else:
            b = int(self.sender().objectName())

        self.numbers_var['count'] += 1

        font = QFont()
        font.setFamily("Calibri")
        font.setBold(True)

        if b == self.numbers_var['count']:

            self.sender().setStyleSheet("background-color: lavender")
            if self.numbers_var['count'] == self.numbers_var["loop"]:
                self.clear()

                self.numbers_var['count'] = 0
                self.res_update(self.glbl_var['lvl'] * 3, self.line_edit.text())

                font.setPointSize(14)

                self.lbl_cong = QLabel('Поздравляем, Вы выиграли!', self.frame)
                self.lbl_cong.setAlignment(Qt.AlignCenter)
                self.lbl_cong.setFont(font)
                self.lbl_cong.setProperty("color", "#dc3545")
                self.lbl_cong.setProperty("backcolor", "#cff4fc")
                self.lbl_cong.setGeometry(210, 100, 280, 40)

                self.lbl_res = QLabel(f'Заработанные очки: {self.glbl_var["lvl"] * 3}', self.frame)
                self.lbl_res.setAlignment(Qt.AlignCenter)
                self.lbl_res.setFont(font)
                self.lbl_res.setProperty("color", "#dc3545")
                self.lbl_res.setProperty("backcolor", "#cff4fc")
                self.lbl_res.setGeometry(240, 180, 220, 40)

                font.setPointSize(16)

                self.restart_btn = QPushButton('Играть снова', self.frame)
                self.restart_btn.setFont(font)
                self.restart_btn.setStyleSheet("background-color: #f8d7da")
                self.restart_btn.clicked.connect(self.numbers_run)
                self.restart_btn.setGeometry(250, 260, 190, 60)

                self.show_widgets()

            if self.numbers_var['count'] == self.numbers_var["sub_lvl"] + 3:
                self.numbers_var['count'] = 0
                self.numbers_var["sub_lvl"] += 1
                self.numbers_field()
            if self.numbers_var['count'] == 1:
                for btn in self.btns:
                    btn.setText('')
        else:

            self.clear()  # очистка

            self.numbers_var['count'] = 0

            font.setPointSize(14)

            self.lbl_lose = QLabel("Вы проиграли", self.frame)
            self.lbl_lose.setAlignment(Qt.AlignCenter)
            self.lbl_lose.setFont(font)
            self.lbl_lose.setStyleSheet("background color: #cff4fc")
            self.lbl_lose.setGeometry(280, 100, 140, 40)

            font.setPointSize(16)
            font.setBold(False)

            self.btn_lose = QPushButton('Играть снова', self.frame)
            self.btn_lose.setFont(font)
            self.btn_lose.setStyleSheet("background-color: #f8d7da")
            self.btn_lose.clicked.connect(self.numbers_run)
            self.btn_lose.setGeometry(250, 180, 190, 40)

            self.show_widgets()

    def result_func(self):
        if 'lvl' in self.glbl_var.keys():
            with sqlite3.connect('database.db') as db:
                cursor = db.cursor()

                query2 = '''SELECT * from players'''

                data = cursor.execute(query2).fetchall()

                db.commit()
                cursor.close()

            if data:
                nicknames = list(map(lambda x: x[1], data))

                if len(data) < 5:
                    data_top5 = sorted(data, key=lambda x: x[-1], reverse=True)[:len(data)]
                else:
                    data_top5 = sorted(data, key=lambda x: x[-1], reverse=True)[:5]

                data_pp = list(map(lambda x: [x[1], str(x[2])], data_top5))

                text = 'Лучшие игроки:' + '\n' + '\n'.join([' - '.join(i) for i in data_pp])
                if self.line_edit.text() in nicknames:
                    ind = nicknames.index(self.line_edit.text())
                    text += '\n' + 'Ваш результат: ' + data[ind][1] + ' - ' + str(data[ind][2])

                self.clear()

                font = QFont()
                font.setFamily("Calibri")
                font.setBold(True)
                font.setPointSize(22)

                lbl_res = QLabel(self.frame)
                lbl_res.setText(text)
                lbl_res.setFont(font)
                lbl_res.setAlignment(Qt.AlignCenter)
                lbl_res.adjustSize()

                x = (700 - lbl_res.geometry().width()) // 2
                y = (500 - lbl_res.geometry().height()) // 2

                lbl_res.move(x, y)
                lbl_res.show()

    def exit_func(self):
        self.close()

    def clear(self):
        for widget in self.frame.children():
            widget.setParent(None)

    def show_widgets(self):
        for widget in self.frame.children():
            widget.show()

    def res_update(self, res, nickname):
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()

            query2 = '''SELECT * from players'''

            data = cursor.execute(query2).fetchall()

            nicknames = list(map(lambda x: x[1], data))

            if nickname in nicknames:
                query1 = f"""UPDATE players set points=points+{int(res)} WHERE nickname=?"""
                cursor.execute(query1, (nickname,))
            else:
                query = f"""INSERT INTO players (nickname, points) VALUES (?, ?)"""
                cursor.execute(query, (nickname, res))

            db.commit()
            cursor.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ms = MemoSquare()
    ms.show()
    sys.exit(app.exec())
