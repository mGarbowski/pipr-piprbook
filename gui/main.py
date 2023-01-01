import sys
from typing import Callable

from PySide2.QtCore import QByteArray
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QListWidgetItem, QMainWindow

from core.factory import get_user_service_default
from core.model import Photo
from core.user_service import UserService, UsernameTakenException, EmailAlreadyUsedException
from gui.resources.resources import get_placeholder_picture
from gui.ui_components.ui_invite_friends_page import Ui_InviteFriendsPage
from gui.ui_components.ui_login_window import Ui_LoginWindow
from gui.ui_components.ui_main_window import Ui_MainWindow
from gui.ui_components.ui_messenger_page import Ui_MessengerPage
from gui.ui_components.ui_profile_page import Ui_ProfilePage
from ui_components.ui_login_page import Ui_LoginPage
from ui_components.ui_register_page import Ui_RegisterPage
from core.validation import IncorrectUsernameError, IncorrectEmailError


class LoginPage(QWidget):

    def __init__(self, user_service: UserService, to_register_page: Callable, close_window: Callable, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginPage()
        self.user_service = user_service
        self.to_register_page = to_register_page
        self.close_window = close_window

        self.ui.setupUi(self)
        self._setup()

    def _setup(self):
        self.ui.log_in_button.clicked.connect(self._log_in_user)
        self.ui.register_button.clicked.connect(self.to_register_page)
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

    def _open_main_window(self):
        self.main_window = MainWindow(self.user_service)
        self.main_window.show()
        self.close_window()


class RegisterPage(QWidget):

    def __init__(self, user_service: UserService, to_login_page: Callable, parent=None):
        super().__init__(parent)
        self.ui = Ui_RegisterPage()
        self.user_service = user_service
        self.to_login_page = to_login_page

        self.ui.setupUi(self)
        self._setup()

    def _setup(self):
        self.ui.register_button.clicked.connect(self._register_user)
        self.ui.back_button.clicked.connect(self.to_login_page)
        self._clear_form()

    def _clear_form(self):
        self.ui.registration_failed_text.setText("")
        self.ui.username_input.setText("")
        self.ui.email_input.setText("")
        self.ui.password_input.setText("")
        self.ui.confirm_password_input.setText("")

    def _show_message(self, message: str):
        self.ui.registration_failed_text.setText(message)

    def _register_user(self):
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
            self._show_message("Email address is already used by an existing account")
        except IncorrectUsernameError:
            self._show_message("Username must be at least 4 characters long")
        except IncorrectEmailError:
            self._show_message("Incorrect email address")


class LoginWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.user_service = user_service

        self.login_page = LoginPage(user_service, self._to_register_page, self.hide)
        self.register_page = RegisterPage(user_service, self._to_login_page)
        self.login_page_idx = self.ui.pages.addWidget(self.login_page)
        self.register_page_idx = self.ui.pages.addWidget(self.register_page)

        self.ui.pages.setCurrentIndex(self.login_page_idx)

    def _to_register_page(self):
        self.ui.pages.setCurrentIndex(self.register_page_idx)

    def _to_login_page(self):
        self.ui.pages.setCurrentIndex(self.login_page_idx)


class ProfilePage(QWidget):

    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.user_service = user_service
        self.ui = Ui_ProfilePage()
        self.ui.setupUi(self)

        self._setup_profile_page()

    def refresh(self):
        self._setup_profile_page()

    def _setup_profile_page(self):
        user = self.user_service.get_current_user()

        self.ui.profile_header.setText(f"{user.username}'s profile")
        self.ui.username_display.setText(f"Username: {user.username}")
        self.ui.email_display.setText(f"Email address: {user.email}")
        self.ui.bio_display.setText(f"Bio: {user.bio}" if user.bio else "No bio set")

        self._display_profile_picture()

        self.ui.update_bio_button.clicked.connect(self._update_user_bio)
        self.ui.upload_profile_picture_button.clicked.connect(self._upload_profile_picture)

    def _upload_profile_picture(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_path, _ = file_dialog.getOpenFileName()

        if not file_path:  # No file was selected
            return

        # TODO: validate file, handle errors
        with open(file_path, mode="rb") as file_handle:
            profile_picture = Photo.from_file(file_handle, file_path)

        user = self.user_service.get_current_user()
        previous_profile_picture = self.user_service.get_profile_picture(user)
        self.user_service.add_profile_picture(user, profile_picture)

        if previous_profile_picture is not None:
            self.user_service.delete_picture(previous_profile_picture)

        self._display_profile_picture()

    def _update_user_bio(self):
        user = self.user_service.get_current_user()
        bio = self.ui.bio_input.toPlainText()
        self.user_service.set_bio(user, bio)
        self.ui.bio_display.setText(f"Bio: {user.bio}")
        self.ui.bio_input.setText("")

    def _display_profile_picture(self):
        user = self.user_service.get_current_user()
        profile_picture = self.user_service.get_profile_picture(user)
        profile_picture_bytes = profile_picture.get_bytes() if profile_picture else get_placeholder_picture()

        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(profile_picture_bytes))
        self.ui.profile_picture.setPixmap(pixmap)


class MessengerPage(QWidget):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_MessengerPage()
        self.ui.setupUi(self)
        self.user_service = user_service
        self.__friend = None

        self._setup_friends_list()
        self.ui.send_button.clicked.connect(self._send_message)

    def refresh(self):
        self._setup_friends_list()

    def _setup_friends_list(self):
        self.ui.friends_list.clear()

        user = self.user_service.get_current_user()
        friends = self.user_service.get_friends(user)
        for friend in friends:
            item = QListWidgetItem()
            item.user = friend
            item.setText(friend.username)
            self.ui.friends_list.addItem(item)

        self.ui.friends_list.itemClicked.connect(self._select_friend)
        self._display_messages()
        self._display_firend_info()

    def _display_firend_info(self):
        if self.__friend is None:
            self.ui.user_info.setText("Select friend to chat with")
            self.ui.friend_bio.clear()
            self.ui.friend_profile_picture.clear()
            return

        chat_header = f"Chat with {self.__friend.username}"
        self.ui.user_info.setText(chat_header)

        friend_bio = self.__friend.bio if self.__friend.bio else ""
        self.ui.friend_bio.setText(friend_bio)

        friend_profile_picture = self.user_service.get_profile_picture(self.__friend)
        if friend_profile_picture is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(friend_profile_picture.get_bytes()))
            self.ui.friend_profile_picture.setPixmap(pixmap)

    def _display_messages(self):
        self.ui.messages.clear()
        if self.__friend is None:
            return

        user = self.user_service.get_current_user()
        messages = self.user_service.get_messages(user, self.__friend)
        annotated_messages = []
        for message in messages:
            if message.from_user_id == user.uuid:
                username = user.username
            else:
                username = self.__friend.username
            message_display_text = f"{username}:\t{message.text}"
            annotated_messages.append(message_display_text)

        messages_text = "\n".join(annotated_messages)
        self.ui.messages.setText(messages_text)

    def _select_friend(self, item: QListWidgetItem):
        self.__friend = item.user
        self._display_messages()
        self._display_firend_info()

    def _send_message(self):
        text = self.ui.message_input.text()
        self.ui.message_input.clear()

        if self.__friend is None:
            return

        self.user_service.send_message(
            from_user=self.user_service.get_current_user(),
            to_user=self.__friend,
            text=text
        )
        self._display_messages()


