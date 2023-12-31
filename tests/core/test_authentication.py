from unittest.mock import MagicMock

from pytest import raises, fixture

from core.authentication import Authentication, IncorrectPasswordError, UserDoesNotExistError, hash_password, \
    generate_salt
from core.model import User
from core.validation import is_hash, is_salt
from persistence.repositories import UserRepository


@fixture
def user_1() -> User:
    return User(  # Password: 'password'
        uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
        username="user 1",
        email="email@example.com",
        password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
        salt="aaaaaaaaaa"
    )


@fixture
def user_2() -> User:
    return User(  # Password: 'pass123'
        uuid="9a154c0c-7bba-11ed-9b3d-00155df7f899",
        username="user 2",
        email="email2@example.com",
        password_hash="b5c90ac7dc4c828717699bc943bfeb54e6f682ca055bfc5591c8a471dfc0d794",
        salt="saltsaltsa"
    )


@fixture
def user_repository(user_1, user_2) -> UserRepository:
    def mock_get_user(username):
        if username == user_1.username:
            return user_1
        elif username == user_2.username:
            return user_2
        return None

    mock_user_repository = MagicMock()
    mock_user_repository.get_by_username = mock_get_user
    return mock_user_repository


@fixture
def authentication(user_repository) -> Authentication:
    return Authentication(user_repository)


class TestAuthentication:

    def test_logged_in_user_initially_none(self, authentication):
        assert authentication.logged_in_user is None

    def test_log_in_successful(self, authentication, user_1):
        assert authentication.logged_in_user is None

        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == user_1

    def test_log_in_incorrect_password(self, authentication):
        assert authentication.logged_in_user is None

        with raises(IncorrectPasswordError):
            authentication.log_in("user 1", "incorrect")

        assert authentication.logged_in_user is None

    def test_log_in_user_does_not_exist(self, authentication):
        assert authentication.logged_in_user is None

        with raises(UserDoesNotExistError):
            authentication.log_in("user 3", "qwerty123")

        assert authentication.logged_in_user is None

    def test_log_out_current_user_on_log_in_attempt(self, authentication, user_2):
        with raises(Exception):
            authentication.log_in("user 2", "incorrect password")
        assert authentication.logged_in_user is None

        authentication.log_in("user 2", "pass123")
        assert authentication.logged_in_user == user_2

        with raises(Exception):
            authentication.log_in("user 3", "qwerty123")
        assert authentication.logged_in_user is None

    def test_log_in_other_user_already_logged_in(self, authentication, user_1, user_2):
        authentication.log_in("user 2", "pass123")
        assert authentication.logged_in_user == user_2

        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == user_1

    def test_log_in_same_user_already_logged_in(self, authentication, user_1):
        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == user_1
        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == user_1

    def test_log_out(self, authentication, user_1):
        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == user_1

        authentication.log_out()
        assert authentication.logged_in_user is None

    def test_log_out_not_logged_in(self, authentication):
        assert authentication.logged_in_user is None
        authentication.log_out()
        assert authentication.logged_in_user is None

    def test_user_getter_returns_a_copy(self, authentication, user_1):
        authentication.log_in("user 1", "password")
        assert authentication.logged_in_user == user_1

        user = authentication.logged_in_user
        user.password_hash = "abcd"

        assert authentication.logged_in_user.password_hash != "abcd"
        assert authentication.logged_in_user.password_hash == user_1.password_hash


class TestHashPassword:

    def test_using_salt(self):
        first_hash = hash_password("same_password", "different_salt_1")
        second_hash = hash_password("same_password", "different_salt_2")
        assert first_hash != second_hash

    def test_generated_is_hash(self):
        assert is_hash(hash_password("same_password", "some_salt"))


class TestSalt:

    def test_generated_is_salt(self):
        assert is_salt(generate_salt())
