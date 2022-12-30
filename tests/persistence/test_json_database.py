from io import StringIO

from pytest import fixture, raises

from persistence.json_database import JsonDatabase, InvalidDatabaseFileError, CollectionDoesNotExistError, NoUuidError


@fixture
def empty_database_file():
    return StringIO('{"users": {}, "messages": {}, "friend_requests": {}, "photos": {}}')


@fixture
def default_collection_names():
    return ["users", "messages", "friend_requests", "photos"]


@fixture
def entity_dict():
    return {
        "uuid": "691a3d52-883e-11ed-bff4-00155d211f36",
        "username": "Test_User"
    }


@fixture
def empty_database(empty_database_file, default_collection_names):
    return JsonDatabase(empty_database_file, default_collection_names)


class TestJsonDatabase:

    def test_create_with_existing_data(self, default_collection_names):
        db_file = StringIO("""{
  "users": {
    "c222a07c-8845-11ed-b4fa-00155d211f36": {
      "uuid": "c222a07c-8845-11ed-b4fa-00155d211f36",
      "username": "user1",
      "email": "user1@example.com",
      "password_hash": "f9f20c0f13048727e9199d61bc93b1b52e45f306f3b08a880f50ab3d24f4423d",
      "salt": "NclTLyGryK",
      "friend_uuids": [
        "c9ffd2a6-8845-11ed-b4fa-00155d211f36"
      ],
      "profile_picture_id": null,
      "bio": null
    },
    "c9ffd2a6-8845-11ed-b4fa-00155d211f36": {
      "uuid": "c9ffd2a6-8845-11ed-b4fa-00155d211f36",
      "username": "user2",
      "email": "user@@example.com",
      "password_hash": "6af437b0e56ad428e2cc20562e38ad8a296ab5a0ec4c7d1ac7b6d6e484833363",
      "salt": "YbiJRiZLJZ",
      "friend_uuids": [
        "c222a07c-8845-11ed-b4fa-00155d211f36"
      ],
      "profile_picture_id": null,
      "bio": null
    }
  },
  "messages": {
    "dc0d3ec0-8845-11ed-b4fa-00155d211f36": {
      "uuid": "dc0d3ec0-8845-11ed-b4fa-00155d211f36",
      "text": "Hello!",
      "timestamp": "2022-12-30T14:28:34.433013",
      "from_user_id": "c9ffd2a6-8845-11ed-b4fa-00155d211f36",
      "to_user_id": "c222a07c-8845-11ed-b4fa-00155d211f36"
    }
  },
  "friend_requests": {},
  "photos": {}
}""")
        database = JsonDatabase(db_file, default_collection_names)

        message = database.get_by_id("dc0d3ec0-8845-11ed-b4fa-00155d211f36", "messages")
        assert message["text"] == "Hello!"

        user_1 = database.get_by_id("c222a07c-8845-11ed-b4fa-00155d211f36", "users")
        assert user_1["username"] == "user1"

        assert len(database.get_collection("users")) == 2
        assert len(database.get_collection("photos")) == 0

    def test_create_db_file_not_a_json(self, default_collection_names):
        file = StringIO("<h1>not a json file</h1>")
        with raises(InvalidDatabaseFileError):
            JsonDatabase(file, default_collection_names)

    def test_create_db_file_missing_collections(self, default_collection_names):
        file = StringIO('{"users": {}, "messages": {}, "friend_requests": {}}')
        with raises(InvalidDatabaseFileError):
            JsonDatabase(file, default_collection_names)

    def test_get_entity_does_not_exist(self, empty_database):
        assert empty_database.get_by_id("id1", "users") is None

    def test_get_entity_collection_does_not_exist(self, empty_database):
        with raises(CollectionDoesNotExistError):
            empty_database.get_by_id("id1", "payments")

    def test_save_and_get_by_id(self, empty_database, entity_dict):
        empty_database.save(entity_dict, "users")
        entity_fict_from_db = empty_database.get_by_id(entity_dict["uuid"], "users")
        assert entity_fict_from_db == entity_dict

    def test_save_entity_no_uuid(self, empty_database):
        entity_dict = {"username": "my_username"}
        with raises(NoUuidError):
            empty_database.save(entity_dict, "users")

    def test_save_overwrite_existing_entity(self, empty_database, entity_dict):
        new_entity_dict = {
            "uuid": entity_dict["uuid"],
            "username": "new_username"
        }
        empty_database.save(entity_dict, "users")
        empty_database.save(new_entity_dict, "users")
        assert empty_database.get_by_id(entity_dict["uuid"], "users") == new_entity_dict

    def test_save_entity_collection_does_not_exist(self, empty_database, entity_dict):
        with raises(CollectionDoesNotExistError):
            empty_database.save(entity_dict, "payments")

    def test_delete_entity(self, empty_database, entity_dict):
        empty_database.save(entity_dict, "users")
        assert empty_database.get_by_id(entity_dict["uuid"], "users") is not None
        empty_database.delete_by_id(entity_dict["uuid"], "users")
        assert empty_database.get_by_id(entity_dict["uuid"], "users") is None

    def test_delete_entity_does_not_exits_no_error(self, empty_database):
        empty_database.delete_by_id("does_not_exist", "users")

    def test_delete_entity_collection_does_not_exist(self, empty_database):
        with raises(CollectionDoesNotExistError):
            empty_database.delete_by_id("id", "payments")

    def test_get_empty_collection(self, empty_database):
        assert empty_database.get_collection("messages") == []

    def test_get_collection_does_not_exist(self, empty_database):
        with raises(CollectionDoesNotExistError):
            empty_database.get_collection("payments")

    def test_save_and_get_collection(self, empty_database):
        entity_1 = {
            "uuid": '3621917a-8843-11ed-bff4-00155d211f36',
            "username": "entity_1"
        }
        entity_2 = {
            "uuid": '4324de9a-8843-11ed-bff4-00155d211f36',
            "username": "entity_2"
        }
        entity_3 = {
            "uuid": '47d4c6da-8843-11ed-bff4-00155d211f36',
            "username": "entity_3"
        }
        collection = [entity_1, entity_2, entity_3]

        empty_database.save_collection(collection, "users")
        collection_from_db = empty_database.get_collection("users")
        assert len(collection) == 3
        assert entity_1 in collection_from_db
        assert entity_2 in collection_from_db
        assert entity_3 in collection_from_db

        assert empty_database.get_by_id(entity_1["uuid"], "users") == entity_1
        assert empty_database.get_by_id(entity_2["uuid"], "users") == entity_2
        assert empty_database.get_by_id(entity_3["uuid"], "users") == entity_3

    def test_save_collection_does_not_exist(self, empty_database):
        collection = [{
            "uuid": '3621917a-8843-11ed-bff4-00155d211f36',
            "amount": 199
        }]
        with raises(CollectionDoesNotExistError):
            empty_database.save_collection(collection, "payments")

    def test_save_collection_no_uuid(self, empty_database):
        collection = [
            {"username": "entity_1"},
            {"uuid": "3621917a-8843-11ed-bff4-00155d211f36", "username": "entity_2"}
        ]
        with raises(NoUuidError):
            empty_database.save_collection(collection, "users")

    def test_save_empty_collection(self, empty_database):
        collection = [
            {
                "uuid": '3621917a-8843-11ed-bff4-00155d211f36',
                "username": "entity_1"
            },
            {
                "uuid": '4324de9a-8843-11ed-bff4-00155d211f36',
                "username": "entity_2"
            }
        ]
        empty_database.save_collection(collection, "users")
        assert empty_database.get_collection("users") == collection

        empty_database.save_collection([], "users")
        assert empty_database.get_collection("users") == []
