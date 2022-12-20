from copy import deepcopy
from hashlib import sha256
from typing import Optional

from core.model import User
from persistence.interface import UserRepository


class Authentication:
    """Class for managing user authentication

    Stores currently logged-in user.
    Handles logging in and out.
    Compares user credentials with those stored in UserRepository.
    """

    def __init__(self, user_repository: UserRepository):
        """Create a new Authentication object, initially no user is logged in

        :param user_repository: UserRepository to get user credentials from
        """
        self.__user_repository = user_repository
        self.__logged_in_user: Optional[User] = None

    # TODO: secure aggainst timing attack
    def log_in(self, login: str, password: str) -> None:
        """Attempt to log in with given credentials

        Logs out previously logged-in user if there was any.
        Raises exception on failed log-in attempt

        :raises UserDoesNotExistError: if there is no user with matching login
        :raises IncorrectPasswordError: if given password is incorrect
        """
        if self.__logged_in_user is not None:
            self.log_out()

        user = self.__user_repository.get_by_username(login)
        if user is None:
            raise UserDoesNotExistError(login)

        if hash_password(password, user.salt) == user.password_hash:
            self.__logged_in_user = user
        else:
            raise IncorrectPasswordError()

    def log_out(self) -> None:
        """Log out currently logged-in user if there is any"""
        self.__logged_in_user = None

    @property
    def logged_in_user(self) -> Optional[User]:
        """Return a deep copy of currently logged-in user

        Copying to prevent from mutating the user externally - security vulnerability
        """
        return deepcopy(self.__logged_in_user)


def hash_password(password: str, salt: str) -> str:
    """Hash password with salt using SHA256 algorithm with UTF-8 encoding

    :param password: user's password
    :param salt: random string concatenated to the password before hashing
        for additional security
    """
    salted_password = password + salt
    utf_encoded = salted_password.encode("utf-8")
    hashed_password = sha256(utf_encoded).hexdigest()
    return hashed_password


class UserDoesNotExistError(Exception):
    """Exception signaling that there is no user with given login/username"""

    def __init__(self, username):
        super().__init__(f"User: {username} does not exist")
        self.username = username


class IncorrectPasswordError(Exception):
    """Exception singaling that given password is incorrect"""

    def __init__(self):
        super().__init__("Incorrect password")


class UnauthorizedError(Exception):
    pass
