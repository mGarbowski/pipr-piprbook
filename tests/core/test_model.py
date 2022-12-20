from datetime import datetime

from _pytest.python_api import raises

from core.model import User, Message, FriendRequest, RepresentationError


class TestUserSerialization:

    def test_to_json_all_fields(self):
        user = User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="username",
            email="email@example.com",
            password_hash="DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            salt="abc",
            friend_uuids=[
                "47ea7d2c-7baa-11ed-9382-00155df7f899",
                "4d2845c6-7baa-11ed-9382-00155df7f899",
                "52a4f634-7baa-11ed-9382-00155df7f899"
            ],
            profile_picture_id="657bf91a-7baa-11ed-9382-00155df7f899",
            bio="This is my bio"
        )

        user_json = user.to_json()
        assert user_json == {
            "uuid": "c1a40f26-7ba9-11ed-9382-00155df7f899",
            "username": "username",
            "email": "email@example.com",
            "password_hash": "DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            "salt": "abc",
            "friend_uuids": [
                "47ea7d2c-7baa-11ed-9382-00155df7f899",
                "4d2845c6-7baa-11ed-9382-00155df7f899",
                "52a4f634-7baa-11ed-9382-00155df7f899"
            ],
            "profile_picture_id": "657bf91a-7baa-11ed-9382-00155df7f899",
            "bio": "This is my bio"
        }

    def test_to_json_default_fields(self):
        user = User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="username",
            email="email@example.com",
            password_hash="DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            salt="abc"
        )

        user_json = user.to_json()
        assert user_json == {
            "uuid": "c1a40f26-7ba9-11ed-9382-00155df7f899",
            "username": "username",
            "email": "email@example.com",
            "password_hash": "DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            "salt": "abc",
            "friend_uuids": [],
            "profile_picture_id": None,
            "bio": None
        }

    def test_from_json_all_fields(self):
        user_json = {
            "uuid": "c1a40f26-7ba9-11ed-9382-00155df7f899",
            "username": "username",
            "email": "email@example.com",
            "password_hash": "DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            "salt": "abc",
            "friend_uuids": [
                "47ea7d2c-7baa-11ed-9382-00155df7f899",
                "4d2845c6-7baa-11ed-9382-00155df7f899",
                "52a4f634-7baa-11ed-9382-00155df7f899"
            ],
            "profile_picture_id": "657bf91a-7baa-11ed-9382-00155df7f899",
            "bio": "This is my bio"
        }

        parsed_user = User.from_json(user_json)
        assert parsed_user == User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="username",
            email="email@example.com",
            password_hash="DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            salt="abc",
            friend_uuids=[
                "47ea7d2c-7baa-11ed-9382-00155df7f899",
                "4d2845c6-7baa-11ed-9382-00155df7f899",
                "52a4f634-7baa-11ed-9382-00155df7f899"
            ],
            profile_picture_id="657bf91a-7baa-11ed-9382-00155df7f899",
            bio="This is my bio"
        )

    def test_from_json_default_fields(self):
        user_json = {
            "uuid": "c1a40f26-7ba9-11ed-9382-00155df7f899",
            "username": "username",
            "email": "email@example.com",
            "password_hash": "DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            "salt": "abc",
            "friend_uuids": [],
            "profile_picture_id": None,
            "bio": None
        }
        parsed_user = User.from_json(user_json)
        assert parsed_user == User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="username",
            email="email@example.com",
            password_hash="DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            salt="abc"
        )

    def test_invalid_representation(self):
        with raises(RepresentationError):
            User.from_json({
                "asdfasf": 12312313,
                "adfhaslf": "adfnkaslf",
                "sagnfamf": []
            })


class TestMessageSerialization:

    def test_to_json(self):
        message = Message(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            text="Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )
        message_json = message.to_json()
        assert message_json == {
            "uuid": "926b72f0-7bac-11ed-92f8-00155df7f899",
            "text": "Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
            "timestamp": "2022-12-14T13:41:37",
            "from_user_id": "e5539894-7bac-11ed-92f8-00155df7f899",
            "to_user_id": "f308c144-7bac-11ed-92f8-00155df7f899"
        }

    def test_from_json(self):
        message_json = {
            "uuid": "926b72f0-7bac-11ed-92f8-00155df7f899",
            "text": "Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
            "timestamp": "2022-12-14T13:41:37",
            "from_user_id": "e5539894-7bac-11ed-92f8-00155df7f899",
            "to_user_id": "f308c144-7bac-11ed-92f8-00155df7f899"
        }
        parsed_message = Message.from_json(message_json)
        assert parsed_message == Message(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            text="Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )

    def test_invalid_representation(self):
        with raises(RepresentationError):
            Message.from_json({
                "asdfasf": 12312313,
                "adfhaslf": "adfnkaslf",
                "sagnfamf": []
            })


class TestFriendRequestSerialization:

    def test_to_json(self):
        request = FriendRequest(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )
        request_json = request.to_json()
        assert request_json == {
            "uuid": "926b72f0-7bac-11ed-92f8-00155df7f899",
            "timestamp": "2022-12-14T13:41:37",
            "from_user_id": "e5539894-7bac-11ed-92f8-00155df7f899",
            "to_user_id": "f308c144-7bac-11ed-92f8-00155df7f899"
        }

    def test_from_json(self):
        request_json = {
            "uuid": "926b72f0-7bac-11ed-92f8-00155df7f899",
            "timestamp": "2022-12-14T13:41:37",
            "from_user_id": "e5539894-7bac-11ed-92f8-00155df7f899",
            "to_user_id": "f308c144-7bac-11ed-92f8-00155df7f899"
        }
        parsed_request = FriendRequest.from_json(request_json)
        assert parsed_request == FriendRequest(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )

    def test_invalid_representation(self):
        with raises(RepresentationError):
            FriendRequest.from_json({
                "asdfasf": 12312313,
                "adfhaslf": "adfnkaslf",
                "sagnfamf": []
            })
