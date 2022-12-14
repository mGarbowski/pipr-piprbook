from typing import Protocol, TypeVar

T = TypeVar("T")


class JsonSerializer(Protocol[T]):

    def to_json(self, entity: T) -> dict:
        ...

    def from_json(self, json: dict) -> T:
        ...


class UserJsonSerializer:
    pass


class MessageJsonSerializer:
    pass


class FriendRequestJsonSerializer:
    pass
