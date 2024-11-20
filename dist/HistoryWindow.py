from HistoryWidget import Ui_Form
from PyQt6.QtWidgets import QWidget, QTableWidgetItem
import sqlite3


class HistoryWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.historyTable.setColumnCount(4)
        for i in range(4):
            self.historyTable.setColumnWidth(i, self.historyTable.width() // 4 - 4)
        self.historyTable.setHorizontalHeaderLabels(('ID', 'Time', 'Score', 'Date'))
        self.connection = sqlite3.connect('GamesHistory.sqlite')
        cur = self.connection.cursor()
        name = cur.execute('''SELECT name FROM games''').fetchall()
        time = cur.execute('''SELECT time FROM games''').fetchall()
        score = cur.execute('''SELECT score FROM games''').fetchall()
        date = cur.execute('''SELECT date FROM games''').fetchall()
        self.historyTable.setRowCount(len(name))

        for counter, i in enumerate(zip(name, time, score, date)):
            for j in range(4):
                self.historyTable.setItem(counter, j, QTableWidgetItem(str(i[j][0])))