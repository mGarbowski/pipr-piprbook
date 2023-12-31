"""Utilities for creating class instances with their dependencies."""

from typing import TextIO

from core.authentication import Authentication
from core.model import User, Message, FriendRequest, Photo
from core.serializers import (
    MessageSerializer, UserSerializer, FriendRequestSerializer, PhotoSerializer
)
from core.user_service import UserService
from persistence.json_database import JsonDatabase
from persistence.repositories import (
    PhotoRepository, MessageRepository,
    UserRepository, FriendRequestRepository
)


def get_user_service_default(database_file: TextIO) -> UserService:
    """Create UserService connected to database in given file.

    Creating all dependencies, sharing class instances.
    Expecting default collections - users, messages, friend_requests, photos

    :param database_file: file storing the database used
        by UserService and its dependencies
    """
    collection_name_map = {
        User: "users",
        Message: "messages",
        FriendRequest: "friend_requests",
        Photo: "photos"
    }
    collection_names = list(collection_name_map.values())
    database = JsonDatabase(database_file, collection_names)

    user_serializer = UserSerializer()
    message_serializer = MessageSerializer()
    friend_request_serializer = FriendRequestSerializer()
    photo_serializer = PhotoSerializer()

    user_repository = UserRepository(
        database, user_serializer, collection_name_map[User]
    )
    message_repository = MessageRepository(
        database, message_serializer, collection_name_map[Message]
    )
    friend_request_repository = FriendRequestRepository(
        database, friend_request_serializer, collection_name_map[FriendRequest]
    )
    photo_repository = PhotoRepository(
        database, photo_serializer, collection_name_map[Photo]
    )

    authentication = Authentication(user_repository)
    user_service = UserService(
        authentication,
        user_repository,
        message_repository,
        friend_request_repository,
        photo_repository
    )

    return user_service
