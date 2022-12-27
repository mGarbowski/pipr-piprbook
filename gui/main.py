import sys
from enum import Enum

from PySide2.QtWidgets import QMainWindow, QApplication

from core.factory import get_user_service_default
from core.user_service import UserService, UsernameTakenException, EmailAlreadyUsedException, RegistrationException
from gui.ui_login_window import Ui_login_window
from gui.ui_main_window import Ui_main_window


class Page(Enum):
    LOGIN = 0
    REGISTER = 1
    HOME = 2


class LoginWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.user_service = user_service

        self.ui.stackedWidget.setCurrentIndex(Page.LOGIN.value)
        self._setup_login_page()
        self._setup_register_page()

    def _setup_login_page(self):
        self.ui.log_in_button.clicked.connect(self._log_in_user)
        self.ui.register_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(Page.REGISTER.value)
        )
        self.ui.login_failed_text.setText("")

    def _log_in_user(self):
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        success = self.user_service.log_in_user(username, password)
        if success:
            self._open_main_window()
        else:
            self.ui.login_failed_text.setText("Wrong username or password")
            self.ui.username_input.setText("")
            self.ui.password_input.setText("")

    def _setup_register_page(self):
        self.ui.create_account_button.clicked.connect(self._register_user)
        self._clear_registration_form()
        self.ui.back_to_login_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(Page.LOGIN.value)
        )

    def _register_user(self):
        username = self.ui.username_input_2.text()
        email = self.ui.email_input.text()
        password = self.ui.password_input_2.text()
        repeated_password = self.ui.confirm_password_input.text()

        if password != repeated_password:
            self._clear_registration_form()
            self.ui.registration_failed_message.setText("Passwords do not match")
            return

        try:
            self.user_service.register_new_user(username, email, password)
            self.ui.stackedWidget.setCurrentIndex(Page.LOGIN.value)
            self._clear_registration_form()
        except UsernameTakenException:
            self._clear_registration_form()
            self.ui.registration_failed_message.setText("Username is already taken")
        except EmailAlreadyUsedException:
            self._clear_registration_form()
            self.ui.registration_failed_message.setText("Email address is already used by an existing account")
        except RegistrationException:
            self._clear_registration_form()
            self.ui.registration_failed_message.setText("Registration failed")

    def _clear_registration_form(self):
        self.ui.registration_failed_message.setText("")
        self.ui.username_input_2.setText("")
        self.ui.email_input.setText("")
        self.ui.password_input_2.setText("")
        self.ui.confirm_password_input.setText("")

    def _open_main_window(self):
        self.main_window = MainWindow(self.user_service)
        self.main_window.show()
        self.hide()


class MainWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.user_service = user_service
        self.user = self.user_service.get_current_user()

        self._show_user_info()

    def _show_user_info(self):
        user = self.user
        self.ui.user_info_label.setText(
            f"{user.uuid=}\n{user.username=}\n{user.email=}\n{user.bio=}"
        )


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
