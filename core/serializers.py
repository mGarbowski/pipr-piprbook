from datetime import datetime
from typing import TypeVar

from core.model import User, Message, FriendRequest

T = TypeVar("T")


class UserSerializer:

    @staticmethod
    def to_json(entity: User) -> dict:
        """Convert user object to JSON representation"""
        return {
            "uuid": entity.uuid,
            "username": entity.username,
            "email": entity.email,
            "password_hash": entity.password_hash,
            "salt": entity.salt,
            "friend_uuids": entity.friend_uuids,
            "profile_picture_id": entity.profile_picture_id,
            "bio": entity.bio
        }

    @staticmethod
    def from_json(json_dict: dict) -> User:
        """Create user object from its JSON representation

        :raises RepresentationError: if given json is not a valid representation of a user
        """
        try:
            return User(
                uuid=json_dict["uuid"],
                username=json_dict["username"],
                email=json_dict["email"],
                password_hash=json_dict["password_hash"],
                salt=json_dict["salt"],
                friend_uuids=json_dict["friend_uuids"],
                profile_picture_id=json_dict["profile_picture_id"],
                bio=json_dict["bio"]
            )
        except KeyError:
            raise RepresentationError(json_dict)


class MessageSerializer:
    @staticmethod
    def to_json(entity: Message) -> dict:
        """Convert a message object to JSON representation

        Timestamps are stored as ISO-format strings
        """
        return {
            "uuid": entity.uuid,
            "text": entity.text,
            "timestamp": entity.timestamp.isoformat(),
            "from_user_id": entity.from_user_id,
            "to_user_id": entity.to_user_id,
        }

    @staticmethod
    def from_json(json_dict: dict) -> Message:
        """Create a message object from its JSON representation

        :raises RepresentationError: if json is not a valid representation of a message
        """
        try:
            return Message(
                uuid=json_dict["uuid"],
                text=json_dict["text"],
                timestamp=datetime.fromisoformat(json_dict["timestamp"]),
                from_user_id=json_dict["from_user_id"],
                to_user_id=json_dict["to_user_id"]
            )
        except KeyError:
            raise RepresentationError(json_dict)


class FriendRequestSerializer:
    @staticmethod
    def to_json(entity: FriendRequest) -> dict:
        """Convert a friend request object to a JSON representation

        Timestamps are stored as ISO-format strings
        """
        return {
            "uuid": entity.uuid,
            "timestamp": entity.timestamp.isoformat(),
            "from_user_id": entity.from_user_id,
            "to_user_id": entity.to_user_id,
        }

    @staticmethod
    def from_json(json_dict: dict) -> FriendRequest:
        """Create a friend request object from its JSON representation

        :raises RepresentationError: if json is not a valid representation of a friend request
        """
        try:
            return FriendRequest(
                uuid=json_dict["uuid"],
                timestamp=datetime.fromisoformat(json_dict["timestamp"]),
                from_user_id=json_dict["from_user_id"],
                to_user_id=json_dict["to_user_id"]
            )
        except KeyError:
            raise RepresentationError(json_dict)


class RepresentationError(Exception):
    """Exception signaling invalid representation of an object"""

    def __init__(self, json):
        super().__init__("Received invalid representation of an object")
        self.json = json