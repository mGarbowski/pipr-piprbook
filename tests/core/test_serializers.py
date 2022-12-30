from datetime import datetime

from pytest import raises

from core.model import User, Message, FriendRequest, Photo
from core.serializers import UserSerializer, RepresentationError, MessageSerializer, FriendRequestSerializer, \
    PhotoSerializer


class TestUserSerializer:
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

        serializer = UserSerializer()
        user_json = serializer.to_json(user)
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

        serializer = UserSerializer()
        user_json = serializer.to_json(user)
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

        serializer = UserSerializer()
        parsed_user = serializer.from_json(user_json)
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
        serializer = UserSerializer()
        parsed_user = serializer.from_json(user_json)
        assert parsed_user == User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="username",
            email="email@example.com",
            password_hash="DD130A849D7B29E5541B05D2F7F86A4ACD4F1EC598C1C9438783F56BC4F0FF80",
            salt="abc"
        )

    def test_invalid_representation(self):
        serializer = UserSerializer()
        with raises(RepresentationError):
            serializer.from_json({
                "asdfasf": 12312313,
                "adfhaslf": "adfnkaslf",
                "sagnfamf": []
            })


class TestMessageSerializer:

    def test_to_json(self):
        message = Message(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            text="Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )
        serializer = MessageSerializer()
        message_json = serializer.to_json(message)
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
        serializer = MessageSerializer()
        parsed_message = serializer.from_json(message_json)
        assert parsed_message == Message(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            text="Est deserunt commodi totam adipisci beatae. Enim ut impedit aut.",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )

    def test_invalid_representation(self):
        serializer = MessageSerializer()
        with raises(RepresentationError):
            serializer.from_json({
                "asdfasf": 12312313,
                "adfhaslf": "adfnkaslf",
                "sagnfamf": []
            })


class TestFriendRequestSerializer:

    def test_to_json(self):
        request = FriendRequest(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )
        serializer = FriendRequestSerializer()
        request_json = serializer.to_json(request)
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
        serializer = FriendRequestSerializer()
        parsed_request = serializer.from_json(request_json)
        assert parsed_request == FriendRequest(
            uuid="926b72f0-7bac-11ed-92f8-00155df7f899",
            timestamp=datetime(2022, 12, 14, 13, 41, 37),
            from_user_id="e5539894-7bac-11ed-92f8-00155df7f899",
            to_user_id="f308c144-7bac-11ed-92f8-00155df7f899"
        )

    def test_invalid_representation(self):
        serializer = FriendRequestSerializer()
        with raises(RepresentationError):
            serializer.from_json({
                "asdfasf": 12312313,
                "adfhaslf": "adfnkaslf",
                "sagnfamf": []
            })


class TestPhotoSerializer:

    def test_to_json(self):
        photo = Photo(
            uuid="2c23e9ae-8850-11ed-942c-00155d211f36",
            filename="picture.jpg",
            format="jpg",
            binary_data_hex="deadbeef0123456789"
        )
        serializer = PhotoSerializer()
        photo_json = serializer.to_json(photo)
        assert photo_json == {
            "uuid": "2c23e9ae-8850-11ed-942c-00155d211f36",
            "filename": "picture.jpg",
            "format": "jpg",
            "binary_data_hex": "deadbeef0123456789"
        }

    def test_from_json(self):
        photo_json = {
            "uuid": "2c23e9ae-8850-11ed-942c-00155d211f36",
            "filename": "picture.jpg",
            "format": "jpg",
            "binary_data_hex": "deadbeef0123456789"
        }
        serializer = PhotoSerializer()
        photo = serializer.from_json(photo_json)
        assert photo == Photo(
            uuid="2c23e9ae-8850-11ed-942c-00155d211f36",
            filename="picture.jpg",
            format="jpg",
            binary_data_hex="deadbeef0123456789"
        )

    def test_invalid_representation(self):
        with raises(RepresentationError):
            PhotoSerializer.from_json({
                "asdfasf": "ASfdsaf",
                "ds;hfnlds": []
            })

