"""Repository classes for accessing data persisted in a Database"""

from typing import Optional, List

from core.model import User, Message, FriendRequest, Photo
from persistence.interface import Database, JsonSerializer


class UserRepository:
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
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def get_all(self) -> List[User]:
        """Get all users"""
        users_json = self.__database.get_collection(self.__collection_name)
        users = [self.__serializer.from_json(user_json) for user_json in users_json]
        return users

    def save(self, user: User):
        """Create new user or update existing one

        :param user: user to create or update
        """
        user_dict = self.__serializer.to_json(user)
        self.__database.save(user_dict, self.__collection_name)

    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get user by id or None if it does not exist

        :param user_id: id of searched user
        """
        user_dict = self.__database.get_by_id(user_id, self.__collection_name)
        return self.__serializer.from_json(user_dict) if user_dict is not None else None

    def delete(self, user: User) -> None:
        """Delete user

        :param user: user to delete
        """
        self.__database.delete_by_id(user.uuid, self.__collection_name)

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


class MessageRepository:
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
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def save(self, message: Message):
        """Create new message or update existing one"""
        message_json = self.__serializer.to_json(message)
        self.__database.save(message_json, self.__collection_name)

    def get_by_id(self, message_id: str) -> Optional[Message]:
        """Get message by id or None if it does not exist

        :param message_id: id of searched message
        """
        message_json = self.__database.get_by_id(message_id, self.__collection_name)
        return self.__serializer.from_json(message_json) if message_json else None

    def delete(self, message: Message):
        """Delete message or do nothing if it does not exist in the database"""
        self.__database.delete_by_id(message.uuid, self.__collection_name)

    def get_messages(self, user_a: User, user_b: User) -> List[Message]:
        """Get all messages exchanged between two users, ordered by timestamp

        Earlier messages first
        Order of users does not matter

        :param user_a: one of the users sending or receiving messages
        :param user_b: one of the users sending or receiving messages
        """
        messages_json = self.__database.get_collection(self.__collection_name)
        messages = [self.__serializer.from_json(message_json) for message_json in messages_json]
        messages = [msg for msg in messages if _is_message_matched(msg, user_a, user_b)]
        messages = sorted(messages, key=lambda msg: msg.timestamp)
        return messages


def _is_message_matched(message: Message, user_a: User, user_b: User) -> bool:
    """Return whether message was sent from one of given users to the other"""
    user_ids = (user_a.uuid, user_b.uuid)
    return message.to_user_id in user_ids and message.from_user_id in user_ids


class FriendRequestRepository:
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
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def save(self, friend_request: FriendRequest):
        """Create new friend request or update existing one

        :param friend_request: friend request to save or update
        """
        request_dict = self.__serializer.to_json(friend_request)
        self.__database.save(request_dict, self.__collection_name)

    def get_by_id(self, friend_request_id: str) -> Optional[FriendRequest]:
        """Get friend request by id or None if it does not exist

        :param friend_request_id: id of searched friend request
        """
        request_dict = self.__database.get_by_id(friend_request_id, self.__collection_name)
        return self.__serializer.from_json(request_dict) if request_dict else None

    def delete(self, friend_request: FriendRequest):
        """Delete friend request or do nothing if it does not exist in the database

        :param friend_request: friend request to delete
        """
        self.__database.delete_by_id(friend_request.uuid, self.__collection_name)

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
        requests_json = self.__database.get_collection(self.__collection_name)
        return [self.__serializer.from_json(req_json) for req_json in requests_json]


class PhotoRepository:
    """Class for accessing photos stored in a database"""

    def __init__(
            self,
            database: Database,
            serializer: JsonSerializer[Photo],
            collection_name: str = "photos"
    ):
        """Create a PhotoRepository connected to the given database

        :param database: database to persist photos in
        :param serializer: JSON serializer for photos
        :param collection_name: collection name in the database, defaults to "photos"
        """
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def save(self, photo: Photo):
        """Create new photo or update existing one

        :param photo: photo to create or update
        """
        photo_dict = self.__serializer.to_json(photo)
        self.__database.save(photo_dict, self.__collection_name)

    def get_by_id(self, photo_id: str) -> Optional[Photo]:
        """Get photo by id or None if it does not exist

        :param photo_id: id of searched photo
        """
        photo_dict = self.__database.get_by_id(photo_id, self.__collection_name)
        return self.__serializer.from_json(photo_dict) if photo_dict else None

    def delete(self, photo: Photo):
        """Delete photo or do nothing if it does not exist in the database

        :param photo: photo to delete
        """
        self.__database.delete_by_id(photo.uuid, self.__collection_name)

# TODO: factor out an abstract class
