from typing import Optional, List

from core.model import User, Message, FriendRequest, Photo
from persistence.interface import Database, JsonSerializer


class UserRepository:
    def __init__(self, database: Database, serializer: JsonSerializer[User],
                 collection_name: str = "users"):
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def get_all(self) -> List[User]:
        users_json = self.__database.get_collection(self.__collection_name)
        users = [self.__serializer.from_json(user_json) for user_json in users_json]
        return users

    def save(self, user: User):
        user_dict = self.__serializer.to_json(user)
        self.__database.save(user_dict, self.__collection_name)

    def get_by_id(self, user_id: str) -> Optional[User]:
        user_dict = self.__database.get_by_id(user_id, self.__collection_name)
        return self.__serializer.from_json(user_dict) if user_dict is not None else None

    def delete(self, user: User):
        self.__database.delete_by_id(user.uuid, self.__collection_name)

    def get_by_username(self, username: str) -> Optional[User]:
        users = self.get_all()
        users = [user for user in users if user.username == username]
        return users[0] if users else None

    def get_by_email(self, email: str) -> Optional[User]:
        users = self.get_all()
        users = [user for user in users if user.email == email]
        return users[0] if users else None


class MessageRepository:
    def __init__(self, database: Database, serializer: JsonSerializer[Message],
                 collection_name: str = "messages"):
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def save(self, message: Message):
        message_json = self.__serializer.to_json(message)
        self.__database.save(message_json, self.__collection_name)

    def get_by_id(self, message_id: str) -> Optional[Message]:
        message_json = self.__database.get_by_id(message_id, self.__collection_name)
        return self.__serializer.from_json(message_json) if message_json else None

    def delete(self, message: Message):
        self.__database.delete_by_id(message.uuid, self.__collection_name)

    def get_messages(self, user_a: User, user_b: User) -> List[Message]:
        messages_json = self.__database.get_collection(self.__collection_name)
        messages = [self.__serializer.from_json(message_json) for message_json in messages_json]
        messages = [msg for msg in messages if _is_message_matched(msg, user_a, user_b)]
        messages = sorted(messages, key=lambda msg: msg.timestamp)
        return messages


def _is_message_matched(message: Message, user_a: User, user_b: User) -> bool:
    user_ids = (user_a.uuid, user_b.uuid)
    return message.to_user_id in user_ids and message.from_user_id in user_ids


class FriendRequestRepository:
    def __init__(self, database: Database, serializer: JsonSerializer[FriendRequest],
                 collection_name: str = "friend_requests"):
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def save(self, friend_request: FriendRequest):
        request_dict = self.__serializer.to_json(friend_request)
        self.__database.save(request_dict, self.__collection_name)

    def get_by_id(self, friend_request_id: str) -> Optional[FriendRequest]:
        request_dict = self.__database.get_by_id(friend_request_id, self.__collection_name)
        return self.__serializer.from_json(request_dict) if request_dict else None

    def delete(self, friend_request: FriendRequest):
        self.__database.delete_by_id(friend_request.uuid, self.__collection_name)

    def get_requests_to_user(self, to_user: User) -> List[FriendRequest]:
        requests = self._get_all_requests()
        requests = [req for req in requests if req.to_user_id == to_user.uuid]
        requests = sorted(requests, key=lambda req: req.timestamp)
        return requests

    def get_requests_from_user(self, from_user: User) -> List[FriendRequest]:
        requests = self._get_all_requests()
        requests = [req for req in requests if req.from_user_id == from_user.uuid]
        requests = sorted(requests, key=lambda req: req.timestamp)
        return requests

    def _get_all_requests(self) -> List[FriendRequest]:
        requests_json = self.__database.get_collection(self.__collection_name)
        return [self.__serializer.from_json(req_json) for req_json in requests_json]


class PhotoRepository:

    def __init__(self, database: Database, serializer: JsonSerializer[Photo],
                 collection_name: str = "photos"):
        self.__database = database
        self.__serializer = serializer
        self.__collection_name = collection_name

    def save(self, photo: Photo):
        photo_dict = self.__serializer.to_json(photo)
        self.__database.save(photo_dict, self.__collection_name)

    def get_by_id(self, photo_id: str) -> Optional[Photo]:
        photo_dict = self.__database.get_by_id(photo_id, self.__collection_name)
        return self.__serializer.from_json(photo_dict) if photo_dict else None

    def delete(self, photo: Photo):
        self.__database.delete_by_id(photo.uuid, self.__collection_name)

# TODO: factor out an abstract class
