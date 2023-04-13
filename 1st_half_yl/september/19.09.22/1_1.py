import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        ## Подключаем цифры
        [i.clicked.connect(self.run) for i in self.buttonGroup_digits.buttons()]
        ## Подключаем бинарные операции (+,-,*,/)
        [i.clicked.connect(self.calc) for i in self.buttonGroup_binary.buttons()]
        ## Подключаем точку
        self.btn_dot.clicked.connect(self.run)
        ## Подключаем кнопку равно
        self.btn_eq.clicked.connect(self.result)
        ## Подключаем кнопку очистки
        self.btn_clear.clicked.connect(self.clear)
        ## Подключаем унарные операции
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)

        ## Переменная, в которых хранятся последнее введённое число/результат вычисленного выражения
        self.data = ''
        ## Переменная, в которых хранятся выражение, которое нужно подсчитать
        self.data_eval = ''

    def real_fact(self, n):
        if n < 0:
            return -1
        if n == 0:
            return 1
        else:
            return n * self.real_fact(n - 1)

    def fact(self):
        if self.data_eval:
            self.data_eval = "self.real_fact({})".format(self.data_eval)
            print(self.data_eval)
            self.result()

    ## Сброс всех данных, очистка экрана
    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('')

    def run(self):
        ## Формируется число, с помощью нажатий кнопок и отображается на дисплее
        if self.sender().text() == '.':
            if '.' in self.data:
                return
        if self.data != '0' or (self.data == '0' and self.sender().text() == '.'):
            self.data = self.data + self.sender().text()
            self.data_eval = self.data_eval + self.sender().text()
            self.table.display(self.data)
            print(self.table.intValue())
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)
            print(self.table.intValue())

    def sqrt(self):
        if self.data_eval:
            self.data_eval += '**0.5'
            self.result()

    def calc(self):


    def result(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())