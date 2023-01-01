"""Fixtures shared between test suites"""

from datetime import datetime

from pytest import fixture

from core.model import User, Message, FriendRequest, Photo


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
def message_1(user_1, user_2):
    return Message(
        uuid="9b3772a8-8868-11ed-942c-00155d211f36",
        text="Hello",
        timestamp=datetime(2022, 12, 30, 19, 30, 0),
        from_user_id=user_1.uuid,
        to_user_id=user_2.uuid
    )


@fixture
def message_1_json():
    return {
        'uuid': '9b3772a8-8868-11ed-942c-00155d211f36',
        'text': 'Hello',
        'timestamp': '2022-12-30T19:30:00',
        'from_user_id': 'c1a40f26-7ba9-11ed-9382-00155df7f899',
        'to_user_id': '9a154c0c-7bba-11ed-9b3d-00155df7f899'
    }


@fixture
def message_2(user_1, user_2):
    return Message(
        uuid="48fc2fb4-8869-11ed-942c-00155d211f36",
        text="Hello again",
        timestamp=datetime(2022, 12, 30, 19, 45, 0),
        from_user_id=user_2.uuid,
        to_user_id=user_1.uuid
    )


@fixture
def message_2_json():
    return {
        'uuid': '48fc2fb4-8869-11ed-942c-00155d211f36',
        'text': 'Hello again',
        'timestamp': '2022-12-30T19:45:00',
        'from_user_id': '9a154c0c-7bba-11ed-9b3d-00155df7f899',
        'to_user_id': 'c1a40f26-7ba9-11ed-9382-00155df7f899'
    }


@fixture
def request_1(user_1, user_3):
    return FriendRequest(
        uuid="73cf4b5c-8870-11ed-942c-00155d211f36",
        timestamp=datetime(2022, 12, 30, 20, 30),
        from_user_id=user_1.uuid,
        to_user_id=user_3.uuid
    )


@fixture
def request_1_json():
    return {
        'uuid': '73cf4b5c-8870-11ed-942c-00155d211f36',
        'timestamp': '2022-12-30T20:30:00',
        'from_user_id': 'c1a40f26-7ba9-11ed-9382-00155df7f899',
        'to_user_id': 'fcffaa38-8862-11ed-942c-00155d211f36'
    }


@fixture
def request_2(user_2, user_3):
    return FriendRequest(
        uuid="143e8dd2-8871-11ed-942c-00155d211f36",
        timestamp=datetime(2022, 12, 30, 20, 30),
        from_user_id=user_3.uuid,
        to_user_id=user_2.uuid
    )


@fixture
def request_2_json():
    return {
        'uuid': '143e8dd2-8871-11ed-942c-00155d211f36',
        'timestamp': '2022-12-30T20:30:00',
        'from_user_id': 'fcffaa38-8862-11ed-942c-00155d211f36',
        'to_user_id': '9a154c0c-7bba-11ed-9b3d-00155df7f899'
    }


@fixture
def photo_1():
    return Photo(
        uuid="d9eaaf36-8874-11ed-942c-00155d211f36",
        filename="photo.jpg",
        format="jpg",
        binary_data_hex="1560138213851237906523195361abcbbba"
    )


@fixture
def photo_2():
    return Photo(
        uuid="8af8fc5e-8a02-11ed-8f81-00155d211d29",
        filename="picture.png",
        format="png",
        binary_data_hex="1759805982659826165"
    )


@fixture
def photo_1_json():
    return {
        'uuid': 'd9eaaf36-8874-11ed-942c-00155d211f36',
        'filename': 'photo.jpg',
        'format': 'jpg',
        'binary_data_hex': '1560138213851237906523195361abcbbba'
    }
