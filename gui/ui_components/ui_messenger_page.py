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


class Ui_MessengerPage(object):
    def setupUi(self, MessengerPage):
        if not MessengerPage.objectName():
            MessengerPage.setObjectName(u"MessengerPage")
        MessengerPage.resize(670, 480)
        self.header = QLabel(MessengerPage)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(9, 9, 142, 16))
        self.user_info = QLabel(MessengerPage)
        self.user_info.setObjectName(u"user_info")
        self.user_info.setGeometry(QRect(390, 20, 111, 16))
        self.friends_list = QListWidget(MessengerPage)
        self.friends_list.setObjectName(u"friends_list")
        self.friends_list.setGeometry(QRect(20, 60, 191, 381))
        self.messages_container = QScrollArea(MessengerPage)
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
        self.message_input = QLineEdit(MessengerPage)
        self.message_input.setObjectName(u"message_input")
        self.message_input.setGeometry(QRect(360, 400, 113, 23))
        self.send_button = QPushButton(MessengerPage)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(510, 400, 80, 23))

        self.retranslateUi(MessengerPage)

        QMetaObject.connectSlotsByName(MessengerPage)
    # setupUi

    def retranslateUi(self, MessengerPage):
        MessengerPage.setWindowTitle(QCoreApplication.translate("MessengerPage", u"Form", None))
        self.header.setText(QCoreApplication.translate("MessengerPage", u"Messages", None))
        self.user_info.setText(QCoreApplication.translate("MessengerPage", u"Chat with ...", None))
        self.messages.setText(QCoreApplication.translate("MessengerPage", u"Messages", None))
        self.send_button.setText(QCoreApplication.translate("MessengerPage", u"Send", None))
    # retranslateUi

