# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messenger_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_messenger_page(object):
    def setupUi(self, messenger_page):
        if not messenger_page.objectName():
            messenger_page.setObjectName(u"messenger_page")
        messenger_page.resize(670, 480)
        self.header = QLabel(messenger_page)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(9, 9, 142, 16))
        self.user_info = QLabel(messenger_page)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setGeometry(QRect(390, 20, 111, 16))
        self.friends_list = QListWidget(messenger_page)
        self.friends_list.setObjectName(u"friends_list")
        self.friends_list.setGeometry(QRect(20, 60, 191, 381))
        self.messages_container = QScrollArea(messenger_page)
        self.messages_container.setObjectName(u"messages_container")
        self.messages_container.setGeometry(QRect(360, 160, 241, 211))
        self.messages_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 239, 209))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.messages = QLabel(self.scrollAreaWidgetContents)
        self.messages.setObjectName(u"messages")
        self.messages.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.messages)

        self.messages_container.setWidget(self.scrollAreaWidgetContents)
        self.message_input = QLineEdit(messenger_page)
        self.message_input.setObjectName(u"message_input")
        self.message_input.setGeometry(QRect(360, 400, 113, 23))
        self.send_button = QPushButton(messenger_page)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(510, 400, 80, 23))

        self.retranslateUi(messenger_page)

        QMetaObject.connectSlotsByName(messenger_page)
    # setupUi

    def retranslateUi(self, messenger_page):
        messenger_page.setWindowTitle(QCoreApplication.translate("messenger_page", u"Form", None))
        self.header.setText(QCoreApplication.translate("messenger_page", u"Messages", None))
        self.user_info.setText(QCoreApplication.translate("messenger_page", u"Chat with ...", None))
        self.messages.setText(QCoreApplication.translate("messenger_page", u"Messages", None))
        self.send_button.setText(QCoreApplication.translate("messenger_page", u"Send", None))
    # retranslateUi

