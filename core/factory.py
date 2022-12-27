from typing import TextIO

from core.authentication import Authentication
from core.model import User, Message, FriendRequest
from core.serializers import MessageSerializer, UserSerializer, FriendRequestSerializer
from core.user_service import UserService
from persistence.json_database import JsonDatabase
from persistence.repositories import PhotoRepository, MessageRepository, UserRepository, FriendRequestRepository


def get_user_service_default(db_file: TextIO) -> UserService:
    collection_names = {
        User: "users",
        Message: "messages",
        FriendRequest: "friend_requests"
    }
    database = JsonDatabase(db_file, collection_names)

    user_serializer = UserSerializer()
    message_serializer = MessageSerializer()
    friend_request_serializer = FriendRequestSerializer()

    user_repository = UserRepository(database, user_serializer)
    message_repository = MessageRepository(database, message_serializer)
    friend_request_repository = FriendRequestRepository(database, friend_request_serializer)
    photo_repository = PhotoRepository()

    authentication = Authentication(user_repository)
    user_service = UserService(
        authentication,
        user_repository,
        message_repository,
        friend_request_repository,
        photo_repository
    )

    return user_service
