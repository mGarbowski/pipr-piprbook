from io import StringIO

from core.factory import get_user_service_default


class TestDefaultUserServiceFactory:

    def test_create_with_empty_database(self):
        database_file = StringIO('{"users": {}, "messages": {}, "friend_requests": {}, "photos": {}}')
        user_service = get_user_service_default(database_file)

        assert user_service.get_current_user() is None
        assert user_service.get_user_by_id("1904713e-885c-11ed-942c-00155d211f36") is None

    def test_create_with_initial_data(self):
        database_file = StringIO("""{
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
      "email": "user2@example.com",
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
        user_service = get_user_service_default(database_file)
        user_1 = user_service.get_user_by_id("c222a07c-8845-11ed-b4fa-00155d211f36")
        user_2 = user_service.get_user_by_id("c9ffd2a6-8845-11ed-b4fa-00155d211f36")
        assert user_1.is_friends_with(user_2)
        assert user_1.username == "user1"
        assert user_2.email == "user2@example.com"

        user_service.log_in_user("user1", "user1")
        messages = user_service.get_messages(user_1, user_2)
        assert len(messages) == 1
        assert messages[0].text == "Hello!"
