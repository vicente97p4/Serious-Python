# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(429, 542)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.list_chat = QListWidget(self.centralwidget)
        self.list_chat.setObjectName(u"list_chat")
        self.list_chat.setGeometry(QRect(30, 10, 381, 481))
        self.edit_nickname = QLineEdit(self.centralwidget)
        self.edit_nickname.setObjectName(u"edit_nickname")
        self.edit_nickname.setGeometry(QRect(30, 500, 81, 21))
        self.edit_text = QLineEdit(self.centralwidget)
        self.edit_text.setObjectName(u"edit_text")
        self.edit_text.setGeometry(QRect(122, 500, 221, 22))
        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(354, 500, 61, 24))
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\uba54\uc2e0\uc800", None))
        self.btn_send.setText(QCoreApplication.translate("mainWindow", u"\uc804\uc1a1", None))
    # retranslateUi

