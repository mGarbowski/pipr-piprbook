from dataclasses import dataclass, field
from datetime import datetime

from typing import Optional


@dataclass
class User:
    uuid: str
    username: str
    email: str
    password_hash: str
    salt: str
    friends: list['User'] = field(default_factory=list)
    profile_picture_id: Optional[str] = None
    bio: Optional[str] = None


@dataclass
class Message:
    uuid: str
    text: str
    timestamp: datetime
    from_user_id: str
    to_user_id: str


@dataclass
class FriendRequest:
    uuid: str
    timestamp: datetime
    from_user_id: str
    to_user_id: str
