from typing import Protocol, TypeVar, Optional

T = TypeVar("T")


class Database(Protocol):
    def save(self, entity_dict: dict, collection_name: str):
        ...

    def get_by_id(self, entity_id: str, collection_name: str) -> Optional[dict]:
        ...

    def delete_by_id(self, entity_id: str, collection_name: str):
        ...

    def save_collection(self, collection: list[dict], collection_name: str):
        ...

    def get_collection(self, collection_name: str) -> list[dict]:
        ...


class JsonSerializer(Protocol[T]):

    @staticmethod
    def to_json(entity) -> dict:
        ...

    @staticmethod
    def from_json(json_dict: dict) -> T:
        ...
