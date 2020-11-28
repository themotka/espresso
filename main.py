import sqlite3
import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        self.con = sqlite3.connect("coffee.sqlite")
        self.load_table()

    def load_table(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        query = "SELECT * FROM coffee"
        res = self.con.cursor().execute(query).fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