class InviteFriendsPage(QWidget):

    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)

        self.ui = Ui_InviteFriendsPage()
        self.ui.setupUi(self)

        self.user_service = user_service
        self.__selected_user = None
        self.__awaiting_invitation = None
        self.__sent_invitation = None

        self._setup_event_handles()
        self._display_sent_invitations()
        self._display_awaiting_invitations()

    def refresh(self):
        pass

    def _setup_event_handles(self):
        self.ui.search_button.clicked.connect(self._search_users)
        self.ui.invite_button.clicked.connect(self._invite_selected_user)
        self.ui.accept_button.clicked.connect(self._accept_awaiting_invitaiton)
        self.ui.ignore_button.clicked.connect(self._ignore_awaiting_invitation)
        self.ui.cancel_button.clicked.connect(self._cancel_sent_invitation)

        self.ui.search_result.itemClicked.connect(self._select_user)
        self.ui.awaiting_invitations.itemClicked.connect(self._select_awaiting_invitation)
        self.ui.sent_invitations.itemClicked.connect(self._select_sent_invitation)

    def _select_user(self, item: QListWidgetItem):
        self.__selected_user = item.user

    def _search_users(self):
        self.ui.search_result.clear()

        current_user = self.user_service.get_current_user()
        username_fragment = self.ui.search_bar.text()
        sent_invitations = self.user_service.get_friend_requests_from(current_user)
        invited_user_ids = [invitation.to_user_id for invitation in sent_invitations]
        awaiting_invitations = self.user_service.get_friend_requests_to(current_user)
        already_invited_by_ids = [invitation.from_user_id for invitation in awaiting_invitations]

        users = self.user_service.get_users_by_username_fragment(username_fragment)
        users = [user for user in users if user.uuid != current_user.uuid]
        users = [user for user in users if not current_user.is_friends_with(user)]
        users = [user for user in users if user.uuid not in invited_user_ids]
        users = [user for user in users if user.uuid not in already_invited_by_ids]

        for user in users:
            item = QListWidgetItem(user.username)
            item.user = user
            self.ui.search_result.addItem(item)

    def _invite_selected_user(self):
        if self.__selected_user is None:
            return

        current_user = self.user_service.get_current_user()
        self.user_service.send_friend_request(current_user, self.__selected_user)
        self._search_users()
        self._display_sent_invitations()

    def _select_awaiting_invitation(self, item: QListWidgetItem):
        self.__awaiting_invitation = item.invitation

    def _display_awaiting_invitations(self):
        self.ui.awaiting_invitations.clear()

        current_user = self.user_service.get_current_user()
        awaiting_invitations = self.user_service.get_friend_requests_to(current_user)
        for invitation in awaiting_invitations:
            from_user = self.user_service.get_user_by_id(invitation.from_user_id)
            item = QListWidgetItem(from_user.username)
            item.invitation = invitation
            self.ui.awaiting_invitations.addItem(item)

    def _accept_awaiting_invitaiton(self):
        if self.__awaiting_invitation is None:
            return

        self.user_service.accept_friend_request(self.__awaiting_invitation)
        self._display_awaiting_invitations()
        self._search_users()

    def _ignore_awaiting_invitation(self):
        if self.__awaiting_invitation is None:
            return

        self.user_service.delete_friend_request(self.__awaiting_invitation)
        self._search_users()
        self._display_awaiting_invitations()

    def _select_sent_invitation(self, list_item: QListWidgetItem):
        self.__sent_invitation = list_item.invitation

    def _display_sent_invitations(self):
        self.ui.sent_invitations.clear()
        current_user = self.user_service.get_current_user()
        sent_invitations = self.user_service.get_friend_requests_from(current_user)
        for invitation in sent_invitations:
            to_user = self.user_service.get_user_by_id(invitation.to_user_id)
            list_item = QListWidgetItem(to_user.username)
            list_item.invitation = invitation
            self.ui.sent_invitations.addItem(list_item)

    def _cancel_sent_invitation(self):
        if self.__sent_invitation is None:
            return

        self.user_service.delete_friend_request(self.__sent_invitation)
        self._display_sent_invitations()


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
