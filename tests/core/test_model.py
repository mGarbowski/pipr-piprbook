from datetime import datetime
from io import BytesIO

from pytest import raises

from core.model import User, Message, FriendRequest, Photo
from core.validation import (
    IncorrectUuidError,
    IncorrectUsernameError,
    IncorrectEmailError,
    IncorrectPasswordHashError,
    IncorrectSaltError,
    IncorrectMessageTextError,
    SelfReferenceError,
    IncorrectFilenameError,
    IncorrectHexRepresentationError,
    UnsupportedFileFormatError
)


class TestUser:

    def test_default_init_values(self):
        user = User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="user 1",
            email="email@example.com",
            password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
            salt="aaaaaaaaaa"
        )

        assert user.friend_uuids == []
        assert user.profile_picture_id is None
        assert user.bio is None

    def test_incorrect_uuid(self):
        with raises(IncorrectUuidError):
            _ = User(
                uuid="invalid",
                username="user 1",
                email="email@example.com",
                password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
                salt="aaaaaaaaaa"
            )

    def test_username_too_short(self):
        with raises(IncorrectUsernameError):
            User(
                uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
                username="abc",
                email="email@example.com",
                password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
                salt="aaaaaaaaaa"
            )

    def test_incorrect_email(self):
        with raises(IncorrectEmailError):
            User(
                uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
                username="user 1",
                email="user@192.168.1.1",
                password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
                salt="aaaaaaaaaa"
            )

    def test_incorrect_password_hash(self):
        with raises(IncorrectPasswordHashError):
            User(
                uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
                username="user 1",
                email="email@example.com",
                password_hash="not a sha256 hash",
                salt="aaaaaaaaaa"
            )

    def test_incorrect_salt(self):
        with raises(IncorrectSaltError):
            User(
                uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
                username="user 1",
                email="email@example.com",
                password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
                salt="wronglen"
            )

    def test_incorrect_friend_uuid(self):
        with raises(IncorrectUuidError):
            User(
                uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
                username="user 1",
                email="email@example.com",
                password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
                salt="aaaaaaaaaa",
                friend_uuids=[
                    "901d01ba-887e-11ed-b239-00155d211f36",
                    "incorrect uuid",
                    "9a2eca6c-887e-11ed-b239-00155d211f36"
                ]
            )

    def test_incorrect_profile_picture_id(self):
        with raises(IncorrectUuidError):
            User(
                uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
                username="user 1",
                email="email@example.com",
                password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
                salt="aaaaaaaaaa",
                profile_picture_id="incorrect uuid"
            )

    def test_is_friends_with(self):
        user_1 = User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="user 1",
            email="email@example.com",
            password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
            salt="aaaaaaaaaa",
            friend_uuids=["9a154c0c-7bba-11ed-9b3d-00155df7f899"]
        )
        user_2 = User(
            uuid="9a154c0c-7bba-11ed-9b3d-00155df7f899",
            username="user 2",
            email="email2@example.com",
            password_hash="b5c90ac7dc4c828717699bc943bfeb54e6f682ca055bfc5591c8a471dfc0d794",
            salt="saltsaltsa",
            friend_uuids=["c1a40f26-7ba9-11ed-9382-00155df7f899"]
        )
        assert user_1.is_friends_with(user_2)
        assert user_2.is_friends_with(user_1)

    def test_is_not_friends_with(self):
        user_1 = User(
            uuid="c1a40f26-7ba9-11ed-9382-00155df7f899",
            username="user 1",
            email="email@example.com",
            password_hash="fb99705459b651e7c37b0da74a53a23fe1920b91a0553eaacd9098a3fe4025cd",
            salt="aaaaaaaaaa"
        )
        user_2 = User(
            uuid="9a154c0c-7bba-11ed-9b3d-00155df7f899",
            username="user 2",
            email="email2@example.com",
            password_hash="b5c90ac7dc4c828717699bc943bfeb54e6f682ca055bfc5591c8a471dfc0d794",
            salt="saltsaltsa"
        )
        assert not user_1.is_friends_with(user_2)
        assert not user_2.is_friends_with(user_1)


