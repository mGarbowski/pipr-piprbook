from typing import Protocol, TypeVar, Optional

from core.model import User, Message, FriendRequest

T = TypeVar("T")


class Repository(Protocol[T]):

    def save(self, entity: T) -> T:
        ...

    def get_by_id(self, entity_id: str) -> Optional[T]:
        ...


class UserRepository(Repository[User]):

    def get_by_username(self, username: str) -> Optional[User]:
        ...


class MessageRepository(Repository[Message]):

    def get_messages_to_user(self, to_user: User, last: int) -> list[Message]:
        ...

    def get_messages_from_user(self, from_user: User, last: int) -> list[Message]:
        ...

    def get_messages_from_to(self, from_user: User, to_user: User, last: int) -> list[Message]:
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
