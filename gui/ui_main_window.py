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
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.header_label = QLabel(self.centralwidget)
        self.header_label.setObjectName(u"header_label")
        self.header_label.setGeometry(QRect(260, 60, 59, 15))
        self.user_info_label = QLabel(self.centralwidget)
        self.user_info_label.setObjectName(u"user_info_label")
        self.user_info_label.setGeometry(QRect(230, 110, 351, 231))
        self.user_info_label.setWordWrap(True)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"PIPRbook", None))
        self.header_label.setText(QCoreApplication.translate("main_window", u"Hello", None))
        self.user_info_label.setText(QCoreApplication.translate("main_window", u"user_ifno", None))
    # retranslateUi

