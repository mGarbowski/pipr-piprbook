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
        InviteFriendsPage.resize(682, 590)
        self.verticalLayout_5 = QVBoxLayout(InviteFriendsPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_bar = QLineEdit(InviteFriendsPage)
        self.search_bar.setObjectName(u"search_bar")

        self.horizontalLayout.addWidget(self.search_bar)

        self.search_button = QPushButton(InviteFriendsPage)
        self.search_button.setObjectName(u"search_button")

        self.horizontalLayout.addWidget(self.search_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.search_result_label = QLabel(InviteFriendsPage)
        self.search_result_label.setObjectName(u"search_result_label")

        self.horizontalLayout_3.addWidget(self.search_result_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.invite_button = QPushButton(InviteFriendsPage)
        self.invite_button.setObjectName(u"invite_button")

        self.horizontalLayout_3.addWidget(self.invite_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.search_result = QListWidget(InviteFriendsPage)
        self.search_result.setObjectName(u"search_result")

        self.verticalLayout_2.addWidget(self.search_result)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.awaiting_invitations_label = QLabel(InviteFriendsPage)
        self.awaiting_invitations_label.setObjectName(u"awaiting_invitations_label")

        self.verticalLayout.addWidget(self.awaiting_invitations_label)

        self.awaiting_invitations = QListWidget(InviteFriendsPage)
        self.awaiting_invitations.setObjectName(u"awaiting_invitations")

        self.verticalLayout.addWidget(self.awaiting_invitations)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.accept_button = QPushButton(InviteFriendsPage)
        self.accept_button.setObjectName(u"accept_button")

        self.horizontalLayout_2.addWidget(self.accept_button)

        self.ignore_button = QPushButton(InviteFriendsPage)
        self.ignore_button.setObjectName(u"ignore_button")

        self.horizontalLayout_2.addWidget(self.ignore_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sent_invitations_label = QLabel(InviteFriendsPage)
        self.sent_invitations_label.setObjectName(u"sent_invitations_label")

        self.verticalLayout_3.addWidget(self.sent_invitations_label)

        self.sent_invitations = QListWidget(InviteFriendsPage)
        self.sent_invitations.setObjectName(u"sent_invitations")

        self.verticalLayout_3.addWidget(self.sent_invitations)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.cancel_button = QPushButton(InviteFriendsPage)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_4.addWidget(self.cancel_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.retranslateUi(InviteFriendsPage)

        QMetaObject.connectSlotsByName(InviteFriendsPage)
    # setupUi

    def retranslateUi(self, InviteFriendsPage):
        InviteFriendsPage.setWindowTitle(QCoreApplication.translate("InviteFriendsPage", u"Form", None))
        self.search_bar.setPlaceholderText(QCoreApplication.translate("InviteFriendsPage", u"username", None))
        self.search_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Search", None))
        self.search_result_label.setText(QCoreApplication.translate("InviteFriendsPage", u"Users", None))
        self.invite_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Invite", None))
        self.awaiting_invitations_label.setText(QCoreApplication.translate("InviteFriendsPage", u"Awaiting invitations", None))
        self.accept_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Accept", None))
        self.ignore_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Ignore", None))
        self.sent_invitations_label.setText(QCoreApplication.translate("InviteFriendsPage", u"Sent invitations", None))
        self.cancel_button.setText(QCoreApplication.translate("InviteFriendsPage", u"Cancel", None))
    # retranslateUi