class TestMessage:

    def test_init(self):
        message = Message(
            uuid="9b3772a8-8868-11ed-942c-00155d211f36",
            text="Hello",
            timestamp=datetime(2022, 12, 30, 19, 30, 0),
            from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
            to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"
        )

        assert message.uuid == "9b3772a8-8868-11ed-942c-00155d211f36"
        assert message.text == "Hello"
        assert message.timestamp == datetime(2022, 12, 30, 19, 30, 0)
        assert message.from_user_id == "c1a40f26-7ba9-11ed-9382-00155df7f899"
        assert message.to_user_id == "9a154c0c-7bba-11ed-9b3d-00155df7f899"

    def test_incorrect_uuid(self):
        with raises(IncorrectUuidError):
            Message(
                uuid="incorrect",
                text="Hello",
                timestamp=datetime(2022, 12, 30, 19, 30, 0),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"
            )

    def test_empty_text(self):
        with raises(IncorrectMessageTextError):
            Message(
                uuid="9b3772a8-8868-11ed-942c-00155d211f36",
                text="",
                timestamp=datetime(2022, 12, 30, 19, 30, 0),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"
            )

    def test_incorrect_from_user_uuid(self):
        with raises(IncorrectUuidError):
            Message(
                uuid="9b3772a8-8868-11ed-942c-00155d211f36",
                text="Hello",
                timestamp=datetime(2022, 12, 30, 19, 30, 0),
                from_user_id="incorrect",
                to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"
            )

    def test_incorrect_to_user_id(self):
        with raises(IncorrectUuidError):
            Message(
                uuid="9b3772a8-8868-11ed-942c-00155d211f36",
                text="Hello",
                timestamp=datetime(2022, 12, 30, 19, 30, 0),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="incorrect"
            )

    def test_self_reference(self):
        with raises(SelfReferenceError):
            Message(
                uuid="9b3772a8-8868-11ed-942c-00155d211f36",
                text="Hello",
                timestamp=datetime(2022, 12, 30, 19, 30, 0),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899"
            )


class TestFriendRequest:

    def test_incorrect_uuid(self):
        with raises(IncorrectUuidError):
            FriendRequest(
                uuid="incorrect",
                timestamp=datetime(2022, 12, 30, 20, 30),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"
            )

    def test_incorrect_to_user_id(self):
        with raises(IncorrectUuidError):
            FriendRequest(
                uuid="73cf4b5c-8870-11ed-942c-00155d211f36",
                timestamp=datetime(2022, 12, 30, 20, 30),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="incorrect"
            )

    def test_incorrect_from_user_id(self):
        with raises(IncorrectUuidError):
            FriendRequest(
                uuid="73cf4b5c-8870-11ed-942c-00155d211f36",
                timestamp=datetime(2022, 12, 30, 20, 30),
                from_user_id="incorrect",
                to_user_id="9a154c0c-7bba-11ed-9b3d-00155df7f899"
            )

    def test_self_reference(self):
        with raises(SelfReferenceError):
            FriendRequest(
                uuid="73cf4b5c-8870-11ed-942c-00155d211f36",
                timestamp=datetime(2022, 12, 30, 20, 30),
                from_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899",
                to_user_id="c1a40f26-7ba9-11ed-9382-00155df7f899"
            )


class TestPhoto:

    def test_incorrect_uuid(self):
        with raises(IncorrectUuidError):
            Photo(
                uuid="incorrect",
                filename="photo.jpg",
                format="jpg",
                binary_data_hex="1560138213851237906523195361abcbbba"
            )

    def test_incorrect_filename(self):
        with raises(IncorrectFilenameError):
            Photo(
                uuid="d9eaaf36-8874-11ed-942c-00155d211f36",
                filename="no_extension",
                format="jpg",
                binary_data_hex="1560138213851237906523195361abcbbba"
            )

    def test_unsupported_file_format(self):
        with raises(UnsupportedFileFormatError):
            Photo(
                uuid="d9eaaf36-8874-11ed-942c-00155d211f36",
                filename="photo.gif",
                format="gif",
                binary_data_hex="1560138213851237906523195361abcbbba"
            )

    def test_incorrect_hex_representation(self):
        with raises(IncorrectHexRepresentationError):
            Photo(
                uuid="d9eaaf36-8874-11ed-942c-00155d211f36",
                filename="photo.jpg",
                format="jpg",
                binary_data_hex="not hex"
            )

    def test_get_bytes(self):
        photo = Photo(
            uuid="d9eaaf36-8874-11ed-942c-00155d211f36",
            filename="photo.jpg",
            format="jpg",
            binary_data_hex=b"deadbeef01234".hex()
        )
        assert photo.get_bytes() == b"deadbeef01234"

    def test_from_file(self):
        file = BytesIO(b"deadbeef01234")
        file_path = "/home/user/photos/picture.jpg"
        photo = Photo.from_file(file, file_path)

        assert photo.filename == "picture.jpg"
        assert photo.format == "jpg"
        assert photo.get_bytes() == b"deadbeef01234"
