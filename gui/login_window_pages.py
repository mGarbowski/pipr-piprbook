"""Pages for the login window"""

from typing import Callable

from PySide2.QtWidgets import QWidget

from core.user_service import (
    UserService, UsernameTakenException, EmailAlreadyUsedException
)
from core.validation import IncorrectUsernameError, IncorrectEmailError
from gui.ui_components.ui_login_page import Ui_LoginPage
from gui.ui_components.ui_register_page import Ui_RegisterPage


class LoginPage(QWidget):
    """Page for user login"""

    def __init__(
            self,
            user_service: UserService,
            to_register_page: Callable,
            open_main_window: Callable, parent=None
    ):
        """Create login page

        :param user_service: user service to provide login logic
        :param to_register_page: switch to register page callback function
        :param open_main_window: open main window after successfully logging in
            and close login window callback function
        :param parent: parent widget
        """
        super().__init__(parent)
        self.ui = Ui_LoginPage()
        self.user_service = user_service
        self.to_register_page = to_register_page
        self.open_main_window = open_main_window

        self.ui.setupUi(self)
        self._setup()

    def _setup(self):
        """Setup event handlers and display"""
        self.ui.log_in_button.clicked.connect(self._log_in_user)
        self.ui.register_button.clicked.connect(self.to_register_page)
        self.ui.login_failed_text.setText("")

    def _log_in_user(self):
        """Attempt to log in, display message on failure"""
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        success = self.user_service.log_in_user(username, password)
        if success:
            self.open_main_window()
        else:
            self.ui.login_failed_text.setText("Wrong username or password")
            self.ui.username_input.setText("")
            self.ui.password_input.setText("")


class RegisterPage(QWidget):
    """Page for user registration"""

    def __init__(
            self,
            user_service: UserService,
            to_login_page: Callable,
            parent=None
    ):
        """Create registration page

        :param user_service: user service handling registration logic
        :param to_login_page: switch to login page callback function
        :param parent: parent widget
        """
        super().__init__(parent)
        self.ui = Ui_RegisterPage()
        self.user_service = user_service
        self.to_login_page = to_login_page

        self.ui.setupUi(self)
        self._setup()

    def _setup(self):
        """Setup event handlers and display"""
        self.ui.register_button.clicked.connect(self._register_user)
        self.ui.back_button.clicked.connect(self.to_login_page)
        self._clear_form()

    def _clear_form(self):
        """Clear registration form"""
        self.ui.registration_failed_text.setText("")
        self.ui.username_input.setText("")
        self.ui.email_input.setText("")
        self.ui.password_input.setText("")
        self.ui.confirm_password_input.setText("")

    def _show_message(self, message: str):
        """Display message after failed registration"""
        self.ui.registration_failed_text.setText(message)

    def _register_user(self):
        """Attempt to register user with given credentials"""
        username = self.ui.username_input.text()
        email = self.ui.email_input.text()
        password = self.ui.password_input.text()
        repeated_password = self.ui.confirm_password_input.text()
        self._clear_form()

        if password != repeated_password:
            self.ui.registration_failed_text.setText("Passwords do not match")
            return

        try:
            self.user_service.register_new_user(username, email, password)
            self.to_login_page()
        except UsernameTakenException:
            self._show_message("Username is already taken")
        except EmailAlreadyUsedException:
            self._show_message(
                "Email address is already used by an existing account"
            )
        except IncorrectUsernameError:
            self._show_message("Username must be at least 4 characters long")
        except IncorrectEmailError:
            self._show_message("Incorrect email address")
