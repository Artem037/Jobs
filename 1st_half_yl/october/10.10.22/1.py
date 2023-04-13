import csv
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget, QWidget


class MyWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.loadTable('price.csv')
        self.tableWidget.itemChanged().connect(self.update_check)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            title.append('Количество')
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                self.tableWidget.setItem(i, 2, QTableWidgetItem('0'))
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
            self.tableWidget.resizeColumnsToContents()

    def update_check(self):
        price = [int(self.tableWidget.item(i, 1).text()) for i in range(self.tableWidget.rowCount())]
        count = [int(self.tableWidget.item(i, 2).text()) if self.tableWidget.item(i, 2).text() != '' else 0 for i in range(self.tableWidget.rowCount())]
        sum_of = 0
        for i in range(len(price)):
            sum_of += price[i] * count[i]
        self.limeEdit.setText(str(sum_of))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
