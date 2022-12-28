# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 600)
        self.action_log_out = QAction(main_window)
        self.action_log_out.setObjectName(u"action_log_out")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.profile_picture_header = QLabel(self.profile_page)
        self.profile_picture_header.setObjectName(u"profile_picture_header")
        self.profile_picture_header.setGeometry(QRect(470, 110, 151, 16))
        self.profile_picture = QLabel(self.profile_page)
        self.profile_picture.setObjectName(u"profile_picture")
        self.profile_picture.setGeometry(QRect(470, 150, 211, 181))
        self.profile_picture.setScaledContents(True)
        self.profile_header = QLabel(self.profile_page)
        self.profile_header.setObjectName(u"profile_header")
        self.profile_header.setGeometry(QRect(50, 20, 161, 16))
        self.username_display = QLabel(self.profile_page)
        self.username_display.setObjectName(u"username_display")
        self.username_display.setGeometry(QRect(40, 70, 241, 16))
        self.email_display = QLabel(self.profile_page)
        self.email_display.setObjectName(u"email_display")
        self.email_display.setGeometry(QRect(40, 100, 241, 16))
        self.bio_display = QLabel(self.profile_page)
        self.bio_display.setObjectName(u"bio_display")
        self.bio_display.setGeometry(QRect(40, 130, 241, 71))
        self.bio_display.setWordWrap(True)
        self.bio_input = QTextEdit(self.profile_page)
        self.bio_input.setObjectName(u"bio_input")
        self.bio_input.setGeometry(QRect(60, 210, 221, 181))
        self.update_bio_button = QPushButton(self.profile_page)
        self.update_bio_button.setObjectName(u"update_bio_button")
        self.update_bio_button.setGeometry(QRect(70, 410, 211, 23))
        self.upload_profile_picture_button = QPushButton(self.profile_page)
        self.upload_profile_picture_button.setObjectName(u"upload_profile_picture_button")
        self.upload_profile_picture_button.setGeometry(QRect(440, 410, 151, 23))
        self.pages.addWidget(self.profile_page)
        self.messenger_page = QWidget()
        self.messenger_page.setObjectName(u"messenger_page")
        self.pages.addWidget(self.messenger_page)
        self.invite_friends_page = QWidget()
        self.invite_friends_page.setObjectName(u"invite_friends_page")
        self.pages.addWidget(self.invite_friends_page)

        self.horizontalLayout.addWidget(self.pages)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.action_log_out)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"PIPRbook", None))
        self.action_log_out.setText(QCoreApplication.translate("main_window", u"Log out", None))
        self.profile_picture_header.setText(QCoreApplication.translate("main_window", u"Profile picture", None))
        self.profile_picture.setText("")
        self.profile_header.setText(QCoreApplication.translate("main_window", u"Profile header", None))
        self.username_display.setText(QCoreApplication.translate("main_window", u"Username display", None))
        self.email_display.setText(QCoreApplication.translate("main_window", u"Email display", None))
        self.bio_display.setText(QCoreApplication.translate("main_window", u"Bio display", None))
        self.update_bio_button.setText(QCoreApplication.translate("main_window", u"Update bio", None))
        self.upload_profile_picture_button.setText(QCoreApplication.translate("main_window", u"Upload profile picture", None))
        self.menuOptions.setTitle(QCoreApplication.translate("main_window", u"Options", None))
    # retranslateUi

