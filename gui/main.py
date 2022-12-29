import sys
from enum import Enum

from PySide2.QtCore import QByteArray
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QFileDialog, QListWidgetItem, QMainWindow

from core.factory import get_user_service_default
from core.model import Photo
from core.user_service import UserService, UsernameTakenException, EmailAlreadyUsedException, RegistrationException
from gui.resources.resources import get_placeholder_picture
from gui.ui_components.ui_invite_friends_page import Ui_InviteFriendsPage
from gui.ui_components.ui_login_window import Ui_login_window
from gui.ui_components.ui_main_window import Ui_main_window
from gui.ui_components.ui_messenger_page import Ui_messenger_page
from gui.ui_components.ui_profile_page import Ui_ProfilePage


class LoginWindowPages(Enum):
    LOGIN = 0
    REGISTER = 1
    HOME = 2


class LoginWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.user_service = user_service

        self.ui.stackedWidget.setCurrentIndex(LoginWindowPages.LOGIN.value)
        self._setup_login_page()
        self._setup_register_page()

    def _setup_login_page(self):
        self.ui.log_in_button.clicked.connect(self._log_in_user)
        self.ui.register_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(LoginWindowPages.REGISTER.value)
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
            lambda: self.ui.stackedWidget.setCurrentIndex(LoginWindowPages.LOGIN.value)
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
            self.ui.stackedWidget.setCurrentIndex(LoginWindowPages.LOGIN.value)
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


class ProfilePage(QWidget):

    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.user_service = user_service
        self.user = self.user_service.get_current_user()
        self.ui = Ui_ProfilePage()
        self.ui.setupUi(self)

        self._setup_profile_page()

    def _setup_profile_page(self):
        user = self.user

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

        previous_profile_picture = self.user_service.get_profile_picture(self.user)
        self.user_service.add_profile_picture(self.user, profile_picture)

        if previous_profile_picture is not None:
            self.user_service.delete_picture(previous_profile_picture)

        self._display_profile_picture()

    def _update_user_bio(self):
        bio = self.ui.bio_input.toPlainText()
        self.user_service.set_bio(self.user, bio)
        self.ui.bio_display.setText(f"Bio: {self.user.bio}")
        self.ui.bio_input.setText("")

    def _display_profile_picture(self):
        profile_picture = self.user_service.get_profile_picture(self.user)
        profile_picture_bytes = profile_picture.get_bytes() if profile_picture else get_placeholder_picture()

        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(profile_picture_bytes))
        self.ui.profile_picture.setPixmap(pixmap)


class MessengerPage(QWidget):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_messenger_page()
        self.ui.setupUi(self)
        self.user_service = user_service
        self.__friend = None
        self.__user = user_service.get_current_user()

        self._setup_friends_list()
        self.ui.send_button.clicked.connect(self._send_message)

    def _setup_friends_list(self):
        friends = self.user_service.get_friends(self.__user)
        for friend in friends:
            item = QListWidgetItem()
            item.user = friend
            item.setText(friend.username)
            self.ui.friends_list.addItem(item)

        self.ui.friends_list.itemClicked.connect(self._select_friend)
        self._display_messages()

    def _display_messages(self):
        self.ui.messages.setText("")

        if self.__friend is None:
            self.ui.user_info.setText("Select friend to chat with")
            return

        self.ui.user_info.setText(f"Chat with {self.__friend.username}")
        messages = self.user_service.get_messages(self.__user, self.__friend)
        annotated_messages = []
        for message in messages:
            if message.from_user_id == self.__user.uuid:
                username = self.__user.username
            else:
                username = self.__friend.username
            message_display_text = f"{username}:\t{message.text}"
            annotated_messages.append(message_display_text)

        messages_text = "\n".join(annotated_messages)
        self.ui.messages.setText(messages_text)

    def _select_friend(self, item: QListWidgetItem):
        self.__friend = item.user
        self._display_messages()

    def _send_message(self):
        text = self.ui.message_input.text()
        self.ui.message_input.clear()

        if self.__friend is None:
            return

        self.user_service.send_message(
            from_user=self.__user,
            to_user=self.__friend,
            text=text
        )
        self._display_messages()


