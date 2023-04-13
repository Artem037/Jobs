import sys
import os.path

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('file_stats.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if not os.path.exists(os.path.abspath(self.lineEdit.text())):
            self.label_5.setText(f'файл {self.lineEdit.text()} не найден')
        else:
            with open(self.lineEdit.text(), 'r', encoding="utf8") as f:
                data = f.read()
            data2 = data.split()
            if any(True for i in data2 if not i.isdigit()):
                self.label_5.setText(f'В файле {self.lineEdit.text()} содержатся некорректные данные')
            else:
                self.label_5.setText('')
                data1 = [int(i) for i in data2]
                maxx = max(data1)
                minn = min(data1)
                sr = sum(data1) / len(data1)
                self.spinBox.setValue(maxx)
                self.spinBox_2.setValue(minn)
                self.doubleSpinBox.setValue(sr)
                with open('output.txt', 'w', encoding="utf8") as f:
                    f.write(f'Максимальное значение: {str(maxx)}\n')
                    f.write(f'Минимальное значение: {str(minn)}\n')
                    f.write(f'Среднее значение: {str(sr)}\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
