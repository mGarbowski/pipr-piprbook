from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional, Protocol, List, BinaryIO

from core.identifiers import generate_uuid


class Entity(Protocol):
    uuid: str


@dataclass
class User:
    uuid: str
    username: str
    email: str
    password_hash: str
    salt: str
    friend_uuids: List[str] = field(default_factory=list)
    profile_picture_id: Optional[str] = None
    bio: Optional[str] = None

    def is_friends_with(self, user: 'User') -> bool:
        return user.uuid in self.friend_uuids


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


@dataclass
class Photo:
    """Class representing a photo

    Content of the binary file is stored as a hexadecimal string
    """
    uuid: str
    filename: str
    format: str
    binary_data_hex: str

    def get_bytes(self) -> bytes:
        return bytes.fromhex(self.binary_data_hex)

    @classmethod
    def from_file(cls, file_handle: BinaryIO, file_path: str) -> 'Photo':
        uuid = generate_uuid()

        path = Path(file_path)
        filename = path.name
        file_format = path.suffix.replace(".", "")

        photo_data = file_handle.read()
        binary_data_hex = photo_data.hex()

        return cls(uuid, filename, file_format, binary_data_hex)
