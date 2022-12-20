from dataclasses import dataclass, field
from datetime import datetime

from typing import Optional, Protocol


class Entity(Protocol):
    uuid: str


class JsonSerializable(Entity, Protocol):
    def to_json(self) -> dict:
        ...

    @classmethod
    def from_json(cls, json: dict) -> 'JsonSerializable':
        ...


@dataclass
class User:
    uuid: str
    username: str
    email: str
    password_hash: str
    salt: str
    friend_uuids: list[str] = field(default_factory=list)
    profile_picture_id: Optional[str] = None
    bio: Optional[str] = None

    def to_json(self) -> dict:
        """Convert user object to JSON representation"""
        return {
            "uuid": self.uuid,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "salt": self.salt,
            "friend_uuids": self.friend_uuids,
            "profile_picture_id": self.profile_picture_id,
            "bio": self.bio
        }

    @classmethod
    def from_json(cls, json: dict) -> 'User':
        """Create user object from its JSON representation

        :raises RepresentationError: if given json is not a valid representation of a user
        """
        try:
            return cls(
                uuid=json["uuid"],
                username=json["username"],
                email=json["email"],
                password_hash=json["password_hash"],
                salt=json["salt"],
                friend_uuids=json["friend_uuids"],
                profile_picture_id=json["profile_picture_id"],
                bio=json["bio"]
            )
        except KeyError:
            raise RepresentationError(json)


@dataclass
class Message:
    uuid: str
    text: str
    timestamp: datetime
    from_user_id: str
    to_user_id: str

    def to_json(self) -> dict:
        """Convert a message object to JSON representation

        Timestamps are stored as ISO-format strings
        """
        return {
            "uuid": self.uuid,
            "text": self.text,
            "timestamp": self.timestamp.isoformat(),
            "from_user_id": self.from_user_id,
            "to_user_id": self.to_user_id,
        }

    @classmethod
    def from_json(cls, json: dict) -> 'Message':
        """Create a message object from its JSON representation

        :raises RepresentationError: if json is not a valid representation of a message
        """
        try:
            return cls(
                uuid=json["uuid"],
                text=json["text"],
                timestamp=datetime.fromisoformat(json["timestamp"]),
                from_user_id=json["from_user_id"],
                to_user_id=json["to_user_id"]
            )
        except KeyError:
            raise RepresentationError(json)


@dataclass
class FriendRequest:
    uuid: str
    timestamp: datetime
    from_user_id: str
    to_user_id: str

    def to_json(self) -> dict:
        """Convert a friend request object to a JSON representation

        Timestamps are sotred as ISO-format strings
        """
        return {
            "uuid": self.uuid,
            "timestamp": self.timestamp.isoformat(),
            "from_user_id": self.from_user_id,
            "to_user_id": self.to_user_id,
        }

    @classmethod
    def from_json(cls, json: dict) -> 'FriendRequest':
        """Create a friend request object from its JSON representation

        :raises RepresentationError: if json is not a valid representation of a friend request
        """
        try:
            return cls(
                uuid=json["uuid"],
                timestamp=datetime.fromisoformat(json["timestamp"]),
                from_user_id=json["from_user_id"],
                to_user_id=json["to_user_id"]
            )
        except KeyError:
            raise RepresentationError(json)


class RepresentationError(Exception):
    """Exception signaling invalid representation of an object"""

    def __init__(self, json):
        super().__init__("Received invalid representation of an object")
        self.json = json
