# Form implementation generated from reading ui file 'GameWidget.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GameWidget(object):
    def setupUi(self, GameWidget):
        GameWidget.setObjectName("GameWidget")
        GameWidget.resize(984, 576)
        self.newButton = QtWidgets.QPushButton(parent=GameWidget)
        self.newButton.setGeometry(QtCore.QRect(550, 340, 111, 41))
        self.newButton.setObjectName("newButton")
        self.oldButton = QtWidgets.QPushButton(parent=GameWidget)
        self.oldButton.setGeometry(QtCore.QRect(310, 340, 111, 41))
        self.oldButton.setObjectName("oldButton")
        self.wordShowingLabel = QtWidgets.QLabel(parent=GameWidget)
        self.wordShowingLabel.setGeometry(QtCore.QRect(445, 200, 300, 81))
        self.wordShowingLabel.setObjectName("wordShowingLabel")
        self.label = QtWidgets.QLabel(parent=GameWidget)
        self.label.setGeometry(QtCore.QRect(400, 110, 71, 41))
        self.label.setObjectName("label")
        self.scoreCounter = QtWidgets.QLCDNumber(parent=GameWidget)
        self.scoreCounter.setGeometry(QtCore.QRect(500, 110, 81, 41))
        self.scoreCounter.setObjectName("scoreCounter")
        self.label_2 = QtWidgets.QLabel(parent=GameWidget)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 181, 51))
        self.label_2.setObjectName("label_2")
        self.lifeCounter = QtWidgets.QLCDNumber(parent=GameWidget)
        self.lifeCounter.setGeometry(QtCore.QRect(500, 50, 81, 41))
        self.lifeCounter.setObjectName("lifeCounter")

        self.retranslateUi(GameWidget)
        QtCore.QMetaObject.connectSlotsByName(GameWidget)

    def retranslateUi(self, GameWidget):
        _translate = QtCore.QCoreApplication.translate
        GameWidget.setWindowTitle(_translate("GameWidget", "Form"))
        self.newButton.setText(_translate("GameWidget", "Новое"))
        self.oldButton.setText(_translate("GameWidget", "Было"))
        self.wordShowingLabel.setText(_translate("GameWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">TextLabel</span></p></body></html>"))
        self.label.setText(_translate("GameWidget", "<html><head/><body><p><span style=\" font-size:11pt;\">Счёт:</span></p></body></html>"))
        self.label_2.setText(_translate("GameWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Осталось попыток:</span></p></body></html>"))
