"""Utilities for parameter validation and appropriate exceptions"""

import re
from string import ascii_letters

SALT_LENGTH = 10


def is_uuid(uuid: str) -> bool:
    """Check if string is a correct uuid

    :param uuid: string to check
    """
    uuid_pattern = re.compile(
        r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    )
    return bool(re.fullmatch(uuid_pattern, uuid))


def is_email(text: str) -> bool:
    """Return whether given text is a valid email address"""
    email_pattern = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    return bool(re.fullmatch(email_pattern, text))


def is_filename(text: str) -> bool:
    """Return whether given text is a valid filename"""
    filename_pattern = re.compile(r".+\..+")
    return bool(re.fullmatch(filename_pattern, text))


def is_hex(text: str) -> bool:
    """Return whether given text is a string of hexadecimal digits"""
    return all(char in "01234556789abcdef" for char in text)


def is_hash(text: str) -> bool:
    """Return whether given text is a valid hash"""
    if len(text) != 64:
        return False
    if any(char not in "0123456789abcdef" for char in text):
        return False

    return True


def is_salt(text: str) -> bool:
    """Return whether given text is a valid salt"""
    if len(text) != SALT_LENGTH:
        return False
    if any(char not in ascii_letters for char in text):
        return False

    return True


class ModelError(ValueError):
    """Exception signaling incorrect value for a model class"""
    pass


class IncorrectUuidError(ModelError):
    def __init__(self, uuid):
        super().__init__(f"{uuid} is not a uuid")
        self.uuid = uuid


class IncorrectUsernameError(ModelError):
    pass


class IncorrectEmailError(ModelError):
    def __init__(self, email):
        super().__init__(f"{email} is not a valid email address")
        self.email = email


class IncorrectPasswordHashError(ModelError):
    def __init__(self, password_hash):
        super().__init__(f"{password_hash} is not a valid hash")
        self.password_hash = password_hash


class IncorrectSaltError(ModelError):
    def __init__(self, salt):
        super().__init__(f"{salt} is not a valid salt")
        self.salt = salt


class IncorrectMessageTextError(ModelError):
    def __init__(self):
        super().__init__("Message text cannot be empty")


class IncorrectFilenameError(ModelError):
    def __init__(self, filename):
        super().__init__(f"{filename} is not a correct filename")
        self.filename = filename


class UnsupportedFileFormatError(ModelError):
    def __init__(self, file_format):
        super().__init__(f"{file_format} is not supported")
        self.file_format = file_format


class IncorrectHexRepresentationError(ModelError):
    def __init__(self):
        super().__init__(
            "Hex representation must be a string consisting of digits 0-9 "
            "and letters a-f"
        )


class SelfReferenceError(ModelError):

    def __init__(self):
        super().__init__("to_user and from_user cannot be the same")
