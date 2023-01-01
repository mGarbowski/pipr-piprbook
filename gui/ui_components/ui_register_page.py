# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        if not RegisterPage.objectName():
            RegisterPage.setObjectName(u"RegisterPage")
        RegisterPage.resize(887, 664)
        self.verticalLayout_2 = QVBoxLayout(RegisterPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.page_header = QLabel(RegisterPage)
        self.page_header.setObjectName(u"page_header")
        self.page_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.page_header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.username_label = QLabel(RegisterPage)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(RegisterPage)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.email_label = QLabel(RegisterPage)
        self.email_label.setObjectName(u"email_label")

        self.verticalLayout.addWidget(self.email_label)

        self.email_input = QLineEdit(RegisterPage)
        self.email_input.setObjectName(u"email_input")

        self.verticalLayout.addWidget(self.email_input)

        self.password_label = QLabel(RegisterPage)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(RegisterPage)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.confirm_password_label = QLabel(RegisterPage)
        self.confirm_password_label.setObjectName(u"confirm_password_label")

        self.verticalLayout.addWidget(self.confirm_password_label)

        self.confirm_password_input = QLineEdit(RegisterPage)
        self.confirm_password_input.setObjectName(u"confirm_password_input")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.confirm_password_input)

        self.register_button = QPushButton(RegisterPage)
        self.register_button.setObjectName(u"register_button")

        self.verticalLayout.addWidget(self.register_button)

        self.registration_failed_text = QLabel(RegisterPage)
        self.registration_failed_text.setObjectName(u"registration_failed_text")

        self.verticalLayout.addWidget(self.registration_failed_text)

        self.back_label = QLabel(RegisterPage)
        self.back_label.setObjectName(u"back_label")

        self.verticalLayout.addWidget(self.back_label)

        self.back_button = QPushButton(RegisterPage)
        self.back_button.setObjectName(u"back_button")

        self.verticalLayout.addWidget(self.back_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 318, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(RegisterPage)

        QMetaObject.connectSlotsByName(RegisterPage)
    # setupUi

    def retranslateUi(self, RegisterPage):
        RegisterPage.setWindowTitle(QCoreApplication.translate("RegisterPage", u"Form", None))
        self.page_header.setText(QCoreApplication.translate("RegisterPage", u"Register", None))
        self.username_label.setText(QCoreApplication.translate("RegisterPage", u"Username", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("RegisterPage", u"username", None))
        self.email_label.setText(QCoreApplication.translate("RegisterPage", u"Email address", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("RegisterPage", u"email@example.com", None))
        self.password_label.setText(QCoreApplication.translate("RegisterPage", u"Password", None))
        self.confirm_password_label.setText(QCoreApplication.translate("RegisterPage", u"Confirm password", None))
        self.register_button.setText(QCoreApplication.translate("RegisterPage", u"Create account", None))
        self.registration_failed_text.setText(QCoreApplication.translate("RegisterPage", u"placeholder", None))
        self.back_label.setText(QCoreApplication.translate("RegisterPage", u"or log in to an existing account", None))
        self.back_button.setText(QCoreApplication.translate("RegisterPage", u"Back", None))
    # retranslateUi

