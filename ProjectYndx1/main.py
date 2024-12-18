import sys
import datetime
import sqlite3
from FirstWindow import Ui_MainWindow

from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow

from GameWindow import GameWindow
from HistoryWindow import HistoryWindow


class StartWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.startButton.clicked.connect(self.start_test)
        self.historyButton.clicked.connect(self.open_history_db)
        self.clearButton.clicked.connect(self.clear_history_db)

        self.connection = sqlite3.connect('GamesHistory.sqlite')
        self.cur = self.connection.cursor()

        self.setFixedSize(1100, 680)

    def open_history_db(self) -> None:
        self.table = HistoryWindow()
        self.table.show()

    def clear_history_db(self) -> None:
        self.cur.execute('''DELETE FROM Games''')

    def start_test(self) -> None:
        start_time = datetime.time()
        game = GameWindow('../ProjectYndx1/a_bunch_of_words.txt')
        self.score = game
        self.delta_time = datetime.time() - start_time
        self.date = '.'.join(datetime.date.today().__str__().split('-')[::-1])
        self.add_game_results(self.delta_time, self.score, self.date)

    def add_game_results(self, time, score, date) -> None:
        self.cur.execute('''INSERT INTO Games VALUES (?, ?, ?)''',
                         (time, score, date))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    ex = StartWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
