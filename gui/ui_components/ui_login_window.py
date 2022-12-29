# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(719, 554)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout = QVBoxLayout(self.login_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login_page_label = QLabel(self.login_page)
        self.login_page_label.setObjectName(u"login_page_label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_page_label.sizePolicy().hasHeightForWidth())
        self.login_page_label.setSizePolicy(sizePolicy)
        self.login_page_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.login_page_label)

        self.login_form_container = QWidget(self.login_page)
        self.login_form_container.setObjectName(u"login_form_container")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_form_container.sizePolicy().hasHeightForWidth())
        self.login_form_container.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.login_form_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.form_controls_container = QWidget(self.login_form_container)
        self.form_controls_container.setObjectName(u"form_controls_container")
        self.verticalLayout_3 = QVBoxLayout(self.form_controls_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.username_label = QLabel(self.form_controls_container)
        self.username_label.setObjectName(u"username_label")

        self.verticalLayout_3.addWidget(self.username_label)

        self.username_input = QLineEdit(self.form_controls_container)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout_3.addWidget(self.username_input)

        self.password_label = QLabel(self.form_controls_container)
        self.password_label.setObjectName(u"password_label")

        self.verticalLayout_3.addWidget(self.password_label)

        self.password_input = QLineEdit(self.form_controls_container)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.password_input)

        self.log_in_button = QPushButton(self.form_controls_container)
        self.log_in_button.setObjectName(u"log_in_button")

        self.verticalLayout_3.addWidget(self.log_in_button)

        self.login_failed_text = QLabel(self.form_controls_container)
        self.login_failed_text.setObjectName(u"login_failed_text")

        self.verticalLayout_3.addWidget(self.login_failed_text)

        self.register_label = QLabel(self.form_controls_container)
        self.register_label.setObjectName(u"register_label")

        self.verticalLayout_3.addWidget(self.register_label)

        self.register_button = QPushButton(self.form_controls_container)
        self.register_button.setObjectName(u"register_button")

        self.verticalLayout_3.addWidget(self.register_button)


        self.horizontalLayout_2.addWidget(self.form_controls_container)

        self.horizontalSpacer_2 = QSpacerItem(250, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.login_form_container)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.verticalLayout_2 = QVBoxLayout(self.register_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.register_page_label = QLabel(self.register_page)
        self.register_page_label.setObjectName(u"register_page_label")

        self.verticalLayout_2.addWidget(self.register_page_label)

        self.username_label_2 = QLabel(self.register_page)
        self.username_label_2.setObjectName(u"username_label_2")

        self.verticalLayout_2.addWidget(self.username_label_2)

        self.username_input_2 = QLineEdit(self.register_page)
        self.username_input_2.setObjectName(u"username_input_2")

        self.verticalLayout_2.addWidget(self.username_input_2)

        self.email_label = QLabel(self.register_page)
        self.email_label.setObjectName(u"email_label")

        self.verticalLayout_2.addWidget(self.email_label)

        self.email_input = QLineEdit(self.register_page)
        self.email_input.setObjectName(u"email_input")

        self.verticalLayout_2.addWidget(self.email_input)

        self.password_label_2 = QLabel(self.register_page)
        self.password_label_2.setObjectName(u"password_label_2")

        self.verticalLayout_2.addWidget(self.password_label_2)

        self.password_input_2 = QLineEdit(self.register_page)
        self.password_input_2.setObjectName(u"password_input_2")
        self.password_input_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.password_input_2)

        self.confirm_password_label = QLabel(self.register_page)
        self.confirm_password_label.setObjectName(u"confirm_password_label")

        self.verticalLayout_2.addWidget(self.confirm_password_label)

        self.confirm_password_input = QLineEdit(self.register_page)
        self.confirm_password_input.setObjectName(u"confirm_password_input")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.confirm_password_input)

        self.create_account_button = QPushButton(self.register_page)
        self.create_account_button.setObjectName(u"create_account_button")

        self.verticalLayout_2.addWidget(self.create_account_button)

        self.registration_failed_message = QLabel(self.register_page)
        self.registration_failed_message.setObjectName(u"registration_failed_message")

        self.verticalLayout_2.addWidget(self.registration_failed_message)

        self.back_to_login_label = QLabel(self.register_page)
        self.back_to_login_label.setObjectName(u"back_to_login_label")
        self.back_to_login_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.back_to_login_label)

        self.back_to_login_button = QPushButton(self.register_page)
        self.back_to_login_button.setObjectName(u"back_to_login_button")

        self.verticalLayout_2.addWidget(self.back_to_login_button)

        self.stackedWidget.addWidget(self.register_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 719, 20))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"PIPRbook Login", None))
        self.login_page_label.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
        self.username_label.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"username", None))
        self.password_label.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"password", None))
        self.log_in_button.setText(QCoreApplication.translate("LoginWindow", u"Log in", None))
        self.login_failed_text.setText(QCoreApplication.translate("LoginWindow", u"placeholder", None))
        self.register_label.setText(QCoreApplication.translate("LoginWindow", u"or create new account", None))
        self.register_button.setText(QCoreApplication.translate("LoginWindow", u"Register", None))
        self.register_page_label.setText(QCoreApplication.translate("LoginWindow", u"Register", None))
        self.username_label_2.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.username_input_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"username", None))
        self.email_label.setText(QCoreApplication.translate("LoginWindow", u"Email address", None))
        self.email_input.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"email@example.com", None))
        self.password_label_2.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.password_input_2.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"password", None))
        self.confirm_password_label.setText(QCoreApplication.translate("LoginWindow", u"Confirm password", None))
        self.confirm_password_input.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"password", None))
        self.create_account_button.setText(QCoreApplication.translate("LoginWindow", u"Create account", None))
        self.registration_failed_message.setText(QCoreApplication.translate("LoginWindow", u"placeholder", None))
        self.back_to_login_label.setText(QCoreApplication.translate("LoginWindow", u"or log in to an existing account", None))
        self.back_to_login_button.setText(QCoreApplication.translate("LoginWindow", u"Back", None))
    # retranslateUi

