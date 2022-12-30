from unittest.mock import MagicMock

from pytest import fixture

from core.model import User
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
def user_1_json():
    return {
        'uuid': 'c1a40f26-7ba9-11ed-9382-00155df7f899',
        'username': 'user 1',
        'email': 'email@example.com',
        'password_hash': 'fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd',
        'salt': 'aaaaaaaaaa',
        'friend_uuids': [],
        'profile_picture_id': None,
        'bio': None
    }


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
def user_2_json():
    return {
        'uuid': '9a154c0c-7bba-11ed-9b3d-00155df7f899',
        'username': 'user 2',
        'email': 'email2@example.com',
        'password_hash': 'b5c90ac7dc4c828717699bc943bfeb54e6f682ca055bfc5591c8a471dfc0d794',
        'salt': 'saltsaltsa',
        'friend_uuids': [],
        'profile_picture_id': None,
        'bio': None
    }


@fixture
def user_3() -> User:
    return User(  # Password: "user3"
        uuid="fcffaa38-8862-11ed-942c-00155d211f36",
        username="user 3",
        email="user3@example.com",
        password_hash="b18e08d8a1bab666c11253364eb187208390b714a144392ce9b84f9f2dd6d6bf",
        salt="bbbbbbbbbb"
    )


@fixture
def user_3_json():
    return {
        'uuid': 'fcffaa38-8862-11ed-942c-00155d211f36',
        'username': 'user 3',
        'email': 'user3@example.com',
        'password_hash': 'b18e08d8a1bab666c11253364eb187208390b714a144392ce9b84f9f2dd6d6bf',
        'salt': 'bbbbbbbbbb',
        'friend_uuids': [],
        'profile_picture_id': None,
        'bio': None
    }


@fixture
def users_collection(user_1, user_2, user_3):
    return [user_1, user_2, user_3]


@fixture
def users_json_collection(user_1_json, user_2_json, user_3_json):
    return [user_1_json, user_2_json, user_3_json]


@fixture
def database(user_1_json, user_2_json, user_3_json, users_json_collection):
    def get_by_id(entity_id, collection_name):
        if collection_name == "users":
            if entity_id == user_1_json["uuid"]:
                return user_1_json
            elif entity_id == user_2_json["uuid"]:
                return user_2_json
            elif entity_id == user_3_json["uuid"]:
                return user_3_json
            else:
                return None

    def get_collection(collection_name):
        if collection_name == "users":
            return users_json_collection

    database = MagicMock()
    database.get_by_id = get_by_id
    database.get_collection = get_collection
    return database


@fixture
def user_serializer(user_1, user_2, user_3, user_1_json, user_2_json, user_3_json):
    def to_json(user):
        if user == user_1:
            return user_1_json
        elif user == user_2:
            return user_2_json
        elif user == user_3:
            return user_3_json

    def from_json(json_dict):
        if json_dict == user_1_json:
            return user_1
        elif json_dict == user_2_json:
            return user_2
        elif json_dict == user_3_json:
            return user_3

    serializer = MagicMock()
    serializer.to_json = to_json
    serializer.from_json = from_json
    return serializer


@fixture
def user_repository(database, user_serializer):
    return UserRepository(database, user_serializer, "users")


class TestUserRepository:

    def test_get_all(self, user_repository, users_collection):
        assert user_repository.get_all() == users_collection

    def test_save(self, database, user_repository, user_1, user_1_json):
        user_repository.save(user_1)
        database.save.assert_called_with(user_1_json, "users")

    def test_get_by_id(self, user_repository, user_1):
        assert user_repository.get_by_id(user_1.uuid) == user_1

    def test_get_by_id_does_not_exist(self, user_repository):
        assert user_repository.get_by_id("02240d58-8866-11ed-942c-00155d211f36") is None

    def test_delete(self, user_repository, database, user_1):
        user_repository.delete(user_1)
        database.delete_by_id.assert_called_with(user_1.uuid, "users")

    def test_get_by_username(self, user_repository, user_1):
        assert user_repository.get_by_username(user_1.username) == user_1

    def test_get_by_username_does_not_exist(self, user_repository):
        assert user_repository.get_by_username("doesnotexist") is None

    def test_get_by_email(self, user_repository, user_1):
        assert user_repository.get_by_email(user_1.email) == user_1

    def test_get_by_email_does_not_exist(self, user_repository):
        assert user_repository.get_by_email("doesnotexist@example.com") is None

    def test_get_by_username_fragment(self, user_repository, user_1, user_2, user_3):
        found = user_repository.get_by_username_fragment("us")
        assert len(found) == 3
        assert user_1 in found
        assert user_2 in found
        assert user_3 in found

    def test_get_by_username_fragment_empty(self, user_repository):
        assert user_repository.get_by_username_fragment("no match") == []
