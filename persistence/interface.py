from typing import Protocol, TypeVar, Optional

from core.model import User, Message, FriendRequest

T = TypeVar("T")


class Repository(Protocol[T]):

    def save(self, entity: T) -> T:
        ...

    def get_by_id(self, entity_id: str) -> Optional[T]:
        ...

    def delete(self, entity: T) -> None:
        ...


class UserRepository(Repository[User]):

    def get_by_username(self, username: str) -> Optional[User]:
        ...


class MessageRepository(Repository[Message]):

    def get_messages(self, user_a: User, user_b: User,
                     count: Optional[int] = None, offset: int = 0) -> list[Message]:
        """Return messages between users a and b, newer messages first

        Messages sorted by timestamps.
        Supports pagination with count and offset.

        :param user_a: User sending or receiving messages
        :param user_b: User sending or receiving messages
        :param count: How many messages to get, starting from the newest + offset, defaults to all
        :param offset: Offset for the first message to return, starting from the newest by default
        """
        ...


class FriendRequestRepository(Repository[FriendRequest]):

    def get_requests_to_user(self, to_user: User) -> list[FriendRequest]:
        ...

    def get_requests_from_user(self, from_user: User) -> list[FriendRequest]:
        ...


class PhotoRepository(Protocol):

    def save(self, file_path) -> str:
        """Save photo and return its id"""
        ...

    def get_by_id(self, photo_id: str) -> str:
        """Return path of the photo file"""
        ...
