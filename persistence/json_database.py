import json
from typing import TextIO, TypeVar, Optional

from core.model import User, Message, FriendRequest, Entity

T = TypeVar("T")
Collection = dict[str, T]

COLLECTION_NAMES: dict[type, str] = {
    User: "users",
    Message: "messages",
    FriendRequest: "friend_requests",
}


def infer_collection_type(collection: Collection) -> type:
    items = list(collection.values())
    first_item = items[0]
    return type(first_item)


class JsonDatabase:
    def __init__(self, db_file: TextIO, collection_name_mapping: dict[type, str]):
        JsonDatabase._verify_file(db_file, collection_name_mapping)
        self.__db_file = db_file
        self.__collection_name_mapping = collection_name_mapping

    def get_item(self, item_id: str, item_type: type) -> Optional[Entity]:
        collection = self.get_collection(item_type)
        return collection.get(item_id, None)

    def save_item(self, item: Entity) -> Entity:
        item_type = type(item)
        collection = self.get_collection(item_type)
        collection[item.uuid] = item
        return item

    def get_collection(self, collection_type: type) -> Collection:
        collections = self._load_collections()
        name = self.collection_name(collection_type)
        return collections[name]

    def save_collection(self, collection: Collection, collection_type: Optional[type] = None) -> None:
        if not collection and collection_type is None:
            raise ValueError("If collection is empty, type must be specified")

        if collection and collection_type is not None:
            raise ValueError("Collection type can only be specified for empty collections")

        collections = self._load_collections()
        collection_type = infer_collection_type(collection) if collection else collection_type
        name = self.collection_name(collection_type)
        collections[name] = collection
        self._save_collections(collections)

    def collection_name(self, collection_type: type) -> str:
        return self.__collection_name_mapping[collection_type]

    def _load_collections(self) -> dict[str, Collection]:
        return json.load(self.__db_file)

    def _save_collections(self, collections: dict[str, Collection]) -> None:
        json.dump(collections, self.__db_file)

    @staticmethod
    def _verify_file(db_file: TextIO, collection_name_mapping: dict[type, str]) -> None:
        """Verify that given file valid for given mapping of collection names

        :param db_file: file storing the database
        :param collection_name_mapping: dictionary mapping model classes
            to names of their corresponding collections in the database file
        """
        pass


class FilesystemUserRepository:
    pass


class FilesystemMessageRepository:
    pass


class FilesystemFriendRequestRepository:
    pass
