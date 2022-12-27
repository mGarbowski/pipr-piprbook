import sys

from PySide2.QtWidgets import QMainWindow, QApplication

from core.factory import get_user_service_default
from core.user_service import UserService
from gui.ui_piprbook_desktop import Ui_MainWindow


class PiprbookWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user_service = user_service

        self.ui.stackedWidget.setCurrentIndex(0)
        self._setup_login_page()

    def _setup_login_page(self):
        self.ui.log_in_button.clicked.connect(self._log_in_user)
        self.ui.login_failed_text.setText("")

    def _log_in_user(self):
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        success = self.user_service.log_in_user(username, password)
        if success:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.login_failed_text.setText("Wrong username or password")
            self.ui.username_input.setText("")
            self.ui.password_input.setText("")


def main(args):
    db_filename = args[1]
    db_file = open(db_filename, mode="r+", encoding="utf-8")
    user_service = get_user_service_default(db_file)

    app = QApplication(args)
    window = PiprbookWindow(user_service)
    window.show()
    return app.exec_()


if __name__ == '__main__':
    main(sys.argv)
