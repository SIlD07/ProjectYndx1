from GameWidget import Ui_GameWidget
from PyQt6.QtWidgets import QWidget, QInputDialog
import random
import sqlite3
import datetime
import time


class GameWindow(QWidget, Ui_GameWidget):
    def __init__(self, file_name):
        super().__init__()
        self.setupUi(self)
        self.hitpoints = 3
        self.lifeCounter.display(self.hitpoints)
        self.word_checker = set()
        self.file_name = file_name
        self.newButton.clicked.connect(self.click)
        self.oldButton.clicked.connect(self.click)

        self.connection = sqlite3.connect('GamesHistory.sqlite')
        self.cur = self.connection.cursor()

        self.game()

    def game(self) -> None:
        self.start_time = time.time()
        with open(self.file_name, encoding='utf-8', mode='rt') as f:
            self.all_words = list({i.strip() for i in f.readlines()})
        self.score = 0
        word = random.choice(self.all_words)
        self.wordShowingLabel.setText(word)
        self.show()
        self.first_word_flag = True

    def click(self):
        if self.sender().text() == 'Новое':
            if self.wordShowingLabel.text() in self.word_checker:
                self.hitpoints -= 1
            else:
                self.word_checker.add(self.wordShowingLabel.text())
        else:
            if self.wordShowingLabel.text() not in self.word_checker:
                self.hitpoints -= 1
                self.word_checker.add(self.wordShowingLabel.text())

        if random.choice((0, 1)) or self.first_word_flag:
            self.first_word_flag = False
            while True:
                word = random.choice(self.all_words)
                if word not in self.word_checker:
                    break
            self.wordShowingLabel.setText(word)
        else:
            while True:
                word = random.choice(list(self.word_checker))
                if word != self.wordShowingLabel.text():
                    break
                print("2")
            self.wordShowingLabel.setText(word)

        self.lifeCounter.display(self.hitpoints)
        self.score += 1
        self.scoreCounter.display(self.score)

        if self.hitpoints == 0:
            self.delta_time = time.time() - self.start_time
            self.date = '.'.join(datetime.date.today().__str__().split('-')[::-1])
            self.add_game_results(self.delta_time, self.score, self.date)
            self.close()

    def add_game_results(self, time, score, date) -> None:
        name, ok_pressed = QInputDialog.getText(self, "Введите имя",
                                                "Не более 10 символов")
        if not ok_pressed:
            name = 'Безымянный'
        name = name[:10]
        self.cur.execute('''INSERT INTO Games VALUES (?, ?, ?, ?)''',
                         (name, int(time), score, date))
        self.connection.commit()