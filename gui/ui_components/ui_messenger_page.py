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
        self.gridLayout = QGridLayout(MessengerPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_5 = QWidget(MessengerPage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.widget_4)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.user_info = QLabel(self.widget_3)
        self.user_info.setObjectName(u"user_info")

        self.verticalLayout_3.addWidget(self.user_info)

        self.friend_bio = QLabel(self.widget_3)
        self.friend_bio.setObjectName(u"friend_bio")

        self.verticalLayout_3.addWidget(self.friend_bio)


        self.horizontalLayout_2.addWidget(self.widget_3)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.friend_profile_picture = QLabel(self.widget_6)
        self.friend_profile_picture.setObjectName(u"friend_profile_picture")
        self.friend_profile_picture.setGeometry(QRect(100, 0, 71, 51))
        self.friend_profile_picture.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget = QWidget(self.widget_5)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.messages_container = QScrollArea(self.widget)
        self.messages_container.setObjectName(u"messages_container")
        self.messages_container.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 352, 299))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.messages = QLabel(self.scrollAreaWidgetContents)
        self.messages.setObjectName(u"messages")
        self.messages.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.messages)

        self.messages_container.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.messages_container)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.message_input = QLineEdit(self.widget_2)
        self.message_input.setObjectName(u"message_input")

        self.horizontalLayout.addWidget(self.message_input)

        self.send_button = QPushButton(self.widget_2)
        self.send_button.setObjectName(u"send_button")

        self.horizontalLayout.addWidget(self.send_button)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.widget)


        self.gridLayout.addWidget(self.widget_5, 0, 1, 1, 1)

        self.friends_list = QListWidget(MessengerPage)
        self.friends_list.setObjectName(u"friends_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.friends_list.sizePolicy().hasHeightForWidth())
        self.friends_list.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.friends_list, 0, 0, 1, 1)


        self.retranslateUi(MessengerPage)

        QMetaObject.connectSlotsByName(MessengerPage)
    # setupUi

    def retranslateUi(self, MessengerPage):
        MessengerPage.setWindowTitle(QCoreApplication.translate("MessengerPage", u"Form", None))
        self.user_info.setText(QCoreApplication.translate("MessengerPage", u"Chat with ...", None))
        self.friend_bio.setText(QCoreApplication.translate("MessengerPage", u"friend's bio", None))
        self.friend_profile_picture.setText("")
        self.messages.setText(QCoreApplication.translate("MessengerPage", u"Messages", None))
        self.send_button.setText(QCoreApplication.translate("MessengerPage", u"Send", None))
    # retranslateUi

