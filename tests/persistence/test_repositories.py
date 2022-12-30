from unittest.mock import MagicMock

from pytest import fixture

from persistence.repositories import UserRepository, MessageRepository, FriendRequestRepository, PhotoRepository


@fixture
def database(user_1_json, user_2_json, user_3_json, users_json_collection,
             message_1_json, message_2_json,
             request_1_json, request_2_json,
             photo_1_json):
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
        elif collection_name == "messages":
            if entity_id == message_1_json["uuid"]:
                return message_1_json
            elif entity_id == message_2_json["uuid"]:
                return message_2_json
            else:
                return None
        elif collection_name == "friend_requests":
            if entity_id == request_1_json["uuid"]:
                return request_1_json
            elif entity_id == request_2_json["uuid"]:
                return request_2_json
            else:
                return None
        elif collection_name == "photos":
            if entity_id == photo_1_json["uuid"]:
                return photo_1_json

    def get_collection(collection_name):
        if collection_name == "users":
            return users_json_collection
        elif collection_name == "messages":
            return [message_1_json, message_2_json]
        elif collection_name == "friend_requests":
            return [request_1_json, request_2_json]
        elif collection_name == "photos":
            return [photo_1_json]

    database = MagicMock()
    database.get_by_id = get_by_id
    database.get_collection = get_collection
    return database


@fixture
def message_serializer(message_1, message_2, message_1_json, message_2_json):
    def to_json(message):
        if message == message_1:
            return message_1_json
        elif message == message_2:
            return message_2_json

    def from_json(json_dict):
        if json_dict == message_1_json:
            return message_1
        elif json_dict == message_2_json:
            return message_2

    serializer = MagicMock()
    serializer.to_json = to_json
    serializer.from_json = from_json
    return serializer


@fixture
def friend_request_serializer(request_1, request_2, request_1_json, request_2_json):
    def to_json(entity):
        if entity == request_1:
            return request_1_json
        elif entity == request_2:
            return request_2_json

    def from_json(json_dict):
        if json_dict == request_1_json:
            return request_1
        elif json_dict == request_2_json:
            return request_2

    serializer = MagicMock()
    serializer.to_json = to_json
    serializer.from_json = from_json
    return serializer


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
def photo_serializer(photo_1, photo_1_json):
    def to_json(entity):
        if entity == photo_1:
            return photo_1_json

    def from_json(json_dict):
        if json_dict == photo_1_json:
            return photo_1

    serializer = MagicMock()
    serializer.to_json = to_json
    serializer.from_json = from_json
    return serializer


@fixture
def user_repository(database, user_serializer):
    return UserRepository(database, user_serializer, "users")


@fixture
def message_repository(database, message_serializer):
    return MessageRepository(database, message_serializer, "messages")


@fixture
def friend_request_repository(database, friend_request_serializer):
    return FriendRequestRepository(database, friend_request_serializer, "friend_requests")


@fixture
def photo_repository(database, photo_serializer):
    return PhotoRepository(database, photo_serializer, "photos")


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


class TestMessageRepository:

    def test_save(self, message_repository, message_1, message_1_json, database):
        message_repository.save(message_1)
        database.save.assert_called_with(message_1_json, "messages")

    def test_get_by_id(self, message_repository, message_1):
        assert message_repository.get_by_id(message_1.uuid) == message_1

    def test_by_id_does_not_exist(self, message_repository):
        assert message_repository.get_by_id("66fb0af2-886a-11ed-942c-00155d211f36") is None

    def test_delete(self, message_repository, message_1, database):
        message_repository.delete(message_1)
        database.delete_by_id.assert_called_with(message_1.uuid, "messages")

    def test_get_messages_order_of_users_does_not_matter(self, message_repository, user_1, user_2):
        first = message_repository.get_messages(user_2, user_1)
        second = message_repository.get_messages(user_1, user_2)
        assert first == second

    def test_get_messages_earliest_first(self, message_repository, message_1, message_2, user_1, user_2):
        messages = message_repository.get_messages(user_2, user_1)
        assert messages == [message_1, message_2]

    def test_get_messages_empty(self, message_repository, user_1, user_2, user_3):
        assert message_repository.get_messages(user_1, user_3) == []
        assert message_repository.get_messages(user_2, user_3) == []


class TestFriendRequestRepository:

    def test_save(self, friend_request_repository, database, request_1, request_1_json):
        friend_request_repository.save(request_1)
        database.save.assert_called_with(request_1_json, "friend_requests")

    def test_get_by_id(self, friend_request_repository, request_1):
        assert friend_request_repository.get_by_id(request_1.uuid) == request_1

    def test_get_by_id_does_not_exist(self, friend_request_repository):
        assert friend_request_repository.get_by_id("75ea57ea-8872-11ed-942c-00155d211f36") is None

    def test_delete(self, friend_request_repository, database, request_1):
        friend_request_repository.delete(request_1)
        database.delete_by_id.assert_called_with(request_1.uuid, "friend_requests")

    def test_get_requests_to_user(self, friend_request_repository, user_3, user_2, user_1, request_1, request_2):
        assert friend_request_repository.get_requests_to_user(user_3) == [request_1]
        assert friend_request_repository.get_requests_to_user(user_2) == [request_2]
        assert friend_request_repository.get_requests_to_user(user_1) == []

    def test_get_requests_from_user(self, friend_request_repository, user_1, user_2, user_3, request_1, request_2):
        assert friend_request_repository.get_requests_from_user(user_1) == [request_1]
        assert friend_request_repository.get_requests_from_user(user_2) == []
        assert friend_request_repository.get_requests_from_user(user_3) == [request_2]


class TestPhotoRepository:

    def test_save(self, photo_repository, database, photo_1, photo_1_json):
        photo_repository.save(photo_1)
        database.save.assert_called_with(photo_1_json, "photos")

    def test_get_by_id(self, photo_repository, photo_1):
        assert photo_repository.get_by_id(photo_1.uuid) == photo_1

    def test_get_by_id_does_not_exist(self, photo_repository):
        assert photo_repository.get_by_id("3857ab2c-8876-11ed-b239-00155d211f36") is None

    def test_delete(self, photo_repository, database, photo_1):
        photo_repository.delete(photo_1)
        database.delete_by_id.assert_called_with(photo_1.uuid, "photos")
