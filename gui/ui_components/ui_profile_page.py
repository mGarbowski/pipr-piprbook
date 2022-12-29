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
        self.verticalLayout_4 = QVBoxLayout(ProfilePage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.profile_header = QLabel(ProfilePage)
        self.profile_header.setObjectName(u"profile_header")

        self.verticalLayout_4.addWidget(self.profile_header)

        self.widget_5 = QWidget(ProfilePage)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.username_display = QLabel(self.widget_4)
        self.username_display.setObjectName(u"username_display")

        self.verticalLayout_3.addWidget(self.username_display)

        self.email_display = QLabel(self.widget_4)
        self.email_display.setObjectName(u"email_display")

        self.verticalLayout_3.addWidget(self.email_display)

        self.bio_display = QLabel(self.widget_4)
        self.bio_display.setObjectName(u"bio_display")
        self.bio_display.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.bio_display)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_3 = QWidget(ProfilePage)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bio_input = QTextEdit(self.widget)
        self.bio_input.setObjectName(u"bio_input")

        self.verticalLayout.addWidget(self.bio_input)

        self.update_bio_button = QPushButton(self.widget)
        self.update_bio_button.setObjectName(u"update_bio_button")

        self.verticalLayout.addWidget(self.update_bio_button)


        self.horizontalLayout.addWidget(self.widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.upload_profile_picture_button = QPushButton(self.widget_2)
        self.upload_profile_picture_button.setObjectName(u"upload_profile_picture_button")
        self.upload_profile_picture_button.setGeometry(QRect(30, 210, 138, 23))
        self.profile_picture = QLabel(self.widget_2)
        self.profile_picture.setObjectName(u"profile_picture")
        self.profile_picture.setGeometry(QRect(9, 9, 189, 192))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.profile_picture.sizePolicy().hasHeightForWidth())
        self.profile_picture.setSizePolicy(sizePolicy1)
        self.profile_picture.setScaledContents(True)

        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(ProfilePage)

        QMetaObject.connectSlotsByName(ProfilePage)
    # setupUi

    def retranslateUi(self, ProfilePage):
        ProfilePage.setWindowTitle(QCoreApplication.translate("ProfilePage", u"Form", None))
        self.profile_header.setText(QCoreApplication.translate("ProfilePage", u"Profile header", None))
        self.username_display.setText(QCoreApplication.translate("ProfilePage", u"Username display", None))
        self.email_display.setText(QCoreApplication.translate("ProfilePage", u"Email display", None))
        self.bio_display.setText(QCoreApplication.translate("ProfilePage", u"Bio display", None))
        self.update_bio_button.setText(QCoreApplication.translate("ProfilePage", u"Update bio", None))
        self.upload_profile_picture_button.setText(QCoreApplication.translate("ProfilePage", u"Upload profile picture", None))
        self.profile_picture.setText("")
    # retranslateUi

