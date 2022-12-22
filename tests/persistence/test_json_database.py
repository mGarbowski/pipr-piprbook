from copy import copy
from datetime import datetime
from io import StringIO
from typing import TextIO

from pytest import fixture, mark, raises

from core.model import User, Message, FriendRequest
from core.serializers import UserSerializer, MessageSerializer, FriendRequestSerializer
from persistence.json_database import JsonDatabase, InvalidDatabaseFileError


@fixture
def user_1() -> User:
    return User(  # Password: 'password'
        uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
        username="user 1",
        email="email@example.com",
        password_hash="846ec57e1d6d3999798bfddb39de19c08e6a74ec17705d88b7314dd4a7694e48",
        salt="abcdefgh"
    )


@fixture
def user_2() -> User:
    return User(  # Password: 'pass123'
        uuid="9a154c0c-7bba-11ed-9b3d-00155df7f899",
        username="user 2",
        email="email2@example.com",
        password_hash="f06d0349dd77b094c4ea1f756a1653408f27eda416f08ffd32e37e5c989ce043",
        salt="saltsaltsalt"
    )


@fixture
def message_1() -> Message:
    return Message(
        uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
        text="Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
        timestamp=datetime(2022, 12, 14, 13, 41, 37),
        from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",  # from user_1
        to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"  # to user_2
    )


@fixture
def message_2() -> Message:
    return Message(
        uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
        text="Vel animi tempore enim praesentium. Exercitationem aperiam ullam dicta eum quia tempore quas.",
        timestamp=datetime(2022, 12, 14, 13, 41, 37),
        from_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899",  # from user_2
        to_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899"  # to user_1
    )


@fixture
def message_collection(message_1, message_2) -> dict[str, Message]:
    return {
        message_1.uuid: message_1,
        message_2.uuid: message_2
    }


@fixture
def users_collection(user_1, user_2) -> dict[str, User]:
    return {
        user_1.uuid: user_1,
        user_2.uuid: user_2
    }


@fixture
def collection_name_mapping():
    return {
        User: "users",
        Message: "messages",
        FriendRequest: "friend_requests"
    }


@fixture
def empty_database_file() -> TextIO:
    return StringIO('{"users": {},"messages": {},"friend_requests": {}}')


@fixture
def serializers():
    # TODO: Mock
    return {
        User: UserSerializer(),
        Message: MessageSerializer(),
        FriendRequest: FriendRequestSerializer()
    }


@fixture
def empty_database(empty_database_file, collection_name_mapping, serializers):
    return JsonDatabase(empty_database_file, collection_name_mapping, serializers)


