from unittest.mock import MagicMock

from pytest import raises

from core.authentication import Authentication, IncorrectPasswordError, UserDoesNotExistError, hash_password
from core.model import User

USER_1 = User(  # Password: 'password'
    uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
    username="user 1",
    email="email@example.com",
    password_hash="846ec57e1d6d3999798bfddb39de19c08e6a74ec17705d88b7314dd4a7694e48",
    salt="abcdefgh"
)

USER_2 = User(  # Password: 'pass123'
    uuid="9a154c0c-7bba-11ed-9b3d-00155df7f899",
    username="user 2",
    email="email2@example.com",
    password_hash="f06d0349dd77b094c4ea1f756a1653408f27eda416f08ffd32e37e5c989ce043",
    salt="saltsaltsalt"
)


def get_mock_user_repository():
    def mock_get_user(username):
        if username == "user 1":
            return USER_1
        elif username == "user 2":
            return USER_2
        return None

    mock_user_repository = MagicMock()
    mock_user_repository.get_by_username = mock_get_user
    return mock_user_repository


class TestAuthentication:

    def test_log_in_successful(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)
        assert authentication.logged_in_user is None

        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == USER_1

    def test_log_in_incorrect_password(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)
        assert authentication.logged_in_user is None

        with raises(IncorrectPasswordError):
            authentication.log_in("user 1", "incorrect")

        assert authentication.logged_in_user is None

    def test_log_in_user_does_not_exist(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)
        assert authentication.logged_in_user is None

        with raises(UserDoesNotExistError):
            authentication.log_in("user 3", "qwerty123")

        assert authentication.logged_in_user is None

    def test_log_out_current_user_on_log_in_attempt(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)

        with raises(Exception):
            authentication.log_in("user 2", "incorrect password")
        assert authentication.logged_in_user is None

        authentication.log_in("user 2", "pass123")
        assert authentication.logged_in_user == USER_2

        with raises(Exception):
            authentication.log_in("user 3", "qwerty123")
        assert authentication.logged_in_user is None

    def test_log_in_other_user_already_logged_in(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)

        authentication.log_in("user 2", "pass123")
        assert authentication.logged_in_user == USER_2
        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == USER_1

    def test_log_in_same_user_already_logged_in(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)

        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == USER_1
        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == USER_1

    def test_log_out(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)
        authentication.log_in("user 1", "password")

        authentication.log_out()
        assert authentication.logged_in_user is None

    def test_log_out_not_logged_in(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)
        authentication.log_out()
        assert authentication.logged_in_user is None

    def test_user_getter_returns_a_copy(self):
        mock_user_repository = get_mock_user_repository()
        authentication = Authentication(mock_user_repository)
        authentication.log_in("user 1", "password")

        user = authentication.logged_in_user
        user.password_hash = "abcd"

        assert authentication.logged_in_user.password_hash != "abcd"
        assert authentication.logged_in_user.password_hash == USER_1.password_hash


class TestHashPassword:

    def test_using_salt(self):
        first_hash = hash_password("same_password", "different_salt_1")
        second_hash = hash_password("same_password", "different_salt_2")
        assert first_hash != second_hash