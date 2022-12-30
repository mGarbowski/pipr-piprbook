"""Model classes structuring data used by the application and persisted in a database"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional, Protocol, List, BinaryIO, Tuple

from core.identifiers import generate_uuid
from core.validation import (
    is_email, is_filename, is_hex, is_uuid,
    IncorrectUuidError,
    IncorrectUsernameError,
    IncorrectEmailError,
    IncorrectPasswordHashError,
    IncorrectSaltError,
    IncorrectMessageTextError,
    IncorrectFilenameError,
    UnsupportedFileFormatError,
    IncorrectHexRepresentationError, is_hash, is_salt
)


class Entity(Protocol):
    uuid: str


@dataclass
class User:
    """Class for storing data about a user"""

    uuid: str
    username: str
    email: str
    password_hash: str
    salt: str
    friend_uuids: List[str] = field(default_factory=list)
    profile_picture_id: Optional[str] = None
    bio: Optional[str] = None

    def __post_init__(self):
        """Validate parameters

        :raises IncorrectUuidError: if uuid, profile_picure_id or any of friend_uuids is not a valid uuid
        :raises IncorrectEmailError: if email is not a correct email address
        :raises IncorrectPasswordHashError: if password_hash is not a valid sha256 hash
        :raises IncorrectSaltError: if salt has wrong length or illegal characters
        """
        if not is_uuid(self.uuid):
            raise IncorrectUuidError(self.uuid)
        if len(self.username) <= 3:
            raise IncorrectUsernameError("Username must be at least 3 characters long")
        if not is_email(self.email):
            raise IncorrectEmailError(self.email)
        if not is_hash(self.password_hash):
            raise IncorrectPasswordHashError(self.password_hash)
        if not is_salt(self.salt):
            raise IncorrectSaltError(self.salt)
        for friend_id in self.friend_uuids:
            if not is_uuid(friend_id):
                raise IncorrectUuidError(friend_id)
        if (self.profile_picture_id is not None) and (not is_uuid(self.profile_picture_id)):
            raise IncorrectUuidError(self.profile_picture_id)

    def is_friends_with(self, user: 'User') -> bool:
        """Return whether self is friends with user

        :param user: user to check
        """
        return user.uuid in self.friend_uuids


@dataclass
class Message:
    """Class for storing data about a message"""

    uuid: str
    text: str
    timestamp: datetime
    from_user_id: str
    to_user_id: str

    def __post_init__(self):
        """Validate parameters

        :raises IncorrectUuidError: if uuid, from_user_id or to_user_id is not a valid uuid
        :raises IncorrectMessageTextError: if text is empty
        """
        if not is_uuid(self.uuid):
            raise IncorrectUuidError(self.uuid)
        if not self.text:
            raise IncorrectMessageTextError()
        if not is_uuid(self.from_user_id):
            raise IncorrectUuidError(self.from_user_id)
        if not is_uuid(self.to_user_id):
            raise IncorrectUuidError(self.to_user_id)


@dataclass
class FriendRequest:
    """Class for storing data about a friend request"""

    uuid: str
    timestamp: datetime
    from_user_id: str
    to_user_id: str

    def __post_init__(self):
        """Validate parameters

        :raises IncorrectUuidError: if uuid, from_user_id or to_user_id is not a valid uuid
        """
        if not is_uuid(self.uuid):
            raise IncorrectUuidError(self.uuid)
        if not is_uuid(self.from_user_id):
            raise IncorrectUuidError(self.from_user_id)
        if not is_uuid(self.to_user_id):
            raise IncorrectUuidError(self.to_user_id)


@dataclass
class Photo:
    """Class representing a photo

    Content of the binary file is stored as a string of hexadecimal digits
    """
    uuid: str
    filename: str
    format: str
    binary_data_hex: str

    def __post_init__(self):
        """Validate parameters

        :raises IncorrectUuidError: if uuid is not a valid uuid
        :raises IncorrectFilenameError: if filename is incorrect
        :raises UnsupportedFileFormatError: if file format is not supported
        :raises IncorrectHexRepresentationError: if binary_data_hex is not a string of hex digits
        """
        if not is_uuid(self.uuid):
            raise IncorrectUuidError(self.uuid)
        if not is_filename(self.filename):
            raise IncorrectFilenameError(self.filename)
        formats = self.supported_file_formats
        if self.format not in formats:
            raise UnsupportedFileFormatError(self.format)
        if not is_hex(self.binary_data_hex):
            raise IncorrectHexRepresentationError()

    @property
    def supported_file_formats(self) -> Tuple[str, ...]:
        """Return tuple of suppoerted file formats"""
        return "jpg", "png"

    def get_bytes(self) -> bytes:
        """Return binary data of the photo"""
        return bytes.fromhex(self.binary_data_hex)

    @classmethod
    def from_file(cls, file_handle: BinaryIO, file_path: str) -> 'Photo':
        """Create a Photo object from a binary file

        :param file_handle: binary file
        :param file_path: path to the file

        :raises IncorrectFilenameError: if file's name is incorrect
        :raises UnsupportedFileFormatError: if file format is not supported
        """
        uuid = generate_uuid()

        path = Path(file_path)
        filename = path.name
        file_format = path.suffix.replace(".", "")

        photo_data = file_handle.read()
        binary_data_hex = photo_data.hex()

        return cls(uuid, filename, file_format, binary_data_hex)
