from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    user_id: str
    username: str
    email: str
    password_hash: str
    salt: str
    friends: list['User'] = field(default_factory=list)
    profile_picture_id: Optional[str] = None
    bio: Optional[str] = None
