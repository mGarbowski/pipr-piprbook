import json
from typing import TextIO, Optional, TypeVar, Protocol


class Entity(Protocol):
    uuid: str


T = TypeVar("T", bound=Entity)


class JsonSerializer(Protocol):

    @staticmethod
    def to_json(entity) -> dict:
        ...

    @staticmethod
    def from_json(json_dict: dict) -> Entity:
        ...


Collection = dict[str, T]
SerializedCollection = dict[str, dict]
SerializerMapping = dict[type[T], JsonSerializer]


class JsonDatabase:
    """Database in a JSON file storing generic collections

    Collection is a dictionary mapping string uuids to entities.
    Entity is an instance of a model class
        persisted in the database
        implementing JsonSerializable(Entity) interface

    File storing the database is assigned in the constructor.
    Public save methods modify this file in a safe way

    Model classes have names assigned to their corresponding collections in the database,
    mapping is passed as a contructor parameter
    """

    def __init__(self, db_file: TextIO, collection_name_mapping: dict[type, str], serializers: SerializerMapping):
        """Create a new database instance persisting data in the given file

        :param db_file: file to persist data in
        :param collection_name_mapping: dictionary mapping model classes to collection names in the database
        """
        JsonDatabase._verify_file(db_file, collection_name_mapping)
        self.__db_file = db_file
        self.__collection_name_mapping = collection_name_mapping
        self.__serializers = serializers

    def get_item(self, item_id: str, item_type: type[T]) -> Optional[T]:
        """Get an entity by its id or None if not found

        :param item_id: id of entity
        :param item_type: type of searched entity
        """
        collection = self._get_serialized_collection(item_type)
        if item_id not in collection:
            return None

        item_json = collection[item_id]
        serializer = self.__serializers[item_type]
        return serializer.from_json(item_json)

    def save_item(self, item: T) -> None:
        """Save an entity to the database, overwriting previous value if it existed"""
        collection_type = type(item)
        serializer = self.__serializers[collection_type]
        collection_name = self._collection_name(collection_type)
        collection = self._get_serialized_collection(collection_type)
        collection[item.uuid] = serializer.to_json(item)
        self._save_serialized_collection(collection, collection_name)

    def delete_item(self, item: T) -> None:
        """Delete given entity from the database

        If entity is not saved in the database - do nothing
        """
        item_type = type(item)
        self.delete_item_by_id(item.uuid, item_type)

    def delete_item_by_id(self, item_id: str, item_type: type[T]) -> None:
        """Delete an existing entity from the database by its id

        If entity is not saved in the database - do nothing
        """
        collection = self._get_serialized_collection(item_type)
        try:
            collection.pop(item_id)
            collection_name = self._collection_name(item_type)
            self._save_serialized_collection(collection, collection_name)
        except KeyError:
            pass

    def get_collection(self, collection_type: type[T]) -> Collection:
        """Get collection of entities by their type"""
        serialized_collection = self._get_serialized_collection(collection_type)
        return self._deserialize_collection(serialized_collection, collection_type)

    def save_collection(self, collection: Collection, collection_type: Optional[type[T]] = None) -> None:
        """Save a collection to the database, overwriting all existing items

        :param collection: collection of entities to save in the database
        :param collection_type: type of the collection in case it is empty
            by default type is inferred
            only specify type explicitly when saving an empty collection
        :raises ValueError: if at the same time collection is empty and type is not specified
            or the collection is not empty and type is specified
        """
        if not collection and collection_type is None:
            raise ValueError("If collection is empty, type must be specified")

        if collection and collection_type is not None:
            raise ValueError("Collection type can only be specified for empty collections")

        collection_type = _infer_collection_type(collection) if collection_type is None else collection_type
        name = self._collection_name(collection_type)

        serialized_collection = self._serialize_collection(collection)
        self._save_serialized_collection(serialized_collection, name)

    def _get_serialized_collection(self, collection_type: type[T]) -> SerializedCollection:
        """Get serialized collection of a given type"""
        name = self._collection_name(collection_type)
        serialized_collections = self._load_all_collections()
        return serialized_collections[name]

    def _save_serialized_collection(
            self,
            serialized_collection: SerializedCollection,
            collection_name: str
    ) -> None:
        """Save a serialized collection in the database"""
        all_collections = self._load_all_collections()
        all_collections[collection_name] = serialized_collection
        self._save_all_collections(all_collections)

    def _collection_name(self, collection_type: type) -> str:
        """Get name mapped to a given type"""
        return self.__collection_name_mapping[collection_type]

    def _load_all_collections(self) -> dict[str, SerializedCollection]:
        """Load database from file"""
        self.__db_file.seek(0)  # Go to the first byte before reading
        data = json.load(self.__db_file)
        return data

    def _save_all_collections(self, collections: dict[str, SerializedCollection]) -> None:
        """Save database to the file"""
        self.__db_file.seek(0)  # Go to the first byte before reading
        self.__db_file.truncate(0)  # Delete file content
        json.dump(collections, self.__db_file)

    def _serialize_collection(self, collection: Collection) -> SerializedCollection:
        """Serialize a collection to JSON format"""
        if not collection:
            return {}

        item_type = _infer_collection_type(collection)
        serializer = self.__serializers[item_type]
        return {
            uuid: serializer.to_json(item)
            for uuid, item in collection.items()
        }

    def _deserialize_collection(
            self,
            serialized_collection: SerializedCollection,
            collection_type: type[T]
    ) -> Collection:
        """Deserialize a collection from JSON format"""
        if not serialized_collection:
            return {}

        serializer = self.__serializers[collection_type]
        return {
            uuid: serializer.from_json(item_json)
            for uuid, item_json in serialized_collection.items()
        }

    @staticmethod
    def _verify_file(db_file: TextIO, collection_name_mapping: dict[type, str]) -> None:
        """Verify that given file valid for given mapping of collection names

        File must be readable and writable.
        File must be in JSON format.
        JSON must contain all collection names as defined in the mapping

        :param db_file: file storing the database
        :param collection_name_mapping: dictionary mapping model classes
            to names of their corresponding collections in the database file
        :raises InvalidDatabaseFileError: if given file is not valid
        """
        if not db_file.readable() or not db_file.writable():
            raise InvalidDatabaseFileError("File must be readable and writable")

        try:
            file_data = json.load(db_file)
            collection_names = set(collection_name_mapping.values())
            file_keys = set(file_data.keys())
            if not collection_names.issubset(file_keys):
                raise InvalidDatabaseFileError("JSON must contain all specified collections")
        except Exception as e:
            raise InvalidDatabaseFileError("File must be in JSON format") from e


def _infer_collection_type(collection: Collection) -> type:
    """Infer type of items in the collection based on first element"""
    items = list(collection.values())
    first_item = items[0]
    return type(first_item)


class InvalidDatabaseFileError(ValueError):
    """Error Signaling that a JSON file is not a valid representation of a database"""
    pass
