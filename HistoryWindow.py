from HistoryWidget import Ui_Form
from PyQt6.QtWidgets import QWidget, QTableWidgetItem
import sqlite3


class HistoryWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.historyTable.setColumnCount(4)
        self.historyTable.setHorizontalHeaderLabels(('ID', 'Time', 'Score', 'Date'))
        self.connection = sqlite3.connect('GamesHistory.sqlite')
        cur = self.connection.cursor()
        id = cur.execute('''SELECT id FROM games''')
        time = cur.execute('''SELECT time FROM games''')
        score = cur.execute('''SELECT score FROM games''')
        date = cur.execute('''SELECT date FROM games''')
        self.historyTable.setColumnCount(len(list(id)))

        for counter, i in enumerate(zip(id, time, score, date)):
            for j in range(4):
                self.historyTable.setItem(counter, j, QTableWidgetItem(i[j]))