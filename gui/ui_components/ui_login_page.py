# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(LoginPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.page_header = QLabel(LoginPage)
        self.page_header.setObjectName(u"page_header")
        self.page_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.page_header)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.username_label = QLabel(LoginPage)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout.addWidget(self.username_label)

        self.username_input = QLineEdit(LoginPage)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout.addWidget(self.username_input)

        self.password_label = QLabel(LoginPage)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout.addWidget(self.password_label)

        self.password_input = QLineEdit(LoginPage)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_input)

        self.log_in_button = QPushButton(LoginPage)
        self.log_in_button.setObjectName(u"log_in_button")

        self.verticalLayout.addWidget(self.log_in_button)

        self.login_failed_text = QLabel(LoginPage)
        self.login_failed_text.setObjectName(u"login_failed_text")

        self.verticalLayout.addWidget(self.login_failed_text)

        self.register_label = QLabel(LoginPage)
        self.register_label.setObjectName(u"register_label")

        self.verticalLayout.addWidget(self.register_label)

        self.register_button = QPushButton(LoginPage)
        self.register_button.setObjectName(u"register_button")

        self.verticalLayout.addWidget(self.register_button)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Form", None))
        self.page_header.setText(QCoreApplication.translate("LoginPage", u"Login", None))
        self.username_label.setText(QCoreApplication.translate("LoginPage", u"Username", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("LoginPage", u"username", None))
        self.password_label.setText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.log_in_button.setText(QCoreApplication.translate("LoginPage", u"Log In", None))
        self.login_failed_text.setText(QCoreApplication.translate("LoginPage", u"placeholder", None))
        self.register_label.setText(QCoreApplication.translate("LoginPage", u"or create new account", None))
        self.register_button.setText(QCoreApplication.translate("LoginPage", u"Register", None))
    # retranslateUi

