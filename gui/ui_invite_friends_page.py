# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invite_friends_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InviteFriendsPage(object):
    def setupUi(self, InviteFriendsPage):
        if not InviteFriendsPage.objectName():
            InviteFriendsPage.setObjectName(u"InviteFriendsPage")
        InviteFriendsPage.resize(537, 567)
        self.search_bar = QLineEdit(InviteFriendsPage)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setGeometry(QRect(60, 30, 231, 23))
        self.search_button = QPushButton(InviteFriendsPage)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(330, 30, 80, 23))
        self.search_result = QListWidget(InviteFriendsPage)
        self.search_result.setObjectName(u"search_result")
        self.search_result.setGeometry(QRect(60, 80, 221, 121))
        self.awaiting_invitations = QListWidget(InviteFriendsPage)
        self.awaiting_invitations.setObjectName(u"awaiting_invitations")
        self.awaiting_invitations.setGeometry(QRect(60, 250, 211, 141))
        self.invite_button = QPushButton(InviteFriendsPage)
        self.invite_button.setObjectName(u"invite_button")
        self.invite_button.setGeometry(QRect(330, 110, 80, 23))
        self.accept_button = QPushButton(InviteFriendsPage)
        self.accept_button.setObjectName(u"accept_button")
        self.accept_button.setGeometry(QRect(330, 280, 80, 23))
        self.ignore_button = QPushButton(InviteFriendsPage)
        self.ignore_button.setObjectName(u"ignore_button")
        self.ignore_button.setGeometry(QRect(330, 320, 80, 23))
        self.sent_invitations = QListWidget(InviteFriendsPage)
        self.sent_invitations.setObjectName(u"sent_invitations")
        self.sent_invitations.setGeometry(QRect(60, 450, 191, 91))
        self.search_result_label = QLabel(InviteFriendsPage)
        self.search_result_label.setObjectName(u"search_result_label")
        self.search_result_label.setGeometry(QRect(60, 60, 59, 15))
        self.awaiting_invitations_label = QLabel(InviteFriendsPage)
        self.awaiting_invitations_label.setObjectName(u"awaiting_invitations_label")
        self.awaiting_invitations_label.setGeometry(QRect(60, 230, 201, 16))
        self.sent_invitations_label = QLabel(InviteFriendsPage)
        self.sent_invitations_label.setObjectName(u"sent_invitations_label")
        self.sent_invitations_label.setGeometry(QRect(70, 430, 121, 16))

        self.retranslateUi(InviteFriendsPage)

        QMetaObject.connectSlotsByName(InviteFriendsPage)
    # setupUi

    def retranslateUi(self, InviteFriendsPage):
        InviteFriendsPage.setWindowTitle(QCoreApplication.translate("InviteFriendsPage", u"Form", None))
        self.search_bar.setPlaceholderText(QCoreApplication.translate("InviteFriendsPage", u"username", None))
        self.search_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Search", None))
        self.invite_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Invite", None))
        self.accept_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Accept", None))
        self.ignore_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Ignore", None))
        self.search_result_label.setText(QCoreApplication.translate("InviteFriendsPage", u"Users", None))
        self.awaiting_invitations_label.setText(QCoreApplication.translate("InviteFriendsPage", u"Awaiting invitations", None))
        self.sent_invitations_label.setText(QCoreApplication.translate("InviteFriendsPage", u"Sent invitations", None))
    # retranslateUi

