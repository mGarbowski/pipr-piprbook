import json
from typing import TextIO, Optional

SerializedCollection = dict[str, dict]


# TODO: update docs, refactor, add unit tests
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

    def __init__(self, db_file: TextIO, collection_name_mapping: dict[type, str]):
        """Create a new database instance persisting data in the given file

        :param db_file: file to persist data in
        :param collection_name_mapping: dictionary mapping model classes to collection names in the database
        """
        JsonDatabase._verify_file(db_file, collection_name_mapping)
        self.__db_file = db_file
        self.__collection_name_mapping = collection_name_mapping

    def get_by_id(self, entity_id: str, collection_name: str) -> Optional[dict]:
        """Get an entity by its id or None if not found

        :param entity_id: id of entity
        :param collection_name: type of searched entity
        """
        collection = self._get_serialized_collection(collection_name)
        return collection[entity_id] if entity_id in collection else None

    def save(self, entity_dict: dict, collection_name: str) -> None:
        """Save an entity to the database, overwriting previous value if it existed"""
        collection = self._get_serialized_collection(collection_name)
        collection[entity_dict["uuid"]] = entity_dict
        self._save_serialized_collection(collection, collection_name)

    def delete_by_id(self, entity_id: str, collection_name: str) -> None:
        """Delete an existing entity from the database by its id

        If entity is not saved in the database - do nothing
        """
        collection = self._get_serialized_collection(collection_name)
        try:
            collection.pop(entity_id)
            self._save_serialized_collection(collection, collection_name)
        except KeyError:
            pass

    def get_collection(self, collection_name: str) -> list[dict]:
        """Get collection of entities by their type"""
        collection = self._get_serialized_collection(collection_name)
        return list(collection.values())

    def save_collection(self, collection: list[dict], collection_name: str) -> None:
        """Save a collection to the database, overwriting all existing items

        :param collection: collection of entities to save in the database
        :param collection_name: type of the collection in case it is empty
            by default type is inferred
            only specify type explicitly when saving an empty collection
        :raises ValueError: if at the same time collection is empty and type is not specified
            or the collection is not empty and type is specified
        """
        serialized_collection = {entity_dict["uuid"]: entity_dict for entity_dict in collection}
        self._save_serialized_collection(serialized_collection, collection_name)

    def _get_serialized_collection(self, collection_name: str) -> SerializedCollection:
        """Get serialized collection of a given type"""
        serialized_collections = self._load_all_collections()
        return serialized_collections[collection_name]

    def _save_serialized_collection(
            self,
            serialized_collection: SerializedCollection,
            collection_name: str
    ) -> None:
        """Save a serialized collection in the database"""
        all_collections = self._load_all_collections()
        all_collections[collection_name] = serialized_collection
        self._save_all_collections(all_collections)

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


class InvalidDatabaseFileError(ValueError):
    """Error Signaling that a JSON file is not a valid representation of a database"""
    pass
