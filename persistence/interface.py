from typing import Protocol, TypeVar, Optional, Dict, List

T = TypeVar("T")


class Database(Protocol):
    def save(self, entity_dict: Dict, collection_name: str):
        ...

    def get_by_id(self, entity_id: str, collection_name: str) -> Optional[Dict]:
        ...

    def delete_by_id(self, entity_id: str, collection_name: str):
        ...

    def save_collection(self, collection: List[dict], collection_name: str):
        ...

    def get_collection(self, collection_name: str) -> List[dict]:
        ...


class JsonSerializer(Protocol[T]):

    @staticmethod
    def to_json(entity) -> Dict:
        ...

    @staticmethod
    def from_json(json_dict: Dict) -> T:
        ...
