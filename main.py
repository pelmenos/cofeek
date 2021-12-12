import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        self.res = cur.execute('Select * from cofechko').fetchall()
        self.table()

    def table(self):
        self.tableWidget.setRowCount(len(self.res))
        self.tableWidget.setColumnCount(len(self.res[0]))
        for i, elem in enumerate(self.res):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
