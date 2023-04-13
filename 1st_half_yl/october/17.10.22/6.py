import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pushButton.clicked.connect(self.run)


    def run(self):
        parameter = self.comboBox.currentText()
        value = self.lineEdit.text()
        if parameter == 'Название':
            if not value.isalpha():
                self.errorLabel.setText('Неко ')
            if not value:
        con = sqlite3.connect('films_db.sqlite')
        cur = con.cursor()
        result = cur.execute(f"""SELECT * FROM films
            WHERE films.{parameter} = {value}""").fetchall()
        # id = result[0]
        # title = result[1]
        # year = result[2]
        # genre = result[6]
        # duration = result[4]
        self.idEdit.setText(result[0])
        self.idEdit.setText(result[1])
        self.idEdit.setText(result[2])
        self.idEdit.setText(result[6])
        self.idEdit.setText(result[4])
        con.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())