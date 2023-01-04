"""Pages for the main window"""

from PySide2.QtCore import QByteArray
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QWidget, QFileDialog, QListWidgetItem

from core.model import Photo
from core.user_service import UserService
from gui.resources.resources import get_placeholder_picture
from gui.ui_components.ui_invite_friends_page import Ui_InviteFriendsPage
from gui.ui_components.ui_messenger_page import Ui_MessengerPage
from gui.ui_components.ui_profile_page import Ui_ProfilePage


class ProfilePage(QWidget):
    """Page showing user's profile"""

    def __init__(self, user_service: UserService, parent=None):
        """Create profile page

        :param user_service: user service providing access to user data
        :param parent: parent widget
        """
        super().__init__(parent)
        self.user_service = user_service
        self.ui = Ui_ProfilePage()
        self.ui.setupUi(self)

        self._setup_profile_page()

    def refresh(self):
        """Refresh page"""
        self._setup_profile_page()

    def _setup_profile_page(self):
        """Setup event handlers and display user info"""
        user = self.user_service.get_current_user()

        self.ui.profile_header.setText(f"{user.username}'s profile")
        self.ui.username_display.setText(f"Username: {user.username}")
        self.ui.email_display.setText(f"Email address: {user.email}")
        self.ui.bio_display.setText(
            f"Bio: {user.bio}" if user.bio else "No bio set"
        )

        self._display_profile_picture()

        self.ui.update_bio_button.clicked.connect(self._update_user_bio)
        self.ui.upload_profile_picture_button.clicked.connect(
            self._upload_profile_picture
        )

    def _upload_profile_picture(self):
        """Select photo and set as user's new profile picture"""
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
        """Update user's bio"""
        user = self.user_service.get_current_user()
        bio = self.ui.bio_input.toPlainText()
        self.user_service.set_bio(user, bio)
        self.ui.bio_display.setText(f"Bio: {user.bio}")
        self.ui.bio_input.setText("")

    def _display_profile_picture(self):
        """Display user's profile picture or a placeholder if not set"""
        user = self.user_service.get_current_user()
        profile_picture = self.user_service.get_profile_picture(user)
        if profile_picture:
            picture_bytes = profile_picture.get_bytes()
        else:
            picture_bytes = get_placeholder_picture()

        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(picture_bytes))
        self.ui.profile_picture.setPixmap(pixmap)


