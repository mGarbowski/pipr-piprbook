import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from core.factory import get_user_service_default
from core.user_service import UserService
from gui.ui_components.ui_login_window import Ui_LoginWindow
from gui.ui_components.ui_main_window import Ui_MainWindow
from gui.login_window_pages import LoginPage, RegisterPage
from gui.main_window_tabs import ProfilePage, MessengerPage, InviteFriendsPage


class LoginWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.user_service = user_service

        self.login_page = LoginPage(user_service, self._to_register_page, self._open_main_window)
        self.register_page = RegisterPage(user_service, self._to_login_page)
        self.login_page_idx = self.ui.pages.addWidget(self.login_page)
        self.register_page_idx = self.ui.pages.addWidget(self.register_page)

        self.ui.pages.setCurrentIndex(self.login_page_idx)

    def _to_register_page(self):
        self.ui.pages.setCurrentIndex(self.register_page_idx)

    def _to_login_page(self):
        self.ui.pages.setCurrentIndex(self.login_page_idx)

    def _open_main_window(self):
        self.main_window = MainWindow(self.user_service)
        self.main_window.show()
        self.hide()


class MainWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.user_service = user_service
        self.user = self.user_service.get_current_user()

        self._setup_main_window()

    def _setup_main_window(self):
        self.ui.action_log_out.triggered.connect(self._log_out)

        self.__profile_tab = ProfilePage(self.user_service)
        self.__messenger_tab = MessengerPage(self.user_service)
        self.__invite_friends_tab = InviteFriendsPage(self.user_service)

        self.__tab_index_by_name = {
            "Profile": self.ui.tabs.addTab(self.__profile_tab, "Profile"),
            "Messenger": self.ui.tabs.addTab(self.__messenger_tab, "Messenger"),
            "Invite Friends": self.ui.tabs.addTab(self.__invite_friends_tab, "Invite Friends")
        }
        self.__tab_by_index = {
            self.__tab_index_by_name["Profile"]: self.__profile_tab,
            self.__tab_index_by_name["Messenger"]: self.__messenger_tab,
            self.__tab_index_by_name["Invite Friends"]: self.__invite_friends_tab,
        }

        self.ui.tabs.setCurrentIndex(self.__tab_index_by_name["Profile"])
        self.ui.tabs.currentChanged.connect(self._refresh_tab)

    def _refresh_tab(self, tab_index):
        self.__tab_by_index[tab_index].refresh()

    def _log_out(self):
        self.user_service.log_out_user()
        self.login_window = LoginWindow(self.user_service)
        self.login_window.show()
        self.hide()


def main(args):
    db_filename = args[1]
    db_file = open(db_filename, mode="r+", encoding="utf-8")
    user_service = get_user_service_default(db_file)

    app = QApplication(args)
    window = LoginWindow(user_service)
    window.show()
    return app.exec_()


if __name__ == '__main__':
    main(sys.argv)
