"""Protocol classes (interfaces) used by the persistence layer."""

from typing import Protocol, TypeVar, Optional, Dict, List

from core.model import Entity

T = TypeVar("T", bound=Entity, covariant=True)


class Database(Protocol):
    """Interface for a database storing collections of entity dictionaries."""

    def save(self, entity_dict: Dict, collection_name: str):
        """Create new entity or update existing."""
        ...

    def get_by_id(
            self, entity_id: str, collection_name: str
    ) -> Optional[Dict]:
        """Get entity dictionary by id or None if it does not exist."""
        ...

    def delete_by_id(self, entity_id: str, collection_name: str):
        """Delete entity by its id or do nothing if it does not exist."""
        ...

    def save_collection(self, collection: List[Dict], collection_name: str):
        """Save a collection of entity dictionaries, overwrite all existing."""
        ...

    def get_collection(self, collection_name: str) -> List[Dict]:
        """Get collection of entity dictionaries by name."""
        ...


class JsonSerializer(Protocol[T]):
    """Generic interface for JSON serializer of model classes."""

    @staticmethod
    def to_json(entity) -> Dict:
        """Serialize entity to its JSON-like dictionary representation."""
        ...

    @staticmethod
    def from_json(json_dict: Dict) -> T:
        """Deserialize entity from its JSON-like dictionary representation."""
        ...
