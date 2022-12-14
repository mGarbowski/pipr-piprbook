from core.authentication import Authentication
from persistence.repository import FriendRequestRepository, MessageRepository, PhotoRepository, UserRepository


class UserService:
    authentication: Authentication
    user_repository: UserRepository
    message_repository: MessageRepository
    friend_request_repository: FriendRequestRepository
    photo_repository: PhotoRepository
