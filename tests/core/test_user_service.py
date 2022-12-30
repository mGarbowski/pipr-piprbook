from copy import deepcopy
from datetime import datetime
from unittest.mock import MagicMock

from pytest import fixture, raises

from core.authentication import LoginFailedError, UnauthorizedError
from core.user_service import UserService, UsernameTakenException, EmailAlreadyUsedException
from model import FriendRequest


@fixture
def authentication(user_1):
    def log_in(username, password):
        if username == user_1.username and password == "password":
            auth.logged_in_user = user_1
        else:
            raise LoginFailedError()

    auth = MagicMock()
    auth.logged_in_user = None
    auth.log_in = log_in
    return auth


@fixture
def user_repository(user_1, user_2, user_3):
    def get_by_id(user_id):
        if user_id == user_1.uuid:
            return user_1
        elif user_id == user_2.uuid:
            return user_2
        elif user_id == user_3.uuid:
            return user_3
        else:
            return None

    def get_by_username(username):
        if username == user_1.username:
            return user_1
        else:
            return None

    def get_by_email(email):
        if email == user_1.email:
            return email
        else:
            return None

    repository = MagicMock()
    repository.get_by_id = get_by_id
    repository.get_by_username = get_by_username
    repository.get_by_email = get_by_email
    return repository


@fixture
def message_repository():
    repository = MagicMock()
    return repository


@fixture
def friend_request_repository():
    repository = MagicMock()
    return repository


@fixture
def photo_repository(photo_1):
    def get_by_id(photo_id):
        if photo_id == photo_1.uuid:
            return photo_1
        else:
            return None

    repository = MagicMock()
    repository.get_by_id = get_by_id
    return repository


@fixture
def user_service(authentication, user_repository, message_repository,
                 friend_request_repository, photo_repository):
    return UserService(authentication, user_repository, message_repository,
                       friend_request_repository, photo_repository)


class TestUserService:

    def test_log_in_success(self, user_service, user_1):
        success = user_service.log_in_user(user_1.username, "password")
        assert success
        assert user_service.get_current_user() == user_1

    def test_log_in_failed(self, user_service, user_1):
        success = user_service.log_in_user(user_1.username, "wrongpassword")
        assert not success
        assert user_service.get_current_user() is None

    def test_log_out(self, user_service, authentication, user_1):
        user_service.log_in_user(user_1.username, "password")
        user_service.log_out_user()
        authentication.log_out.assert_called_once()

    def test_get_user_by_id(self, user_service, user_repository, user_1):
        assert user_service.get_user_by_id(user_1.uuid) == user_1

    def test_get_users_by_username_fragment(self, user_service, user_repository):
        user_service.get_users_by_username_fragment("fragment")
        user_repository.get_by_username_fragment.assert_called_once_with("fragment")

    def test_register_new_user(self, user_service, user_repository):
        user_service.register_new_user("user2", "user2@example.com", "user2")
        user_repository.save.assert_called_once()

    def test_register_new_user_username_taken(self, user_service, user_1):
        with raises(UsernameTakenException):
            user_service.register_new_user(user_1.username, "new@example.com", "newpassword")

    def test_register_new_user_email_taken(self, user_service, user_1):
        with raises(EmailAlreadyUsedException):
            user_service.register_new_user("new username", user_1.email, "newpassword")

    def test_set_bio(self, user_service, user_repository, user_1):
        user_service.log_in_user(user_1.username, "password")
        user_service.set_bio(user_1, "Hello world")
        expected = user_1
        expected.bio = "Hello world"
        user_repository.save.assert_called_once_with(expected)

    def test_set_bio_unauthorized(self, user_service, user_1):
        with raises(UnauthorizedError):
            user_service.set_bio(user_1, "Hello world")

    def test_get_profile_picture(self, user_service, user_1, photo_1):
        user_1.profile_picture_id = photo_1.uuid
        photo = user_service.get_profile_picture(user_1)
        assert photo == photo_1

    def test_add_profile_picture(self, user_service, user_repository, photo_repository, user_1, photo_1):
        expected = user_1
        expected.profile_picture_id = photo_1.uuid

        user_service.add_profile_picture(user_1, photo_1)
        user_repository.save.assert_called_once_with(expected)
        photo_repository.save.assert_called_once_with(photo_1)

    def test_delete_photo(self, user_service, photo_repository, photo_1):
        user_service.delete_picture(photo_1)
        photo_repository.delete.assert_called_once_with(photo_1)

    def test_get_friends(self, user_service, user_1, user_2, user_3):
        user_1.friend_uuids = [user_2.uuid, user_3.uuid]
        friends = user_service.get_friends(user_1)
        assert user_2 in friends
        assert user_3 in friends

    def test_send_message(self, user_service, message_repository, user_1, user_2):
        user_service.log_in_user(user_1.username, "password")
        user_service.send_message(user_1, user_2, "Hello")
        message_repository.save.assert_called_once()

    def test_send_message_unauthorized(self, user_service, user_1, user_2):
        with raises(UnauthorizedError):
            user_service.send_message(user_1, user_2, "Hello")

    def test_get_friend_requests_from(self, user_service, friend_request_repository, user_1):
        user_service.log_in_user(user_1.username, "password")
        user_service.get_friend_requests_from(user_1)
        friend_request_repository.get_requests_from_user.assert_called_once_with(user_1)

    def test_get_friend_requests_from_unauthorized(self, user_service, user_1):
        with raises(UnauthorizedError):
            user_service.get_friend_requests_from(user_1)

    def test_get_friend_requests_to(self, user_service, friend_request_repository, user_1):
        user_service.log_in_user(user_1.username, "password")
        user_service.get_friend_requests_to(user_1)
        friend_request_repository.get_requests_to_user.assert_called_once_with(user_1)

    def test_get_friend_requests_to_unauthorized(self, user_service, user_1):
        with raises(UnauthorizedError):
            user_service.get_friend_requests_to(user_1)

    def test_send_friend_request(self, user_service, friend_request_repository, user_1, user_2):
        user_service.log_in_user(user_1.username, "password")
        user_service.send_friend_request(user_1, user_2)
        friend_request_repository.save.assert_called_once()

    def test_send_friend_request_unauthorized(self, user_service, user_1, user_2):
        with raises(UnauthorizedError):
            user_service.send_friend_request(user_1, user_2)

    def test_accept_friend_request(self, user_service, user_repository, friend_request_repository, user_1, user_2):
        request = FriendRequest("22854a44-8893-11ed-b239-00155d211f36",
                                datetime.now(), user_2.uuid, user_1.uuid)
        user_1_expected = deepcopy(user_1)
        user_1_expected.friend_uuids = [user_2.uuid]
        user_2_expected = deepcopy(user_2)
        user_2_expected.friend_uuids = [user_1.uuid]
        user_service.log_in_user(user_1.username, "password")

        user_service.accept_friend_request(request)

        user_repository.save.assert_any_call(user_1_expected)
        user_repository.save.assert_any_call(user_2_expected)
        friend_request_repository.delete.assert_called_once_with(request)

    def test_delete_friend_request(self, user_service, request_1, friend_request_repository):
        user_service.delete_friend_request(request_1)
        friend_request_repository.delete.assert_called_once_with(request_1)

    def test_get_messages(self, user_service, message_repository, user_1, user_2):
        user_service.log_in_user(user_1.username, "password")
        user_service.get_messages(user_1, user_2)
        message_repository.get_messages.assert_called_once_with(user_1, user_2)

    def test_get_messages_unauthorized(self, user_service, user_1, user_2):
        with raises(UnauthorizedError):
            user_service.get_messages(user_1, user_2)
