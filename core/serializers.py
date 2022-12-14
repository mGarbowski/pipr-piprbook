from datetime import datetime

from core.model import User, Message, FriendRequest


def user_to_json(user: User) -> dict:
    """Convert user object to JSON representation"""
    return {
        "uuid": user.uuid,
        "username": user.username,
        "email": user.email,
        "password_hash": user.password_hash,
        "salt": user.salt,
        "friend_uuids": user.friend_uuids,
        "profile_picture_id": user.profile_picture_id,
        "bio": user.bio
    }


def user_from_json(json: dict) -> User:
    """Create user object from its JSON representation

    :raises RepresentationError: if given json is not a valid representation of a user
    """
    try:
        return User(
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


def message_to_json(message: Message) -> dict:
    """Convert a message object to JSON representation

    Timestamps are stored as ISO-format strings
    """
    return {
        "uuid": message.uuid,
        "text": message.text,
        "timestamp": message.timestamp.isoformat(),
        "from_user_id": message.from_user_id,
        "to_user_id": message.to_user_id,
    }


def message_from_json(json: dict) -> Message:
    """Create a message object from its JSON representation

    :raises RepresentationError: if json is not a valid representation of a message
    """
    try:
        return Message(
            uuid=json["uuid"],
            text=json["text"],
            timestamp=datetime.fromisoformat(json["timestamp"]),
            from_user_id=json["from_user_id"],
            to_user_id=json["to_user_id"]
        )
    except KeyError:
        raise RepresentationError(json)


def friend_request_to_json(friend_request: FriendRequest) -> dict:
    """Convert a friend request object to a JSON representation

    Timestamps are sotred as ISO-format strings
    """
    return {
        "uuid": friend_request.uuid,
        "timestamp": friend_request.timestamp.isoformat(),
        "from_user_id": friend_request.from_user_id,
        "to_user_id": friend_request.to_user_id,
    }


def friend_request_from_json(json: dict) -> FriendRequest:
    """Create a friend request object from its JSON representation

    :raises RepresentationError: if json is not a valid representation of a friend request
    """
    try:
        return FriendRequest(
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
