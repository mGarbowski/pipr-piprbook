"""Database in a JSON file"""

import json
from typing import TextIO, Optional, Dict, List

SerializedCollection = Dict[str, Dict]


class JsonDatabase:
    """Database in a JSON file storing collections of entity dictionaries

    List of collections used by the database is passed to init.
    Handle to the JSON file is passed to init.
    Attempts to access collection with other names than those from the list
    raise exceptions.

    A collection is a list of entity dictionaries.
    An entity dictionary must have uuid key
    """

    def __init__(self, db_file: TextIO, collection_names: List[str]):
        """Create a new database instance persisting data in the given file

        :param db_file: file to persist data in and to load data from
        :param collection_names: list of collection names used by the database
        :raises InvalidDatabaseFileError: if file is not JSON or if file
        does not have all the required collections
        """
        JsonDatabase._verify_file(db_file, collection_names)
        self.__db_file = db_file
        self.__collection_names = collection_names

    def get_by_id(
            self, entity_id: str, collection_name: str
    ) -> Optional[Dict]:
        """Get an entity by its id or None if not found

        :param entity_id: id of entity
        :param collection_name: entity collection's name
        :raises CollectionDoesNotExistError: when collection with given name
            does not exist
        """
        self._verify_collection_name(collection_name)
        collection = self._get_serialized_collection(collection_name)
        return collection[entity_id] if entity_id in collection else None

    def save(self, entity_dict: Dict, collection_name: str) -> None:
        """Save an entity to the database, overwriting previous value if it
        existed

        :param entity_dict: entity dictionary to be peristed in the database
        :param collection_name: entity collection's name
        :raises CollectionDoesNotExistError: when collection with given name
            does not exist
        :raises NoUuidError: when entity_dict does not have a uuid
        """
        self._verify_collection_name(collection_name)
        self._verify_has_uuid(entity_dict)

        collection = self._get_serialized_collection(collection_name)
        collection[entity_dict["uuid"]] = entity_dict
        self._save_serialized_collection(collection, collection_name)

    def delete_by_id(self, entity_id: str, collection_name: str) -> None:
        """Delete an existing entity from the database by its id

        If there is no entity with given id - do nothing

        :param entity_id: id of the entity to delete
        :param collection_name: entity collection's name
        :raises CollectionDoesNotExistError: when collection with given name
            does not exist
        """
        self._verify_collection_name(collection_name)
        collection = self._get_serialized_collection(collection_name)
        try:
            collection.pop(entity_id)
            self._save_serialized_collection(collection, collection_name)
        except KeyError:
            pass

    def get_collection(self, collection_name: str) -> List[Dict]:
        """Get collection of entities by its name

        :param collection_name: name of the collection
        :raises CollectionDoesNotExistError: when collection with given name
            does not exist
        """
        self._verify_collection_name(collection_name)
        collection = self._get_serialized_collection(collection_name)
        return list(collection.values())

    def save_collection(self, collection: List[Dict],
                        collection_name: str) -> None:
        """Save collection to the database, overwriting all existing items

        :param collection: collection of entities to persist in the database
        :param collection_name: name of the collection
        :raises CollectionDoesNotExistError: when collection with given name
            does not exist
        :raises NoUuidError: when any entiy dict in the collection does not
            have a uuid
        """
        self._verify_collection_name(collection_name)
        for entity_dict in collection:
            self._verify_has_uuid(entity_dict)

        serialized_collection = {
            entity_dict["uuid"]: entity_dict
            for entity_dict in collection
        }
        self._save_serialized_collection(
            serialized_collection, collection_name
        )

    def _get_serialized_collection(
            self,
            collection_name: str
    ) -> SerializedCollection:
        """Get serialized collection by its name

        :param collection_name: name of the collection
        """
        serialized_collections = self._load_all_collections()
        return serialized_collections[collection_name]

    def _save_serialized_collection(
            self,
            serialized_collection: SerializedCollection,
            collection_name: str
    ) -> None:
        """Save serialized collection in the database

        :param serialized_collection: serialized collection to save
        :param collection_name: name of the collection
        """
        all_collections = self._load_all_collections()
        all_collections[collection_name] = serialized_collection
        self._save_all_collections(all_collections)

    def _load_all_collections(self) -> Dict[str, SerializedCollection]:
        """Load all collection from the database file

        :return: dictionary mapping collection names to serialized collections
        """
        self.__db_file.seek(0)  # Go to the first byte before reading
        data = json.load(self.__db_file)
        return data

    def _save_all_collections(
            self,
            collections: Dict[str, SerializedCollection]
    ) -> None:
        """Save all serialized collection to the database file

        :param collections: dictionary mapping collection names to
        serialized collections
        """
        self.__db_file.seek(0)  # Go to the first byte before reading
        self.__db_file.truncate(0)  # Delete file content
        json.dump(collections, self.__db_file)

    def _verify_collection_name(self, collection_name: str):
        """Verify if collection with given name exists

        :param collection_name: name of a collection to verify
        :raises CollectionDoesNotExistError: if collection with given name
            does not exist
        """
        if collection_name not in self.__collection_names:
            raise CollectionDoesNotExistError(collection_name)

    @staticmethod
    def _verify_has_uuid(entity_dict: Dict) -> None:
        """Verify if entiy dictionary has uuid key

        :param entity_dict: dictionary to verify
        :raises NoUuidError: if dictionary does not have a uuid key
        """
        if "uuid" not in entity_dict:
            raise NoUuidError()

    @staticmethod
    def _verify_file(db_file: TextIO, collection_names: List[str]) -> None:
        """Verify database file against list of collection names

        File must be readable and writable.
        File must be in JSON format.
        File must contain all collections given in the list of names.

        Collections can be empty

        :param db_file: database file to verify
        :param collection_names: list of names of the collections
        :raises InvalidDatabaseFileError: if file is not readable or writable,
            if any of the collection names is not represented in the file,
            if file is not a valid JSON
        """
        if not db_file.readable() or not db_file.writable():
            raise InvalidDatabaseFileError(
                "File must be readable and writable")

        try:
            file_data = json.load(db_file)
            file_keys = set(file_data.keys())
            collection_names_set = set(collection_names)
            if not collection_names_set.issubset(file_keys):
                raise InvalidDatabaseFileError(
                    "JSON must contain all specified collections")
        except Exception as e:
            raise InvalidDatabaseFileError(
                "File must be in JSON format") from e


class JsonDatabaseException(Exception):
    """Generic exception signaling a problem with the JsonDatabase"""
    pass


class InvalidDatabaseFileError(JsonDatabaseException):
    """Error Signaling that a JSON file is not a valid representation of a
    database"""
    pass


class CollectionDoesNotExistError(JsonDatabaseException):
    def __init__(self, collection_name):
        super().__init__(f"Collection: {collection_name} does not exist")
        self.collection_name = collection_name


class NoUuidError(JsonDatabaseException):
    def __init__(self):
        super().__init__("Entity dictionary must have a uuid key")
