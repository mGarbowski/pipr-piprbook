from datetime import datetime
from typing import Optional, List

from core.authentication import Authentication, UnauthorizedError
from core.common import generate_uuid
from core.model import FriendRequest, Message, User
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

    def save_user(self, user: User) -> User:
        return self.__user_repository.save(user)

    def set_bio(self, user: User, bio: str) -> User:
        self._check_if_logged_in(user)

        user.bio = bio
        return self.save_user(user)

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

    def get_messages(self, user_a: User, user_b: User, count: Optional[int] = None, offset: int = 0) -> List[Message]:
        current_user = self.__authentication.logged_in_user
        if user_a != current_user and user_b != current_user:
            raise UnauthorizedError()

        return self.__message_repository.get_messages(user_a, user_b, count, offset)

    def _check_if_logged_in(self, user: User) -> None:
        if user != self.__authentication.logged_in_user:
            raise UnauthorizedError()
