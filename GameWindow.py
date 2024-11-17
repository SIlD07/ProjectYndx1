from GameWidget import Ui_GameWidget
from PyQt6.QtWidgets import QWidget
import random


class GameWindow(QWidget, Ui_GameWidget):
    def __init__(self, file_name):
        super().__init__()
        self.hitpoints = 3
        self.lifeCounter.display(self.hitpoints)
        self.word_checker = set()
        self.file_name = file_name
        self.game()
        self.newButton.clicked.connect(self.click)
        self.oldButton.clicked.connect(self.click)

    def game(self) -> None:
        with open(self.file_name, encoding='utf-8', mode='rt') as f:
            self.all_words = list({i.strip() for i in f.readlines()})
        self.score = 0
        word = random.choice(self.all_words)
        self.wordShowingLabel.setText(word)
        self.show()

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

        while True:
            word = random.choice(self.all_words)
            if word not in self.word_checker:
                break
        self.wordShowingLabel.setText(word)

        self.lifeCounter.display(self.hitpoints)
        self.score += 1
        self.scoreCounter.display(self.score)

        if self.hitpoints == 0:
            self.end_game()

    def end_game(self) -> int:
        self.hide()
        return self.score

    # def results(self) -> int:
    #     return self.score