class InviteFriendsPage(QWidget):
    # TODO: fix display of search result after accepting / ignoring invitation
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_InviteFriendsPage()
        self.ui.setupUi(self)
        self.user_service = user_service
        self.__user = self.user_service.get_current_user()
        self.__selected_user = None
        self.__selected_invitation = None

        self._display_sent_invitations()
        self._display_awaiting_invitations()
        self.ui.search_button.clicked.connect(self._search_users)
        self.ui.search_result.itemClicked.connect(self._select_user)
        self.ui.invite_button.clicked.connect(self._invite_selected_user)
        self.ui.accept_button.clicked.connect(self._accept_selected_invitaiton)
        self.ui.ignore_button.clicked.connect(self._ignore_selected_invitation)
        self.ui.awaiting_invitations.itemClicked.connect(self._select_invitation)

    def _select_user(self, item: QListWidgetItem):
        self.__selected_user = item.user

    def _display_sent_invitations(self):
        sent_invitations = self.user_service.get_friend_requests_from(self.__user)
        for invitation in sent_invitations:
            to_user = self.user_service.get_user_by_id(invitation.to_user_id)
            item = QListWidgetItem(to_user.username)
            item.invitation = invitation
            self.ui.sent_invitations.addItem(item)

    def _display_awaiting_invitations(self):
        self.ui.awaiting_invitations.clear()
        awaiting_invitations = self.user_service.get_friend_requests_to(self.__user)
        for invitation in awaiting_invitations:
            from_user = self.user_service.get_user_by_id(invitation.from_user_id)
            item = QListWidgetItem(from_user.username)
            item.invitation = invitation
            self.ui.awaiting_invitations.addItem(item)

    def _select_invitation(self, item: QListWidgetItem):
        self.__selected_invitation = item.invitation

    def _accept_selected_invitaiton(self):
        self.user_service.accept_friend_request(self.__selected_invitation)
        self._display_awaiting_invitations()

    def _ignore_selected_invitation(self):
        self.user_service.delete_friend_request(self.__selected_invitation)
        self._display_awaiting_invitations()

    def _search_users(self):
        self.ui.search_result.clear()

        username_fragment = self.ui.search_bar.text()
        sent_invitations = self.user_service.get_friend_requests_from(self.__user)
        invited_user_ids = [invitation.to_user_id for invitation in sent_invitations]

        users = self.user_service.get_users_by_username_fragment(username_fragment)
        users = [user for user in users if user != self.__user]
        users = [user for user in users if not self.__user.is_friends_with(user)]
        users = [user for user in users if user.uuid not in invited_user_ids]

        for user in users:
            item = QListWidgetItem(user.username)
            item.user = user
            self.ui.search_result.addItem(item)

    def _invite_selected_user(self):
        if self.__selected_user is None:
            return

        self.user_service.send_friend_request(self.__user, self.__selected_user)
        self._search_users()
        self._display_sent_invitations()


class MainWindowPages(Enum):
    PROFILE = 0
    MESSENGER = 1
    INVITE_FRIENDS = 2


class MainWindow(QMainWindow):
    def __init__(self, user_service: UserService, parent=None):
        super().__init__(parent)
        self.ui = Ui_main_window()
        self.ui.setupUi(self)
        self.user_service = user_service
        self.user = self.user_service.get_current_user()

        self.ui.action_log_out.triggered.connect(self._log_out)

        profile_tab_idx = self.ui.tabs.addTab(ProfilePage(self.user_service), "Profile")
        self.ui.tabs.addTab(MessengerPage(self.user_service), "Messenger")
        self.ui.tabs.addTab(InviteFriendsPage(self.user_service), "Invite Friends")
        self.ui.tabs.setCurrentIndex(profile_tab_idx)

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
