# Form implementation generated from reading ui file 'HistoryWidget.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(924, 504)
        self.historyTable = QtWidgets.QTableWidget(parent=Form)
        self.historyTable.setGeometry(QtCore.QRect(150, 30, 641, 211))
        self.historyTable.setMaximumSize(QtCore.QSize(16777215, 211))
        self.historyTable.setStyleSheet("background-color: rgb(255, 255, 215);")
        self.historyTable.setObjectName("historyTable")
        self.historyTable.setColumnCount(0)
        self.historyTable.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
