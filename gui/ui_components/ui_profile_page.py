# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProfilePage(object):
    def setupUi(self, ProfilePage):
        if not ProfilePage.objectName():
            ProfilePage.setObjectName(u"ProfilePage")
        ProfilePage.resize(737, 547)
        self.bio_display = QLabel(ProfilePage)
        self.bio_display.setObjectName(u"bio_display")
        self.bio_display.setGeometry(QRect(10, 110, 241, 71))
        self.bio_display.setWordWrap(True)
        self.profile_picture_header = QLabel(ProfilePage)
        self.profile_picture_header.setObjectName(u"profile_picture_header")
        self.profile_picture_header.setGeometry(QRect(440, 90, 151, 16))
        self.bio_input = QTextEdit(ProfilePage)
        self.bio_input.setObjectName(u"bio_input")
        self.bio_input.setGeometry(QRect(30, 190, 221, 181))
        self.pushButton_2 = QPushButton(ProfilePage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 480, 80, 23))
        self.username_display = QLabel(ProfilePage)
        self.username_display.setObjectName(u"username_display")
        self.username_display.setGeometry(QRect(10, 50, 241, 16))
        self.email_display = QLabel(ProfilePage)
        self.email_display.setObjectName(u"email_display")
        self.email_display.setGeometry(QRect(10, 80, 241, 16))
        self.update_bio_button = QPushButton(ProfilePage)
        self.update_bio_button.setObjectName(u"update_bio_button")
        self.update_bio_button.setGeometry(QRect(40, 390, 211, 23))
        self.pushButton = QPushButton(ProfilePage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 480, 80, 23))
        self.upload_profile_picture_button = QPushButton(ProfilePage)
        self.upload_profile_picture_button.setObjectName(u"upload_profile_picture_button")
        self.upload_profile_picture_button.setGeometry(QRect(410, 390, 151, 23))
        self.profile_header = QLabel(ProfilePage)
        self.profile_header.setObjectName(u"profile_header")
        self.profile_header.setGeometry(QRect(20, 10, 161, 16))
        self.profile_picture = QLabel(ProfilePage)
        self.profile_picture.setObjectName(u"profile_picture")
        self.profile_picture.setGeometry(QRect(430, 210, 59, 15))
        self.profile_picture.setScaledContents(True)

        self.retranslateUi(ProfilePage)

        QMetaObject.connectSlotsByName(ProfilePage)
    # setupUi

    def retranslateUi(self, ProfilePage):
        ProfilePage.setWindowTitle(QCoreApplication.translate("ProfilePage", u"Form", None))
        self.bio_display.setText(QCoreApplication.translate("ProfilePage", u"Bio display", None))
        self.profile_picture_header.setText(QCoreApplication.translate("ProfilePage", u"Profile picture", None))
        self.pushButton_2.setText(QCoreApplication.translate("ProfilePage", u"PushButton", None))
        self.username_display.setText(QCoreApplication.translate("ProfilePage", u"Username display", None))
        self.email_display.setText(QCoreApplication.translate("ProfilePage", u"Email display", None))
        self.update_bio_button.setText(QCoreApplication.translate("ProfilePage", u"Update bio", None))
        self.pushButton.setText(QCoreApplication.translate("ProfilePage", u"PushButton", None))
        self.upload_profile_picture_button.setText(QCoreApplication.translate("ProfilePage", u"Upload profile picture", None))
        self.profile_header.setText(QCoreApplication.translate("ProfilePage", u"Profile header", None))
        self.profile_picture.setText("")
    # retranslateUi