class TestJsonDatabase:

    def test_create_database_incomplete_collections(self, collection_name_mapping, serializers):
        incomplete_file = StringIO('{"messages": {},"friend_requests": {}}')

        with raises(InvalidDatabaseFileError):
            JsonDatabase(incomplete_file, collection_name_mapping, serializers)

    def test_create_database_not_a_json_file(self, collection_name_mapping, serializers):
        not_a_json = StringIO("<h1>This is not a json file</h1>")
        with raises(InvalidDatabaseFileError):
            JsonDatabase(not_a_json, collection_name_mapping, serializers)

    def test_save_and_get_from_initially_empty_database(self, empty_database, user_1):
        empty_database.save_item(user_1)
        user_from_db = empty_database.get_item(user_1.uuid, User)
        assert user_from_db == user_1

    def test_save_and_get_multiple_times(self, empty_database, user_1):
        empty_database.save_item(user_1)

        user_from_db = empty_database.get_item(user_1.uuid, User)
        assert user_from_db == user_1

        second_user_from_db = empty_database.get_item(user_1.uuid, User)
        assert second_user_from_db == user_1

        third_user_from_db = empty_database.get_item(user_1.uuid, User)
        assert third_user_from_db == user_1

    def test_get_item_from_empty_db(self, empty_database, user_1):
        user = empty_database.get_item(user_1.uuid, User)
        assert user is None

    def test_get_existing_item_wrong_type(self, empty_database, user_1):
        empty_database.save_item(user_1)
        search_result = empty_database.get_item(user_1.uuid, Message)
        assert search_result is None

    def test_update_existing_entity(self, empty_database, user_1):
        initial_user = copy(user_1)
        empty_database.save_item(user_1)

        user_from_db = empty_database.get_item(initial_user.uuid, User)
        assert user_from_db == initial_user
        assert user_from_db.username == "user 1"

        user_1.username = "new_user_1"
        empty_database.save_item(user_1)
        user_from_db = empty_database.get_item(initial_user.uuid, User)

        assert user_from_db != initial_user
        assert user_from_db == user_1
        assert user_from_db.username == "new_user_1"

    def test_save_multiple_entities(self, empty_database, user_1, user_2):
        empty_database.save_item(user_1)
        empty_database.save_item(user_2)

        user_1_from_db = empty_database.get_item(user_1.uuid, User)
        user_2_from_db = empty_database.get_item(user_2.uuid, User)

        assert user_1 == user_1_from_db
        assert user_2 == user_2_from_db

    def test_delete_existing_item(self, empty_database, user_1):
        empty_database.save_item(user_1)
        assert empty_database.get_item(user_1.uuid, User) is not None

        empty_database.delete_item(user_1)
        assert empty_database.get_item(user_1.uuid, User) is None

    def test_delete_non_existing_item(self, empty_database, user_1):
        assert empty_database.get_item(user_1.uuid, User) is None
        empty_database.delete_item(user_1)
        assert empty_database.get_item(user_1.uuid, User) is None

    def test_delete_existing_item_by_id(self, empty_database, user_1):
        empty_database.save_item(user_1)
        assert empty_database.get_item(user_1.uuid, User) is not None

        empty_database.delete_item_by_id(user_1.uuid, User)
        assert empty_database.get_item(user_1.uuid, User) is None

    def test_delete_non_existing_item_by_id(self, empty_database, user_1):
        assert empty_database.get_item(user_1.uuid, User) is None
        empty_database.delete_item_by_id(user_1.uuid, User)
        assert empty_database.get_item(user_1.uuid, User) is None

    @mark.parametrize("collection_type", [User, Message, FriendRequest])
    def test_get_collection_empty(self, empty_database, collection_type):
        collection = empty_database.get_collection(collection_type)
        assert collection == {}

    def test_get_collection_single_element(self, empty_database, user_1):
        empty_database.save_item(user_1)
        collection = empty_database.get_collection(User)

        assert len(collection) == 1
        assert user_1.uuid in collection
        assert collection[user_1.uuid] == user_1

    def test_get_collection_multiple_elements(self, empty_database, user_1, user_2, users_collection):
        empty_database.save_item(user_1)
        empty_database.save_item(user_2)
        collection = empty_database.get_collection(User)

        assert collection == users_collection
        assert len(collection) == 2
        assert user_1.uuid in collection
        assert user_2.uuid in collection
        assert collection[user_1.uuid] == user_1
        assert collection[user_2.uuid] == user_2

    def test_get_collection_wrong_type(self, empty_database, user_1, user_2, users_collection):
        empty_database.save_item(user_1)
        empty_database.save_item(user_2)
        collection = empty_database.get_collection(Message)

        assert collection != users_collection
        assert collection == {}

    def test_overwrite_with_empty_collection(self, empty_database, users_collection):
        empty_database.save_collection(users_collection)
        empty_database.save_collection({}, User)
        collection = empty_database.get_collection(User)

        assert collection != users_collection
        assert collection == {}

    def test_save_empty_collection(self, empty_database):
        empty_database.save_collection({}, Message)
        collection = empty_database.get_collection(Message)
        assert collection == {}

    def test_save_empty_collection_incorrect_use(self, empty_database):
        with raises(ValueError):
            empty_database.save_collection({})

    def test_save_collection_typical_use(self, empty_database, users_collection, user_1, user_2):
        empty_database.save_collection(users_collection)
        collection = empty_database.get_collection(User)

        assert collection == users_collection
        assert collection[user_1.uuid] == user_1
        assert collection[user_2.uuid] == user_2

        user_1_from_db = empty_database.get_item(user_1.uuid, User)
        user_2_from_db = empty_database.get_item(user_2.uuid, User)
        assert user_1_from_db == user_1
        assert user_2_from_db == user_2

    def test_save_nonempty_collection_specify_correct_type(self, empty_database, users_collection):
        with raises(ValueError):
            empty_database.save_collection(users_collection, User)

    def test_save_nonempty_collection_specify_incorrect_type(self, empty_database, users_collection):
        with raises(ValueError):
            empty_database.save_collection(users_collection, Message)
