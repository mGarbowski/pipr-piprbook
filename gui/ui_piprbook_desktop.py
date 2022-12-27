# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'piprbook_desktop.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.horizontalSpacer = QSpacerItem(242, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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


        self.horizontalLayout_2.addWidget(self.form_controls_container)

        self.horizontalSpacer_2 = QSpacerItem(242, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.login_form_container)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.login_page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 30, 59, 15))
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PIPRbook", None))
        self.login_page_label.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.log_in_button.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.login_failed_text.setText(QCoreApplication.translate("MainWindow", u"placeholder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Logged in", None))
    # retranslateUi

