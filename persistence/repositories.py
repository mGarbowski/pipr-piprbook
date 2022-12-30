"""Repository classes for accessing data persisted in a Database"""
from abc import ABC
from typing import Optional, List, TypeVar

from core.model import User, Message, FriendRequest, Entity
from persistence.interface import Database, JsonSerializer

T = TypeVar("T", bound=Entity)


class BaseRepository(ABC):
    def __init__(
            self,
            database: Database,
            serializer: JsonSerializer,
            collection_name: str
    ):
        """Create a Repository connected to the given database

        :param database: database to persist entities in
        :param serializer: JSON serializer for entities
        :param collection_name: collection name in the database
        """
        self._database = database
        self._serializer = serializer
        self._collection_name = collection_name

    def save(self, entity: T):
        """Create new entity or update existing one

        :param entity: entity to create or update
        """
        entity_dict = self._serializer.to_json(entity)
        self._database.save(entity_dict, self._collection_name)

    def get_by_id(self, entity_id: str) -> Optional[T]:
        """Get entity by id or None if it does not exist

        :param entity_id: id of searched entity
        """
        entity_dict = self._database.get_by_id(entity_id, self._collection_name)
        return self._serializer.from_json(entity_dict) if entity_dict else None

    def delete(self, entity: T):
        """Delete entity or do nothing if it does not exist in the database

        :param entity: entity to delete
        """
        self._database.delete_by_id(entity.uuid, self._collection_name)


class UserRepository(BaseRepository):
    """Class for accessing users stored in a database"""

    def __init__(
            self,
            database: Database,
            serializer: JsonSerializer[User],
            collection_name: str = "users"
    ):
        """Create UserRepository connected to the given database

        :param database: database object to persist users in
        :param serializer: JSON serializer for users
        :param collection_name: name of collection in datbase, defaults to "users"
        """
        super().__init__(database, serializer, collection_name)

    def get_all(self) -> List[User]:
        """Get all users"""
        users_json = self._database.get_collection(self._collection_name)
        users = [self._serializer.from_json(user_json) for user_json in users_json]
        return users

    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username or None if not found

        :param username: username matched exactly to a user
        """
        users = self.get_all()
        users = [user for user in users if user.username == username]
        return users[0] if users else None

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email or None if not found

        If email is not unique, may return any matching user instance

        :param email: email address of searched user
        """
        users = self.get_all()
        users = [user for user in users if user.email == email]
        return users[0] if users else None

    def get_by_username_fragment(self, username_fragment: str) -> List[User]:
        """Get all users with username matching fragment

        :param username_fragment: string contained in user's username
        """
        return [
            user for user in self.get_all()
            if username_fragment in user.username
        ]


class MessageRepository(BaseRepository):
    """Class for accessing messages persisted in a database"""

    def __init__(
            self,
            database: Database,
            serializer: JsonSerializer[Message],
            collection_name: str = "messages"
    ):
        """Create a message repository connected to the given database

        :param database: database object to persist messages in
        :param serializer: JSON serializer for messages
        :param collection_name: name of collection in datbase, defaults to "messages"
        """
        super().__init__(database, serializer, collection_name)

    def get_messages(self, user_a: User, user_b: User) -> List[Message]:
        """Get all messages exchanged between two users, ordered by timestamp

        Earlier messages first
        Order of users does not matter

        :param user_a: one of the users sending or receiving messages
        :param user_b: one of the users sending or receiving messages
        """
        messages_json = self._database.get_collection(self._collection_name)
        messages = [self._serializer.from_json(message_json) for message_json in messages_json]
        messages = [msg for msg in messages if _is_message_matched(msg, user_a, user_b)]
        messages = sorted(messages, key=lambda msg: msg.timestamp)
        return messages


def _is_message_matched(message: Message, user_a: User, user_b: User) -> bool:
    """Return whether message was sent from one of given users to the other"""
    user_ids = (user_a.uuid, user_b.uuid)
    return message.to_user_id in user_ids and message.from_user_id in user_ids


class FriendRequestRepository(BaseRepository):
    """Class for accessing friend requests stored in a database"""

    def __init__(
            self,
            database: Database,
            serializer: JsonSerializer[FriendRequest],
            collection_name: str = "friend_requests"
    ):
        """Create FriendRequestRepository connected to the given database

        :param database: database to persist friend requests in
        :param serializer: JSON serializer for friend requests
        :param collection_name: collection name in the database, default to "friend_requests"
        """
        super().__init__(database, serializer, collection_name)

    def get_requests_to_user(self, to_user: User) -> List[FriendRequest]:
        """Get all requests sent to given user, ordered by timestamp

        :param to_user: user receiving friend requests
        """
        requests = self._get_all_requests()
        requests = [req for req in requests if req.to_user_id == to_user.uuid]
        requests = sorted(requests, key=lambda req: req.timestamp)
        return requests

    def get_requests_from_user(self, from_user: User) -> List[FriendRequest]:
        """Get all requests sent by the given user, ordered by timestamp

        :param from_user: user sending friend requests
        """
        requests = self._get_all_requests()
        requests = [req for req in requests if req.from_user_id == from_user.uuid]
        requests = sorted(requests, key=lambda req: req.timestamp)
        return requests

    def _get_all_requests(self) -> List[FriendRequest]:
        """Get all friend requests from the database"""
        requests_json = self._database.get_collection(self._collection_name)
        return [self._serializer.from_json(req_json) for req_json in requests_json]


class PhotoRepository(BaseRepository):
    """Class for accessing photos stored in a database"""

    def __init__(
            self,
            database: Database,
            serializer: JsonSerializer,
            collection_name: str = "photos"
    ):
        """Create PhotoRepository connected to the given database

        :param database: database to persist photos in
        :param serializer: JSON serializer for photos
        :param collection_name: collection name in the database, defaults to "photos"
        """
        super().__init__(database, serializer, collection_name)
