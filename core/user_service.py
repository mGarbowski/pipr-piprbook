from datetime import datetime
from typing import Optional, List

from core.authentication import Authentication, UnauthorizedError, LoginFailedException, hash_password, generate_salt
from core.common import generate_uuid
from core.model import FriendRequest, Message, User, Photo
from persistence.repositories import (
    FriendRequestRepository, MessageRepository, PhotoRepository, UserRepository
)


class UserService:

    def __init__(
            self,
            authentication: Authentication,
            user_repository: UserRepository,
            message_repository: MessageRepository,
            friend_request_repository: FriendRequestRepository,
            photo_repository: PhotoRepository
    ) -> None:
        self.__authentication = authentication
        self.__user_repository = user_repository
        self.__message_repository = message_repository
        self.__friend_request_repository = friend_request_repository
        self.__photo_repository = photo_repository

    def log_in_user(self, username: str, password: str) -> bool:
        """Attempt to log in, return True if successful"""
        try:
            self.__authentication.log_in(username, password)
            return True
        except LoginFailedException:
            return False

    def log_out_user(self):
        self.__authentication.log_out()

    def register_new_user(self, username: str, email: str, password: str) -> None:
        """Attempt to register new user with given credentials"""
        if self.__user_repository.get_by_username(username) is not None:
            raise UsernameTakenException(username)
        if self.__user_repository.get_by_email(email) is not None:
            raise EmailAlreadyUsedException(email)
        # TODO: validate weak password
        # TODO: validate username
        # TODO: validate email address

        salt = generate_salt()
        user = User(
            uuid=generate_uuid(),
            username=username,
            email=email,
            password_hash=hash_password(password, salt),
            salt=salt
        )
        self.save_user(user)

    def get_current_user(self) -> User:
        return self.__authentication.logged_in_user

    def save_user(self, user: User) -> User:
        return self.__user_repository.save(user)

    def set_bio(self, user: User, bio: str):
        self._check_if_logged_in(user)

        user.bio = bio
        self.save_user(user)

    def get_profile_picture(self, user: User) -> Optional[Photo]:
        return self.__photo_repository.get_by_id(user.profile_picture_id)

    def add_profile_picture(self, user: User, photo: Photo):
        user.profile_picture_id = photo.uuid
        self.__user_repository.save(user)
        self.__photo_repository.save(photo)

    def delete_picture(self, photo: Photo):
        self.__photo_repository.delete(photo)

    def get_friends(self, user: User) -> List[User]:
        return [
            self.__user_repository.get_by_id(friend_id)
            for friend_id in user.friend_uuids
        ]

    def send_message(self, from_user: User, to_user: User, text: str) -> Message:
        self._check_if_logged_in(from_user)
        return self.__message_repository.save(
            Message(
                uuid=generate_uuid(),
                text=text,
                timestamp=datetime.now(),
                from_user_id=from_user.uuid,
                to_user_id=to_user.uuid
            )
        )

    def send_friend_request(self, from_user: User, to_user: User) -> FriendRequest:
        self._check_if_logged_in(from_user)
        return self.__friend_request_repository.save(
            FriendRequest(
                uuid=generate_uuid(),
                timestamp=datetime.now(),
                from_user_id=from_user.uuid,
                to_user_id=to_user.uuid
            )
        )

    def accept_friend_request(self, friend_request: FriendRequest) -> None:
        from_user = self.__user_repository.get_by_id(friend_request.from_user_id)
        to_user = self.__user_repository.get_by_id(friend_request.to_user_id)
        if to_user is None or from_user is None:
            raise ValueError("There are no users with given IDs")

        self._check_if_logged_in(to_user)

        if from_user.uuid in to_user.friend_uuids:
            raise ValueError("Users are already friends")

        to_user.friend_uuids.append(from_user.uuid)
        from_user.friend_uuids.append(to_user.uuid)

        self.__user_repository.save(to_user)
        self.__user_repository.save(from_user)
        self.__friend_request_repository.delete(friend_request)

    def get_messages(self, user_a: User, user_b: User) -> List[Message]:
        current_user = self.__authentication.logged_in_user
        if user_a != current_user and user_b != current_user:
            raise UnauthorizedError()

        return self.__message_repository.get_messages(user_a, user_b)

    def _check_if_logged_in(self, user: User) -> None:
        if user.uuid != self.__authentication.logged_in_user.uuid:
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