class MessengerPage(QWidget):
    """Page for sending messages to friends"""

    def __init__(self, user_service: UserService, parent=None):
        """Create messenger page

        :param user_service: user service handling sending
            and retreiving messages
        :param parent: parent widget
        """
        super().__init__(parent)
        self.ui = Ui_MessengerPage()
        self.ui.setupUi(self)
        self.user_service = user_service
        self.__friend = None

        self._setup_friends_list()
        self.ui.send_button.clicked.connect(self._send_message)

    def refresh(self):
        """Refresh page"""
        self._setup_friends_list()

    def _setup_friends_list(self):
        """Display list of user's friends"""
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
        """Display info about selected friend"""
        if self.__friend is None:
            self.ui.user_info.setText("Select friend to chat with")
            self.ui.friend_bio.clear()
            self.ui.friend_profile_picture.clear()
            return

        chat_header = f"Chat with {self.__friend.username}"
        self.ui.user_info.setText(chat_header)

        friend_bio = self.__friend.bio if self.__friend.bio else ""
        self.ui.friend_bio.setText(friend_bio)

        friend_profile_picture = self.user_service.get_profile_picture(
            self.__friend
        )
        if friend_profile_picture is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(friend_profile_picture.get_bytes()))
            self.ui.friend_profile_picture.setPixmap(pixmap)

    def _display_messages(self):
        """Display messages exchanged with selected friend"""
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
        """Select friend to exchange messages with"""
        self.__friend = item.user
        self._display_messages()
        self._display_firend_info()

    def _send_message(self):
        """Send message to the selected friend"""
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
    """Page for managing friend invitations"""

    def __init__(self, user_service: UserService, parent=None):
        """Create page for inviting friends

        :param user_service: service handling invitation and user search logic
        :param parent: parent widget
        """
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
        """Refresh page

        Required by MainWindow's interface
        """
        pass

    def _setup_event_handles(self):
        """Setup event handlers for buttons and lists"""
        self.ui.search_button.clicked.connect(self._search_users)
        self.ui.invite_button.clicked.connect(self._invite_selected_user)
        self.ui.accept_button.clicked.connect(self._accept_awaiting_invitaiton)
        self.ui.ignore_button.clicked.connect(self._ignore_awaiting_invitation)
        self.ui.cancel_button.clicked.connect(self._cancel_sent_invitation)

        self.ui.search_result.itemClicked.connect(self._select_user)
        self.ui.awaiting_invitations.itemClicked.connect(
            self._select_awaiting_invitation
        )
        self.ui.sent_invitations.itemClicked.connect(
            self._select_sent_invitation
        )

    def _select_user(self, item: QListWidgetItem):
        """Select user from search result"""
        self.__selected_user = item.user

    def _search_users(self):
        """Search and display users"""
        self.ui.search_result.clear()

        current_user = self.user_service.get_current_user()
        username_fragment = self.ui.search_bar.text()
        sent_invitations = self.user_service.get_friend_requests_from(
            current_user
        )
        invited_user_ids = [invitation.to_user_id
                            for invitation in sent_invitations]
        awaiting_invitations = self.user_service.get_friend_requests_to(
            current_user
        )
        already_invited_by_ids = [invitation.from_user_id
                                  for invitation in awaiting_invitations]

        users = self.user_service.get_users_by_username_fragment(
            username_fragment
        )
        users = [user for user in users
                 if user.uuid != current_user.uuid]
        users = [user for user in users
                 if not current_user.is_friends_with(user)]
        users = [user for user in users
                 if user.uuid not in invited_user_ids]
        users = [user for user in users
                 if user.uuid not in already_invited_by_ids]

        for user in users:
            item = QListWidgetItem(user.username)
            item.user = user
            self.ui.search_result.addItem(item)

    def _invite_selected_user(self):
        """Send a friend request to the selected user from search result"""
        if self.__selected_user is None:
            return

        current_user = self.user_service.get_current_user()
        self.user_service.send_friend_request(
            current_user, self.__selected_user
        )
        self._search_users()
        self._display_sent_invitations()

    def _select_awaiting_invitation(self, item: QListWidgetItem):
        """Select invitation from list of received invitations"""
        self.__awaiting_invitation = item.invitation

    def _display_awaiting_invitations(self):
        """Display received invitations"""
        self.ui.awaiting_invitations.clear()

        current_user = self.user_service.get_current_user()
        awaiting_invitations = self.user_service.get_friend_requests_to(
            current_user
        )
        for invitation in awaiting_invitations:
            from_user = self.user_service.get_user_by_id(
                invitation.from_user_id
            )
            item = QListWidgetItem(from_user.username)
            item.invitation = invitation
            self.ui.awaiting_invitations.addItem(item)

    def _accept_awaiting_invitaiton(self):
        """Accept selected received invitation"""
        if self.__awaiting_invitation is None:
            return

        self.user_service.accept_friend_request(self.__awaiting_invitation)
        self._display_awaiting_invitations()
        self._search_users()

    def _ignore_awaiting_invitation(self):
        """Delete selected received invitation"""
        if self.__awaiting_invitation is None:
            return

        self.user_service.delete_friend_request(self.__awaiting_invitation)
        self._search_users()
        self._display_awaiting_invitations()

    def _select_sent_invitation(self, list_item: QListWidgetItem):
        """Select sent invitation"""
        self.__sent_invitation = list_item.invitation

    def _display_sent_invitations(self):
        """Display invitations sent by the logged-in user"""
        self.ui.sent_invitations.clear()
        current_user = self.user_service.get_current_user()
        sent_invitations = self.user_service.get_friend_requests_from(
            current_user
        )
        for invitation in sent_invitations:
            to_user = self.user_service.get_user_by_id(invitation.to_user_id)
            list_item = QListWidgetItem(to_user.username)
            list_item.invitation = invitation
            self.ui.sent_invitations.addItem(list_item)

    def _cancel_sent_invitation(self):
        """Delete selected sent invitation"""
        if self.__sent_invitation is None:
            return

        self.user_service.delete_friend_request(self.__sent_invitation)
        self._display_sent_invitations()
