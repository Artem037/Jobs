import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)  # Загружаем дизайн
        self.btn1.clicked.connect(self.run)        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        text = self.btn1.text()
        self.table.setintValue(int(text))
        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())