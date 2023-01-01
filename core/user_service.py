"""The main interface for all operations related with users"""

from datetime import datetime
from typing import Optional, List

from core.authentication import Authentication, UnauthorizedError, LoginFailedError, hash_password, generate_salt
from core.identifiers import generate_uuid
from core.model import FriendRequest, Message, User, Photo
from persistence.repositories import (
    FriendRequestRepository, MessageRepository, PhotoRepository, UserRepository
)


class UserService:
    """Class for performing operations on users

    Some operations require authorization, authentication and authorization logic is delegated to Authentication object.
    Attempt to perform an action without appropriate permissions raises core.authentication.UnauthorizedError.
    """

    def __init__(
            self,
            authentication: Authentication,
            user_repository: UserRepository,
            message_repository: MessageRepository,
            friend_request_repository: FriendRequestRepository,
            photo_repository: PhotoRepository
    ) -> None:
        """Create user service instance with dependencies provided as arguments"""
        self.__authentication = authentication
        self.__user_repository = user_repository
        self.__message_repository = message_repository
        self.__friend_request_repository = friend_request_repository
        self.__photo_repository = photo_repository

    def log_in_user(self, username: str, password: str) -> bool:
        """Attempt to log in, return True if successful

        :param username: user's username
        :param password: user's password in plain text
        """
        try:
            self.__authentication.log_in(username, password)
            return True
        except LoginFailedError:
            return False

    def log_out_user(self):
        """Log out currently logged-in user if there is any"""
        self.__authentication.log_out()

    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Get user by id or None if not found"""
        return self.__user_repository.get_by_id(user_id)

    def get_users_by_username_fragment(self, username_fragment: str) -> List[User]:
        """Get all users with usernames matching given fragment

        :param username_fragment: exact text contained in users' usernames
        """
        return self.__user_repository.get_by_username_fragment(username_fragment)

    def register_new_user(self, username: str, email: str, password: str) -> None:
        """Attempt to create new user with given credentials

        Raises appropriate exceptions on invalid credentials

        :param username: username, cannot be used by an existing user
        :param email: email address, cannot be used by an existing user
        :param password: password in plain text

        :raises UsernameTakenException: if given username is already used by some other user
        :raises EmailAlreadyUsedException: if given email address is already used by some existing user
        :raises IncorrectUsernameError: if username is shorter than 4 characters
        :raises IncorrectEmailError: if email is not a correct email address
        """
        if self.__user_repository.get_by_username(username) is not None:
            raise UsernameTakenException(username)
        if self.__user_repository.get_by_email(email) is not None:
            raise EmailAlreadyUsedException(email)
        # TODO: validate weak password

        salt = generate_salt()
        user = User(
            uuid=generate_uuid(),
            username=username,
            email=email,
            password_hash=hash_password(password, salt),
            salt=salt
        )
        self.save_user(user)

    def get_current_user(self) -> Optional[User]:
        """Get currently logged-in user or None if nobody is logged-in

        Refreshes user data from the database to avoid comparisons with stale information
        """
        current_user = self.__authentication.logged_in_user
        return self._refresh_user_data(current_user) if current_user else None

    def _refresh_user_data(self, user: User) -> Optional[User]:
        """Return the same user from the database, with his current state"""
        return self.get_user_by_id(user.uuid)

    def save_user(self, user: User) -> None:
        """Save user in the database"""
        self.__user_repository.save(user)

    def set_bio(self, user: User, bio: str) -> None:
        """Set user's bio, requires user to be logged-in

        :raises UnauthorizedError: if user is not logged-in
        """
        self._check_if_logged_in(user)

        user.bio = bio
        self.save_user(user)

    def get_profile_picture(self, user: User) -> Optional[Photo]:
        """Get user's profile picture or None if not set"""
        if user.profile_picture_id is None:
            return None

        return self.__photo_repository.get_by_id(user.profile_picture_id)

    def add_profile_picture(self, user: User, photo: Photo) -> None:
        """Add user's profile picture overwriting existing if there was any

        Requires user to be logged-in
        Previous profile picture is deleted

        :raises UnauthorizedError: if user is not logged-in
        """
        self._check_if_logged_in(user)

        previous_id = user.profile_picture_id
        if previous_id is not None:
            previous = self.__photo_repository.get_by_id(previous_id)
            if previous is not None:
                self.delete_picture(previous)

        user.profile_picture_id = photo.uuid
        self.__user_repository.save(user)
        self.__photo_repository.save(photo)

    def delete_picture(self, photo: Photo) -> None:
        """Delte photo from the database"""
        self.__photo_repository.delete(photo)

    def get_friends(self, user: User) -> List[User]:
        """Return list of user's friends

        List can be in any order
        """
        return [
            friend for friend_id in user.friend_uuids
            if (friend := self.__user_repository.get_by_id(friend_id)) is not None
        ]

    def send_message(self, from_user: User, to_user: User, text: str) -> None:
        """Send text message from one user to another

        Requires sending user to be logged-in
        Users do not have to be friends

        :param from_user: message sender, must be logged-in
        :param to_user: message receiver
        :param text: message content, nonempty

        :raises UnauthorizedError: if sending user is not logged-in
        :raises IncorrectMessageTextError: if text is empty
        :raises SelfReferenceError: if sending and receiving users are the same
        """
        self._check_if_logged_in(from_user)
        self.__message_repository.save(
            Message(
                uuid=generate_uuid(),
                text=text,
                timestamp=datetime.now(),
                from_user_id=from_user.uuid,
                to_user_id=to_user.uuid
            )
        )

    def get_friend_requests_from(self, user: User) -> List[FriendRequest]:
        """Get a list of all awaiting friend requests sent by the user

        Requires user to be logged-in

        :raises UnauthorizedError: if user is not logged-in
        """
        self._check_if_logged_in(user)
        return self.__friend_request_repository.get_requests_from_user(user)

    def get_friend_requests_to(self, user: User) -> List[FriendRequest]:
        """Get a list of all awaiting friend requests sent to the user

        Requires user to be logged-in

        :raises UnauthorizedError: if user is not logged-in
        """
        self._check_if_logged_in(user)
        return self.__friend_request_repository.get_requests_to_user(user)

    def send_friend_request(self, from_user: User, to_user: User) -> FriendRequest:
        """Send a friend request from one user to another

        Requires sending user to be logged-in
        Users cannot already be friends

        :raises UnauthorizedError: if sending user is not logged in
        :raises AlreadyFriendsException: if users are already friends
        """
        self._check_if_logged_in(from_user)
        if from_user.is_friends_with(to_user):
            raise AlreadyFriendsException(from_user, to_user)

        return self.__friend_request_repository.save(
            FriendRequest(
                uuid=generate_uuid(),
                timestamp=datetime.now(),
                from_user_id=from_user.uuid,
                to_user_id=to_user.uuid
            )
        )

    def accept_friend_request(self, friend_request: FriendRequest) -> None:
        """Accept a friend request, users will be friends after accepting

        Accepting user must be logged-in

        :raises UnauthorizedError: if user is not logged-in
        :raises ValueError: if friend requests refers to non-existing users
        :raises AlreadyFriendsException: if sending and receiving users are already friends
        """
        from_user = self.__user_repository.get_by_id(friend_request.from_user_id)
        to_user = self.__user_repository.get_by_id(friend_request.to_user_id)
        if to_user is None or from_user is None:
            raise ValueError("There are no users with given IDs")

        self._check_if_logged_in(to_user)

        if from_user.uuid in to_user.friend_uuids:
            raise AlreadyFriendsException(from_user, to_user)

        to_user.friend_uuids.append(from_user.uuid)
        from_user.friend_uuids.append(to_user.uuid)

        self.__user_repository.save(to_user)
        self.__user_repository.save(from_user)
        self.__friend_request_repository.delete(friend_request)

    def delete_friend_request(self, friend_request: FriendRequest) -> None:
        """Delete friend request

        Does not require users to be logged-in as they may not exist
        """
        self.__friend_request_repository.delete(friend_request)

    def get_messages(self, user_a: User, user_b: User) -> List[Message]:
        """Get all messages exchanged between two users in chronological order

        Requires user to be logged-in,
        users can only view messages they sent or received

        :raises UnauthorizedError: if user is not logged-in
        """
        current_user = self.get_current_user()
        if current_user is None:
            raise UnauthorizedError()

        if user_a.uuid != current_user.uuid and user_b.uuid != current_user.uuid:
            raise UnauthorizedError()

        return self.__message_repository.get_messages(user_a, user_b)

    def _check_if_logged_in(self, user: User) -> None:
        """Raise exception if given user is not currently logged in

        :raises UnauthorizedError: if user is not logged-in
        """
        current_user = self.get_current_user()
        if current_user is None:
            raise UnauthorizedError()
        if user.uuid != current_user.uuid:
            raise UnauthorizedError()


class RegistrationException(Exception):
    pass


class UsernameTakenException(RegistrationException):
    def __init__(self, username):
        super().__init__("Username is already taken by someone else")
        self.username = username


class EmailAlreadyUsedException(RegistrationException):
    def __init__(self, email):
        super().__init__("There already exists a user with this email address")
        self.email = email


class WeakPasswordException(RegistrationException):
    def __init__(self):
        super().__init__("Password is too weak")


class AlreadyFriendsException(Exception):
    def __init__(self, user_1, user_2):
        super().__init__("Users are already friends")
        self.user_1 = user_1
        self.user_2 = user_2
