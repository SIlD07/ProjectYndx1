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
        id_ = cur.execute('''SELECT id FROM games''').fetchall()
        time = cur.execute('''SELECT time FROM games''').fetchall()
        score = cur.execute('''SELECT score FROM games''').fetchall()
        date = cur.execute('''SELECT date FROM games''').fetchall()
        self.historyTable.setRowCount(len(id_))
        print(id_)

        for counter, i in enumerate(zip(id_, time, score, date)):
            for j in range(4):
                print(i)
                print(i[j][0])
                self.historyTable.setItem(counter, j, QTableWidgetItem(str(i[j][0])))